import os

import pytest

from pylocwolowitz import Pylocwolowitz


def test_no_supported_format():
    directory = os.getcwd() + '/i18n' if 'tests' in os.getcwd(
    ) else os.getcwd() + '/tests/i18n'

    with pytest.raises(ValueError):
        Pylocwolowitz(directory, 'format')
