## -*- coding: utf-8 -*-
"""
#Created on Mon May 31 17:53:21 2021

#@author: KHC
"""

import pandas as pd

import json

df = pd.read_excel ('jd_cvs.xlsx',sheet_name='Sorted')

 
cvs_jds_dict= dict()
df['job_id'] = df['Job ID'].map(str)
#jd_ids=[]
jd_ids=df["job_id"].to_list()
jd_ids=list(set(jd_ids))
for j_id in jd_ids:
#    cvs_jds_dict[j_id]=[]
    df1=df.loc[df['job_id'] == j_id]
    cvs_jds_dict[j_id]=list(df1['Resume File ID'].values)



    
    
#with open('jds1.json', 'r', encoding="cp866") as input_file:
with open('jds1.json', 'r', encoding="utf") as input_file:
    jd_data = input_file.read()
    jd_list = json.loads(jd_data)
    
    

#with open('data.json') as json_file:
#    data = json.load(json_file)

#
#for row in rng:
#    # your code
#    ...
#
#    # new code
#    d[row] = result
#
#
#for i in range(len(df)) :
#  print(df.loc[i, "Job ID"], df.loc[i, "Resume File ID"])
#  
#df1=df.loc[df['job_id'] == '5835']
#  
  
  
#for index, row in df.iterrows():
#    print(row['Location'], row['Langue'],row['Job ID'])