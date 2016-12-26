# @Author: rnishtala
# @Date:   2016-12-19T09:04:11-05:00
# @Last modified by:   rnishtala
# @Last modified time: 2016-12-19T09:08:39-05:00



#!/usr/bin/python
######################################################################################
#  FILENAME:       utility.py
#
#  DESCRIPTION:    This script contains utility functions for the Leda Test Suite
######################################################################################

import os
import datetime
import time
import re
import ntpath
import sys
import csv
import base64
import hashlib
import hmac
import uuid
from requests import compat

import logging
import doParallel
import CommonConfig
import sqlite3

SIGNATURE = "Signature"
SIGNATURE_METHOD = "HMAC-SHA1"
SIGNATURE_VERSION = "1.0"
MD5_CHUNK_SIZE = 1024 * 1024
PERCENT_SAFE = "._-~"
ENCODING = "utf8"

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

def get_signature_params():
    """
    Gets the signature parameters for the query
    return dict: signature parameters
    """
    params = {"SignatureMethod": SIGNATURE_METHOD,
              "SignatureVersion": SIGNATURE_VERSION,
              "SignatureNonce": uuid.uuid4().hex}
    return params

def generate_signature(method, secret_key, params):
    """
    Generates the signature with the SIG_METHOD(HMAC-SHA1)
    :param str method: the query method
    :param str secret_key: the account secret key
    :param dict params: all query parameters
    :return str: base64 encoded string of the hex signature
    """
    query_str = percent_encode(params.items(), True)

    str_to_sign = "{0}&%2F&{1}".format(
        method, percent_quote(query_str)
    )

    sig = hmac.new(
        (secret_key + "&").encode(ENCODING),
        str_to_sign.encode(ENCODING),
        hashlib.sha1
    )
    return base64.b64encode(sig.digest())

def percent_encode(params_tuple, sort=False):
    """
    Percent encode
    :param list params_tuple: the parameters
    :param bool sort: the sort condition for the tuple
    :return str : encoded quote params for query
    """
    if sort:
        params = sorted(params_tuple, key=lambda x: x[0])
    else:
        params = list(params_tuple)

    encoded = "&".join([
        "{0}={1}".format(percent_quote(opt), percent_quote(val))
        for opt, val in params
        if val is not None
    ])
    return encoded

def percent_quote(query):
    """
    Percent quote
    :param str query: the query
    :return str : quote encode for query
    """
    return compat.quote(query.encode(ENCODING), PERCENT_SAFE)
