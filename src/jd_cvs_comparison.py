# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:40:06 2021

@author: KHC
"""



job_id= 5838
jd_job_title=["Conseillers Clients Techniques"]
jd_skills= ["Une parfaite maîtrise de la langue française","Maîtrise de l’outil informatique","Sens de l’écoute.","Logique et rapidité","Aptitude à la communication","Sens du service","Résistance au stress"]
min_experience= "Etudiant - Stagiaire"
jd_location=["Alger"]
jd_language=['Algerian','French']
jd_qualification= ["Secondaire","NA"]
role_designation= "Conseil"
unit= "1 ",
industry="Conseils"



import pickle
import pandas as pd

# open a file, where you stored the pickled data
# file = open('cvs_df.pickle', 'rb')
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 



import gensim.downloader as api
from gensim import corpora
from gensim.matutils import softcossim
import time


##print ('I am soft cosine and I am called')
if 'fasttext_model300' in locals():
    print ('fasttest already loaded')
else:
    start_time = time.time()
    fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')
    end_time=time.time()
    loading_time=end_time-start_time
    print ('loading time is:',loading_time)
#from soft_cosine import get_diff

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 

df = pd.read_csv("clean1.csv",converters={'qualification': eval,'skills':eval}) 
df['name'].str.lower()
# Preview the first 5 lines of the loaded data 
df.head()

# df['c2'] = df['total_experience']

df['total_experience_score'] = ''
df['recent_exp_score'] = ''



mask1_exp = (df['total_experience'] >0) & (df['total_experience'] <365)
mask2_exp = (df['total_experience'] >365) & (df['total_experience'] <365*2)
mask3_exp = (df['total_experience'] >365*2) & (df['total_experience'] <365*4)
mask4_exp= (df['total_experience'] >365*4) & (df['total_experience'] <365*5)
mask5_exp= (df['total_experience'] >365*5) & (df['total_experience'] <365*9)
mask6_exp= (df['total_experience'] >365*10) 
df['total_experience_score'][mask1_exp] = 2
df['total_experience_score'][mask2_exp] = 3
df['total_experience_score'][mask3_exp] = 5
df['total_experience_score'][mask4_exp] = 7
df['total_experience_score'][mask5_exp] = 9
df['total_experience_score'][mask6_exp] = 10






mask1_job_stay = (df['recent_job_experience'] <365) 
mask2_job_stay = (df['total_experience'] >365) & (df['total_experience'] <365*2)
mask3_job_stay = (df['total_experience'] >365*2) & (df['total_experience'] <365*4)
mask4_job_stay = (df['total_experience'] >365*4) & (df['total_experience'] <365*6)
mask5_job_stay= (df['total_experience'] >365*6) 

df['recent_exp_score'][mask1_exp] = 4
df['recent_exp_score'][mask2_exp] = 6
df['recent_exp_score'][mask3_exp] = 8
df['recent_exp_score'][mask4_exp] = 7
df['recent_exp_score'][mask5_exp] = 10



df = df.dropna(axis=0, subset=['qualification'])


df.to_csv('features_scores.csv')




def get_diff(phrase_1, phrase_2):
#    print ('phrase 1 is:',phrase_1)
#    print ('phrase 2 is:',phrase_2)
    sent_1 = phrase_1.split()  # electronics engineer
    sent_2 = phrase_2.split()
    

# Prepare a dictionary and a corpus.

# Prepare a dictionary and a corpus.
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

def get_similarity(list_a,feature_string):
    diff_list=[]
#    print ('values of list_a are:',list_a)
#    print ('getting data of new row')
#    print ('=================================================================')
#    print ('=================================================================')
#    print ('=================================================================')
#    print ('calling the phrase comparison method')
#    print ('total number of elements in list a are:',len(list_a))
    
    if feature_string=='qualification':
        compare_feature_list=jd_qualification
       
        
    elif feature_string=='skill':
        compare_feature_list=jd_skills
    elif feature_string=='location':
        compare_feature_list=jd_location
    elif feature_string=='language':
        compare_feature_list=jd_language
    elif feature_string=='job_title':
        compare_feature_list=jd_job_title
    
        
        

    for l1 in compare_feature_list:  # each element of jd qualification
        for l2 in list_a:
            
            
#        print ('value of l1 is:',l1)
            my_score=get_diff(l1,l2)
#    my_score=[get_diff(x) for x in zip(list_a, list_b)]
#        print ('score is:',my_score)
            diff_list.append(my_score)
#            print ('returning list is:', diff_list)
    max_score=max(diff_list)
    sum_score=sum(diff_list)
#        return (max_score_qual, min_score_qual)   
    return (max_score,sum_score)

def clean_recent_job(dirty_list):
    if ':' in dirty_list:
#        print (': is present')
#        print ('list is:',dirty_list)
        dirty_list=dirty_list.split(':')[1]
    else: 
        print ('its already clean')
        
    return (dirty_list)

df['cleaned_recent_job'] = df.apply(lambda x: clean_recent_job(x['recent_job']), axis = 1)
    
    


df.drop(df.tail(2).index,inplace=True) # drop last n rows
    
# Two iterables are passed

#df['add'] = df.apply(lambda row : add(row['A'],
#                     row['B'], row['C']), axis = 1)
  

#df['job_title_similarity_score_max'] = df.apply(lambda x: get_similarity(x['experience'],'job_title')[0], axis = 1)  # experience
#df['job_title_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['experience'],'job_title')[1], axis = 1)

df['qualification_similarity_score_max'] = df.apply(lambda x: get_similarity(x['qualification'],'qualification')[0], axis = 1)
df['qualification_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['qualification'],'qualification')[1], axis = 1)
df['skills_similarity_score_max'] = df.apply(lambda x: get_similarity(x['skills'],'skill')[0], axis = 1)
df['skills_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['skills'],'skill')[1], axis = 1)
df['recent_job_title_similarity_score_max'] = df.apply(lambda x: get_similarity(x['recent_job'],'job_title')[0], axis = 1)
df['recent_job_title_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['recent_job'],'job_title')[1], axis = 1)
df['location_similarity_score_max'] = df.apply(lambda x: get_similarity(x['location'],'location')[0], axis = 1)
df['location_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['location'],'location')[1], axis = 1)

df['language_similarity_score_max'] = df.apply(lambda x: get_similarity(x['languages'],'location')[0], axis = 1)
df['language_similarity_score_sum'] = df.apply(lambda x: get_similarity(x['languages'],'location')[1], axis = 1)

df_classifier_features=df[['name','total_experience_score','recent_exp_score','qualification_similarity_score_max','qualification_similarity_score_sum','skills_similarity_score_max','skills_similarity_score_sum','job_title_similarity_score_max','job_title_similarity_score_sum','location_similarity_score_max','location_similarity_score_sum','language_similarity_score_max','language_similarity_score_sum']]
# to do: change name of exp 

df_classifier_features.to_csv('classifier_features.csv')

# (df['total_experience'] > 100) 