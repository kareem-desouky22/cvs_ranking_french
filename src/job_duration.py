
import pickle
import pandas as pd
import os

results_folder=os.path.join(os.path.abspath(os.path.join(__file__,"../../")),'data/results')
file_list = open(os.path.join(results_folder,'ranking_list1.pickle'), 'rb')
data = pickle.load(file_list)
file_list.close()
for dicts in data:
    couples_list=[dicts['couples']]    
    if len(couples_list[0])>0:
        for i,element in enumerate(couples_list):
            latest_post=couples_list[i][0][0]
            latest_post_duration=couples_list[i][0][4]
            total_exp=0
            for j in element:
                if j[4]>0: # dont add experience if it is negative 
                    total_exp=total_exp+j[4] # add experience of all jobs
                else:
                    j[4]=0  #  negative value is incorrect
        dicts['recent_job_cv']=latest_post
        dicts['recent_job_experience']=latest_post_duration
        dicts['total_experience_cv']=total_exp
        
    else:
        continue

df = pd.DataFrame(data) 
df=df[df.astype(str)['qualification_cv'] != '[]']
df = df.drop(['couples','text paras','experience_index','date index'],axis=1)

with open(os.path.join(results_folder,'clean_df.pickle'), 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

#df.to_csv(os.path.join(results_folder,'clean_features.csv'))
    
    
