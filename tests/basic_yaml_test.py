#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple basic test to YAML"""
from __future__ import unicode_literals


def test_sample(pylocwolowitz_yaml):
    """Simple test no placeholders"""
    assert pylocwolowitz_yaml.loc('hello', 'es') == 'Hola'


def test_sample_token(pylocwolowitz_yaml):
    """Tests with placeholders"""
    fr = pylocwolowitz_yaml.loc(
        'welcome {name}', 'fr', {'name': 'hobbestigrou'})
    assert fr == 'Bienvenue hobbestigrou'

    en = pylocwolowitz_yaml.loc(
        'welcome {name}', 'en', {'name': 'hobbestigrou'})
    assert en == 'Welcome hobbestigrou'

    se = pylocwolowitz_yaml.loc(
        'welcome {name}', 'se', {'name': 'hobbestigrou'})
    assert se == 'Välkommen hobbestigrou'


def test_no_key(pylocwolowitz_yaml):
    """Test to try with a non existing key"""
    assert pylocwolowitz_yaml.loc('world', 'fr') == 'world'


def test_no_lang(pylocwolowitz_yaml):
    """Test with a no lang"""
    assert pylocwolowitz_yaml.loc('hello', 'lu') == 'hello'


def test_default_key(pylocwolowitz_default_key):
    assert pylocwolowitz_default_key.loc('world', 'fr') == 'Valeur par défaut'
    assert pylocwolowitz_default_key.loc('world', 'en') == 'world'
