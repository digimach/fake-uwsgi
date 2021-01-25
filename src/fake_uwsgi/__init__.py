"""
This is module attempts to fake out the uwsgi module provided by uWSGI when running
a Python application in uWSGI.

To use this put the following in the module that requires the uwsgi module:

try:
    # The following import will fail if not running in uWSGI
    import uwsgi  # pylint: disable=import-error
except ImportError:
    import fake_uwsgi as uwsgi  # pylint: disable-msg=ungrouped-imports
"""

import os
import time

__version__ = "0.1.0"

opt = numproc = LOGVAR = IMPORT_TIME = None  # pylint: disable=invalid-name


def setup_fake_uwsgi():
    """
    Setup the fake uWSGI. This function is called upon import by the module itself.
    """
    global opt  # pylint: disable=invalid-name,global-statement
    global numproc  # pylint: disable=invalid-name,global-statement
    global LOGVAR  # pylint: disable=global-statement
    global IMPORT_TIME  # pylint: disable=global-statement

    os.environ["INSTALL_PATH"] = os.path.abspath(os.path.join(__file__, os.pardir))
    os.environ["APP_RUN_MODE"] = "development"
    opt = {"mode": b"development", "vassal-name": b"fake-uwsgi"}

    numproc = 4

    LOGVAR = dict()
    IMPORT_TIME = time.time()

setup_fake_uwsgi()
