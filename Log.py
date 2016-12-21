################################################################################
#
# FILE NAME: Log.py
#
# DESCRIPTION: Perform Log file setup with python's Logging Module
#

##################################################################
# Pre-requisite(s): This script requires CommonConfig.py
##################################################################

'''This script performs logging setup based on some configuration.

   returns none.
'''

import sys
import os
import CommonConfig
import logging
import datetime

log_level = CommonConfig.CURR_LOG_LEVEL

def create_log(log_string):
    '''Creates a log file.

       \param <log_string>: an arbitrary string

       returns <log_string>_<Timestamp>.log or "ERR"
    '''

    log_file = CommonConfig.LOG_FILE_LOCATION + log_string + "_" + \
            datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".log"
    if not os.path.exists(log_file):
        open(log_file, 'w').close()
        return log_file

    return "ERR"

def setup_log(log_string):
    '''Performs basic logging setup.

       \param <log_string>: an arbitrary string

       returns none.
    '''

    try:
        # Create Log if it does not exist
        log_file = create_log(log_string)

        if log_file != "ERR":
            # Configure Log settings
            if log_level not in CommonConfig.VALID_LOG_LEVELS or log_level == 4:
                logging.basicConfig(filename=log_file, format='%(asctime)s [ {%(threadName)s} %(levelname)s:%(module)s:%(lineno)d]: %(message)s', \
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
            elif log_level == 1:
                logging.basicConfig(filename=log_file, format='%(asctime)s [ {%(threadName)s} %(levelname)s:%(module)s:%(lineno)d]: %(message)s', \
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.CRITICAL)
            elif log_level == 2:
                logging.basicConfig(filename=log_file, format='%(asctime)s [ {%(threadName)s} %(levelname)s:%(module)s:%(lineno)d]: %(message)s', \
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.ERROR)
            elif log_level == 3:
                logging.basicConfig(filename=log_file, format='%(asctime)s [ {%(threadName)s} %(levelname)s:%(module)s:%(lineno)d]: %(message)s', \
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.WARNING)
            else:
                logging.basicConfig(filename=log_file, format='%(asctime)s [ {%(threadName)s} %(levelname)s:%(module)s:%(lineno)d]: %(message)s', \
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
        else:
            print "oops ... log file generation failed"
    except Exception, err:
        print str(err)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: python Log.py <string : some string to identify your log>"
        sys.exit(1)
    setup_log(sys.argv[1])
