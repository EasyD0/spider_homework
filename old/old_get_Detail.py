import time
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import translators as ts
import json

def get_abstrack_translation(url):

    html=urlopen(url)
    html_byte=html.read()

    '''print(html_byte)
    f=open("test.html","wb")
    f.write(html_byte)
    f.close()'''

    bs=BeautifulSoup(html_byte, features="lxml")
    abstract = bs.find('meta', {'property': 'twitter:description'})['content']
    abstract_translation=ts.google(abstract,from_language="en",to_language='zh', host_url="https://translate.google.com/")


    return abstract,abstract_translation

def get_keywords_of_author(url):

    html=urlopen(url)
    html_byte=html.read()
    
    bs=BeautifulSoup(html_byte, features="lxml")
    temp=bs.find("body",{"class","body-resp"}).find('div', id="LayoutWrapper").find('div', {"class",'col'}).find_all("script", type="text/javascript")

    for script_tag in temp:
        if script_tag:
            script_text=script_tag.string
            if script_text:
                match = re.search(r'xplGlobal\.document\.metadata\s*=\s*(\{.*?\};)', script_text, re.DOTALL) #正则表达式匹配
                if match:
                    metadata_text = match.group()
                    break
            else:
                continue
        else:
            continue

    keywords_string=re.search(r'"keywords":\s*\[.*?\],"', metadata_text, re.DOTALL).group()
    All_Keywords_list_string=re.search(r'\[.*\]', keywords_string, re.DOTALL)
    keywords_list_author=json.loads(All_Keywords_list_string.group())[3]['kwd']

    return keywords_list_author

def get_date(url):

    return 0


if __name__=='__main__':

    url="https://ieeexplore.ieee.org/document/9411225"
    
    print(get_abstrack_translation(url))
    print(get_keywords_of_author(url))
