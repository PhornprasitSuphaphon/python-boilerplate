import logging

class Logger:
    logger = None  # Class-level logger instance

    @classmethod
    def setupLogger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger(__name__)
            cls.logger.setLevel(logging.DEBUG)

            # Create a file handler
            fileHandler = logging.FileHandler('file.log')
            fileHandler.setLevel(logging.ERROR)

            # Create a console handler
            consoleHandler = logging.StreamHandler()
            consoleHandler.setLevel(logging.DEBUG)

            # Set color codes for level names in console output
            consoleColorCodes = {
                logging.DEBUG: '\033[94m',    # Blue
                logging.INFO: '\033[92m',     # Green
                logging.WARNING: '\033[93m',  # Yellow
                logging.ERROR: '\033[91m',    # Red
                logging.CRITICAL: '\033[91m'  # Red
            }

            # Reset color code
            consoleReset = '\033[0m'

            class ColoredFormatter(logging.Formatter):
                def format(self, record):
                    levelName = record.levelname
                    colorCode = consoleColorCodes.get(record.levelno, '')
                    resetCode = consoleReset if colorCode else ''
                    record.levelname = f"{colorCode}{levelName}{resetCode}"
                    return super().format(record)

            consoleHandler.setFormatter(ColoredFormatter('%(asctime)s [%(levelname)s] %(message)s'))
            fileFormatter = logging.Formatter('%(asctime)s  [%(levelname)s] %(message)s')
            fileHandler.setFormatter(fileFormatter)

            # Add the handlers to the logger
            cls.logger.addHandler(fileHandler)
            cls.logger.addHandler(consoleHandler)

    @classmethod
    def log(cls, level, message):
        cls.setupLogger()
        getattr(cls.logger, level)(message)

    @classmethod
    def debug(cls, message):
        cls.log('debug', message)

    @classmethod
    def info(cls, message):
        cls.log('info', message)

    @classmethod
    def warning(cls, message):
        cls.log('warning', message)

    @classmethod
    def error(cls, message):
        cls.log('error', message)

    @classmethod
    def critical(cls, message):
        cls.log('critical', message)

if __name__ == '__main__':
    Logger.debug('debug message')
    Logger.info('info message')
    Logger.warning('warning message')
    Logger.error('error message')
    Logger.critical('critical message')
