def input_info():

    target_url=''
    main_name=''
    keywords=[]
    url_name_key_index=0

    temp_path =input('输入保存的位置和名称(默认为当前目录):')
    excel_path=temp_path if temp_path else '.\\output.xlsx'
    print(f'保存位置为{excel_path}')

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

    return target_url, main_name, keywords, excel_path, url_name_key_index


if __name__=='__main__':
    input_info()
