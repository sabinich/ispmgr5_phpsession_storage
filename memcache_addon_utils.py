#!/usr/bin/python
import re
import inspect
import datetime
import sys
import xml.etree.ElementTree as ET
import json
import os
import ConfigParser
import portalocker
from inspect import currentframe, getframeinfo
CONFIG_PARAMS_PATH = "addon/memcache_addon.json"
LOG_PATH = "addon/memcache_addon.log"

#not thread safe
class Log:
        def __init__(self, path):
                pass
		#self.log = open(path, "a")
                #self.write("START ACTION")
        def write(self, string):
                pass
		#(frame, filename, line_number, function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
                #self.log.write("%s %s:%d %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), filename, line_number, string))
