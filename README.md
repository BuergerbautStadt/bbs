BuergerbautStadt
================

[http://buergerbautstadt.de][bbs] - Finde geplante Bauvorhaben in deinem Kiez.

## Setup

1. Have Python 2.7.x installed.
2. Clone [https://github.com/webuildcity/wbc][wbc-github] to a location of your choice.
3. Clone this repository, [https://github.com/BuergerbautStadt/bbs][bbs-github], to a location of your choice.
4. Copy `/path/to/bbs/bbs/default.local.py` to `/path/to/bbs/bbs/local.py`.
5. Edit `/path/to/bbs/bbs/local.py` to match your setup. At least edit the database adapter settings. For testing purposes, use the sqlite3 adapter.
6. Install the dependencies using pip `pip install -r /path/to/bbs/requirements.txt`. You might want to use a [virtualenv][virtualenv] for this.
7. Change to the `bbs` directory and execute `python maname.py migrate`. Give an admin username and a password when asked.
8. Start the development server using `python maname.py runserver`.
10. Use `python maname.py load-fixtures` to load the administrative information about Berlin into the database.
11. Open a browser and go to [http://localhost:8000/][bbs-home]. A map of berlin should appear.
12. Use [http://localhost:8000/admin/][bbs-admin] to log in. Under *region* and *process*, districts, departmentsplaces and publications can be added or edited.

[bbs]: http://buergerbautstadt.de
[bbs-github]: https://github.com/BuergerbautStadt/bbs
[wbc-github]: https://github.com/webuildcity/wbc
[django]: https://docs.djangoproject.com/en/1.8/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[bbs-home]: http://localhost:8000/
[bbs-admin]: http://localhost:8000/admin/
