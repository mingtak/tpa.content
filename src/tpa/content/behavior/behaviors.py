from Products.CMFCore.interfaces import IDublinCore
#from tpa.content import MessageFactory as _
from tpa.content import _
#from collective.gtags.field import Tags
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope import schema


@provider(IFormFieldProvider)
class IPubDep(model.Schema):

    pubdep = schema.TextLine(
            title=_(u"Published Department"),
            required=True,
        )


@implementer(IPubDep)
#@adapter(IDublinCore)
class PubDep(object):

    def __init__(self, context):
        self.context = context

    @property
    def pubdep(self):
        return self.context.pubdep
    @pubdep.setter
    def pubdep(self, value):
        self.context.pubdep = value
