#program to calculate 9 incides

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


df1 = pd.read_csv( "/home/singh.shreya1/Task-Wang/Data_2010_Tsv_all.tsv", sep="\t")

value_list =[]
for index, row in df1.iterrows():
    value_list.append(str(row['value']))


print("done")

gunning_fog_index =[]
hv_pos_index = []
hv_neg_index =[]
hv_pol_index =[]
hv_sim_index = []

LM_pos_index =[]
LM_neg_index = []
LM_pol_index = []
LM_sim_index = []

hiv4 = ps.HIV4()
lm = ps.LM()

for text in value_list:
    
    gf = textstat.gunning_fog(text)
    gunning_fog_index.append(gf)
    tokens = hiv4.tokenize(text) 
    score = hiv4.get_score(tokens)
    hv_pos_index.append(list(score.values())[0])
    hv_neg_index.append(list(score.values())[1])
    hv_pol_index.append(list(score.values())[2])
    hv_sim_index.append(list(score.values())[3])
    score2 = lm.get_score(tokens)
    LM_pos_index.append(list(score2.values())[0])
    LM_neg_index.append(list(score2.values())[1])
    LM_pol_index.append(list(score2.values())[2])
    LM_sim_index.append(list(score2.values())[3])

df1['gf_index'] = gunning_fog_index
df1['hv_index_pos'] = hv_pos_index
df1['hv_index_neg'] = hv_neg_index
df1['hv_index_pol'] = hv_pol_index
df1['hv_index_sub'] = hv_sim_index

df1['LM_index_pos'] = LM_pos_index
df1['LM_index_neg'] = LM_neg_index
df1['LM_index_pol'] = LM_pol_index
df1['LM_index_sub'] = LM_sim_index

print("done")

select_col = df1[['id','adsh','series','class','tag','cik','filed','form','gf_index','hv_index_pos','hv_index_neg','hv_index_pol','hv_index_sub','LM_index_pos','LM_index_neg','LM_index_pol','LM_index_sub']]

df2 = select_col.copy()

df2.to_csv("/home/singh.shreya1/Task-Wang/Final_Data_Tsv_with_9indices.tsv",sep ="\t")
