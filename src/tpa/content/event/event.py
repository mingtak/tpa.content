# -*- coding: utf-8 -*-
# from Products.CMFPlone.utils import safe_unicode
# from plone import api


def moveContentToTop(item, event):
    """ Moves Item to the top of its folder """
    folder = item.getParentNode()
    if hasattr(folder, 'moveObjectsToTop') and folder.id == 'news':
        folder.moveObjectsToTop(item.id)
