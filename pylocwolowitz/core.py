"""Locolazation system."""
import glob
import os.path
from collections import defaultdict


class Pylocwolowitz(object):

    """Pylocwolitz is a very simple text localization system.

    Pylocwolitz is a very simple text localization system, meant to be used
    by web applications (but can pretty much be used anywhere). Yes, another
    localization system.

    :param path: File path translation
    :type path: str
    :param format_deserializer: Indicate the serializer to use json or yaml
    :type format_deserializer: str
    :raises ValueError: Format not supported, only json or yaml.
    """

    def __init__(self, path, format_deserializer='json'):
        """To init the locolization system."""
        if format_deserializer not in ('json', 'yaml'):
            raise ValueError('FormatNotSupported')

        self.path = path
        self.format_deserializer = format_deserializer
        self.locales = defaultdict(dict)
        self._find_file()

    def _find_file(self):
        """Find all json files."""
        listing = glob.glob(
            os.path.join(self.path, '*.' + self.format_deserializer))

        for infile in listing:
            self._make_loc(infile)

    def _make_loc(self, infile):
        """Store content of the file in a memory."""
        lang = os.path.basename(infile).split('.')[0]

        if self.format_deserializer == 'json':
            import json
            with open(infile) as fil:
                data = json.load(fil)
        else:
            import yaml
            with open(infile) as fil:
                data = yaml.load(fil)

        for key, value in data.items():
            if isinstance(value, dict):
                self.locales[key].update(value)
            else:
                self.locales[key].update({lang: value})

    def loc(self, key, lang, values=None):
        """Get the translate.

        Return the string key, translated to the requested language (if such
        a translation exists, otherwise no traslation occurs). Any other
        parameters passed to the method are injected to the placeholders in the
        string (if present).

        :param key: Key translate
        :type key: str
        :param lang: Language to translate
        :type lang: str
        :param values: Arguments are injected to the placeholders in the string
        :type values: dict
        :returns: Translated to the requested language
        :rtype: str
        """
        if self.locales[key].get(lang) is None:
            return key

        ret = self.locales[key][lang] if key in self.locales else key
        if values is None:
            return ret
        else:
            return ret.format(**values)
