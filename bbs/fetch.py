# coding: utf-8
import os,subprocess,json,urllib2,time,sys

from wbc.region.models import District
from wbc.process.models import Place

class PlaceFetcher():

    def fetch(self):

        # get time since last download
        try:
            time_delta = time.time() - os.stat('/tmp/re_bplan.json').st_ctime
        except OSError:
            time_delta = 86400

        # download data if older than 10 minutes
        if time_delta > 600:
            try:
                os.remove('/tmp/re_bplan.json')
            except OSError:
                pass

            # call org2org to fetch the bplan geojson from the FIZ-Broker
            cmd = 'ogr2ogr -s_srs EPSG:25833 -t_srs WGS84 -f geoJSON /tmp/re_bplan.json WFS:"http://fbinter.stadt-berlin.de/fb/wfs/geometry/senstadt/re_bplan?TYPENAMES=GML2" re_bplan'
            subprocess.call(cmd,shell=True);

        # open geojson
        geojson = json.load(open('/tmp/re_bplan.json','r'))

        n = 0
        for feature in geojson["features"]:

            # prepare values dictionary
            place_values = {}

            # get identifier
            try:
                place_values['identifier'] = feature['properties']['spatial_alias'].replace(' ','')
            except AttributeError:
                continue

            # switch lat and lon in (multi) polygon and get center
            latMin,latMax,lonMin,lonMax = 90,-90,180,-180
            if feature['geometry']['type'] == 'Polygon':
                for path in feature['geometry']['coordinates']:
                    for point in path:
                        point[0],point[1] = point[1],point[0]
                        latMin = min(latMin,point[0])
                        latMax = max(latMax,point[0])
                        lonMin = min(lonMin,point[1])
                        lonMax = max(lonMax,point[1])
                place_values['polygon'] = json.dumps([feature['geometry']['coordinates']])
            else:
                for polygon in feature['geometry']['coordinates']:
                    for path in polygon:
                        for point in path:
                            point[0],point[1] = point[1],point[0]
                            latMin = min(latMin,point[0])
                            latMax = max(latMax,point[0])
                            lonMin = min(lonMin,point[1])
                            lonMax = max(lonMax,point[1])
                place_values['polygon'] = json.dumps(feature['geometry']['coordinates'])

            # get lat and lon
            place_values['lat'] = str((latMax + latMin) * 0.5)
            place_values['lon'] = str((lonMax + lonMin) * 0.5)

            # get area description
            if feature['properties']['BEREICH']:
                place_values['description'] = feature['properties']['BEREICH']
            else:
                place_values['description'] = ''

            # see if is marked active
            if feature['properties']['FESTSG']:
                if feature['properties']['FESTSG'].lower() == 'ja':
                    place_values['active'] = False
                else:
                    place_values['active'] = True
            else:
                place_values['active'] = False

            # update the place or create a new one
            place,created = Place.objects.update_or_create(identifier=place_values['identifier'],defaults=place_values)

            if created:
                n += 1
                try:
                    district = District.objects.get(name=feature['properties']['BEZIRK'])
                    place.entities.add(district)
                    place.save()
                except District.DoesNotExist:
                    pass

                # get address from open street map
                url = "http://open.mapquestapi.com/nominatim/v1/reverse.php?format=json&lat=%s&lon=%s" % (place.lat,place.lon)
                response = urllib2.urlopen(url).read()
                data = json.loads(response)
                if 'road' in data['address']:
                    place.address = data['address']['road']
                else:
                    place.address = ''
                place.save()
                print place, 'created'
                time.sleep(1)

        print n,'places created'
