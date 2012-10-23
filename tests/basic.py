#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pylocwolowitz import Pylocwolowitz

class TestSequenceFunctions(unittest.TestCase):
    '''Basic test class with simple test'''

    def setUp(self):
        '''To set up thing we need, init a Pylocwolowitz'''
        self.i18n = Pylocwolowitz('./i18n')

    def test_sample(self):
        '''Simple test no placeholders'''
        self.assertEqual(self.i18n.loc('hello', 'es'), 'Hola')

    def test_sample_token(self):
        '''Tests with placeholders'''
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'fr', {'name':
            'hobbestigrou'}), 'Bienvenue hobbestigrou')
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'en', {'name':
            'hobbestigrou'}), 'Welcome hobbestigrou')
        self.assertEqual(self.i18n.loc('welcome %(name)s', 'se', {'name':
            'hobbestigrou'}), u'Välkommen hobbestigrou')

    def test_no_key(self):
        '''Test to try with a non existing key'''
        self.assertEqual(self.i18n.loc('world', 'fr'), 'world')

    def test_no_lang(self):
        '''Test with a no lang'''
        self.assertEqual(self.i18n.loc('hello', 'lu'), 'hello')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
