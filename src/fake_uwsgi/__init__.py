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


def log(*args, **kwargs):
    """A wrapper that invokes the built-in print function with the args and kwargs
    passed to this function.
    """
    print(*args, **kwargs)


def set_logvar(*args, **kwargs):
    """Set the log variables.
    If a single argument is passed it will use that as the key and set the value to
    None.
    If two arguments are passed, example set_logvar("key", "value") it will set the key
    (first argument) to the value (second argument)
    If kwargs are provided it will update the log variable dictionary.
    """
    global LOGVAR  # pylint: disable=global-statement

    if len(args) == 1:
        key = args[0]
        LOGVAR[key] = None
    elif len(args) == 2:
        key = args[0]
        val = args[1]
        LOGVAR[key] = val
    elif len(kwargs.keys()) != 0:
        LOGVAR.update(kwargs)


def get_logvar(key):
    """Get the log variable given the key.

    Args:
        key (*): The key for which the value is required

    Returns:
        *: Returns the value in the type it was set. None if its not set.
    """
    return LOGVAR.get(key, None)


def worker_id():
    """Return a predefined worker ID.

    Returns:
        int: The static work id
    """
    return 123


setup_fake_uwsgi()
