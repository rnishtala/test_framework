#!/usr/bin/python
######################################################################################
#  FILENAME:       AliyunQuery.py
#
#  DESCRIPTION:    AliyunQuery queries the Aliyun ECS instance data
#

########################################################################################
# Pre-requisite(s): This script requires
#
########################################################################################


import abc
from TestBase import TestBase
import os

import CommonConfig
import logging
import Log
import getInstanceData
import utility
import doParallel
import csv

class AliyunQuery(TestBase):

    """
    Class inheriting from TestBase executes Aliyun Query for ECS instances
    """

    def __init__(self):
        self.HTTP_SUCCESS = 200
        self._params = {"RegionId": CommonConfig.hosts[0][0], "InstanceId": CommonConfig.hosts[0][1]}

    def setup(self):
        """
        Set up the test scenario
        """
        logging.debug('Inside setup()...')


        if os.path.exists(CommonConfig.summary_file['AliyunQuery']+'.csv'):
            os.remove(CommonConfig.summary_file['AliyunQuery']+'.csv')
        return True

    def run(self):
        """
        Run the the test scenario
        """
        logging.debug('Inside run()...')
        params = {}
        return doParallel.doParallel(1,getInstanceData.getInstanceData,[(self._params, 'ecs', 'GET')])

    def analyze(self, results):
        """
        Analyze the results
        """
        if results[0][2] == self.HTTP_SUCCESS:
            return 'PASS'


    def cleanup(self):
        """
        Clean up after the test finishes
        """
        logging.debug('Inside cleanup()...')
