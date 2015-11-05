# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tpa.content.testing import TPA_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that tpa.content is properly installed."""

    layer = TPA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tpa.content is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tpa.content'))

    def test_browserlayer(self):
        """Test that ITpaContentLayer is registered."""
        from tpa.content.interfaces import ITpaContentLayer
        from plone.browserlayer import utils
        self.assertIn(ITpaContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TPA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tpa.content'])

    def test_product_uninstalled(self):
        """Test if tpa.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('tpa.content'))

    def test_browserlayer_removed(self):
        """Test that ITpaContentLayer is removed."""
        from tpa.content.interfaces import ITpaContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITpaContentLayer, utils.registered_layers())
