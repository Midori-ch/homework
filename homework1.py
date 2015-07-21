# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:11:46 2015
@author: vk
"""

math_ok = {
    'Tom',
    'John',
    'Mary',
    'Jimmy',
    'Sunny',
    'Amy'
}

eng_ok = {
    'John',
    'Mary',
    'Tony',
    'Bob',
    'Pony',
    'Tom',
    'Alice'
}

mathok_but_efail = (math_ok - eng_ok)
engok_but_mfail = (eng_ok - math_ok)
all_pass = (math_ok & eng_ok)
members = (len(math_ok | eng_ok))

print (('Math pass but english fail: [%s]') % (mathok_but_efail))
print (engok_but_mfail)
print (all_pass)
print (members)
