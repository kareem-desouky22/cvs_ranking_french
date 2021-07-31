# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:51:27 2021

@author: KHC
"""

import pandas as pd

import json
import os
import pickle

data_path=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data')
results_folder=os.path.join(data_path,'results')

with open(os.path.join(data_path,'jds3.json'),encoding="utf8") as f:
  data = json.load(f)
  
df_jd=pd.DataFrame(data)
df_jd['qualifications_jd']=df_jd.qualification.str.split("|")


# using split to convert them to list items
#titles=df_jd['jobTitle'].values.tolist()
df_jd['jobTitle']=df_jd['jobTitle'].str.split(":")
df_jd['location_jd']=df_jd['locations'].str.split(":")
df_jd.drop(['jobDescription','qualification','roleDesignation','unit','industry'],axis=1, inplace=True)


file = open(os.path.join(results_folder,'clean_df.pickle'), 'rb')
df_cvs = pickle.load(file)
file.close()  
#df_cvs =pd.read_csv(os.path.join(results_folder,'clean_features.csv'),  index_col=0)
df_cvs['name'] = df_cvs['name_cv'].str.lower()
#data=data.drop(['name'],axis=1)
#data=data.fillna(0)

  

  
#jd_cvs =pd.read_excel('jd_cvs_1.xlsx')
jd_cvs =pd.read_csv(os.path.join(results_folder,'cv_scores_manual.csv'))
jd_cvs['cv_name'] = jd_cvs['without Ext'].str.lower()
#jd_cvs.drop_duplicates(subset ="cv_name",
#                     keep = "first", inplace = True)
#jd_cvs=jd_cvs[['Job ID','cv_name']]


#merged_df = df_cvs.merge(jd_cvs, how = 'left', on = "cv_name")

out=df_cvs.merge(jd_cvs,left_on=('name'),right_on=('cv_name'),how='outer',suffixes=('_left','_right'))


jd_cvs_combined=df_jd.merge(out,left_on=('jobID'),right_on=('Job ID'),how='outer',suffixes=('_left','_right'))



#out1=df_cvs.merge(jd_cvs,left_on=('name'),right_on=('cv_name'),how='outer')
#
#out2=jd_cvs.merge(df_cvs,left_on=('cv_name'),right_on=('name'),how='outer',suffixes=('_right','_left'))

jd_cvs_combined=jd_cvs_combined.dropna(subset=['name','Job ID'])
#out4=out3.dropna(subset=['Job ID'])
#out4 = out3[len(out3['experience']>=1]

with open(os.path.join(results_folder,'combined_df.pickle'), 'wb') as handle:
    pickle.dump(jd_cvs_combined, handle, protocol=pickle.HIGHEST_PROTOCOL)


#jd_cvs_combined.to_csv(os.path.join(results_folder, 'jd_cvs_combined.csv'))