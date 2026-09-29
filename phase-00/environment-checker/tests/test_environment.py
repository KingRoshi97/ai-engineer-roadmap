import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import main


def test_python_check():
    assert main.check_python() is True


def test_virtual_environment_check():
    assert main.check_virtual_environment() is True


def test_disk_space_check():
    assert main.check_disk_space() is True