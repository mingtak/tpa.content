# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from tpa.content import interfaces


@indexer(interfaces.IAd)
def url_indexer(obj):
     return obj.url

