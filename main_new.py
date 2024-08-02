from get_excel import get_excel_from_keyword, get_excel_from_urlname
from input_new import input_info
import numpy as np
import matplotlib.pyplot as plt

#测试url='https://ieeexplore.ieee.org/document/8939691'

Target_Url,Main_name,Key_words,Excel_Path,Main_Article,Requirement,year, sim_num =input_info()


if Key_words:
    get_excel_from_keyword(Key_words,Excel_Path)

elif Target_Url or Main_name:
    sim_article, scores, score_ranking=get_excel_from_urlname(url=Target_Url,name=Main_name,path=Excel_Path,requirement=Requirement, timerange=year,sim_num=sim_num)

    top5_index_list=[scores.index(x) for x in sorted(scores,reverse=True)[0:min(5,len(sim_article))] ]

    [sim_article[k].get_pdf() for k in top5_index_list]
    [sim_article[k].get_ris() for k in top5_index_list]

    #绘图
    fig=plt.figure(figsize=(9,6))
    fig.subplots_adjust(right=0.7)
    ax=fig.subplots()

    handle1=ax.plot(np.array(range(len(score_ranking))),np.array(score_ranking),c='r',label='Similarity ranking')
    handle2=ax.plot(np.array(range(len(score_ranking))),np.array(range(len(score_ranking))),c='b',label='Original ranking')
    ax.set_xlabel('Article order of search results')
    ax.set_ylabel('Order number')
    handle_list=[handle1[0], handle2[0]]
    ax.legend(handles=handle_list,loc='upper left',bbox_to_anchor=(1.0, 1))
    fig.savefig('./排名.svg')
    fig.show()
else:
    print("main_new出错")












    


