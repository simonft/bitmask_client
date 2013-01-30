import unittest
import hashlib

import sip
sip.setapi('QVariant', 2)

from leap.gui import mainwindow_rc

# I have to admit that there's something
# perverse in testing this.
# But I thought that it could be a good idea
# to put a check to avoid non-updated resources files.

# so, if you came here because an updated resource
# did break a test, what you have to do is getting
# the md5 hash of your qt_resource_data and change it here.

# annoying? yep. try making a script for that :P


class MainWindowResourcesTest(unittest.TestCase):

    def test_mainwindow_resources_hash(self):
        self.assertEqual(
            hashlib.md5(mainwindow_rc.qt_resource_data).hexdigest(),
            '5cc26322f96fabaa05c404f22774c716')