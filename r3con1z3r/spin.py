#!/usr/bin/env python
# coding: utf-8
# Author: Domnan
# Deven96
# Twitter: @diretnan
# Github: deven96
# Spinner
from __future__ import print_function
import sys
import time
import multiprocessing

def spinner_func(**kwargs):
    """
    Spinner function for rudimentary spinner
    """
    DELAY = kwargs.get('delay')
    DISPLAY = ['|', '/', '-', '\\']
    write, flush = sys.stdout.write, sys.stdout.flush

    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY)
        msg = kwargs.get('before') + "  " + DISPLAY[pos] + "  " + kwargs.get('after')
        write(msg); flush()
        # clear
        write('\x08' * len(msg))
        time.sleep(DELAY)

def create_spinner(delay=0.1, before='', after=''):
    """
    Runs the function on the main thread while spinner runs on separate process
    Args:
        delay: (float/int) time betweeen rotation of spinner 
        before: (str) message to show before the spinner
        after: (str) message to show after the spinner
    Returns:
        Spinner thread that can be terminated with spinner.terminate() 
    """
    spinner = multiprocessing.Process(None, spinner_func, 
                kwargs={'delay':delay, 
                        'before':before,
                        'after':after})
    return spinner
