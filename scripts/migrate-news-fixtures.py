#!/usr/bin/env python
import os,sys,json

try:
    fixtures = json.loads(open(sys.argv[1]).read())
except (IndexError,IOError):
    sys.exit('Usage: ./migrate-process-fixtures.py FIXTUREFILE')

new_fixtures = []
for fixture in fixtures:

    if fixture['model'] == 'news.abonnent':

        entitites = []
        for i in fixture['fields']['bezirke']:
            entitites.append(i+1)

        new_fixtures.append({
            "fields": {
                "entities": entitites,
                "email": fixture['fields']['email'],
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated']
            },
            "model": "news.subscriber",
            "pk": fixture['pk']
        })

print json.dumps(new_fixtures)