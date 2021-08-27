# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:04:36 2021

@author: KHC
"""

import re
sentence="  how are you. My sajid@eveati.com and sajid@gmail.com "
s = re.sub(r"\s+"," ", sentence, flags = re.I)

lst = re.findall('\S+@\S+', s)   

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

