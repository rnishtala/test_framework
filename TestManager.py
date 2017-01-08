# @Author: rnishtala
# @Date:   2016-12-19T09:04:11-05:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-12-19T09:08:28-05:00



#!/usr/bin/python
#########################################################################################################
#  FILENAME:       TestManager.py
#
#  DESCRIPTION:    Controller script that executes a list of tests and returns their results in PASS / FAIL format.
#
"""
This script is a controller script that executes a list of tests and returns their results in PASS / FAIL format.
"""

import TestConfig
import os
import Log
import logging
import utility
import subprocess
import datetime
import csv
import pdb

def clean():
    """
    Invokes cleanup() of each test
    """

    TestConfig.TESTS[num].cleanup()
    combineLogs()

    for t in range(num, num_of_tests):
        print "Test #", t+1, "[",  TestConfig.TESTS_MAPPING[str(TestConfig.TESTS[t]).split('.')[0][1:]], "]:\tFAIL"
        logging.info('Test # %d [ %s ]: FAIL', t+1, TestConfig.TESTS_MAPPING[str(TestConfig.TESTS[t]).split('.')[0][1:]])

    print " "
    print "TOTAL # of tests:", num_of_tests
    logging.info('TOTAL # of tests: %d', num_of_tests)
    print "PASSED:", num_pass
    logging.info('PASSED: %d', num_pass)
    print "FAILED:", num_of_tests - num_pass
    logging.info('FAILED: %d', num_of_tests - num_pass)
    print " "
    for i in range(len(results)):
        logging.info('Test # %d [ %s ]: %s',results[i][1],results[i][0],results[i][2])

def combineLogs():
    """
    Moves the latest test run's log and the latest syslog
    to a directory (Format is Time)
    """

    # Make a directory with the timestamp in the latest Leda log filename
    # Move the latest Leda log and the latest SYSLOG logs to the above created directory
    cmd = "cd " + TestConfig.LOG_LOC + "; dir=$(ls -ltr Leda*.log | awk '{print $9}' | sed s/Leda_//g | sed s/.log//g); mkdir $dir; FILES1=$(ls -ltr Leda*.log | awk '{printf \"%s \", $9}'); for f in $FILES1; do mv $f $dir; done; FILES2=$(ls -al SYSLOG*.zip | awk '{printf \"%s \", $9}'); for f in $FILES2; do mv $f $dir; done"
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    """
    Calling the scripts depending on Tests List in TestConfig
    """

    try:
        num = 0
        results = []
        num_pass = 0
        num_of_tests = len(TestConfig.TESTS)

        Log.setup_log('Leda')

        print "Executing", num_of_tests,"Test(s)...\n"
        logging.info('Obtained %d Test(s) to execute...', num_of_tests)
        logging.info('Invoking these tests %s ', str(TestConfig.TESTS))

        for test in TestConfig.TESTS:
            Test_Name = TestConfig.TESTS_MAPPING[str(TestConfig.TESTS[num]).split('.')[0][1:]]
            logging.info('================================== BEGIN OF %s ==================================', Test_Name)
            if test.performTest(str(TestConfig.TESTS[num]).split('.')[0][1:]) != "PASS":
                logging.debug('Completed PerformTest')
                results.append((Test_Name, num+1, 'FAIL'))
                print "Test #", num+1, "[",  Test_Name, "]:\tFAIL"
                logging.info('Test # %d [ %s ]: FAIL', num+1, Test_Name)
            else:
                logging.debug('Completed PerformTest')
                results.append((Test_Name, num+1, 'PASS'))
                print "Test #", num+1, "[", Test_Name, "]:\tPASS"
                logging.info('Test # %d [ %s ]: PASS', num+1, Test_Name)
                num_pass += 1
            num += 1
            logging.info('================================== END OF %s ==================================', Test_Name)

        print " "
        print "TOTAL # of tests:", num_of_tests
        logging.info('TOTAL # of tests: %d', num_of_tests)
        print "PASSED:", num_pass
        logging.info('PASSED: %d', num_pass)
        print "FAILED:", num_of_tests - num_pass
        logging.info('FAILED: %d', num_of_tests - num_pass)

    except KeyboardInterrupt:
        print "Detected ^C. Invoking cleanup()..."
        logging.warning('Detected ^C. Invoking cleanup()...')
        clean()
    except Exception, err:
        logging.critical('============ Exception ============')
        logging.critical(str(err))
        logging.critical('========================================')
        print "EXCEPTION: ", str(err)
        clean()
