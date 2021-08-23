# cvs_ranking_french
This project has following .py files:
 # 1- features_extraction.py
 This file takes CVs directory and then extract all features from the CVs.
 
 
 # 2 job_duration.py
 This file runs after features_extraction.py and extract the job duration against each job title in days. 
 
 # assign_label_score.py
 This file read the excel file containing list of CVs and scores of CV features like skills, qualification e.t.c. against each job description. 
 This code gives overall score to CVs against each job description. 
 
 # combine_jd_cv.py
 This part of code combines extracted features from CVs, target scores assigned to those CVs and Job IDs.
 
 # read_extract_jds.py
 This file read JSON file containing job description and extract features from JDs. 
 
 # jd_cvs_comparison.py
 This file compares extracted features of CV and JD and then give scores to CVs based on different criterias. 
 
 # ranking_regressor.py
 This file runs the training algorithm on finalized features and label scores. 
 
