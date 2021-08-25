# import pandas 
import pandas as pd 

# read csv data 
df1 = pd.read_csv('/home/singh.shreya1/Task-Wang/Data_2010_Tsv_all.tsv', sep = '\t')

df1.reset_index(inplace=True)
df1 = df1.rename(columns = {'index':'id'})

index = df1.index
number_of_rows = len(index)
print(number_of_rows)

value_length_list =[]
for index, row in df1.iterrows():
    value_length_list.append(len(str(row['value']).strip()))

df1['value_length'] = value_length_list

#print(df1.groupby('tag').size())

unique =[]

for index, row in df1.iterrows():
    iden = str(row['adsh']).strip()+str(row['series']).strip()+str(row['class']).strip()+str(row['tag']).strip()+str(row['cik']).strip()
    unique.append(iden)

df1['unique_identifier'] = unique

#grouping = df1.groupby('unique_identifier')["name"].count().to_frame(name="count").reset_index()
#grouping.to_csv("C:/Users/user/Desktop/Task-Wang/2010s/grouping_original.tsv", index=False, sep="\t")

df1 = df1.sort_values(['series','class','tag','form','filed','cik','adsh','value_length'],ascending=[True,True,True, True, True, True,True,False])

df2 = df1.drop_duplicates(subset='unique_identifier')

series_length_list = []

for index, row in df2.iterrows():
    le = len(str(row['series']).strip())
    series_length_list.append(le)


df2['series_length'] = series_length_list

df_fil =  df2[df2['series_length'] == 10]


index = df_fil.index
number_of_rows = len(index)
print(number_of_rows)

df_fil.to_csv( "/home/singh.shreya1/Task-Wang/Final_Data_Tsv_form.tsv", sep="\t")

print("done")
