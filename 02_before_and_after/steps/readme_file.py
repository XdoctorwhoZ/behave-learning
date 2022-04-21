import os
import time
import logging
from behave import *

###############################################################################
###############################################################################

@given('we are working in the 01_print_and_logging directory')
def step(context):
    # Just get the current path
    cwd = os.getcwd()

    # To print do not forget the "\n" at the end
    print(f"Current directory: {cwd}", "\n")
    time.sleep(1)
    
    # Check if the path is a directory, else the test fails
    assert os.path.isdir(cwd) == True

    # Check that the directory has the correct name
    assert os.path.basename(cwd) == '01_print_and_logging'

###############################################################################
###############################################################################

@then('the README file exists')
def step(context):
    logging.basicConfig(level=logging.DEBUG)

    # Create the file path
    filepath = os.path.join(os.getcwd(), 'README.md')

    # Or use the logging module
    logger = logging.getLogger('example')
    logger.info(f"Path of the file README.md: {filepath}")
    time.sleep(1)

    # To print do not forget the "\n" at the end
    print(f"Path of the file README.md: {filepath}", "\n")
    time.sleep(1)

    # Check if the path is a file, else the test fails
    assert os.path.isfile(filepath) == True


