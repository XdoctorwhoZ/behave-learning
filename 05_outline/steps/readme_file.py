import os
import time
import logging
from behave import *

###############################################################################
###############################################################################

# Required to parse arguments in steps, for example "{thing}"
use_step_matcher("parse")

###############################################################################
###############################################################################

@given('we are working in the "{example_directory}" directory')
def step(context, example_directory):
    # Just get the current path
    context.cwd = os.getcwd()

    # To print do not forget the "\n" at the end
    print(f"Current directory in context: {context.cwd}", "\n")
    
    # Check if the path is a directory, else the test fails
    assert os.path.isdir(context.cwd) == True

    # Check that the directory has the correct name
    assert os.path.basename(context.cwd) == example_directory

###############################################################################
###############################################################################

@then('the "{the_file}" file exists')
def step(context, the_file):
    # Check that cwd is in this scenario
    assert hasattr(context, 'cwd')
    
    # Create the file path
    filepath = os.path.join(context.cwd, the_file)

    # Or use the logging module
    context.logger.info(f"Path of the file {the_file}: {filepath}")

    # To print do not forget the "\n" at the end
    print(f"Path of the file {the_file}: {filepath}", "\n")

    # Check if the path is a file, else the test fails
    assert os.path.isfile(filepath) == True

###############################################################################
###############################################################################

@given('the context does not contain cwd from the last scenario')
def step(context):
    # Check that cwd is not in this scenario
    assert not hasattr(context, 'cwd')
