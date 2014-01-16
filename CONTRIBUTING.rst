Choice to use a fairly close process to what is in us in other
Free and Open Source Software projects.

It is recommended for a new developer or contributor to read this document.


Create a ticket
---------------

For all new features or bug fixes, fill a new ticket in the issue
tracker.

Try to be specific in the ticket, with a proper title and description,
if you can provide steps to help the developper to understand the
process or the feature request. Without enough context, it can be
difficult to understand.

The ticket number is then used as a reference for the branch and
commits.


Create a branch
---------------

Except in exceptional cases, a developer must not directly commits in master.

**The rule also applies to project core developers.**

The branch must be prefixed by the ticket number, for example:

.. code-block:: bash

    git pull origin master
    git branch 425-assign_nobody

Don't forget to be update master before creating your new branch from it.


Unit test
---------

Except in exceptional cases, a pull request must come with tests.

It is important to write tests, it's annoying but it pays in the long
run, not regression, refactoring opportunities, and so on.

If this is a bug fix, write a test for this case.

A branch will not merged if there is no test. Learn from the many
existing tests, ask questions if needed.


Code review
-----------

To err is human, several pair of eyes are better than one.

A developer should not merge in the master.

The code must be reviewed by another developer and merged by an
experienced core developer.

It is possible to discuss and point out any mistakes or errors.

If we detect a mistake after the branch as been merged, we will all
work together to fix it as soon as possible.


Hook to exec flake8
-------------------

We want our beautiful code to be PEP8 compliant so it is strongly
recommended to add this pre-commit hook in git
(peopleask/.git/hooks/pre-commit):


.. code-block:: bash

    #!/usr/bin/env bash
    flake8 ./peopleask/

If not pep8 it will not be commiting


Conclusion
----------

It is important to follow up the process. It is not to be annoying,
but it opens the discussion, helps to progress and to have a better
quality of code as well as letting every developer sees and valid
project progress.

Do not take the critic for you, each developer make mistakes and it is
fine.

Despite this process of functional bugs and errors happen and it is
fine as well, never forget it.
