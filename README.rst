##########
Fake uWSGI
##########

.. image:: https://img.shields.io/pypi/pyversions/fake-uwsgi.svg
   :target: https://pypi.org/project/fake-uwsgi
   :alt: Python Versions

.. image:: https://github.com/digimach/fake-uwsgi/workflows/tests/badge.svg?branch=master
   :target: https://github.com/digimach/fake-uwsgi/actions?query=workflow%3Atests+event%3Apush+branch%3Amaster
   :alt: Test Status

.. image:: https://img.shields.io/pypi/l/cookiecutter-python-package
   :target: https://github.com/digimach/fake-uwsgi/blob/master/LICENSE.rst
   :alt: License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://black.readthedocs.io/en/stable/
   :alt: Code Style

.. image:: https://deepsource.io/gh/digimach/fake-uwsgi.svg/?label=resolved+issues
   :target: https://deepsource.io/gh/digimach/fake-uwsgi/?ref=repository-badge

.. image:: https://deepsource.io/gh/digimach/fake-uwsgi.svg/?label=active+issues
   :target: https://deepsource.io/gh/digimach/fake-uwsgi/?ref=repository-badge

.. image:: https://scrutinizer-ci.com/g/digimach/fake-uwsgi/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/digimach/fake-uwsgi/

.. image:: https://www.codefactor.io/repository/github/digimach/fake-uwsgi/badge
   :target: https://www.codefactor.io/repository/github/digimach/fake-uwsgi
   :alt: CodeFactor

.. image:: https://codecov.io/gh/digimach/fake-uwsgi/branch/master/graph/badge.svg?token=HDF2UGHDPU
   :target: https://codecov.io/gh/digimach/fake-uwsgi

A Python module that attempts to fake out the uwsgi module exposed to uWSGI
application. When testing applications outside uWSGI, for example Flask, this module
can provide some functionality of the uwsgi module

``fake_uwsgi`` attempts to replicate APIs and variables that the `uwsgi <https://uwsgi-docs.readthedocs.io/en/latest/PythonModule.html>`_
module exposes to Python applications running in uWSGI.

* GitHub repo: https://github.com/digimach/fake-uwsgi
* Documentation: https://github.com/digimach/fake-uwsgi/blob/master/README.rst

.. contents::

Features
========
* Provides the following `uwsgi module`_ APIs:
    * log
    * set_logvar
    * get_logvar
    * worker_id
    * workers
    * total_requests

* Provides the following `uwsgi module`_ global variables:
    * numproc
    * opt

* Sets the following environment variables:
    * INSTALL_PATH
    * APP_RUN_MODE

Quickstart
==========

In order to make use of Fake uWSGI everywhere ``import uwsgi`` is used has to be
replaced with::

    try:
        # The following import will fail if not running in uWSGI
        import uwsgi  # pylint: disable=import-error
    except ImportError:
        import fake_uwsgi as uwsgi  # pylint: disable-msg=ungrouped-imports

If your code makes use of other APIs and/or global variables that Fake uWSGI does not
expose you have two options:

    1. Monkey patch or expand the ``fake_uwsgi`` module inside your code.
    2. Raise an feature request with this project.

Development
===========

1. This project uses `tox`_ to setup a development environment. Make sure you have
   ``tox`` installed::

        pip install tox

2. Clone this repository

3. You can setup the development environment by running the ``setup-dev`` make rule
   from the project directory::

        make setup-dev

4. You can run tests by doing::

        make test

5. To lint your code::

        make lint

6. To format your code with `Black`_ run::

        make black

.. _Black: https://black.readthedocs.io/en/stable/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _uwsgi module: https://uwsgi-docs.readthedocs.io/en/latest/PythonModule.html
