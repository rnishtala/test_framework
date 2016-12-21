# @Author: rnishtala
# @Date:   2016-12-19T09:04:11-05:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-12-19T09:06:09-05:00



################################################################################
#
# FILE NAME: execRemoteCommand.py
#
# DESCRIPTION: Gets Aliyun ECS instances.
################################################################################


import getopt
import sys
import ast
import time
import select

import paramiko

import CommonConfig
import logging
import Log

def printUsage():
    ''' Prints the usage of main().

        \param: none

        returns none.
    '''
    logging.debug('In printUsage()...')
    print "Usage: python getECSinstances.py -c <id> -H <host>"

def get_credentials():
    """ Obtains the login credentials from CommonConfig.

        \param <ip>: IPv4 Address of remote machine

        returns tuple: (username, password) if <ip> is found. Else, returns (None,None)
    """
    return (CommonConfig.AccessKeyID, CommonConfig.AccessKeySecret)

def getECSinstances(hostname, id, region):
    """Executes the given command (cmd) on a remote machine

       and prints the results.
       \param <hostname>: hostname
       \param <id>: id of the instance
       \param <region>

       returns JSON data
    """
    logging.getLogger("paramiko").setLevel(logging.WARNING)
    logging.debug('In getECSinstances()...')

if __name__ == "__main__":

    Log.setup_log('execRemoteCommand')

    try:
       opts, args = getopt.getopt(sys.argv[1:], "hH:c:r:", ["help", "Host=", "id=", "region="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)

    logging.debug('In main()...')

    for opt, arg in opts:
        print 'YES'
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit(3)
        elif opt in ("-H", "--Host"):
            host = arg
            #host = ast.literal_eval(arg);
        elif opt in ("-c", "--id"):
            ecsid = arg
        elif opt in ("-r", "--region"):
            region = arg
    logging.info('=============== Start of getECSinstances ===============')

    print hostname
    ret_val = getECSinstances(host, ecsid, region)
    logging.info('=============== End of getECSinstances ===============')
