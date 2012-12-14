Exemple of i18n file
====================

Store files in the language folder first argument specified when creating the object.

Use YAML format
---------------

Here is an example with one language per file:

.. code-block:: yaml

    ---
    "welcome %(name)s": "Välkommen %(name)s"
    "Hello": "Hej"

An example with two language in the same file:

.. code-block:: yaml

    ---
    "welcome %(name)s":
      "fr": "Bienvenue %(name)s"
      "en": "Welcome %(name)s"

Use JSON format
---------------

Here is an example with one language per file:

.. code-block:: json

    {
        "welcome %(name)s": "Välkommen %(name)s"
        "Hello": "Hej"
    }



An example with two language in the same file:

.. code-block:: json

   {
       "welcome %(name)s": {
           "fr": "Bienvenue %(name)s",
           "en": "Welcome %(name)s"
       }
   }
