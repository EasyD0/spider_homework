import time
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import translators as ts
import json
import requests
import os
from selenium.webdriver.chrome.service import Service as ChromeService

class Article:
    #公共成员
    Main_Index=False  #用户指定
    Journal_Index=False  #get_impact_factor

    Html='' 
    Html_Driver=''
    Url=''

    Title='' #依赖html, get_title()
    Date='' #依赖html_driver
    Journal_Name='' #依赖html_driver get_journal_name()
    Abstract=''  #依赖 Html
    Abstract_Translation=''

    #主要成员
    Keywords=[]    #依赖html
    References_Link=[] #依赖html_driver

    #参考成员
    Impact_Factor='' #依赖html_driver
    Doi='' #依赖 html_driver get_doi()
#_________________________________________________________

    def __init__(self, url='', main_index=False, **kwargs):
        self.Url=url
        self.Main_Index=main_index
        
        '''        
        for key, wd in kwargs:
            
            if key =='Title' or 'title':
                self.Title=wd
            if key =='Keywords' or 'Keyword':
                self.Keywords=wd
            if key =='Abstract' or 'abstract':
                self.Abstract=wd
        '''

        if url:
            '''            
            self.get_html()
            if not self.Main_Index:
                self.get_html_driver()
            '''

            self.get_html()
            self.get_html_driver()
            self.get_journal_index()

            if self.Main_Index:
                self.get_title()
                self.get_date()
                self.get_abstract()
                self.get_keywords()
                self.get_references()
            else:
                self.get_title()
                self.get_date()
                self.get_journal_name()
                self.get_abstract()
                self.get_impact_factor()
                self.get_doi()
        else:
            print("警告,该文章类没有传入链接,文章未定义")

        '''
        if self.Html:
            self.get_abstract()
            self.get_title()
            self.get_date()

        if self.Html_Driver:
            self.get_journal_name()
            self.get_abstract()
            self.get_title()
        '''
#_________________________________________________________

    def get_html(self):
        #print("get_html")
        #if self.Url:  #如果加了这行, 后面很多函数在 做 get_html之前不用再检测  //更新下,这行不能要
        #为何不在这里检测Url?? 是为了防止循环 例如在get_abstract 中没有 if self.Url检测,则陷入循环

        self.Html=urlopen(self.Url).read() #byte类型
        return 0
