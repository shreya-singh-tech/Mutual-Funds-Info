#program to combine files as needed
import os
import glob
import pandas as pd
os.chdir("C:/Users/user/Desktop/Task-Wang/2010s/comb/")

extension = 'tsv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,sep='\t') for f in all_filenames ])
combined_csv = combined_csv.drop(columns="value")
combined_csv = combined_csv.sort_values(['adsh','tag'])
#export to csv
combined_csv.to_csv( "C:/Users/user/Desktop/Task-Wang/2010s/Final_2010_Tsv2.tsv", index=False, sep="\t")