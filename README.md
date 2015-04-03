BuergerbautStadt
================

[http://buergerbautstadt.de][bbs] - Finde geplante Bauvorhaben in deinem Kiez.

## Setup

1. Have Python 2.7.x installed.
2. Clone [https://github.com/webuildcity/wbc][wbc-github] to a location of your choice.
3. Clone this repository, [https://github.com/BuergerbautStadt/bbs][bbs-github], to a location of your choice.
4. Copy `/path/to/bbs/bbs/default.local.py` to `/path/to/bbs/bbs/local.py`.
5. Edit `/path/to/bbs/bbs/local.py` to match your setup. At least edit the path to the `wbc` repository and the database adapter settings. For testing purposes, use the sqlite3 adapter.
6. Install the dependencies using pip `pip install -r /path/to/bbs/requirements.txt`. You might want to use a [virtualenv][virtualenv] for this.
7. Change to the `bbs` directory and execute `python manage.py migrate` to set up the database structure.
8. Use `python manage.py load-fixtures` to load the administrative information about Berlin into the database.
9. Run `python manage.py createsuperuser` to create an admin account.
10. Start the development server using `python manage.py runserver`.
11. Open a browser and go to [http://localhost:8000/][bbs-home]. A map of berlin should appear.
12. Use [http://localhost:8000/admin/][bbs-admin] to log in. Under *region* and *process*, districts, departments, places and publications can be added or edited.

[bbs]: http://buergerbautstadt.de
[bbs-github]: https://github.com/BuergerbautStadt/bbs
[wbc-github]: https://github.com/webuildcity/wbc
[django]: https://docs.djangoproject.com/en/1.8/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[bbs-home]: http://localhost:8000/
[bbs-admin]: http://localhost:8000/admin/
