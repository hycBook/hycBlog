#!/usr/bin/env Python
# -- coding: utf-8 --

"""
@version: v1.0
@author: huangyc
@file: xml_2_json.py
@Description: 
@time: 2022/10/31 20:37
"""
import sys
import xml.dom.minidom

from bs4 import BeautifulSoup


def get_text(element, tag_name: str):
    titles = element.getElementsByTagName(tag_name)[0]
    return ''.join(child.data for child in titles.childNodes)


class RawText(xml.dom.minidom.Text):
    def writexml(self, writer, indent="", addindent="", newl="", encoding=None):
        if self.data:
            writer.write('%s%s%s' % (indent, self.data, newl))


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
        # cot = RawText()
        # cot.ownerDocument = new_doc
        # cot.data = BeautifulSoup(content, 'lxml').text
        # new_content.appendChild(cot)
        phone_content_value = new_doc.createTextNode(BeautifulSoup(content, 'lxml').text)
        new_content.appendChild(phone_content_value)
        new_entry.appendChild(new_content)

        # 添加子节点
        root_node.appendChild(new_entry)

    new_doc.appendChild(root_node)

    # 结果输出
    with open("public/search.txt", "w", encoding="utf-8") as f:
        new_doc.writexml(f, indent='', addindent='\t', newl='\n', encoding='utf-8')

    print("xml转json结束")


if __name__ == '__main__':
    p_file_path = sys.argv[1]
    # p_file_path = r"F:\Desktop\fsdownload\search.xml"
    start_run(file_path=p_file_path)
