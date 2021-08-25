#program to find cosine similarity

import spacy
import textstat
from textstat.textstat import textstatistics
#from textstat import legacy_round,neasy_word_set
import pandas as pd
import pysentiment2 as ps
import math
import re
from collections import Counter
import numpy as np


df1 = pd.read_csv( "/home/singh.shreya1/Task-Wang/Final_Data_Tsv_form.tsv", sep="\t")

unique =[]
for index, row in df1.iterrows():
    iden = str(row['series']).strip()+str(row['class']).strip()+str(row['tag']).strip()+str(row['form']).strip()+str(row['cik']).strip()
    unique.append(iden)

df1['unique_identifier_form'] = unique

#df1 = df1.sort_values(['unique_identifier_form'])

#group_by_size = df1.groupby('unique_identifier_form').size()

#value_lag_index =[]
#for i in group_by_size:
#    value_lag_index.append(i)

#value_list =[]
#for index, row in df1.iterrows():
#    value_list.append(str(row['value']))

#filed_list = []
#for index,row in df1.iterrows():
#    filed_list.append(str(row['filed']))

df1['value_lag'] = df1.groupby('unique_identifier_form')['value'].shift()

#start_index = 0
#value_lag = []
#i = 0
#k = 0
#last_filed =[]

#while i < len(value_list):
    
#    index_max = value_lag_index[k]
#    while index_max > 0 :
#        last_filed.append(filed_list[i+value_lag_index[k]-1])
#        value_lag.append(value_list[i+value_lag_index[k]-1])
#        index_max = index_max -1

#    i = i+value_lag_index[k]    
#    k = k+1
   
    
#df1['value_lag'] = value_lag
#df1['filed_lag'] = last_filed

df1.value_lag = df1.value_lag.fillna('')

print("done")

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


df1['vector1']=df1['value'].apply(lambda x: text_to_vector(str(x))) 
df1['vector2']=df1['value_lag'].apply(lambda x: text_to_vector(str(x)))
df1['cos_Sim_score']=df1.apply(lambda x: get_cosine(x['vector1'],x['vector2']),axis=1)

df1.to_csv("/home/singh.shreya1/Task-Wang/cos_sample_form.tsv",sep ="\t")


