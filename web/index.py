import os
import sys
_runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(_runPath, ".."))

import lib.searcher
import random
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import json
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = str(random.getrandbits(256))

@app.route('/', methods=['POST'])
def search():
    q = request.form.get('query')
    output = request.form.get('format')
    print (output)
    r = lib.searcher.search()
    x = []
    x.append(q)
    l = r.search(QueryTerms=x)
    if output == "json":
        return json.dumps(l)
    else:
        return render_template('results.html', results=l)

http_server = HTTPServer(WSGIContainer(app))
http_server.bind(8090, address='0.0.0.0')
http_server.start(0)
IOLoop.instance().start()