#_________________________________________________________

    def get_html_driver(self):
        #print("get_html_driver")
        #注意驱动的位置
        service = ChromeService(executable_path='./chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options, service=service)
        #driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--headless=new'))
        driver.get(self.Url)
        time.sleep(10)
        self.Html_Driver = driver.page_source
        driver.quit()
        return 0
#_________________________________________________________

    def get_abstract(self):
        #print("get_abstract")
        #如果发生异常,需要修改包'translators'的源码,将链接translate.google.cn改为.com
        if self.Abstract:
            return 0
        
        if self.Html:
            bs=BeautifulSoup(self.Html,"lxml")
            self.Abstract = str(bs.find('meta', {'property': 'twitter:description'})['content'])#.replace('\n','')
            #用str防止Nonetype 报错
            
            if self.Abstract:
                #5.16日之后的tranlators 包修改了方法,如果报错没有该方法,请根据官网文档自行修改
                self.Abstract_Translation=ts.google(self.Abstract,from_language="en",to_language='zh', host_url="https://translate.google.com/")
            return 0        
        else:
            if self.Url:
                self.get_html()
                self.get_abstract()
            else:
                print('get_abstract:获取摘要失败,文章未定义,链接缺失')
                return 0
#_________________________________________________________      

    def get_date(self):
        #print("get_date")
        if self.Date:
            return 0
        if self.Html_Driver:
            bs_driver=BeautifulSoup(self.Html_Driver,"lxml")

            if self.Journal_Index:
                self.Date=str(bs_driver.find('strong', text='Date of Publication:').next_sibling)
            else:
                self.Date=str(bs_driver.find('strong', text='Date of Conference: ').next_sibling)
            return 0

        else:
            if self.Url:
                self.get_html()
                self.get_date()
                return 0   # 这行最好加上
            else:
                print('get_date:获取日期失败,文章未定义,链接缺失')
                return 0
#_________________________________________________________

    def get_title(self):
        #print("get_title")
        if self.Title:
            return 0
        
        if self.Html:
            bs=BeautifulSoup(self.Html,"lxml")
            self.Title=bs.find("title").find_next_sibling().get('content')
            return 0
        
        else:
            if self.Url:
                self.get_html()
                self.get_title()
                return 0
            else:
                print('get_title:获取标题失败,文章未定义,链接缺失')
                return 0
#_________________________________________________________

    def get_doi(self):
        #print("get_doi")
        if self.Doi:
            print("已经有了Doi")
            return 0
        
        if self.Html_Driver:
            bs_driver=BeautifulSoup(self.Html_Driver,"lxml")
            self.Doi=bs_driver.find('strong', text='DOI: ').find_next_sibling().get_text()
            #Doi_link='https://doi.org/'+doi
            return 0
        
        else:
            if self.Url:
                self.get_html()
                self.get_doi()
                return 0
            else:
                print('获取doi失败,文章未定义,链接缺失')
                return 0
#_________________________________________________________

    def get_journal_name(self):
        #print("get_journal_name")
        if self.Journal_Name:
            print("已经有了期刊名/会议名")
            return 0
        
        if self.Html_Driver:
            bs_driver=BeautifulSoup(self.Html_Driver,"lxml")
            self.Journal_Name=bs_driver.find('strong', text='Published in: ').find_next_sibling().get_text()
            return 0
        else:
            if self.Url:
                self.get_html_driver()
                self.get_journal_name()
                return 0
            else:
                print('get_journal_name:获取期刊名/会议名失败,文章未定义,链接缺失')
                return 0
#_________________________________________________________

    def get_keywords(self):
        #print("get_keywords")
        if self.Keywords:
            print("已经有了关键词")
            return 0
        if self.Html:
            bs=BeautifulSoup(self.Html,"lxml")
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
            self.Keywords=json.loads(All_Keywords_list_string.group())[3]['kwd']

            return 0
        
        else:
            if self.Url:
                self.get_html()
                self.get_keywords()
                return 0
            else:
                print("get_keywords:获取关键词失败,文章未定义,链接缺失")
                return 0
#_________________________________________________________

    def get_journal_index(self):
        #print("get_journal_index")
        if self.Html_Driver:
            bs_driver=BeautifulSoup(self.Html_Driver,"lxml")

            if bs_driver.find(href="/browse/periodicals/title/"):
                self.Journal_Index=True  #this is a Journals or Magazines paper'
                return 0
            else:
                return 0
        
        else:
            if self.Url:
                self.get_html_driver()
                self.get_journal_index()
                return 0
            else:
                print("get_journal_index:获取期刊会议指标失败,文章未定义,链接缺失")
                return 0
#_________________________________________________________

    def get_impact_factor(self):
        #print("get_impact_factor")
        if self.Html_Driver:

            if self.Journal_Index:

                bs_driver=BeautifulSoup(self.Html_Driver,"lxml")

                if bs_driver.find(href="/browse/periodicals/title/"):
                    
                    self.Journal_Index=True  #this is a Journals or Magazines paper'

                    journal_link='https://ieeexplore.ieee.org'+bs_driver.find('strong', text='Published in: ').find_next_sibling().get('href')
                    service = ChromeService(executable_path='./chromedriver.exe')
                    options = webdriver.ChromeOptions()
                    options.add_argument('--headless=new')
                    driver = webdriver.Chrome(options=options, service=service)
                    #driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--headless=new'))
                    driver.get(journal_link)
                    time.sleep(5)
                    journal_html = driver.page_source
                    driver.quit()

                    bs_temp=BeautifulSoup(journal_html,"lxml")
                    self.Impact_Factor=bs_temp.find('a',{'class':'stats-jhp-impact-factor'}).find('span',{'class':'text-md-md-lh'}).get_text()
                    return 0
                else :
                    self.Impact_Factor=''
                    return 0
        else:
            if self.Url:
                self.get_html_driver()
                self.get_impact_factor()
                return 0
            else:
                print("get_impact_factor:获取因子失败,文章未定义,链接缺失")
                return 0
#_________________________________________________________

    def get_references(self):
        #print("get_references")
        if self.References_Link:
            return 0
        if self.Html_Driver:
            bs_driver=BeautifulSoup(self.Html_Driver,"lxml")
            View_Article=bs_driver.find_all("a",{"class":'stats-reference-link-viewArticle'})
            #CrossRef=bs_driver.find_all("a",{"class":'stats-reference-link-crossRef'})
            
            View_Article_list=[]
            #CrossRef_list=[]

            for article in View_Article:
                if article:
                    View_Article_list.append(article.get("href"))
            
            temp=['https://ieeexplore.ieee.org'+link for link in View_Article_list]
            self.References_Link=sorted(set(temp),key=temp.index)
            
            '''
            for article in CrossRef:
                if article:
                    CrossRef_list.append(article.get("href"))
            '''
            return 0

        else:
            if self.Url:
                self.get_html_driver()
                self.get_references()
                return 0
            else:
                print("get_references:获取参考文献失败,文章未定义,链接缺失")
                return 0   
#_________________________________________________________

    def get_pdf(self, save_path='.\\pdf\\'):
        if self.Doi:

            scihub_link='https://sci-hub.se/'+self.Doi
            scihub_html=urlopen(scihub_link).read()
            bs_pdf=BeautifulSoup(scihub_html,"lxml")
            pdf_link='https:'+bs_pdf.find('embed',{'type':"application/pdf"}).get('src')

            response = requests.get(pdf_link)


            file_name =self.Title+'.pdf' if self.Title else os.path.basename(pdf_link)+'.pdf'

            with open(save_path+file_name, 'wb') as f:
                f.write(response.content)
            
            return 0
        else:
            print('get_pdf:Doi 缺失,无法获取pdf')
            if self.Url:
                print('get_pdf:文章链接存在,尝试获取Doi')
                self.get_doi()
                self.get_pdf()
                return 0
            else:
                print("get_pdf:获取pdf失败,文章未定义,链接缺失")
                return 0
#_________________________________________________________


if __name__=="__main__":
    url_conference="https://ieeexplore.ieee.org/document/7809977"
    url_trans='https://ieeexplore.ieee.org/document/5165285'

    conference=Article(url_conference,True)
    trans=Article(url_trans)

    print(conference.Main_Index)
    print(conference.Journal_Index)
    print(conference.Title)
    print(conference.Date)
    print(conference.Journal_Name)
    print(conference.Abstract)
    print(conference.Abstract_Translation)
    print(conference.Keywords)
    print(conference.References_Link)
    print(conference.Impact_Factor)
    print(conference.Doi)

    print(trans.Main_Index)
    print(trans.Journal_Index)
    print(trans.Title)
    print(trans.Date)
    print(trans.Journal_Name)
    print(trans.Abstract)
    print(trans.Abstract_Translation)
    print(trans.Keywords)
    print(trans.References_Link)
    print(trans.Impact_Factor)
    print(trans.Doi)
