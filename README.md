minimal-webindexer
==================

minimal-webindexer is a simple web indexer for static web pages. minimal-webindexer
is written in Python. At the current stage, the indexer only indexes a list of URLs
from a sitemap file.

Requirements
============

- [Whoosh](https://pythonhosted.org/Whoosh/) - Indexer in Python
- [requests](http://docs.python-requests.org/en/latest/) - Requests: HTTP for Humans

Install
=======

~~~
 pip install -r requirements
~~~

Usage
=====

Start the indexer:

~~~
 python bin/sitemap-crawler.py -u http://<yourwebsite>/sitemap.xml
~~~

Search via the test web interface:

~~~
 cd web
 python index.py
 open index.html
~~~

Adapt the index.html to your needs and the results template.


License
=======

Copyright (C) 2015 Alexandre Dulaunoy - a(at)foo.be

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

