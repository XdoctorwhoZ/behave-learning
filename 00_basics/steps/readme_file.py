import os
from behave import *

###############################################################################
###############################################################################

@given('we are working in the 00_basics directory')
def step(context):
    # Just get the current path
    cwd = os.getcwd()

    # Check if the path is a directory, else the test fails
    assert os.path.isdir(cwd) == True

    # Check that the directory has the correct name
    assert os.path.basename(cwd) == '00_basics'

###############################################################################
###############################################################################

@then('the README file exists')
def step(context):
    # Create the file path
    filepath = os.path.join(os.getcwd(), 'README.md')
    
    # Check if the path is a file, else the test fails
    assert os.path.isfile(filepath) == True


