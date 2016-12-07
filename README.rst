Example Project: CSV Wrangler
=============================

This is a small example project about reading in a column from a CSV file and
computing some simple statistic based on it.

It has some unit tests using unittest, it has a tox.ini for running unit tests
on both Python 2 and 3 in separate virtual environments and another one for
testing the style with pep8. It should be easy to add support for running
coverage tests (and maybe we will in the future). Some unit tests are simple
and others contain more complex structures like patching and StringIO.

It should be trivial to plug this system into e.g. Jenkins or Travis for
testing.

The library has been put into a Python module that also contains one runner
script. Other parts of the library can be reused to extend the functionality
in one way or another.

Docstrings could be improved on to make this an example about documenting a
project using Sphinx.

This can be the goal of several days of working on the same project.
Alternatively it can be expaned upon as an example.

Testing
-------

To run tests run::

        $ tox

This will run code style tests and unit tests against chosen Python versions
(2.7 and 3.5, see tox.ini).


