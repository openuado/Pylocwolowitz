#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple basic test to YAML"""
from __future__ import unicode_literals


def test_sample(pylocwolowitz):
    """Simple test no placeholders"""
    assert pylocwolowitz.loc('hello', 'es') == 'Hola'


def test_sample_token(pylocwolowitz):
    """Tests with placeholders"""
    fr = pylocwolowitz.loc('welcome {name}', 'fr', {'name': 'hobbestigrou'})
    assert fr == 'Bienvenue hobbestigrou'

    en = pylocwolowitz.loc('welcome {name}', 'en', {'name': 'hobbestigrou'})
    assert en == 'Welcome hobbestigrou'

    se = pylocwolowitz.loc('welcome {name}', 'se', {'name': 'hobbestigrou'})
    assert se == 'Välkommen hobbestigrou'


def test_no_key(pylocwolowitz):
    """Test to try with a non existing key"""
    assert pylocwolowitz.loc('world', 'fr') == 'world'


def test_no_lang(pylocwolowitz):
    """Test with a no lang"""
    assert pylocwolowitz.loc('hello', 'lu') == 'hello'
