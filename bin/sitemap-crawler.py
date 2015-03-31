import os
import sys
runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

import requests
import lxml.etree
import lib.indexer
import html2text
import re
import argparse

def GetSitemap(url):
        resp = requests.get(url)
        if 200 != resp.status_code:
            return False
        return resp.content

def ParseSitemap(content):
    urls = []
    namespaces = [
         ('sm', 'http://www.sitemaps.org/schemas/sitemap/0.9'),
     ]
    tree = lxml.etree.fromstring(content)
    for sitemap in tree.xpath('//sm:url | //url', namespaces=namespaces):
         for loc in sitemap.xpath('sm:loc | loc', namespaces=namespaces):
             urls.append(loc.text.strip())
    return urls

def GetTitle(content):
    r = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)
    if r.search(content) is not None:
        return r.search(content).group(1)
    else:
        return None

def GetUrl(url, IndexableContent=['text/html']):
    r = requests.get(url)
    content_type = r.headers['Content-Type']
    if r is None:
        return (None, None)
    if content_type == "text/html":
        h = html2text.HTML2Text()
        title = GetTitle(r.content)
        if title is None:
            title = ""
        return (unicode(title, errors='ignore'),h.handle(r.content.decode('utf-8')))
    else:
        return (None, None)


argParser = argparse.ArgumentParser(description='minimal-webindexer - download a sitemap url and index')
argParser.add_argument('-u', type=str, help='Sitemap url to download and index')
argParser.add_argument('-d', default=False, action='store_true', help='Enable debug messages')
args = argParser.parse_args()
if not args.u:
    print ("Missing sitemap url")
    argParser.print_help()
    sys.exit(2)

for url in ParseSitemap(GetSitemap(args.u)):
    if url is None:
        continue
    ix = lib.indexer.index()
    (title, content) = GetUrl(url)
    if content is None:
        ix.close()
        continue
    ix.add(DocumentID=unicode(url), Content=content, Title=title)
    if args.d:
        print (url + " indexed")
    ix.close()
