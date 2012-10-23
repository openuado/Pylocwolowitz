import glob
import json
import re
import os.path
from collections import defaultdict


class Pylocwolowitz(object):
    '''Pylocwolitz is a very simple text localization system, meant to be used
    by web applications (but can pretty much be used anywhere). Yes, another
    localization system.'''

    def __init__(self, path):
        self.path = path
        self.locales = defaultdict(dict)
        self._find_file()

    def _find_file(self):
        '''Find all json files'''
        listing = glob.glob(os.path.join(self.path, '*.json'))
        for infile in listing:
            self._make_loc(infile)

    def _make_loc(self, infile):
        '''Store content of the file in a memory'''
        lang = os.path.basename(infile).split('.')[0]
        with open(infile) as fil:
            data = json.load(fil)
        for key, value in data.items():
            if isinstance(value, dict):
                self.locales[key].update(value)
            else:
                self.locales[key].update({lang: value})

    def loc(self, key, lang, values=None):
        '''Return the string key, translated to the requested language (if such
        a translation exists, otherwise no traslation occurs). Any other
        parameters passed to the method are injected to the placeholders in the
        string (if present).'''

        if self.locales[key].get(lang) is None:
            return key

        ret = self.locales[key][lang] if key in self.locales else key
        if values is None:
            return ret
        else:
            return ret % values
