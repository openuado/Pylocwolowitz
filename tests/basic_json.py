#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Simple basic test for JSON'''

from __future__ import unicode_literals
import unittest

from pylocwolowitz import Pylocwolowitz

import os


class PylocwolowitzTestCase(unittest.TestCase):
    '''Basic test class with simple test'''

    def setUp(self):
        '''To set up thing we need, init a Pylocwolowitz'''
        directory = os.getcwd() + '/i18n' if 'tests' in os.getcwd(
        ) else os.getcwd() + '/tests/i18n'
        self.i18n = Pylocwolowitz(directory)

    def test_sample(self):
        '''Simple test no placeholders'''
        self.assertEqual(self.i18n.loc('hello', 'es'), 'Hola')

    def test_sample_token(self):
        '''Tests with placeholders'''
        self.assertEqual(self.i18n.loc('welcome {name}', 'fr',
                                       {'name': 'hobbestigrou'}),
                         'Bienvenue hobbestigrou')
        self.assertEqual(self.i18n.loc('welcome {name}', 'en',
                                       {'name': 'hobbestigrou'}),
                         'Welcome hobbestigrou')

        self.assertEqual(self.i18n.loc('welcome {name}', 'se',
                                       {'name': 'hobbestigrou'}),
                         'Välkommen hobbestigrou')

    def test_no_key(self):
        '''Test to try with a non existing key'''
        self.assertEqual(self.i18n.loc('world', 'fr'), 'world')

    def test_no_lang(self):
        '''Test with a no lang'''
        self.assertEqual(self.i18n.loc('hello', 'lu'), 'hello')
