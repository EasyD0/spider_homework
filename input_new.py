def input_info():

    target_url=''
    main_name=''
    keywords=[]
    url_name_key_index=0

    default_path='./excel/output.xlsx'
    temp_path =input(f'输入保存的位置和名称,并确保文件夹存在(默认为当前目录{default_path}):')
    excel_path=temp_path if temp_path else default_path
    print(f'保存位置为{excel_path}')

    year=''
    sim_num=20

    while True:
        target_url = input("输入主要链接:")

        if target_url:
            print(f'输入了{target_url}')
            break
        else:
            main_name = input("输入主要文章名:")
            if main_name:
                print(f'输入了{main_name}')
                url_name_key_index=1
                break
            else:
                keywords = input("输入关键词:").split()
                if keywords:
                    print(f'输入了{keywords}')
                    url_name_key_index=3
                    break
                else:
                    print('未输入有效信息,将重新开始')
    requirement_index=0
    while not(requirement_index in [1,2,3]):
        try:
            requirement_index=int(input('获取参考文献按1,获取相似文献按2,全都要按3: '))
        except:
            print('输入错误')  
        if requirement_index not in [1,2,3]:
            print('输入错误')

    if requirement_index>1:
        year=input('指定年份,如2020-2023: ')
        try:
            sim_num=int(input('搜寻相似文献的数目: '))
        except:
            sim_num=20
    
    requirement={1:'ref',2:'sim',3:'all'}.get(requirement_index)

    return target_url, main_name, keywords, excel_path, url_name_key_index, requirement ,year, sim_num

if __name__=='__main__':
    print(input_info())
