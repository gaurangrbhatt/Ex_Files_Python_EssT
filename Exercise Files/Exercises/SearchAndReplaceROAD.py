#!/bin/python3

import sys
import os
import io
import re

addr = '100 NORTH MAIN ROAD'

raod_pattern = r'\bROAD\b'

match_obj = re.search(raod_pattern, addr)
print(match_obj.group())
if match_obj.group():
    addr = addr.replace(match_obj.group(), 'RD')
print(addr)

