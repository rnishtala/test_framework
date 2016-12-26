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
import utility

TIME_FMT = "%Y-%m-%dT%XZ"

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

def getInstanceData(params, service, method='GET'):
    """Queries a URL with given parameters

       and prints the results.
       \param <params>: the query parameters
       \param <method>: the query method
       returns JSON data
    """
    logging.debug('In getInstanceData()...')
    session = requests.Session()
    session.headers['Accept-Encoding'] = None
    update_params(params, method)
    response = session.request(
        method,
        SERVICES['ecs'].url,
        params=params
    )

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError

    return (response.content, response.encoding, response.status_code)

def update_params(params, method):
    """
    Updates the given parameters for a service requests

    :param dict params: the query parameters
    :param str method: the query method
    """
    params["AccessKeyId"] = CommonConfig.AccessKeyID
    params.update(utility.get_signature_params())
    if "Format" not in params:
        params["Format"] = "json"
    if "Version" not in params:
        params["Version"] = SERVICES['ecs'].version
    if "Timestamp" not in params:
        params["Timestamp"] = time.strftime(TIME_FMT,
                                            time.gmtime())
    if "Action" not in params:
        params["Action"] = 'DescribeInstanceMonitorData'

    params["StartTime"] = '2016-12-23T20:13:00Z'
    params["EndTime"] = '2016-12-23T20:30:00Z'

    if "Signature" not in params:
        params["Signature"] = utility.generate_signature(method,
                                                         CommonConfig.AccessKeySecret,
                                                         params)

if __name__ == "__main__":

    Log.setup_log('getInstanceData')
    params = {}
    region = ''
    instanceId = ''
    service = ''
    logging.getLogger("requests.packages.urllib3")

    try:
       opts, args = getopt.getopt(sys.argv[1:], "hH:r:i:s:a", ["help", "RegionId=", "InstanceId=", "Service=", "Action="])
    except getopt.GetoptError:
        printUsage()
        sys.exit(2)

    logging.debug('In main()...')

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit(3)
        elif opt in ("-r", "--RegionId"):
            region = arg
            #host = ast.literal_eval(arg);
        elif opt in ("-i", "--InstanceId"):
            instanceId = arg

    params["RegionId"] = region
    params["InstanceId"] = instanceId

    logging.info('=============== Start of getCPUutilization ===============')

    ret_val = getInstanceData(params, service)

    print ret_val

    logging.info('=============== End of getCPUutilization ===============')
