import pytest

from mynotebook.console import *


def test_main():
    assert main() == "Successfully imported the modules!"
