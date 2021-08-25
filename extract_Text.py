
import pandas as pd 
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re

filename = 'C:/Users/user/Desktop/Task-Wang/sample1000.csv'

df = pd.read_csv(filename, encoding='utf-8-sig')

form_type  = df["FORM"].to_list()

url_list_ori = df["FNAME"].to_list()

accession = df["accession"].to_list()
url_list = url_list_ori
content =''

final_data = []
goal_keywords = ['investment objectives', 'investment objective','investment focus','investment goal', 'investment goals']

for link in url_list:
    info_scrapped = {}
    try :
        info_scrapped["link"] = "https://www.sec.gov/Archives/"+link
        info_scrapped["form"] = form_type[url_list.index(link)]            
        req = Request("https://www.sec.gov/Archives/"+link, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} ) 
        html = urlopen(req).read()
        soup = BeautifulSoup(html, 'lxml')
        for doc in soup.find_all('document'):
            for type in doc.find_all('type'):
                if ((type.text).startswith('GRAPHIC') and (('.jpg' in type.text)  or ('.gif' in type.text)) )or ((type.text).startswith('ZIP') and ('.zip' in type.text)) or ((type.text).startswith('EXCEL') and ('.xlsx' in type.text)) or  ((type.text).startswith('JSON') and ('.json' in type.text)) or ((type.text).startswith('XML') and ('.xml' in type.text)) :
                    type.decompose()
        include_story= []
        #all_content = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', soup.get_text()) if len(i.strip(' ')) > 0])
        content =  soup.get_text().split(".\n")

        for para in content:
            for s in goal_keywords:
                if s.lower() in para.lower():
                    para2 = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', para) if len(i.strip(' ')) > 0])
                    para2 = re.sub(r'[^\x00-\x7F]+',' ',para2)
                    include_story.append(para2.replace("\n"," ").strip())
            
        info_scrapped["objectives/goals"] = include_story
        #print(info_scrapped["objectives/goals"])
        info_scrapped["filename"] = accession[url_list.index(link)]  
        final_data.append(info_scrapped)
        time.sleep(1)
        print("yes1"+info_scrapped["filename"])
    except:
        try:
            req = Request("https://www.sec.gov/Archives/"+link.split(".")[0]+"-index.htm", headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} )
            html = urlopen(req).read()
            soup = BeautifulSoup(html, 'lxml')
            for doc in soup.find_all('a',href=True):
            #print(doc['href'])
                if ((doc['href']).startswith('/Archives/edgar/data') and ('.txt' in doc['href'])):
                    url = "https://www.sec.gov"+doc['href']
                    req2 = Request("https://www.sec.gov"+doc['href'], headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} ) 
                    html2 = urlopen(req2).read()
                    info_scrapped["link"] = url
                    info_scrapped["form"] = form_type[url_list.index(link)] 
                    soup2 = BeautifulSoup(html2, 'lxml')
                    for doc2 in soup2.find_all('document'):
                        for type2 in doc2.find_all('type'):        
                            if ((type2.text).startswith('GRAPHIC') and (('.jpg' in type2.text)  or ('.gif' in type2.text)) )or ((type2.text).startswith('ZIP') and ('.zip' in type2.text)) or ((type2.text).startswith('EXCEL') and ('.xlsx' in type2.text)) or ((type2.text).startswith('JSON') and ('.json' in type2.text))  or ((type2.text).startswith('XML') and ('.xml' in type2.text)) :
                                type2.decompose()
                    include_story= []           
                    #all_content = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', soup2.get_text()) if len(i.strip(' ')) > 0])
                    content = soup2.get_text().split(".\n")
                    for para in content:
                        for s in goal_keywords:
                            if s.lower() in para.lower():
                                para2 = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', para) if len(i.strip(' ')) > 0])
                                para2 = re.sub(r'[^\x00-\x7F]+',' ',para2)
                                include_story.append(para2.replace("\n"," ").strip())
            
                    info_scrapped["objectives/goals"] = include_story
                    #print(info_scrapped["objectives/goals"])
                    info_scrapped["filename"] = accession[url_list.index(link)]  
                    final_data.append(info_scrapped)
                    time.sleep(1)
                    print("yes2"+info_scrapped["filename"])
                    
        except:
            info_scrapped["link"] = "https://www.sec.gov/Archives/"+link.split(".")[0]+"-index.htm"
            info_scrapped["form"] = form_type[url_list.index(link)]
            info_scrapped["objectives/goals"] = None
            info_scrapped["filename"] = accession[url_list.index(link)] 
            final_data.append(info_scrapped)
            time.sleep(1)
            print("yes3"+info_scrapped["filename"])
            continue

df = pd.DataFrame(final_data)
df.to_csv("C:/Users/user/Desktop/Task-Wang/sample3.csv",index = False)