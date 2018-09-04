#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from configparser import ConfigParser, ExtendedInterpolation
from os.path import expanduser


def read_params(fname='config.ini'):
   config = ConfigParser(inline_comment_prefixes='#')
   config._interpolation = ExtendedInterpolation()
   config.read(fname)
   N = int(config['parameters']['N'])
   t0 = int(config['parameters']['t0'])    # Record every t0 seconds
   f = expanduser(config['parameters']['f_data'])
   return N,t0,f

