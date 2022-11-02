#!/usr/bin/env Python
# -- coding: utf-8 --

"""
@version: v1.0
@author: huangyc
@file: xml_2_json.py
@Description: 
@time: 2022/10/31 20:37
"""
import html
import sys
import xml.dom.minidom

from bs4 import BeautifulSoup


def get_text(element, tag_name: str):
    titles = element.getElementsByTagName(tag_name)[0]
    return ''.join(child.data for child in titles.childNodes)


def start_run(file_path: str):
    # 使用minidom解析器打开 XML 文档
    dom_tree = xml.dom.minidom.parse(file_path)
    entrys = dom_tree.documentElement.getElementsByTagName("entry")

    new_doc = xml.dom.minidom.Document()
    root_node = new_doc.createElement('search')

    for entry in entrys:
        # 获取标题、url和内容
        title = get_text(entry, 'title')
        url = get_text(entry, 'url')
        content = get_text(entry, 'content')

        new_entry = new_doc.createElement('entry')

        # 添加标题节点
        new_title = new_doc.createElement('title')
        phone_title_value = new_doc.createTextNode(title)
        new_title.appendChild(phone_title_value)
        new_entry.appendChild(new_title)

        # 添加url节点
        new_url = new_doc.createElement('url')
        phone_url_value = new_doc.createTextNode(url)
        new_url.appendChild(phone_url_value)
        new_entry.appendChild(new_url)

        # 添加内容节点
        new_content = new_doc.createElement('content')
        res = BeautifulSoup(content, 'lxml')
        phone_content_value = new_doc.createTextNode(res.text)
        new_content.appendChild(phone_content_value)
        new_entry.appendChild(new_content)

        # 添加子节点
        root_node.appendChild(new_entry)

    new_doc.appendChild(root_node)
    search_text = html.unescape(new_doc.toprettyxml()).replace('<?xml version="1.0" ?>',
                                                               '<?xml version="1.0" encoding="utf-8"?>')

    # 结果输出
    ori_str = html.unescape(new_doc.toxml())
    with open("public/search.txt", "w", encoding="utf-8") as f:
        new_doc.writexml(f, indent='', addindent='\t', newl='\n', encoding='utf-8')
    with open(r"public/search.txt", 'r', encoding='utf-8') as f:
        s = f.read()
    with open(r"public/search.txt", 'w', encoding='utf-8') as f:
        ns = html.unescape(s)
        f.write(ns)
    print("xml转json结束")


if __name__ == '__main__':
    p_file_path = sys.argv[1]
    # p_file_path = r"D:\桌面\search.xml"
    start_run(file_path=p_file_path)
