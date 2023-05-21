from article import Article
import xlsxwriter

def write_excel(article_list,path,sheet_name):
    title_list=[article.Title for article in article_list ]
    link_list=[article.Url for article in article_list ]
    abstract_list=[article.Abstract for article in article_list]
    abstract_translation_list=[article.Abstract_Translation for article in article_list]
    date_list=[article.Date for article in article_list]
    journal_name_list=[article.Journal_Name for article in article_list]
    impact_list=[article.Impact_Factor for article in article_list]
    doi_list=[article.Doi for article in article_list]

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet(sheet_name)
    worksheet.write_column(1, 0, title_list)
    worksheet.write_column(1, 1, link_list)
    worksheet.write_column(1, 2, abstract_list)
    worksheet.write_column(1, 3, abstract_translation_list)
    worksheet.write_column(1, 4, date_list)
    worksheet.write_column(1, 5, journal_name_list)
    worksheet.write_column(1, 6, impact_list)
    worksheet.write_column(1, 7, doi_list)
    worksheet.write_row(0,0,['标题','链接','摘要','摘要翻译','日期','期刊名/会议名','影响因子','doi'])
    workbook.close()
