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
import execRemoteCommand
import utility
import doParallel
import sqlite3
import csv

class AliyunQuery(TestBase):

    """
    Class inheriting from TestBase executes Aliyun Query for ECS instances
    """
    website_to_ping = []

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
        return doParallel.doParallel(1,getECSinstances.getECSinstances,[(hostname, ecsid, 'us-east-1')])

    def analyze(self, results):
        """
        Analyze the results
        """
        pass

    def cleanup(self):
        """
        Clean up after the test finishes
        """
        logging.debug('Inside cleanup()...')
