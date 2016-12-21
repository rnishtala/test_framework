# @Author: rnishtala
# @Date:   2016-12-19T09:04:11-05:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-12-19T09:08:39-05:00



#!/usr/bin/python
######################################################################################
#  FILENAME:       utility.py
#
#  DESCRIPTION:    This script contains utility functions for the Leda Test Suite


import os
import datetime
import time
import re
import ntpath
import scp
import sys
import csv
import paramiko

import logging
import doParallel
import CommonConfig
import sqlite3

def hold_off(delay):
    '''
    Wait for specified 'delay'

    \param <none>

    returns none.
    '''
    FREQ = 10
    while delay > 0:
        delay -= 1
        time.sleep(1)
        if delay % FREQ == 0:
            logging.debug('delay %d left...', delay)

def gen_index(length):
    """
    Generates an index in range [0, length) based on today's date

    \param <length>: Length of a list

    returns int in range [0, length).
    """
    return datetime.datetime.now().day % length
