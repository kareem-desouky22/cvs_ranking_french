
import pickle
import pandas as pd

# open a file, where you stored the pickled data
# file = open('cvs_df.pickle', 'rb')
file_list = open('ranking_list.pickle', 'rb')

# dump information to that file
data = pickle.load(file_list)

# close the file
file_list.close()

print('Showing the pickled data:')

# df = data.drop(['text paras', 'experience_index', 'date index'],1)
# couples_list=df.couples
# couples_list_1=couples_list[0]# cnt = 0
# for item in df:
#     print('The data ', cnt, ' is : ', item)
#     cnt += 1
for dicts in data:
    print ('dicts is:',dicts)
    
    couples_list=[dicts['couples']]
    print ('I am entering the if condition')
    print ('length of list is:',len(couples_list))
    if len(couples_list[0])>0:
        # print ('length of list is:',len(couples_list))
        # print ('couples list is:', couples_list)
        for i,element in enumerate(couples_list):
            print ('')
            print ('elements in dict is:',element)
            # print ('couples in dict is:',couples_list[i][0][0])
            latest_post=couples_list[i][0][0]
            latest_post_duration=couples_list[i][0][4]
            total_exp=0
            for j in element:
                if j[4]>0: # dont add experience if it is negative 
                    total_exp=total_exp+j[4] # add experience of all jobs
                else:
                    j[4]=0  #  negative value is incorrect
                
            
            print("===========================================")
            print("===========================================")
            print("===========================================")
            print("===========================================")
            print("===========================================")
            
        dicts['recent_job']=latest_post
        dicts['recent_job_experience']=latest_post_duration
        dicts['total_experience']=total_exp
        
    else:
        continue


df = pd.DataFrame(data) 



df=df[df.astype(str)['qualification'] != '[]']
df = df.drop(['couples','text paras','experience_index','date index'],axis=1)
# df.drop(['C', 'D'], axis = 1)
with open('ranking_features.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

df.to_csv('clean_features.csv')
    
    
