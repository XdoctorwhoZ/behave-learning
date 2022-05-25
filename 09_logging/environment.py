import logging
from behave import *

###################################################################################################
###################################################################################################

def before_all(context):
    if not context._config.log_capture:
        logging.basicConfig(level=logging.DEBUG)

###################################################################################################
###################################################################################################

def before_step(context, step):
    localName = f"{step.location}"
    context.logger = logging.getLogger(localName)