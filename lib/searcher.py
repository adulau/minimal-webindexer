from whoosh.qparser import QueryParser
from whoosh import index



class search:
   def __init__(self, IndexDir="../index"):
        self.IndexDir = IndexDir
        from whoosh.fields import Schema, TEXT, ID
        self.schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
        self.ix = index.open_dir(IndexDir)

   def search(self, QueryTerms=None):
        if QueryTerms is None:
            return False

        query = QueryParser("content", self.schema).parse(" ".join(QueryTerms))
        results = []
        with self.ix.searcher() as wsearch:
            r = wsearch.search(query, limit=None)
            for v in r:
                d = {}
                d['title'] = v['title']
                d['url'] = v['path']
                results.append(d)
        return results

if __name__ == '__main__':
    t = search()
    print t.search(QueryTerms=['random'])
