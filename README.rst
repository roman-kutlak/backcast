Current Status |build|
======================

.. |build| image:: https://travis-ci.org/roman-kutlak/backcast.svg?branch=master
    :target: https://travis-ci.org/roman-kutlak/backcast


Intro
=====

Backcast is a tiny example of a symbolic natural language generation system
that uses the python library nlglib_ and the java realiser SimpleNLG.

The main purpose of Backcast is to show how one might use nlglib_ to create
a simple NLG system.


Installation
============

Download the code from the repository and run `python setup.py install`
or `pip install .`.


Execution
============

There is a `main` function in the module `backcast.main`
setuptools should also create a shell script `backcast`
which invokes the function. If you installed `backcast`
into a virtual env, activate the environment
and you should have the command `backcast` available.
If this doesn't work, try to run `python -m backcast.main`.


Audience
========

Mainly people interested in natural language generation, of course.


.. _nlglib: https://github.com/roman-kutlak/nlglib
