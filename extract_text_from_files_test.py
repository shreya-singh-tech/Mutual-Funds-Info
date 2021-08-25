#program to extract keywords from archive files
import pandas as pd 
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import glob

list_urls = 'C:/Users/user/Desktop/Task-Wang/sample1000.csv'
df = pd.read_csv(list_urls, encoding='utf-8-sig')
form_type  = df["FORM"].to_list()
accession = df["accession"].to_list()

#os.chdir("C:/Users/user/Desktop/Task-Wang/AllFilesV3")

extension = 'txt'

filename = ["C:/Users/user/Desktop/Task-Wang/AllFilesV3/0000051931-19-000815.txt"]

final_data = []
goal_keywords = ['investment objectives', 'investment objective','investment focus','investment goal', 'investment goals']
strategy_keywords =['principal investment strategy','principal investment stategies','investment stategies','investment strategy']
risk_keywords =['principal risks of investing in the fund', 'principal risks','risks of holding certain securtities','principal risk']

for link in filename:
    info_scrapped = {}
    with open(link, "r", encoding='utf-8') as input:
        content = input.read().split("\n\n")
        info_scrapped["filename"] = None
        info_scrapped["form"] = None
        info_scrapped["objectives/goals"] = None
        info_scrapped["strategies"] = None
        info_scrapped["risks"] = None
        
    #try :
        include_story_goal= []
        for i, para in enumerate(content):
            for s in goal_keywords:
                if s.lower() in para.lower():
                    #print(para)
                    #print ("----------------------$$$$$")                   
                    para2 = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', para) if len(i.strip(' ')) > 0])                   
                    para2 = re.sub(r'[^\x00-\x7F]+',' ',para2)                    
                    include_story_goal.append(para2.replace("\n"," ").strip())
                    
                    if content[i+1] == "\n" or not (content[i+1] and not (content[i+1].isspace()))  :
                        include_story_goal.append(content[i+2].replace("\n"," ").strip())
                    else:
                        include_story_goal.append(content[i+1].replace("\n"," ").strip())
        
        include_story_strategy= []
        for i, para in enumerate(content):
            for s in strategy_keywords:
                if s.lower() in para.lower():
                                        
                    para2 = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', para) if len(i.strip(' ')) > 0])                   
                    para2 = re.sub(r'[^\x00-\x7F]+',' ',para2)                    
                    include_story_strategy.append(para2.replace("\n"," ").strip())
                    
                    if content[i+1] == "\n" or not (content[i+1] and not (content[i+1].isspace()))  :
                        include_story_strategy.append(content[i+2].replace("\n"," ").strip())
                    else:
                        include_story_strategy.append(content[i+1].replace("\n"," ").strip())

        include_story_risk= []
        for i, para in enumerate(content):
            for s in risk_keywords:
                if s.lower() in para.lower():
                                      
                    para2 = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', para) if len(i.strip(' ')) > 0])                   
                    para2 = re.sub(r'[^\x00-\x7F]+',' ',para2)                    
                    include_story_risk.append(para2.replace("\n"," ").strip())
                    
                    if content[i+1] == "\n" or not (content[i+1] and not (content[i+1].isspace()))  :
                        content[i+2] = re.sub(r'[^\x00-\x7F]+',' ',content[i+2])
                        include_story_risk.append(content[i+2].replace("\n"," ").strip())
                    else:
                        content[i+1] = re.sub(r'[^\x00-\x7F]+',' ',content[i+1])
                        include_story_risk.append(content[i+1].replace("\n"," ").strip())
               
              
        info_scrapped["filename"] = link.split(".")[0]    
        info_scrapped["objectives/goals"] = include_story_goal
        info_scrapped["strategies"] = include_story_strategy
        info_scrapped["risks"] = include_story_risk
        print(info_scrapped["objectives/goals"])
        print(info_scrapped["strategies"])
        print(info_scrapped["risks"])
        indexes = str(df[df["accession"]==link.split(".")[0]].index.values)
        indexes_new = int(indexes[1:-1])        
        
        info_scrapped["form"]  = form_type[indexes_new]
        
        final_data.append(info_scrapped)
        #time.sleep(1)
        print("yes1"+info_scrapped["filename"])
        #print(info_scrapped["objectives/goals"])
    #except:
        #pass

df2 = pd.DataFrame(final_data)
df2.to_csv("C:/Users/user/Desktop/Task-Wang/sample-new5.csv",index = False)