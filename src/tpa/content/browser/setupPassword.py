# -*- coding: utf-8 -*-

from tpa.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
#from DateTime import DateTime
#from plone.memoize import ram
from zope.interface import Interface
from plone.directives import form
from zope import schema
from z3c.form import button
from Products.statusmessages.interfaces import IStatusMessage
#from Acquisition import aq_inner
#from zope.component import getUtility
#from zope.intid.interfaces import IIntIds
#from zope.security import checkPermission
#from zc.relation.interfaces import ICatalog


class ISetupPassword(form.Schema):

    accountId = schema.TextLine(
        title=_(u"Account Id"),
    )

    newPassword = schema.TextLine(
        title=_(u"New Password"),
    )


class SetupPassword(form.SchemaForm):

    schema = ISetupPassword
    ignoreContext = True

    label = _(u"Setup Password")
    description = _(u"Please input account id and password, setup it.")


    @button.buttonAndHandler(_(u'Setup'))
    def handleApply(self, action):
        request = self.request
        response = request.response
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        accountId = self.request.form['form.widgets.accountId']
        newPassword = self.request.form['form.widgets.newPassword']
        user = api.user.get(username=accountId)
        if user:
            user.setSecurityProfile(password=newPassword)
            message = _(u"Already setup password!")
            mType = 'info'
        else:
            message = _(u"User not found!")
            mType = 'warning'
    
        response.redirect('/@@setupPassword')
        api.portal.show_message(message=message, request=request, type=mType)
        return

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):

        request = self.request
        response = request.response
        response.redirect('/@@setupPassword')
        message = _(u"Cancel this action!")
        api.portal.show_message(message=message, request=request, type='info')
        return
