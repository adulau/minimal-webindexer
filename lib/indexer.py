#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os


class index:
    def __init__(self, IndexDir="../index"):
        self.IndexDir = IndexDir
        from whoosh.index import create_in, exists_in, open_dir
        from whoosh.fields import Schema, TEXT, ID
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True, unique=True), content=TEXT)
        if not os.path.exists(IndexDir):
            os.mkdir(IndexDir)

        if not exists_in(IndexDir):
            self.ix = create_in(IndexDir, schema)
        else:
            self.ix = open_dir(IndexDir)
        self.writer = self.ix.writer()

    def add(self, DocumentID=None, Content=None, Title=None):
        if DocumentID is None or Content is None:
            return False
        if Title is None:
            Title = ""
        self.writer.update_document(title=Title, path=DocumentID, content=Content)

    def close(self):
        self.writer.commit()

if __name__ == "__main__":
    i = index()
    i.add(DocumentID=u"http://www.foo.be/", Content=u"this is a test indexing of a random content", Title=u"test homepage")
    i.close()
    i = index()
    i.add(DocumentID=u"http://news.ycombinator.com", Content=u"Test école texte", Title=u"Titre")
    i.close()
