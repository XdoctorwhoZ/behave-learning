import os
from behave import fixture

def check_1(filepath):
    assert os.path.isfile(filepath) == True

@fixture
def save_file_check1(context):
    # -- SETUP-FIXTURE PART:
    context.check_function = check_1

    # -- READY FOR THE STEP --
    yield context.check_function

    # -- CLEANUP-FIXTURE PART:

