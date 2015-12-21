# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from tpa.content import _
from zope import schema
from plone.namedfile.field import NamedBlobImage
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ITpaContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAd(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        description=_("Advertising, show at sidebar in homepage."),
        required = True,
    )

    url = schema.URI(
        title = _(u"URL Address"),
        required = True,
    )

    image = NamedBlobImage(
        title=_(u"Image"),
        required=True,
    )


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
