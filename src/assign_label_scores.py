# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:34:41 2021

@author: KHC
"""

import pandas as pd
import os

data_path=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data')
results_folder=os.path.join(data_path,'results')
df = pd.read_excel (os.path.join(data_path,'cvs_scores_manual.xlsx'),sheet_name='Sorted', engine='openpyxl')
print (df)

mymap = {'-':0, 'N/C':0, 'aucun':0}

df=df.applymap(lambda s: mymap.get(s) if s in mymap else s)
#df=df.iloc[:, 5:] 

df=df.replace({'-': mymap, 'N/C': mymap})


title_match_w=20
rele_exp_years_w=20
exp_years_w=20
current_position_w=20
qual_w=30
skill_w=30
location_w=10
lang_w=1
contact_w=1


#
df["cv_score"]=df['Job Title Matching'].astype(float)*title_match_w+ \
df['Relevant Experience Match'].astype(float)*rele_exp_years_w+ \
df['Experience years'].astype(float)*exp_years_w + \
df['Current position'].astype(float)*current_position_w + \
df['Qualification'].astype(float)*qual_w+ \
df['Skills'].astype(float)*skill_w+ \
df['Location'].astype(float)*location_w+ \
df['Language'].astype(float)*lang_w+ \
df['Contact Information'].astype(float)*contact_w
df=df[['Job ID','without Ext','cv_score']]


df.to_csv(os.path.join(results_folder, 'cv_scores_manual.csv'))

#df['Location'].values.astype(float)
#df['Langue'].values.astype(int)