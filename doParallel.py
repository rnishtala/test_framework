#!/usr/bin/python
######################################################################################
#  FILENAME:       doParallel.py
#
#  DESCRIPTION:    This script spawns threads and assigns work to them

########################################################################################
# Pre-requisite(s): This script requires
#                          (1) Python's multiprocessing module
########################################################################################

from multiprocessing.pool import ThreadPool
from multiprocessing import Process
import Log
import logging
import time

thread_results = []
ZERO = 0
WAIT_TIME_BETWEEN = 10
def get_result(res):
    """
    Used as a callback function to append

    a global list.
    \param <res>: result from a Thread

    returns none.
    """

    logging.debug('Inside get_result()...')

    thread_results.append(res)

def doParallel(num, func, params_lst, interim_func_lst=[], interim_params_lst=(), cback=get_result):
    """Performs asynchronous tasks by spawning threads

       in a pool and assigns work to them.
       \param <num>: # of Threads to spawn
       \param <func>: Name of function to be fed into each thread
                      [must return value/values]
       \param <params_lst>: List of tuple of arguments to <func>
       \param <interim_func>: Intermediate function to be called [optional]
       \param <interim_params>: Tuple of arguments to interim_func [optional]
       \param <cback>: Name of callback function [optional]

       returns a list of values returned by <func> or [] in case of error
    """

    global thread_results
    thread_results = []

    logging.debug('Inside doParallel()...')
    logging.debug('num = %d, func = %s, params_lst = %s, interim_func_lst = %s, interim_params_lst = %s', num, str(func), str(params_lst), str(interim_func_lst), str(interim_params_lst))

    params_len = len(params_lst)
    if params_len != num:
        logging.error('# %d  of parameter tuples does not match # %d  of threads', num, params_len)
        return []
    tpool = ThreadPool(processes=num)
    try:
        for i in range(num):
            if params_len == 1:
                logging.info("Pool has only one thread")
                async_result = tpool.apply_async(func, params_lst[ZERO], callback=cback)
            else:
                logging.info("Number of threads in pool: "+str(num))
                tpool.apply_async(func, params_lst[i], callback=cback)
        time.sleep(WAIT_TIME_BETWEEN)
        if interim_func_lst != []:
            if len(interim_params_lst) != len(interim_func_lst):
                logging.error('# of Parameter tuples does not match # of Intermediate functions...')
                return []
            interim = ThreadPool(processes=len(interim_func_lst))
            for j in range(len(interim_func_lst)):
                interim.apply_async(interim_func_lst[j], interim_params_lst[j])
            interim.close()
            interim.join()
        if num != 1:
            tpool.close()
            tpool.join()
        else:
            logging.debug('Waiting for the single thread to finish')
            tpool.close()
            tpool.join()
            #thread_results.append(async_result.get())
        logging.debug('Thread results %s', str(thread_results))
        return thread_results
    except KeyboardInterrupt:
        logging.warning('Received ^C. Terminating thread...')
        tpool.terminate()
        logging.warning('Thread results = []')
        return []
