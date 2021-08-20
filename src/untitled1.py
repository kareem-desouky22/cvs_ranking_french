# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:55:27 2021

@author: KHC
"""
import spacy
import os

sentence="Système d’exploitation, outils bureautique (Word, Excel, PowerPoint, Access…).Logiciel : SAGE 100 comptabilité, gestion, paie./PC COMPTA (DLG) comptabilité ,gestion, paie"

data_path=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data')
cvs_folder=os.path.join(data_path,'cvs_2')
models_folder=os.path.join(data_path,'models')
results_folder=os.path.join(data_path,'results')

nlp = spacy.load ('fr_core_news_lg')
lsm_j=spacy.load(os.path.join (models_folder,'job_model_fre'))
lsm_s=spacy.load(os.path.join (models_folder,'skill_model_fre'))
lsm_q=spacy.load(os.path.join (models_folder,'Qualification_model_fre'))
doc_skills=lsm_s(sentence)

for X in doc_skills.ents:
        if X.label_=="skills":
            print ('skill is:',X.ents)
            contains_digit = any(map(str.isdigit, X.ents))
            if contains_digit or ':' in X.ents:            
                pass
            else:
#                skills_list.append(X.text)
                skills_list.append(X.ents)
                