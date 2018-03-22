# -*- coding: utf-8 -*-
import os

import pytest

from pylocwolowitz import Pylocwolowitz


def _get_directory():
    return os.getcwd() + '/i18n' if 'tests' in os.getcwd(
    ) else os.getcwd() + '/tests/i18n'


@pytest.fixture
def pylocwolowitz_yaml():
    """To load the pylocwolowitz object"""
    return Pylocwolowitz(_get_directory(), 'yaml')


@pytest.fixture
def pylocwolowitz_default_key():
    """To load the pylocwolowitz object for yaml with default key"""
    return Pylocwolowitz(_get_directory(), 'yaml', default_key='default')


@pytest.fixture
def pylocwolowitz_json():
    """To load the pylocwolowitz object for json"""
    return Pylocwolowitz(_get_directory(), 'json')


@pytest.fixture
def pylocwolowitz_default_key_json():
    """To load the pylocwolowitz object for json with default key"""
    return Pylocwolowitz(_get_directory(), 'json', default_key='default')
