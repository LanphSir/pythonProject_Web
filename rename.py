import os
import re
import sys


def rename():
    file_url = r"D:\work\KR-Web3D-V1.1\html\数字3d人体\sj"
    file_list = os.listdir(file_url)
    # print('当前工程目录：' + os.getcwd())
    current_path = os.getcwd()
    os.chdir(file_url)
    dict1 = {'1': "头部", '2': "颈部", '3': "胸部", '4': "腹部", '5': "盆部", '6': "左上肢", '7': "右上肢",
             '8': "左下肢", '9': "右下肢"}
    dict2 = dict(RD='韧带', SJ='神经')
    for file in file_list:
        file_arr = file.split('-')
        if file_arr[0] == '神经':
            # file_arr[0] = dict2[file_arr[0]]
            if file_arr[1] in dict1:
                file_arr[1] = dict1[file_arr[1]]
        os.rename(file, '-'.join(file_arr))
    os.chdir(current_path)  # 改回程序运行前的工作目录
    sys.stdin.flush()


rename()
