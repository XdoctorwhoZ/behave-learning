import logging
from behave import *

###############################################################################
###############################################################################

def before_all(context):
    logging.basicConfig(level=logging.DEBUG)
    context.logger = logging.getLogger('example')
    print("+++++++++++++++++ before_all", "\n")

def after_all(context):
    print("+++++++++++++++++ after_all", "\n")

###############################################################################
###############################################################################

def before_feature(context, feature):
    print("+++++++++++++++++ before_feature", feature, "\n")

def after_feature(context, feature):
    print("+++++++++++++++++ after_feature", feature, "\n")

###############################################################################
###############################################################################

def before_scenario(context, scenario):
    print("+++++++++++++++++ before_scenario", scenario, "\n")

def after_scenario(context, scenario):
    print("+++++++++++++++++ after_scenario", scenario, "\n")

###############################################################################
###############################################################################

def before_step(context, step):
    print("+++++++++++++++++ before_step", step, "\n")

def after_step(context, step):
    print("+++++++++++++++++ after_step", step, "\n")

