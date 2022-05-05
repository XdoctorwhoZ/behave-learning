import os
import time
import logging
from behave import *
from hamcrest import assert_that, equal_to, has_property, is_not

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
    assert_that(os.path.isdir(context.cwd), equal_to(True))
    # --
    # assert_that(os.path.isdir(context.cwd), is_not(equal_to(True)))
    # --

    # Check that the directory has the correct name
    assert_that(os.path.basename(context.cwd), equal_to(example_directory))
    # --
    # assert_that(os.path.basename(context.cwd), is_not(equal_to(example_directory)))
    # --

###############################################################################
###############################################################################

@then('the "{the_file}" file exists')
def step(context, the_file):
    # Check that cwd is in this scenario
    assert_that(context, has_property('cwd'))
    
    # Create the file path
    filepath = os.path.join(context.cwd, the_file)

    # Or use the logging module
    context.logger.info(f"Path of the file {the_file}: {filepath}")

    # To print do not forget the "\n" at the end
    print(f"Path of the file {the_file}: {filepath}", "\n")

    # Check if the path is a file, else the test fails   
    context.check_function(filepath)

###############################################################################
###############################################################################

@given('the context does not contain cwd from the last scenario')
def step(context):
    # Check that cwd is not in this scenario
    assert_that(context, is_not(has_property('cwd')))

