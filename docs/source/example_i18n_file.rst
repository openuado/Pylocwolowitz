Example of i18n file
====================

Store files in the language folder first argument specified when creating the object.

Use YAML format
---------------

Here is an example with one language per file:

.. code-block:: yaml

    ---
    "welcome {name}": "Välkommen {name}"
    "Hello": "Hej"

An example with two language in the same file:

.. code-block:: yaml

    ---
    "welcome {name}":
      "fr": "Bienvenue {name}"
      "en": "Welcome {name}"

Use JSON format
---------------

Here is an example with one language per file:

.. code-block:: json

    {
        "welcome {name}": "Välkommen {name}"
        "Hello": "Hej"
    }



An example with two language in the same file:

.. code-block:: json

   {
       "welcome {name}": {
           "fr": "Bienvenue {name}",
           "en": "Welcome {name}"
       }
   }
