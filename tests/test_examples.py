"""
Runs and tests everything in the examples folder.
"""

import pytest
import glob
import runpy
import os
import psyneulink
import sys


example_scripts = glob.glob("examples/**/*.py", recursive=True)
example_exclusion_strings = [".reconstructed.py", "generate_json_and_scripts.py"]

# NOTE: xfail mark can be removed if/when a full TimeInterval or
# placeholder class reaches main psyneulink branch. This is only a
# concern for local/non-github-actions installations.
example_scripts = [
    pytest.param(
        script,
        marks=pytest.mark.xfail(
            reason="psyneulink currently must be installed on its 'mdf' branch to work with MDF examples",
            strict=False,
        ),
    )
    if (
        "PsyNeuLink" in os.path.dirname(os.path.realpath(script))
        and not hasattr(psyneulink, "TimeInterval")
    )
    else script
    for script in example_scripts
    if all(e not in script for e in example_exclusion_strings)
]


@pytest.fixture(autouse=True)
def chdir_back_to_root():
    """
    This fixture sets up and tears down state before each example is run. Certain examples
    require that they are run from the local directory in which they reside. This changes
    directory and adds the local directory to sys.path. It reverses this after the test
    finishes.
    """

    # Get the current directory before running the test
    cwd = os.getcwd()
    sys.path.append(".")

    yield

    # We need chdir back to root of the repo
    os.chdir(cwd)
    sys.path.pop()


@pytest.mark.parametrize("script", example_scripts)
def test_example(script):
    """
    Run the examples/MDF
    """
    # Get the full path for the script
    script = os.path.abspath(script)

    # Some of the scripts in examples/MDF import from the local directory. So lets run from the scripts
    # local directory.
    dir_path = os.path.dirname(os.path.realpath(script))
    os.chdir(dir_path)

    runpy.run_path(script, run_name="__main__")
