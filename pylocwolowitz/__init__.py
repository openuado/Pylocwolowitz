import glob
import json
import re
import os.path
from collections import defaultdict

class Pylocwolowitz(object):

    def __init__(self, path):
        self.path     = path
        self.locales  = defaultdict(dict)
        self._make_loc()

    def _make_loc(self):
        listing = glob.glob(self.path + '/*.json')
        for infile in listing:
            with open(infile) as f:
                data = json.load(f)
                for key, value in data.items():
                    if isinstance(value, dict):
                        self.locales[key].update(value)
                    else:
                        lang = os.path.basename(infile).split('.')[0]
                        self.locales[key].update({lang: value})
        return

    def loc(self, key, lang, values = None):
        '''Return the string key, translated to the requested language (if such a translation exists, otherwise no traslation occurs). Any other parameters passed to the method are injected to the placeholders in the string (if present).'''

        if self.locales[key].get(lang) == None:
            return key

        ret = key in self.locales and self.locales[key][lang] or key
        if values is None:
            values = {}

        return ret % values
