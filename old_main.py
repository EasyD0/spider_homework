import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import translators as ts
import json
from selenium.webdriver.chrome.options import Options

#url="https://ieeexplore.ieee.org/document/9411225"
url="https://ieeexplore.ieee.org/document/7809977"
html=urlopen(url)
html_byte=html.read()

bs=BeautifulSoup(html_byte)
abstract = bs.find('meta', {'property': 'twitter:description'})['content']
print(abstract)

temp=bs.find("body",{"class","body-resp"}).find('div', id="LayoutWrapper").find('div', {"class",'col'}).find_all("script", type="text/javascript")

for script_tag in temp:
    if script_tag:
        script_text=script_tag.string
        if script_text:
            match = re.search(r'xplGlobal\.document\.metadata\s*=\s*(\{.*?\};)', script_text, re.DOTALL) #正则表达式匹配
        else:
            continue
    else:
        continue

    if match:
        metadata_text = match.group()
        print(metadata_text)
        break

type(metadata_text)


keywords_string=re.search(r'"keywords":\s*\[.*?\],"', metadata_text, re.DOTALL).group()
All_Keywords_list_string=re.search(r'\[.*\]', keywords_string, re.DOTALL)
keywords_list=json.loads(All_Keywords_list_string.group())[3]['kwd']
print(keywords_list)
print(ts.google(abstract,from_language="en",to_language='zh', host_url="https://translate.google.com/"))

url1='https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=security'
MyDriver = webdriver.Chrome(executable_path=".\\chromedriver.exe")
MyDriver.get(url1)
time.sleep(10)
html = MyDriver.page_source
f=open('search2.html','w')
f.write(html)
f.close()
