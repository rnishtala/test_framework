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


import argparse
import sys
import ast
import time
import requests
import simplejson, dict2xml

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

    return (response.json(), response.encoding, response.status_code, session)

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

    parser = argparse.ArgumentParser(description='Request parameters')
    parser.add_argument('-r','--RegionId', help='Region ID of the device', required=True)
    parser.add_argument('-i','--InstanceId', help='Instance ID', required=True)
    args = vars(parser.parse_args())

    region = args['RegionId']
    instanceId = args['InstanceId']

    params["RegionId"] = region
    params["InstanceId"] = instanceId

    logging.info('=============== Start of getCPUutilization ===============')

    (response, encoding, status, session) = getInstanceData(params, service)

    print type(response)
    instance_data = response['MonitorData']['InstanceMonitorData']
    # print instance_data

    for instance in instance_data:
        instance['Time'] = instance.pop('TimeStamp')

    print instance_data[0]

    instance_data[0]['InternetReceive'] = instance_data[0].pop('InternetRX')

    print instance_data[0]

    xmldata = dict2xml.dict2xml(instance_data[0])

    # print xmldata

    logging.info('=============== End of getCPUutilization ===============')
