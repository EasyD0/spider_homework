from input_new import input_info
from get_excel import get_excel_from_urlname
from get_excel import get_excel_from_keyword

#可行的测试url='https://ieeexplore.ieee.org/document/8939691'

Target_Url,Main_name,Key_words,Excel_Path,Main_Article=input_info()
if Target_Url or Main_name:
    get_excel_from_urlname(url=Target_Url,name=Main_name,path=Excel_Path,requirement='all')
else:
    get_excel_from_keyword(Key_words,Excel_Path)


