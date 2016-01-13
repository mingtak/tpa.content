from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
from DateTime import DateTime
from plone.memoize import ram

#from Acquisition import aq_inner
#from zope.component import getUtility
#from zope.intid.interfaces import IIntIds
#from zope.security import checkPermission
#from zc.relation.interfaces import ICatalog


class GetPortalId(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        return portal.getId()


class SearchResult(BrowserView):

    index = ViewPageTemplateFile("template/search_result.pt")

    def __call__(self):
        context = self.context
        request = self.request
        catalog = context.portal_catalog

        string = getattr(request, 'string', False)
#        import pdb; pdb.set_trace()
        if not string:
            request.response.redirect('/')
            return
        self.brain = catalog({'SearchableText':string.split()})
        self.brain
        return self.index()


class TpaFolderView(BrowserView):
    """ Tpa Folder View
    """


class TpaFolderListingView(BrowserView):
    """ Tpa Folder Listing View
    """


class CoverView(BrowserView):
    """ Cover View (default)
    """


class AdView(BrowserView):
    """ Ad View (default)
    """


class Is_Anonymous(BrowserView):

    def __call__(self):
        return api.user.is_anonymous()


class VisitorCounter(BrowserView):

    @ram.cache(lambda *args: DateTime().hour())
    def __call__(self):
        now = int(DateTime().timeTime())
        return int((now/80)) - 18100000
