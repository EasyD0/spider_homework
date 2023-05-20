import time
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.chrome.options import Options

def get_Link_of_kwds(keywords_list,**kwargs):
    
    base_url = "https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&newsearch=true&matchBoolean=true&queryText="
    query = " OR ".join('("%s":"%s")' % ("All Metadata", item) for item in keywords_list)
    url = base_url + query
    service = ChromeService(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    MyDriver = webdriver.Chrome(options=options, service=service)
    #MyDriver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--headless=new'))# type: ignore
    MyDriver.get(url)
    time.sleep(5)
    html = MyDriver.page_source
    MyDriver.quit()

    #html_byte=urlopen(url).html.read()

    soup = BeautifulSoup(html, features="lxml")
    results = soup.find_all("h3")
    link_list=[]

    for results_i in results:
        if results_i.find("a"):
            href=results_i.find("a").get("href")
            link_list.append(href)

    link_list=sorted(set(link_list),key=link_list.index)

    return ['https://ieeexplore.ieee.org'+link for link in link_list]



if __name__=='__main__':
    keywords_list=['security','location']
    print(get_Link_of_kwds(keywords_list))
