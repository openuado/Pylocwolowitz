#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Simple basic test to YAML'''

from basic_json import PylocwolowitzTestCase
from pylocwolowitz import Pylocwolowitz
import os


class TestSequenceFunctions(PylocwolowitzTestCase):
    '''Basic test class with simple test'''

    def setUp(self):
        '''To set up thing we need, init a Pylocwolowitz'''
        directory = os.getcwd() + '/i18n' if 'tests' in os.getcwd(
        ) else os.getcwd() + '/tests/i18n'
        self.i18n = Pylocwolowitz(directory, 'yaml')
