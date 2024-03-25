import os
import re
import sys


# 批量修改文件名
def rename():
    file_url = r"D:\work\KR-Web3D-V1.1\html\真实人体标本\人体骨骼"
    file_list = os.listdir(file_url)
    # print('当前工程目录：' + os.getcwd())
    current_path = os.getcwd()
    os.chdir(file_url)
    reg = '椎骨'
    for file in file_list:
        file_arr = file.split(reg)
        if len(file_arr) > 1 and len(file_arr[1]) > 0 and file_arr[1][0].isnumeric():
            file_arr[1] = file_arr[1].replace(file_arr[1][0], '(' + str(int(file_arr[1].strip()[0]) - 1) + ')')
        os.rename(file, reg.join(file_arr))
    os.chdir(current_path)  # 改回程序运行前的工作目录
    sys.stdin.flush()


rename()
