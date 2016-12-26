#!/usr/bin/python
#########################################################################################
#  FILENAME:       TestBase
#
#  DESCRIPTION:    An absract class for Test Suite implementation
#
########################################################################################
"""
TestBase - An abstract base class to be inherited by different Test scripts
"""

import abc
from abc import ABCMeta
import subprocess

import utility

class TestBase:
    __metaclass__ = ABCMeta

    # Protected Variable
    _simplex_flag = False

    @abc.abstractmethod
    def setup(self):
        """
        Set up the test scenario
        """
        raise NotImplementedError
        return

    @abc.abstractmethod
    def run(self):
        """
        Run the the test scenario
        """
        raise NotImplementedError
        return

    @abc.abstractmethod
    def analyze(self, results, status):
        """
        Analyze the results of test
        """
        raise NotImplementedError
        return

    @abc.abstractmethod
    def cleanup(self):
        """
        Clean up after the test finishes
        """
        raise NotImplementedError

    #@abc.abstractmethod
    def performTest(self, LOG_TAG):
        """
        Call setup, run and cleanup funtions in order
        """
        outcome = 'FAIL'
        result = []

        if self.setup():
            result = self.run()
            outcome = self.analyze(result)
        self.cleanup()
        return outcome
