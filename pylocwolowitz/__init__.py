import glob
import json
import re
import os
import codecs
from collections import defaultdict

class Pylocwolowitz(object):
    """Lightweight localization class based on serialized dicts"""

    def __init__(self, path, **option):
        """loads the translation dictionnary
        path: where translation are located
        if codec=value is specified, the codec will be used for reading
            default utf-8
        if format=value is specified, it tells which format to used for dict
            default json (works with yaml)
        """
        self._codec   = option.get("codec","utf-8")
        self._format  = option.get("format","json")
        self.path     = path
        self.locales  = defaultdict(dict)
        self._make_loc()

    def _make_loc(self):
        try:
             dict_loader = __import__(self._format)
        except Exception as e:
             raise Exception("Error while loading format <%s> %s" % (
             self._format,e))
        for infile in os.listdir(self.path):
            if infile.lower().endswith(self._format):
                with codecs.open(
                        os.path.join(self.path,infile),
                        "r", 
                        self._codec
                    ) as f:
                    data = dict_loader.load(f)
                    for key, value in data.items():
                        if isinstance(value, dict):
                            self.locales[key].update(value)
                        else:
                            lang = os.path.basename(infile).split('.')[0]
                            self.locales[key].update({lang: value})
        return

    def loc(self, key, lang, values = None):
        '''Return the string key, translated to the requested language (if such a translation exists, otherwise no traslation occurs). Any other parameters passed to the method are injected to the placeholders in the string (if present).'''

        if self.locales[key].get(lang) is None:
            return key

        ret = key in self.locales and self.locales[key][lang] or key
        if values is None:
            values = {}

        return ret % values
