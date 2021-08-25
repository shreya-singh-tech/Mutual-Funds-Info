#python program to finally select cosine similarity values
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


df1 = pd.read_csv( "/home/singh.shreya1/Task-Wang/cos_sample_form.tsv", sep="\t")


cos_sim=[]

comparison_column = np.where(df1["value_lag"].isnull(), True, False)
df1["is_equal"] = comparison_column

df_first_2 = df1[['is_equal']].head(20)
  
# Printing df_first_2
print(df_first_2)

for index, row in df1.iterrows():
    if(row['is_equal']):
        cos_sim.append(" ")
    else:
        cos_sim.append(row['cos_Sim_score'])

df1['cos_sim_score'] = cos_sim

print(df1.tail(10))

select_col = df1[['id','adsh','series','class','tag','cik','filed','form','cos_sim_score']]

df2 = select_col.copy()

df2.to_csv( "/home/singh.shreya1/Task-Wang/Final_Data_Tsv_with_cos_sim.tsv", sep="\t")