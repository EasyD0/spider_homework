#import time
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#import re
#import translators as ts
#import json

#import requests
from article import Article
from old_get_link import get_Link_of_kwds
import pandas as pd
from input import input_info
from concurrent.futures import ThreadPoolExecutor, as_completed

#_________________________

    
ref_link_list=['https://ieeexplore.ieee.org/document/8465238', 'https://ieeexplore.ieee.org/document/1334558']

ref_article_list=[]
i=0
for link in ref_link_list:
    ref_article_list.append(Article(link))
    print(ref_article_list[i].Title)
    i=i+1
    print(i)
print("完成")
    

ref_title_list=[str(article.Title) for article in ref_article_list ]
ref_abstract_list=[str(article.Abstract) for article in ref_article_list]
ref_abstract_translation_list=[str(article.Abstract_Translation) for article in ref_article_list]
ref_date_list=[str(article.Date) for article in ref_article_list]
ref_journal_name_list=[str(article.Journal_Name) for article in ref_article_list]
ref_impact_list=[str(article.Impact_Factor) for article in ref_article_list]
ref_doi_list=[str(article.Doi) for article in ref_article_list]

###############


'''similar_title_list=[str(article.Title) for article in similar_article_list ]
similar_abstract_list=[str(article.Abstract) for article in similar_article_list]
similar_abstract_translation_list=[str(article.Abstract_Translation) for article in similar_article_list]
similar_date_list=[str(article.Date) for article in similar_article_list]
similar_journal_name_list=[str(article.Journal_Name) for article in similar_article_list]
similar_impact_list=[str(article.Impact_Factor) for article in similar_article_list]
similar_doi_list=[str(article.Doi) for article in similar_article_list]'''


df_ref=pd.DataFrame({'标题':ref_title_list,
                     '摘要':ref_abstract_list,
                     '摘要翻译':ref_abstract_translation_list,
                     '日期':ref_date_list,
                     '期刊名/会议名':ref_journal_name_list,
                     '影响因子':ref_impact_list,
                     'doi':ref_doi_list})

'''df_similar=pd.DataFrame({'标题':similar_title_list,
                     '摘要':similar_abstract_list,
                     '摘要翻译':similar_abstract_translation_list,
                     '日期':similar_date_list,
                     '期刊名/会议名':similar_journal_name_list,
                     '影响因子':similar_impact_list,
                     'doi':similar_doi_list})'''

print({'标题':ref_title_list,
    '摘要':ref_abstract_list,
    '摘要翻译':ref_abstract_translation_list,
    '日期':ref_date_list,
    '期刊名/会议名':ref_journal_name_list,
    '影响因子':ref_impact_list,
    'doi':ref_doi_list})

with pd.ExcelWriter('./save.xlsx') as writer:
    df_ref.to_excel(writer, sheet_name='参考文献')
    #df_similar.to_excel(writer, sheet_name='相似文献')
print('OK')