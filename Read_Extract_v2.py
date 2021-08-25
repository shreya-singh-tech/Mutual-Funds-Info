#program to extract from archive

import pandas as pd 
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re

filename = 'C:/Users/user/Desktop/Task-Wang/sample1000.csv'


df = pd.read_csv(filename, encoding='utf-8-sig')

url_list_ori = df["FNAME"].to_list()
url_list = url_list_ori

for link in url_list:
    try :
        req = Request("https://www.sec.gov/Archives/"+link, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} ) 
        html = urlopen(req).read()
        time.sleep(2) 
        soup = BeautifulSoup(html, 'lxml')
        for doc in soup.find_all('document'):
            for type in doc.find_all('type'):
                if ((type.text).startswith('GRAPHIC') and (('.jpg' in type.text)  or ('.gif' in type.text)) )or ((type.text).startswith('ZIP') and ('.zip' in type.text)) or ((type.text).startswith('EXCEL') and ('.xlsx' in type.text)) or  ((type.text).startswith('JSON') and ('.json' in type.text)) or ((type.text).startswith('XML') and ('.xml' in type.text)) :
                    type.decompose()
 
        with open('C:/Users/user/Desktop/Task-Wang/AllFilesV4/'+link.split("/")[3], 'w', encoding="utf-8") as f:
            content = soup.get_text()
            content = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', content) if len(i.strip(' ')) > 0])
            content = re.sub(r'[^\x00-\x7F]+',' ',content)
            f.write(content)
            
            print(link.split("/")[3])
            time.sleep(1)

    except:
        try:
            req = Request("https://www.sec.gov/Archives/"+link.split(".")[0]+"-index.htm", headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} )
            html = urlopen(req).read()
        #print(req)
            time.sleep(2) 
            soup = BeautifulSoup(html, 'lxml')
            for doc in soup.find_all('a',href=True):
            #print(doc['href'])
                if ((doc['href']).startswith('/Archives/edgar/data') and ('.txt' in doc['href'])):
                    url = "https://www.sec.gov"+doc['href']
                    
                    req2 = Request("https://www.sec.gov"+doc['href'], headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'} ) 
                    html2 = urlopen(req2).read()
                    time.sleep(2) 
                    soup2 = BeautifulSoup(html2, 'lxml')
                    #print(soup2.get_text())
                    for doc2 in soup2.find_all('document'):
                        for type2 in doc2.find_all('type'):        
                            if ((type2.text).startswith('GRAPHIC') and (('.jpg' in type2.text)  or ('.gif' in type2.text)) )or ((type2.text).startswith('ZIP') and ('.zip' in type2.text)) or ((type2.text).startswith('EXCEL') and ('.xlsx' in type2.text)) or ((type2.text).startswith('JSON') and ('.json' in type2.text))  or ((type2.text).startswith('XML') and ('.xml' in type2.text)) :
                                type2.decompose()
                    with open('C:/Users/user/Desktop/Task-Wang/AllFilesV4/'+link.split("/")[3], 'w', encoding="utf-8") as f:
                        content = soup2.get_text()
                        content = ' '.join([i.strip(' ') for i in re.split( r'<[^>]+>', content) if len(i.strip(' ')) > 0])
                        content = re.sub(r'[^\x00-\x7F]+',' ',content)                       
                        f.write(content)

                        print(link.split("/")[3])
                        time.sleep(1)
        except:
            print("https://www.sec.gov/Archives/"+link.split(".")[0]+"-index.htm")
            continue
     
            