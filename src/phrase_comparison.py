# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 00:14:58 2021

@author: KHC
"""
import pandas as pd 
df = pd.read_csv("features_scores.csv") 

def fab(row):

  return row['total_experience'] + row['total_experience_score']

df['newcolumn'] = df.apply(fab, axis=0)