Python Classifiers
##################

The package provides PyPI with a list of "trove classifiers" to categorize each
release, describing the target audience, what systems it can run on, and how mature it
is.

There are `Standardized Classifiers <https://pypi.org/classifiers/>`_ that can be used
to define projects based on their desired criteria.

Instructions for how to add trove classifiers to a project can be found on the
`Python Packaging User Guide <https://packaging.python.org/tutorials/distributing-packages/>`_. 

To read the original classifier specification, refer to `PEP 301 <https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification>`_.

For this project classifiers are added to the ``setup.cfg`` file under ``metadata``.

The project should already have valid classifiers and example of situations where
classifiers would need to be updated:

1. The Development Status changes for the project i.e. going from Beta to Production.

2. The licensing terms change for the project.

3. The supported Python version is either included or excluded.

4. The Topic, Environment or Framework is modified during the development cycle
   of the project.