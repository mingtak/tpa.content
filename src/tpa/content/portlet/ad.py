from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope.formlib import form
from plone import api
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IAdvertising(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IAdvertising)

    def __init__(self):
        pass

    @property
    def title(self):
        return "Advertising"


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('advertising.pt')

    def getAds(self):
        portal = api.portal.get()
        adFolder = portal['system']['5ee3544a7ba17406']
        children = adFolder.getChildNodes()
        return children

    def getExternalAds(self):
        portal = api.portal.get()
        adFolder = portal['system']['591690e890237d507ba17406']
        children = adFolder.getChildNodes()
        return children



class AddForm(base.AddForm):
    schema = IAdvertising
    form_fields = form.Fields(IAdvertising)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    schema = IAdvertising
    form_fields = form.Fields(IAdvertising)
