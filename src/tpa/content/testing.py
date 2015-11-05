# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tpa.content


class TpaContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tpa.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tpa.content:default')


TPA_CONTENT_FIXTURE = TpaContentLayer()


TPA_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TPA_CONTENT_FIXTURE,),
    name='TpaContentLayer:IntegrationTesting'
)


TPA_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TPA_CONTENT_FIXTURE,),
    name='TpaContentLayer:FunctionalTesting'
)


TPA_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TPA_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TpaContentLayer:AcceptanceTesting'
)
