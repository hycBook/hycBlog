#!/usr/bin/env Python
# -- coding: utf-8 --

"""
@version: v1.0
@author: huangyc
@file: dir_change.py
@Description: 
@time: 2022/9/10 7:34
"""
import re
import shutil
from urllib.parse import unquote
import os


def platform():
    """ 获取当前操作系统类型 """
    import platform
    return platform.system().lower()


if platform() == 'linux':
    base_path = os.getcwd()
else:
    base_path = r'H:\github\bks\hexo_books\测试\_posts'

target_path = os.path.join(base_path, 'target_dir')
if os.path.exists(target_path):
    shutil.rmtree(target_path)
os.mkdir(target_path)

target_img_path = os.path.join(base_path, 'target_dir_img')
if os.path.exists(target_img_path):
    shutil.rmtree(target_img_path)
os.mkdir(target_img_path)

pat_img = re.compile('src=\"[/.]{0,1}[//]{0,1}(res.*?)\"')
pat_img = re.compile('src=\"[/.]{0,1}[\\\\//]{0,1}(res.*?)\\"')
pat_md = re.compile('!\[.*?\]\([/.]{0,1}[//]{0,1}(res.*?)\)')


def deal_img(file_name):
    file_name = file_name

    def dash_repl(match_obj):
        zf = match_obj.group(0)
        if file_name not in match_obj.string and 'other' not in match_obj.string:
            print("匹配不上:", file_name, match_obj.string)
        # print("匹配不上:", file_name, match_obj.string)
        name = zf.split('/')[-1]
        return f'src="{file_name}/{name}'

    return dash_repl


def deal_md(file_name, sp: str):
    true_file_name = os.path.splitext(file_name)[0]
    res = re.findall(pat_md, sp)
    if len(res) == 1:
        if true_file_name not in sp and 'other' not in sp:
            print("匹配不上:", true_file_name, sp)
        # print("匹配不上:", true_file_name, sp)
        name = res[0].split('/')[-1]
        return f'![img](../../../../img/{true_file_name}/{name})'
    return sp


def write_to_target(target_path: str, file_path, file_name):
    lines = []
    true_file_name = os.path.splitext(file_name)[0]
    inner_deal_img = deal_img(file_name=true_file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = unquote(line, 'utf-8')
            line = re.sub(pat_img, inner_deal_img, line)
            line = deal_md(file_name, line)
            if line.strip() == '[TOC]':
                continue
            lines.append(line)

    target_file = os.path.join(target_path, file_name)
    with open(target_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


# 使用Python实现从各个子文件夹中复制指定文件的方法
# 递归复制文件夹内的文件
def copy_files(sourceDir, targetDir):
    for file in os.listdir(sourceDir):
        try:
            sourceDir1 = os.path.join(sourceDir, file)  # 路径名拼接
            targetDir1 = os.path.join(targetDir, file)

            print("sourceDir1" + sourceDir1)
            print("targetDir1" + targetDir1)

            for file in os.listdir(sourceDir1):
                sourceDir2 = os.path.join(sourceDir1, file)
                print(sourceDir2 + "__sourceDir2")

                if re.search('.*(icon).+', file, re.I):
                    sourceFile = sourceDir2
                    print(file)
                    print("sourceFile__" + sourceFile)
                    targetFile = os.path.join(targetDir1, file)
                    print("目标文件路径__" + targetFile)
                    if os.path.isfile(sourceFile):
                        if not os.path.exists(targetDir1):
                            os.makedirs(targetDir1)
                            print("文件夹已创建")
                        else:
                            print("文件夹已存在")
                        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (
                                os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                            open(targetFile, "wb").write(open(sourceFile, "rb").read())
                            print(targetFile + " copy succeeded")
                        else:
                            print("复制失败")
                    else:
                        print("文件不存在")

                else:
                    print("没有找到icon")
        except OSError:
            pass
        continue
    print('end')


# line= r'>![image-20200322202245440](res/JDBC_JDBC基础/image-20200322202245440.png)\n'


def my_copy_files(cur, target):
    for dir in os.listdir(cur):
        s = os.path.join(cur, dir)
        t = os.path.join(target, dir)
        if os.path.isdir(s):
            shutil.copytree(s, t)
        elif os.path.isfile(s):
            shutil.copy(s, t)


def deal_res(target_path: str, file_path, listdir):
    """ 资源处理 """
    lod_ = []
    true_listdir = [os.path.splitext(file_name)[0] for file_name in listdir if 'res' != file_name]
    for dir in os.listdir(file_path):
        if dir in true_listdir:
            target = os.path.join(target_path, dir)
            cur = os.path.join(file_path, dir)
            lod_.append(target)
            shutil.copytree(cur, target)

    for tl in true_listdir:
        p = os.path.join(target_path, tl)
        if not os.path.exists(p):
            os.mkdir(p)
            lod_.append(p)

    for dir in os.listdir(file_path):
        if dir not in true_listdir:
            for target in lod_:
                cur = os.path.join(file_path, dir)
                my_copy_files(cur, target)


def start():
    for dir in os.listdir(base_path):
        inner_dir = os.path.join(base_path, dir)
        if os.path.isdir(os.path.join(inner_dir, 'res')):
            print(inner_dir)
            listdir = os.listdir(inner_dir)
            for file_name in listdir:
                file_path = os.path.join(inner_dir, file_name)
                if os.path.isfile(file_path):
                    write_to_target(target_path=target_path, file_path=file_path, file_name=file_name)
                elif file_name == 'res' and os.path.isdir(file_path):
                    # deal_res(target_path=target_path, file_path=file_path, listdir=listdir)
                    deal_res(target_path=target_img_path, file_path=file_path, listdir=listdir)


if __name__ == '__main__':
    # sp = '<center><img src="res/Python%20Base/13088413-c5ced16c6b0c2d29.webp" width="400"/></center>'
    # sp = unquote(sp)
    # inner_fn = deal_img("1.python多进程")
    # res = re.sub(pat_img, inner_fn, sp)
    #
    # sp = '![img](res/other/异世界蕾姆_0.jpg)'
    # inner_fn2 = deal_md("1.python多进程")
    # res = re.sub(pat_md, inner_fn2, sp)
    # print(res)

    start()
