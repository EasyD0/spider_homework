from concurrent.futures import ThreadPoolExecutor, as_completed

from article import Article
#import pandas as pd
from input import input_info
from write_excel import write_excel


#可行的测试url='https://ieeexplore.ieee.org/document/8939691/references#references'

Target_Url,Excel_Path,Main_Name,Main_Article=input_info()
#print(Main_Article.Keywords)
#print(Main_Article)

ref_link_list=Main_Article.References_Link
similar_link_list=Main_Article.Similar_Link

'''#参考文献获取
with ThreadPoolExecutor(max_workers=4) as executor:
    futures  = [executor.submit(lambda url: Article(url), link) for link in ref_link_list]
    ref_article_list = [future.result() for future in as_completed(futures)]
write_excel(ref_article_list,Excel_Path,'参考文献')'''

#相似文献获取
with ThreadPoolExecutor(max_workers=4) as executor:
    futures  = [executor.submit(lambda url: Article(url), link) for link in similar_link_list]
    similar_article_list = [future.result() for future in as_completed(futures)]
write_excel(similar_article_list,Excel_Path+'.xlsx','相似文献')
print('OK')


'''
###测试问题
similar_article_list=[]
for link in similar_link_list:
    print(link)
    art_temp=Article(link)
    similar_article_list.append(art_temp)
####测试结束    
'''

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






