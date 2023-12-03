#!/usr/bin/env python3

import os
import re
import sys
import yaml

import xlrd
import xlwt
import pandas as pd
import numpy  as np



document = """
  a: 1
  b:
    c: 3
    d: 4
"""
#print yaml.dump(yaml.load(document))
d = yaml.load(document, Loader=yaml.FullLoader)

print(d["a"])
print(d["b"]["c"])

print(yaml.dump(d))

e = pd.read_excel("/home/kuiliang/Documents/scan_plan.xls", header=None)
#xlrd.open_workbook("/home/kuiliang/Documents/scan_plan.xls")
print(e)

