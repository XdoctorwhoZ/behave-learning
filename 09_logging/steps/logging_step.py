import logging
from behave import *
from fixtures.script_logging import random_logging

###############################################################################
###############################################################################

@step(u'{word:w} step passes')
def step_pass(context, word):
    context.logger.info(f"{word} step passes")

###############################################################################
###############################################################################

@step(u'{word:w} step fails')
def step_fail(context, word):
    context.logger.error(f"{word} step fails")
    context.failed = True

###############################################################################
###############################################################################

@step(u'a script log data')
def step_log(context):
    script = random_logging()
    script.log()

