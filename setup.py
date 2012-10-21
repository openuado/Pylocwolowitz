from distutils.core import setup

setup(
    name = "pylocwolowitz",
    packages = ["pylocwolowitz"],
    version = "0.1",
    description = "Simple localization for web apps with JSON.",
    author = "Natal Ngetal",
    author_email = "hobbestigrou@erakis.im",
    url = "http://pylocwolowitz.readthedocs.org/en/latest/",
    download_url = "",
    keywords = ["i18n", "json"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
Simple localization
-------------------

Pylocwolowitz is a very simple text localization system, meant to be used by web applications (but can pretty much be used anywhere). Yes, another localization system.

This version requires Python 3 or later.
"""
)
