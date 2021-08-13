# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:59:13 2021

@author: KHC
"""
import pandas as pd

import json
import os
import pickle
import re
import unidecode

def clean_string(sent):
    
    sentence=sent.lower().strip()
    sentence=unidecode.unidecode(sentence)
    #remove multiple spaces
    sentence = re.sub(r"\s+"," ", sentence, flags = re.I)
    sentence = re.sub(r"^\s+", "", sentence)
    sentence = re.sub(r"^\s+", "", sentence)
    return (sentence)
  
            
        
        
sent='BAC+4 ou Ã©quivalant (diplÃ´mÃ© de lâ€™ESB ou Ã‰coles de Commerce, gestion, Ã©conomie, finance et banque, assurance, )'

clean_sent=clean_string(sent)
