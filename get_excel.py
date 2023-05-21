from concurrent.futures import ThreadPoolExecutor, as_completed

import xlsxwriter

from article import Article
from write_excel import write_excel

def get_excel_from_keyword(kw,path):

    a=Article(do_nothing=True)

    a.get_keywords(kw)
    print(a.Keywords)
    a.get_similar_link()

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures  = [executor.submit(lambda url: Article(url), link) for link in a.Similar_Link]
        similar_article_list = [future.result() for future in as_completed(futures)]

    write_excel(similar_article_list,path=path,sheet_name='相似文献')
    return True
#____________________________________________________________

def get_excel_from_urlname(url='',name='',path='./output.xlsx',requirement='all'):
    sim_link_list=[]
    ref_link_list=[]

    try:
        if url:
            art_temp=Article(url=url,main_index=True)
        else:
            art_temp=Article(title=name,main_index=True)

        sim_link_list=art_temp.Similar_Link
        ref_link_list=art_temp.References_Link
    except:
        print('初始化失败')
    #part1
    if requirement=='all' or 'sim':
        if not sim_link_list:
            print('无相似文献')
        
        else:
            print('有相似文献')
            print(f'将对如下关键词搜素{art_temp.Keywords}')
            print(f'将对下面进行爬取{sim_link_list}')
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures  = [executor.submit(lambda url: Article(url), link) for link in sim_link_list]
                article_list = [future.result() for future in as_completed(futures)]
            write_excel(article_list,path=path,sheet_name='相似文献')
    #part2
    if requirement=='all' or 'ref':
        if not ref_link_list:
            print('无相似文献')
        
        else:
            print('有参考文献')
            print(f'将对下面进行爬取{sim_link_list}')
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures  = [executor.submit(lambda url: Article(url), link) for link in ref_link_list]
                article_list = [future.result() for future in as_completed(futures)]
            write_excel(article_list,path=path,sheet_name='参考文献')




