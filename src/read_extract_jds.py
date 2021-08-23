# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:51:27 2021

@author: KHC
"""

import pandas as pd

import json
import os
import pickle
import re
import unidecode
import spacy

def clean_string(sent):
    sentence=sent.lower().strip()
    sentence=unidecode.unidecode(sentence)
    #remove multiple spaces
    sentence = re.sub(r"\s+"," ", sentence, flags = re.I)
    sentence = re.sub(r"^\s+", "", sentence)
    sentence = re.sub(r"^\s+", "", sentence)
    return (sentence)


def extract_skills(clean_sent):
    
    skills_list=[]
    doc_skills=lsm_s(clean_sent)
    for X in doc_skills.ents:
        if X.label_=="skills":
            contains_digit = any(map(str.isdigit, X.text))
            if contains_digit or ':' in X.text:            
                pass
            else:
                skills_list.append(X.text)
#    skills_list=top_frequent(skills_list, k=8)
    return(skills_list)

def extract_qualifications(clean_sent):
    qualifications_list=[]
    doc_qual=lsm_q(clean_sent)
    for X in doc_qual.ents:
        if X.label_=="qualification":
            contains_digit = any(map(str.isdigit, X.text))
            if contains_digit or ':' in X.text:
                pass
            else:            
                qualifications_list.append(X.text)
                
#    qualifications_list=top_frequent(qualifications_list, k=8)             
    return qualifications_list
                
            
def extract_locations(sent):
    locations_list=[]
    doc_all=nlp(sent)
    for X in doc_all.ents:
        if (X.label_=='GPE'):
            locations_list.append(X.text)            
    words_list=sent.split(' ')
    for w in words_list:
        if w in l_list:
            locations_list.append(w)
#    loc_list=top_frequent(locations_list, k=3)
    return(locations_list)
            
def extract_languages(sent):
    languages_list=[]
    doc_all=nlp(sent)
    for X in doc_all.ents:
        if (X.label_=='LANGUAGE'):
            languages_list.append(X.text)
#    words_list=sent.split(' ')
#    for w in words_list:
#        if w in lang_list:
#            languages_list.append(w)
#    lang_list=top_frequent(languages_list, k=3)
    return(languages_list)





data_path=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data')
models_folder=os.path.join(data_path,'models')
location_txt=models_folder+'\locations.txt'
language_txt=models_folder+'\languages.txt'
results_folder=os.path.join(data_path,'results')




nlp = spacy.load ('fr_core_news_lg')
lsm_j=spacy.load(os.path.join (models_folder,'job_model_fre'))
lsm_s=spacy.load(os.path.join (models_folder,'skill_model_fre'))
lsm_q=spacy.load(os.path.join (models_folder,'Qualification_model_fre'))


with open (location_txt, "r",encoding="utf8") as myfile:
    data=myfile.read()
l_list=data.split ('\n')
l_list=[l.lower() for l in l_list if l!=""]     

with open (language_txt, "r",encoding="utf8") as myfile:
    data=myfile.read()                
lang_list=data.split ('\n')
lang_list=[lang.lower() for lang in lang_list] 


#json_file=os.path.join(results_folder,'jds_5.json')
#
with open(os.path.join(data_path,'jds.json'),encoding="utf8") as f:
  data = json.load(f)
  
#data=json.loads(json_file)
  
df_jd=pd.DataFrame(data)
df_jd=df_jd.fillna('')
df_jd['qualifications_jd']=df_jd.qualification.str.split("|")


# using split to convert them to list items
#titles=df_jd['jobTitle'].values.tolist()
df_jd['job_title_jd']=df_jd['jobTitle'].str.split(":")
df_jd['location_jd']=df_jd['locations'].str.split(":")
df_jd.drop(['jobTitle','qualification','locations'],axis=1, inplace=True)

  # Cleaning the text
df_jd['candidate_profile'] = df_jd.apply(lambda x: clean_string(x['Candidate-profile']), axis = 1)

df_jd['job_mission'] = df_jd.apply(lambda x: clean_string(x['Job_mission']), axis = 1)

df_jd['job_misc'] = df_jd.apply(lambda x: clean_string(x['Job-miscs']), axis = 1)

# Extraction of skills and qualifications from Candidate profile:

df_jd['skills_list_profile'] = df_jd.apply(lambda x: extract_skills(x['candidate_profile']), axis = 1)

df_jd['qualifications_list_profile'] = df_jd.apply(lambda x: extract_qualifications(x['candidate_profile']), axis = 1)




# Extraction of skills and qualifications from Job Mission:

df_jd['skills_list_mission'] = df_jd.apply(lambda x: extract_skills(x['job_mission']), axis = 1)

df_jd['qualifications_list_mission'] = df_jd.apply(lambda x: extract_qualifications(x['job_mission']), axis = 1)


# Extraction of languages and locations from Job Misc:
df_jd['final_langs_jd'] = df_jd.apply(lambda x: extract_locations(x['job_misc']), axis = 1)

df_jd['locations_list_misc'] = df_jd.apply(lambda x: extract_languages(x['job_misc']), axis = 1)

#  Final qualification list
df_jd['final_qualifications_jd'] =df_jd['qualifications_list_profile']+df_jd['qualifications_list_mission']+df_jd['qualifications_jd']


#  Final skills list
df_jd['final_skills_jd'] =df_jd['skills_list_profile']+df_jd['skills_list_mission']+df_jd['skills']

#  Final locations list
df_jd['final_locs_jd'] =df_jd['locations_list_misc']+df_jd['location_jd']


# Delete unnecessary columns
df_jd.drop(['Candidate-profile','Job_mission','candidate_profile','job_mission','skills_list_profile','skills_list_mission','Job-miscs','job_misc','Job_introduction','industry','Sub-industry','tags','roleDesignation','skills','qualifications_jd','location_jd','qualifications_list_profile','qualifications_list_mission','locations_list_misc'],axis=1, inplace=True)

df_jd.to_csv('jds.csv')










#
#Getting file having CV names with their extracted features
file = open(os.path.join(results_folder,'clean_df.pickle'), 'rb')
df_cvs = pickle.load(file)
file.close()  
df_cvs['name'] = df_cvs['name_cv'].str.lower()

 
##jd_cvs =pd.read_excel('jd_cvs_1.xlsx')
jd_cvs =pd.read_csv(os.path.join(results_folder,'cv_scores_manual.csv'))
jd_cvs['cv_name'] = jd_cvs['without Ext'].str.lower()

out=df_cvs.merge(jd_cvs,left_on=('name'),right_on=('cv_name'),how='outer',suffixes=('_left','_right'))

jd_cvs_combined=df_jd.merge(out,left_on=('jobID'),right_on=('Job ID'),how='outer',suffixes=('_left','_right'))


with open(os.path.join(results_folder,'combined_df.pickle'), 'wb') as handle:
    pickle.dump(jd_cvs_combined, handle, protocol=pickle.HIGHEST_PROTOCOL)

jd_cvs_combined.to_csv(os.path.join(results_folder, 'jd_cvs_combined.csv'))
