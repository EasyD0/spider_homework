import time
from selenium import webdriver
from bs4 import BeautifulSoup
#from urllib.request import urlopen
from article import Article
#from selenium.webdriver.chrome.options import Options
#import requests


'''def input_info(target_url='',
               excel_path='.\\output.xlsx',
               main_name=''):

    target_url =input("输入主要链接:") 
    print("正在检测链接是否有效")
    article=Article(target_url,True)

    #if urlopen(target_url):
    if article.Title:
        print('链接有效')
    else:
        print('链接无效')
        Main_Name =input("输入主要文章名:") 
        if not Main_Name:
            print('未输入有效信息,将重新开始')
            target_url,excel_path,main_name,article=input_info()  #这样迭代容易出问题,改用while控制
            return 0
        else:
            url=("https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText="+Main_Name).replace(' ','%20')
            
            #注意驱动的位置
            driver = webdriver.Chrome(executable_path=".\\chromedriver.exe",options=webdriver.ChromeOptions().add_argument("--headless"))
            driver.get(url)
            time.sleep(5)
            html_driver= driver.page_source
            driver.quit()
            bs=BeautifulSoup(html_driver,'lxml')
            target_url='https://ieeexplore.ieee.org'+bs.find('h3',{'class':"text-md-md-lh"}).find('a').get('href')
            
    excel_path=input('输入保存的位置和名称(默认为当前目录):')
    print(target_url)
    return target_url,excel_path,main_name,article'''

def input_info(target_url='',
               excel_path='',
               main_name=''):
    
    temp_path =input('输入保存的位置和名称(默认为当前目录):')
    excel_path=temp_path if temp_path else '.\\output.xlsx'

    while True:
        target_url = input("输入主要链接:")
        print("正在检测链接是否有效")
        article = Article(target_url, True)

        if article.Title:
            print('链接有效')
            break
        else:
            print('链接无效')
            main_name = input("输入主要文章名:")
            if main_name:
                url = ("https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=" + main_name).replace(' ', '%20')

                # 注意驱动的位置
                driver = webdriver.Chrome(executable_path=".\\chromedriver.exe",options=webdriver.ChromeOptions().add_argument("--headless"))# type: ignore
                driver.get(url)
                time.sleep(5)
                html_driver = driver.page_source
                driver.quit()
                bs = BeautifulSoup(html_driver, 'lxml')
                target_url = 'https://ieeexplore.ieee.org' + bs.find('h3', {'class': "text-md-md-lh"}).find('a').get('href')# type: ignore
                break
            else:
                print('未输入有效信息,将重新开始')

    print('将对该链接进行爬取:{}'.format(target_url))
    return target_url, excel_path, main_name, article