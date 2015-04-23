#!/usr/bin/env python
import os,sys,json

try:
    fixtures = json.loads(open(sys.argv[1]).read())
except (IndexError,IOError):
    sys.exit('Usage: ./migrate-news-fixtures.py FIXTUREFILE')

new_fixtures = []
for fixture in fixtures:
    if fixture['model'] == 'projects.ort':

        if fixture['fields']['polygontype'] == '' or fixture['fields']['polygontype'] == None:
            polygon = None
        elif fixture['fields']['polygontype'] == 'Polygon':
            polygon = [json.loads(fixture['fields']['polygon'])]
        else:
            polygon = json.loads(fixture['fields']['polygon'])

        new_fixtures.append({
            "fields": {
                "active": False,
                "address": fixture['fields']['adresse'],
                "description": fixture['fields']['beschreibung'],
                "lat": fixture['fields']['lat'],
                "lon": fixture['fields']['lon'],
                "identifier": fixture['fields']['bezeichner'],
                "entities": [i+1 for i in fixture['fields']['bezirke']],
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated'],
                "polygon": polygon
            },
            "model": "process.place",
            "pk": fixture['pk']
        })
    elif fixture['model'] == 'projects.veroeffentlichung':
        new_fixtures.append({
            "fields": {
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated'],
                "office_hours": fixture['fields']['zeiten'],
                "process_step": fixture['fields']['verfahrensschritt'],
                "department": fixture['fields']['behoerde'],
                "place": fixture['fields']['ort'],
                "office": fixture['fields']['auslegungsstelle'],
                "description": fixture['fields']['beschreibung'],
                "end": fixture['fields']['ende'],
                "link": fixture['fields']['link'],
                "begin": fixture['fields']['beginn']
            },
            "pk": fixture['pk'],
            "model": "process.publication"
        })
    elif fixture['model'] == 'projects.verfahrensschritt':
        new_fixtures.append({
            "fields": {
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated'],
                "description": fixture['fields']['beschreibung'],
                "hover_icon": fixture['fields']['hoverIcon'],
                "icon": fixture['fields']['icon'],
                "name": fixture['fields']['name'],
                "order": fixture['fields']['reihenfolge'],
                "process_type": fixture['fields']['verfahren'],
            },
            "model": "process.processstep",
            "pk": fixture['pk']
        })
    elif fixture['model'] == 'projects.verfahren':
        new_fixtures.append({
            "fields": {
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated'],
                "name": fixture['fields']['name'],
                "description": fixture['fields']['beschreibung'],
            },
            "model": "process.processtype",
            "pk": fixture['pk']
        })
    elif fixture['model'] == 'projects.behoerde':
        pass
    elif fixture['model'] == 'projects.bezirk':
        pass

print json.dumps(new_fixtures)
