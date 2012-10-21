#!/usr/bin/env python

import unittest
from pylocwolowitz import Pylocwolowitz

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.i18n = Pylocwolowitz('./i18n')

    def test_sample(self):
        self.assertEqual(self.i18n.loc('hello', 'es'), 'Hola')

    def test_sample_token(self):
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'fr', {'name': 'hobbestigrou'}), 'Bienvenue hobbestigrou')
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'en', {'name': 'hobbestigrou'}), 'Welcome hobbestigrou')
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'se', {'name': 'hobbestigrou'}), 'Valkommen hobbestigrou')

    def test_no_key(self):
        self.assertEqual(self.i18n.loc('world', 'fr'), 'world')

    def test_no_lang(self):
        self.assertEqual(self.i18n.loc('hello', 'lu'), 'hello')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
