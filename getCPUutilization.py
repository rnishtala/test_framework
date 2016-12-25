# @Author: rnishtala
# @Date:   2016-12-19T09:04:11-05:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-12-19T09:06:09-05:00



################################################################################
#
# FILE NAME: getCPUutilization.py
#
# DESCRIPTION: Gets CPU utilization for instances.
################################################################################


import getopt
import sys
import ast
import time
import requests

import CommonConfig
from CommonConfig import SERVICES
import logging
import Log

def printUsage():
    ''' Prints the usage of main().

        \param: none

        returns none.
    '''
    logging.debug('In printUsage()...')
    print "Usage: python getCPUutilization.py -i <instanceId> -r <region>"

def get_credentials():
    """ Obtains the login credentials from CommonConfig.

        \param <ip>: IPv4 Address of remote machine

        returns tuple: (username, password) if <ip> is found. Else, returns (None,None)
    """
    return (CommonConfig.AccessKeyID, CommonConfig.AccessKeySecret)

def getCPUutilization(params, method='GET', service):
    """Queries a URL with given parameters

       and prints the results.
       \param <params>: the query parameters
       \param <method>: the query method
       returns JSON data
    """
    logging.debug('In getCPUutilization()...')
    session = requests.Session()
    session.headers['Accept-Encoding'] = None
    update_params(params, method)
    response = session.request

def update_params(params, method):
    pass

if __name__ == "__main__":

    Log.setup_log('getCPUutilization')
    params = {}

    try:
       opts, args = getopt.getopt(sys.argv[1:], "hH:r:i:s:", ["help", "RegionId=", "InstanceId=", "Service="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)

    logging.debug('In main()...')

    for opt, arg in opts:
        print 'YES'
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit(3)
        elif opt in ("-r", "--RegionId"):
            region = arg
            #host = ast.literal_eval(arg);
        elif opt in ("-i", "--InstanceId"):
            instanceId = arg
        elif opt in ("-s", "--Service"):
            service = arg

    params["RegionId"] = region
    params["InstanceId"] = instanceId

    logging.info('=============== Start of getCPUutilization ===============')

    ret_val = getCPUutilization(params, service)

    print ret_val

    logging.info('=============== End of getCPUutilization ===============')
