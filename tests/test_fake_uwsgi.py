"""Test cases fake-uwsgi package"""
import os

import fake_uwsgi


def test_environ():
    """Test the environment values fake_uwsgi should set."""
    assert os.environ.get("INSTALL_PATH") == os.path.abspath(
        os.path.join(fake_uwsgi.__file__, os.pardir)
    )
    assert os.environ.get("APP_RUN_MODE") == "development"


def test_global_variables():
    """Test the global variables set by fake_uwsgi module"""
    assert fake_uwsgi.opt == {"mode": b"development", "vassal-name": b"fake-uwsgi"}

    assert fake_uwsgi.numproc == 4

    assert fake_uwsgi.LOGVAR == dict()
