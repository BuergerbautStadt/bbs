#!/usr/bin/env python
import os,sys,json

try:
    fixtures = json.loads(open(sys.argv[1]).read())
except (IndexError,IOError):
    sys.exit('Usage: ./migrate-comments-fixtures.py FIXTUREFILE')

new_fixtures = []
for fixture in fixtures:

    if fixture['model'] == 'comments.kommentar':

        new_fixtures.append({
            "fields": {
                "author_email": fixture['fields']['author_email'],
                "author_name": fixture['fields']['author_name'],
                "author_url": fixture['fields']['author_url'],
                "enabled": fixture['fields']['enabled'],
                "content": fixture['fields']['content'],
                "place": fixture['fields']['ort'],
                "created": fixture['fields']['created'],
                "updated": fixture['fields']['updated']
            },
            "model": "comments.comment",
            "pk": fixture['pk']
        })

print json.dumps(new_fixtures)