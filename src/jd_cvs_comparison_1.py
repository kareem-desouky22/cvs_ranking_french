# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:40:06 2021

@author: KHC
"""

import time

import pandas as pd
import gensim.downloader as api
from gensim import corpora
from gensim.matutils import softcossim
import time
import os
import pickle
import math

from datetime import datetime

start_time = datetime.now()



results_folder=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data/results')
file = open(os.path.join(results_folder,'combined_df.pickle'), 'rb')
df= pickle.load(file)
file.close()
if 'fasttext_model300' in locals():
    print ('fasttest already loaded')
else:
    start_time = time.time()
    fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')
    end_time=time.time()
    loading_time=end_time-start_time
    print ('loading time is:',loading_time)
    





#df=pd.read_csv(os.path.join(results_folder,"jd_cvs_combined.csv"),converters={'qualification_cv': eval,'skills_cv':eval,'location_cv':eval }) 
df['name'].str.lower()
# Preview the first 5 lines of the loaded data 

# df['c2'] = df['total_experience']

df['total_experience_score_cv'] = ''
df['recent_exp_score_cv'] = ''



mask1_exp = (df['total_experience_cv'] >0) & (df['total_experience_cv'] <365)
mask2_exp = (df['total_experience_cv'] >365) & (df['total_experience_cv'] <365*2)
mask3_exp = (df['total_experience_cv'] >365*2) & (df['total_experience_cv'] <365*4)
mask4_exp= (df['total_experience_cv'] >365*4) & (df['total_experience_cv'] <365*5)
mask5_exp= (df['total_experience_cv'] >365*5) & (df['total_experience_cv'] <365*9)
mask6_exp= (df['total_experience_cv'] >365*10) 
df['total_experience_score_cv'][mask1_exp] = 2
df['total_experience_score_cv'][mask2_exp] = 3
df['total_experience_score_cv'][mask3_exp] = 5
df['total_experience_score_cv'][mask4_exp] = 7
df['total_experience_score_cv'][mask5_exp] = 9
df['total_experience_score_cv'][mask6_exp] = 10






mask1_job_stay = (df['recent_job_duration'] <365) 
mask2_job_stay = (df['recent_job_duration'] >365) & (df['recent_job_duration'] <365*2)
mask3_job_stay = (df['recent_job_duration'] >365*2) & (df['recent_job_duration'] <365*4)
mask4_job_stay = (df['recent_job_duration'] >365*4) & (df['recent_job_duration'] <365*6)
mask5_job_stay= (df['recent_job_duration'] >365*6) 
mask6_job_stay= (type(df['recent_job_duration']==str) )

df['recent_exp_score_cv'][mask1_exp] = 4
df['recent_exp_score_cv'][mask2_exp] = 6
df['recent_exp_score_cv'][mask3_exp] = 8
df['recent_exp_score_cv'][mask4_exp] = 7
df['recent_exp_score_cv'][mask5_exp] = 10



#df = df.dropna(axis=0, subset=['qualification'])

#df.to_csv('features_scores.csv')




def get_diff(phrase_1, phrase_2):
#    print ('phrase 1 is:',phrase_1)
#    print ('phrase 2 is:',phrase_2)
    sent_1 = phrase_1.split()  # electronics engineer
    sent_2 = phrase_2.split()
    documents = [sent_1, sent_2]
    dictionary = corpora.Dictionary(documents)
# Prepare the similarity matrix
    similarity_matrix = fasttext_model300.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)
# Convert the sentences into bag-of-words vectors.
    sent_1 = dictionary.doc2bow(sent_1)
    sent_2 = dictionary.doc2bow(sent_2)
     #Compute soft cosine similarity
    diff=softcossim(sent_1, sent_2, similarity_matrix)
    return(diff)

def get_similarity(list_cv,list_jd):
    print ('list of cvs is:',list_cv) 
    max_score=0
    sum_score=0
    diff_list=[]
    
#    if math.isnan(list_jd) or math.isnan(list_cv):
#        print('got nan value')
#    else:
    for l1 in list_jd:  # each element of jd qualification
        print ('jd element is:', l1)
        for l2 in list_cv:
            if l2=="":
                print ('cv element is empty')
            else:
                print ('cv element is:', l2)
                my_score=get_diff(l1,l2)
                diff_list.append(my_score)
                
            
    if len (diff_list)>0:
        max_score=max(diff_list)
        sum_score=sum(diff_list)
    else:
        pass
#        return (max_score_qual, min_score_qual)   
    return (max_score,sum_score)



def relative_exp_score(list_cv,list_jd):
    print ('list of cvs is:',list_cv) 
    threshold=0.3
    rel_exp_duration=[]
    duration_score=0
    
#    if math.isnan(list_jd) or math.isnan(list_cv):
#        print('got nan value')
#    else:
    for l1 in list_jd:  # each element of jd qualification
        print ('jd element is:', l1)
        for l2 in list_cv:
            if l2[0]=="":
                print ('cv element is empty')
            else:
                print ('cv job title is:', l2[0])
                my_score=get_diff(l1,l2[0])
                if my_score>=threshold:
                    
                    rel_exp_duration.append(l2[1])
                    
                
            
    if len (rel_exp_duration)>0:
        duration=sum(rel_exp_duration)
        
        if duration==0:
            duration_score=0
        elif duration >0 and duration <=365:
            duration_score=3
        elif duration>365 and duration <=365*3:
            duration_score=6
        elif duration>365*3 and duration <=365*5:
            duration_score=8
            
        elif duration>365*5 :
            duration_score=10
            
        

#        return (max_score_qual, min_score_qual)   
    return (duration_score)

def clean_recent_job(dirty_list):
    if ':' in dirty_list:
#        print (': is present')
#        print ('list is:',dirty_list)
        dirty_list=dirty_list.split(':')[1]
    else: 
        print ('its already clean')
        
    clean_list=[dirty_list]
        
    return (clean_list)

#df['cleaned_recent_job'] = df.apply(lambda x: clean_recent_job(x['recent_job_cv']), axis = 1)
    
#df.drop(df.tail(2).index,inplace=True) # drop last n rows
    
df.dropna(subset = ['qualification_cv','final_qualifications_jd','skills_cv','final_skills_jd','location_cv','final_locs_jd','languages_cv','final_langs_jd'], inplace=True)

#
#
#df = df.dropna(axis=1, subset=['qualification_cv','final_qualifications_jd','skills_cv','final_skills_jd','location_cv','final_locs_jd','languages_cv','final_langs_jd' ])
##    
#
df['qualifications_similarity_score_max'] = df.apply(lambda x: get_similarity(x['qualification_cv'],x['final_qualifications_jd'])[0], axis = 1)

df['qualifications_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['qualification_cv'],x['final_qualifications_jd'])[1], axis = 1)

df['skills_similarity_score_max'] = df.apply(lambda x: get_similarity(x['skills_cv'],x['final_skills_jd'])[0], axis = 1)
df['skills_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['skills_cv'],x['final_skills_jd'])[1], axis = 1)

df['relevant_experience_score'] = df.apply(lambda x: relative_exp_score(x['couples'],x['job_title_jd']), axis = 1)
df['job_title_similarity_score_max_cv'] = df.apply(lambda x: get_similarity(x['job_titles_cv'],x['job_title_jd'])[0], axis = 1)
#
df['job_title_similarity_score_sum_cv'] = df.apply(lambda x: get_similarity(x['job_titles_cv'],x['job_title_jd'])[1], axis = 1)

df['locations_similarity_score_max'] = df.apply(lambda x: get_similarity(x['location_cv'],x['final_locs_jd'])[0], axis = 1)

df['locations_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['location_cv'],x['final_locs_jd'])[1], axis = 1)

df['languages_similarity_score_max'] = df.apply(lambda x: get_similarity(x['languages_cv'],x['final_langs_jd'])[0], axis = 1)

df['languages_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['languages_cv'],x['final_langs_jd'])[1], axis = 1)



#df_classifier_features=df[['name','total_experience_score','recent_exp_score','qualification_similarity_score_max','qualification_similarity_score_sum','skills_similarity_score_max','skills_similarity_score_sum','recent_job_title_similarity_score_max','recent_job_title_similarity_score_sum','location_similarity_score_max','location_similarity_score_sum','language_similarity_score_max','language_similarity_score_sum']]
# to do: change name of exp 


df_classifier_features=df[['cv_score','name','total_experience_score_cv','recent_exp_score_cv','relevant_experience_score','qualifications_similarity_score_max','qualifications_similarity_score_sum','skills_similarity_score_max','skills_similarity_score_sum','locations_similarity_score_max','locations_similarity_score_sum']]
## to do: change name of exp 
#
df_classifier_features.to_csv(os.path.join(results_folder,'classifier_features.csv'))


simulation_time=end_time-start_time
print ('time for scoring CV against JDs  is:', simulation_time, ' minutes')
