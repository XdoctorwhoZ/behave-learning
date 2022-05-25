import logging

class random_logging:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.level = logging.INFO

#########################################################################################################
#########################################################################################################
    def log(self):
        self.logger.warning("this is a warning")
        self.logger.debug("this is a debug")
        self.logger.info("this is an info")
