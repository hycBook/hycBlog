#!/usr/bin/env Python
# -- coding: utf-8 --

"""
@version: v1.0
@author: huangyc
@file: xml_2_json.py
@Description: 
@time: 2022/10/31 20:37
"""
import json
from typing import Dict

import xml.dom.minidom
import sys


def json_dump_op(file_name, file: Dict, encoding: str = 'utf-8', ensure_ascii: bool = False, indent: int = 4):
    """
    json文件保存
    :param file_name:
    :param file:
    :param encoding:
    :param ensure_ascii:
    :param indent:
    """
    with open(file_name, 'w', encoding=encoding) as f:
        f.write(json.dumps(file, ensure_ascii=ensure_ascii, indent=indent))


def get_test(obj, elem: str):
    titles = obj.getElementsByTagName(elem)[0]
    texts = [child.data for child in titles.childNodes]
    return ''.join(texts)


def start(file_path):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    # 在集合中获取所有电影
    entrys = collection.getElementsByTagName("entry")

    res = []
    for entry in entrys:
        title = get_test(entry, 'title')
        url = get_test(entry, 'url')
        content = get_test(entry, 'content')
        res.append({'title': title, 'url': url, 'content': content})

    json_dump_op('search.json', res)
    print("xml转json结束")


if __name__ == '__main__':
    file_path = sys.argv[1]
    start(file_path=file_path)
