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

    newDoc = xml.dom.minidom.Document()
    rootNode = newDoc.createElement('search')
    import html

    from bs4 import BeautifulSoup

    for entry in entrys:
        title = get_test(entry, 'title')
        url = get_test(entry, 'url')
        content = get_test(entry, 'content')
        new_entry = newDoc.createElement('entry')

        new_title = newDoc.createElement('title')
        phone_title_value = newDoc.createTextNode(title)
        new_title.appendChild(phone_title_value)

        new_url = newDoc.createElement('url')
        phone_url_value = newDoc.createTextNode(url)
        new_url.appendChild(phone_url_value)

        new_content = newDoc.createElement('content')

        res = BeautifulSoup(content, 'lxml')
        phone_content_value = newDoc.createTextNode(res.text)
        new_content.appendChild(phone_content_value)

        new_entry.appendChild(new_title)
        new_entry.appendChild(new_url)
        new_entry.appendChild(new_content)
        rootNode.appendChild(new_entry)

    newDoc.appendChild(rootNode)

    ori_str = html.unescape(newDoc.toxml())
    with open("public/search.txt", "w", encoding="utf-8") as f:
        newDoc.writexml(f, indent='', addindent='\t', newl='\n', encoding='utf-8')
    print(ori_str)
    print("xml转json结束")


if __name__ == '__main__':
    # file_path = sys.argv[1]
    file_path = r"D:\桌面\search.xml"
    start(file_path=file_path)
