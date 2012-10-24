.. Pylocwolowitz documentation master file, created by
   sphinx-quickstart on Sat Oct 20 23:35:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

* source: https://github.com/hobbestigrou/Pylocwolowitz
* ticketing: https://github.com/hobbestigrou/Pylocwolowitz/issues
* documentation: http://pylocwolowitz.readthedocs.org/en/latest/

Welcome to Pylocwolowitz's documentation!
=========================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Introduction
============

Pylocwolowitz is a port of the awesome `Locale::Wolowitz`_ module from Perl in Python. It is a very imple text localization system, 
meant to be used by web applications (but can pretty much be used anywhere). 

Yes, this is yet another localization system. 

Pylocwolowitz works with JSON and YAML files.

Each file can serve one or more languages. When creating an instance of this module, you are required to pass a path to a directory where your application's 
JSON localization files are present. These are all loaded and merged into one big dict, which is stored in memory. 
A file with only one language has to be named *<lang>*.json (where *<lang>* is the name of the language, you'd probably want to use the two-letter ISO 639-1 code). 
A file with multiple language can be call fr_and_es.json. The basic idea is to write your application in a base language, 
and use the JSON files to translate text to other languages. For example, lets say you're writing your application in English and translating it to Hebrew, 
Spanish, and Dutch. You put Spanish and Dutch translations in one file, and since everybody hates Israel, you put Hebrew translations alone.

.. _`Locale::Wolowitz`: https://metacpan.org/module/Locale::Wolowitz

Public Method
=============

loc
---

.. code-block:: python

    i18n = Pylocwolowitz('./i18n')
    i18n.loc('hello', 'fr')
    i18n.loc('welcome %(name)s', 'se', {'name': 'hobbestigrou'})

Translated to the requested language, if such a translation exists, otherwise no translation occurs.

.. code-block:: python

    input: (Str): Key translate
           (Str): Language to translate
           (Dict): Arguments are injected to the placeholders in the string
    output: (Str): Translated to the requested language
