# -*- coding: utf-8 -*-
import os

import pytest

from pylocwolowitz import Pylocwolowitz


@pytest.fixture
def pylocwolowitz():
    """To load the pylocwolowitz object"""
    directory = os.getcwd() + '/i18n' if 'tests' in os.getcwd(
    ) else os.getcwd() + '/tests/i18n'
    i18n = Pylocwolowitz(directory, 'yaml')

    return i18n
