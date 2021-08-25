#program to combine txt.tsv and sub.tsv, keep changing line no 10
# import pandas 
import pandas as pd 
   
# read csv data 
df1 = pd.read_csv('C:/Users/user/Desktop/Task-Wang/2010s/combinedSub_Tsv.tsv', sep = '\t') 
df2 = pd.read_csv('C:/Users/user/Desktop/Task-Wang/2010s/combinedTxt_Tsv.tsv', sep = '\t')
df1['aciks'] = df1['aciks'].astype(str)
df2_new = df2[['adsh', 'tag', 'series','class','value']].copy()
mask_df = df2_new['tag'].values == 'StrategyNarrativeTextBlock'
# new dataframe 
df2_new = df2_new[mask_df]
   
Left_join = pd.merge(df2_new,df1,on ='adsh',how ='left')
ordered = Left_join.pop('value') # remove column b and store it in df1
 # remove column x and store it in df2
Left_join['value']= ordered

Left_join.to_csv( "C:/Users/user/Desktop/Task-Wang/2010s/Newcombined_ObjTsv_v2.tsv", index=False, sep = '\t')