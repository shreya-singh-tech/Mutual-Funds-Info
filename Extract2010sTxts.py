#program to extract txt.tsv
import pandas as pd
import json
import os
import re


list_of_files =[]

def jsonTocsv(dir):
    for f_name in os.listdir('C:/Users/user/Desktop/Task-Wang/2010s/2010s/'+dir):
        print(f_name)
        if f_name.endswith('txt.tsv'):
            list_of_files.append('C:/Users/user/Desktop/Task-Wang/2010s/2010s/'+dir+'/'+f_name)
    
    print(list_of_files)
    
    story_id = 0
    for f in list_of_files:
        story_id = story_id+1
        df = pd.read_csv(f, sep='\t')
        df.to_csv('C:/Users/user/Desktop/Task-Wang/2010s/AllFiles_tsv/'+str(story_id)+'.tsv', index=False, sep="\t")

for dir in os.listdir('C:/Users/user/Desktop/Task-Wang/2010s/2010s/'):
    jsonTocsv(dir)