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
#from get_link import get_Link_of_kwds
#import pandas as pd
from input import input_info
from concurrent.futures import ThreadPoolExecutor, as_completed
import xlsxwriter

#_________________________

#可行的测试url='https://ieeexplore.ieee.org/document/8939691/references#references'

Target_Url,Excel_Path,Main_Name,Main_Article=input_info()
#my_keywd=Main_Article.Keywords
#print(my_keywd)

ref_link_list=Main_Article.References_Link
similar_link_list=Main_Article.Similar_Link
#similar_link_list=get_Link_of_kwds(my_keywd)

#print(ref_link_list)
#print(similar_link_list)

###测试问题
'''similar_article_list=[]
for link in similar_link_list:
    print(link)
    art_temp=Article(link)
    similar_article_list.append(art_temp)'''
####测试结束    

'''###参考文献获取
with ThreadPoolExecutor(max_workers=4) as executor:
    futures  = [executor.submit(lambda url: Article(url), link) for link in ref_link_list]
    ref_article_list = [future.result() for future in as_completed(futures)]

ref_title_list=[article.Title for article in ref_article_list ]
ref_abstract_list=[article.Abstract for article in ref_article_list]
ref_abstract_translation_list=[article.Abstract_Translation for article in ref_article_list]
ref_date_list=[article.Date for article in ref_article_list]
ref_journal_name_list=[article.Journal_Name for article in ref_article_list]
ref_impact_list=[article.Impact_Factor for article in ref_article_list]
ref_doi_list=[article.Doi for article in ref_article_list]

workbook = xlsxwriter.Workbook(Excel_Path)
worksheet1 = workbook.add_worksheet('参考文献')
worksheet1.write_column(1, 0, ref_title_list)
worksheet1.write_column(1, 1, ref_link_list)
worksheet1.write_column(1, 2, ref_abstract_list)
worksheet1.write_column(1, 3, ref_abstract_translation_list)
worksheet1.write_column(1, 4, ref_date_list)
worksheet1.write_column(1, 5, ref_journal_name_list)
worksheet1.write_column(1, 6, ref_impact_list)
worksheet1.write_column(1, 7, ref_doi_list)
worksheet1.write_row(0,0,['标题','摘要','摘要翻译','日期','期刊名/会议名','影响因子','doi'])
workbook.close()
'''
###相似文献获取
with ThreadPoolExecutor(max_workers=4) as executor:
    futures  = [executor.submit(lambda url: Article(url), link) for link in similar_link_list]
    similar_article_list = [future.result() for future in as_completed(futures)]

similar_title_list=[article.Title for article in similar_article_list ]
similar_abstract_list=[article.Abstract for article in similar_article_list]
similar_abstract_translation_list=[article.Abstract_Translation for article in similar_article_list]
similar_date_list=[article.Date for article in similar_article_list]
similar_journal_name_list=[article.Journal_Name for article in similar_article_list]
similar_impact_list=[article.Impact_Factor for article in similar_article_list]
similar_doi_list=[article.Doi for article in similar_article_list]

workbook = xlsxwriter.Workbook(Excel_Path)
worksheet2 = workbook.add_worksheet('相似文献')
worksheet2.write_column(1, 0, similar_title_list)
worksheet2.write_column(1, 1, similar_link_list)
worksheet2.write_column(1, 2, similar_abstract_list)
worksheet2.write_column(1, 3, similar_abstract_translation_list)
worksheet2.write_column(1, 4, similar_date_list)
worksheet2.write_column(1, 5, similar_journal_name_list)
worksheet2.write_column(1, 6, similar_impact_list)
worksheet2.write_column(1, 7, similar_doi_list)
worksheet2.write_row(0,0,['标题','摘要','摘要翻译','日期','期刊名/会议名','影响因子','doi'])
workbook.close()

'''
#这部分总是莫名出错,提示类型错误,pandas无法处理
df_ref=pd.DataFrame({'标题':ref_title_list,
                     '摘要':ref_abstract_list,
                     '摘要翻译':ref_abstract_translation_list,
                     '日期':ref_date_list,
                     '期刊名/会议名':ref_journal_name_list,
                     '影响因子':ref_impact_list,
                     'doi':ref_doi_list})

df_similar=pd.DataFrame({'标题':similar_title_list,
                     '摘要':similar_abstract_list,
                     '摘要翻译':similar_abstract_translation_list,
                     '日期':similar_date_list,
                     '期刊名/会议名':similar_journal_name_list,
                     '影响因子':similar_impact_list,
                     'doi':similar_doi_list})

with pd.ExcelWriter(Excel_Path) as writer:
    df_ref.to_excel(writer, sheet_name='参考文献')
    #df_similar.to_excel(writer, sheet_name='相似文献')
'''
print('OK')






