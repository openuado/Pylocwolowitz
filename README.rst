Introduction
============
Pylocwolowitz is a port of the awesome `Locale::Wolowitz`_ module from Perl in
Python. It is a very simple text localization system, meant to be used by web
applications (but can pretty much be used anywhere).

Yes, this is yet another localization system.

Pylocwolowitz works with JSON and YAML files.

Each file can serve one or more languages. When creating an instance of this
module, you are required to pass a path to a directory where your application's
JSON localization files are present. These are all loaded and merged into one
big dict, which is stored in memory. A file with only one language has to be
named *<lang>*.json (where *<lang>* is the name of the language, you'd probably
want to use the two-letter ISO 639-1 code).  A file with multiple language can
be call fr_and_es.json. The basic idea is to write your application in a base
language, and use the JSON files to translate text to other languages. For
example, lets say you're writing your application in English and translating it
to Hebrew, Spanish, and Dutch. You put Spanish and Dutch translations in one
file, and since everybody hates Israel, you put Hebrew translations alone.

.. _`Locale::Wolowitz`: https://metacpan.org/module/Locale::Wolowitz


Example:

.. code-block:: python

    from pylocwolowitz import Pylocwolowitz
    i18n = Pylocwolowitz('./i18n')
    i18n.loc('hello', 'fr')
    i18n.loc('welcome {name}', 'se', {'name': 'hobbestigrou'})

