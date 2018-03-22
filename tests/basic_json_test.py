#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple basic test for JSON"""
from __future__ import unicode_literals


def test_sample(pylocwolowitz_json):
    """Simple test no placeholders"""
    assert pylocwolowitz_json.loc('hello', 'es') == 'Hola'


def test_sample_token(pylocwolowitz_json):
    """Tests with placeholders"""
    fr = pylocwolowitz_json.loc(
        'welcome {name}', 'fr', {'name': 'hobbestigrou'})
    assert fr == 'Bienvenue hobbestigrou'

    en = pylocwolowitz_json.loc(
        'welcome {name}', 'en', {'name': 'hobbestigrou'})
    assert en == 'Welcome hobbestigrou'

    se = pylocwolowitz_json.loc(
        'welcome {name}', 'se', {'name': 'hobbestigrou'})
    assert se == 'Välkommen hobbestigrou'


def test_no_key(pylocwolowitz_json):
    """Test to try with a non existing key"""
    assert pylocwolowitz_json.loc('world', 'fr') == 'world'


def test_no_lang(pylocwolowitz_json):
    """Test with a no lang"""
    assert pylocwolowitz_json.loc('hello', 'lu') == 'hello'


def test_default_key(pylocwolowitz_default_key_json):
    assert pylocwolowitz_default_key_json.loc('world', 'fr') == 'Valeur par défaut'
    assert pylocwolowitz_default_key_json.loc('world', 'en') == 'world'
