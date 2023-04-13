import sys

from src.client import is_args_present

def test_is_args_present_no_args():
    # Test case where there are no additional arguments provided to the command line interface
    sys.argv.clear()
    sys.argv = ["test_script.py"]
    result : bool = is_args_present()
    assert result == False

def test_is_args_present():
    # Test case where arguments are present
    sys.argv.clear()
    sys.argv = ["client.py", "true"]
    result : bool = is_args_present()
    assert result == True
