import logging
from behave import *
from fixtures.fixture import save_file_check1

###############################################################################
###############################################################################

def before_all(context):
    logging.basicConfig(level=logging.DEBUG)
    context.logger = logging.getLogger('example')

###############################################################################
###############################################################################

def before_tag(context, tag):
    if tag.startswith("use.file.check1"):
        use_fixture(save_file_check1, context)
        
