#!/usr/bin/env Python
# -- coding: utf-8 --

"""
@version: v1.0
@author: huangyc
@file: upload_search_file.py
@Description: 文件上传至薄荷图床
@time: 2022/10/31 10:06
"""
import os.path
import urllib.parse
import urllib.request
import sys


class HttpMethod:
    def __init__(self, base_url: str, cookie: str, url_data: str = None, save_path: str = None):
        """
        @param base_url: 图床根路径
        @param cookie: cookie, 用于删除文件使用
        @param url_data: 需要上传的文件
        @param save_path: 保存的路径, 默认保存到 "gitbook_search"
        """
        self.base_url = base_url
        self.cookie = cookie
        self.url_data = url_data
        self.save_path = save_path or "gitbook_search"

        self.referer = f'{self.base_url}/url.php'
        self.url_data = self.url_data or "https://raw.githubusercontent.com/hycBook/hycBlog/gh-pages/search.txt"
        self.post_data = {"urlData": url_data, 'savePath': self.save_path}

        self.up_base_url = f'{self.base_url}/url-up-savename.php'
        _, file_name = os.path.split(self.url_data)
        self.delete_url = f"{base_url}/fileNameModeManager.php?p={self.save_path}&del={file_name}"
        self.del_referer = f'{base_url}/fileNameModeManager.php?p={self.save_path}'

        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"

    def delete_file(self, timeout: float = 100):
        inner_head = {'user-agent': self.ua, 'Referer': self.del_referer, "cookie": self.cookie}
        add = urllib.request.Request(url=self.delete_url, headers=inner_head, method='GET')
        response = urllib.request.urlopen(url=add, timeout=timeout)

    def upload_file(self, timeout: float = 100):
        data = urllib.parse.urlencode(self.post_data)
        data = data.encode('ascii')
        inner_head = {'user-agent': self.ua, 'Referer': self.referer, 'cookie': 'name-mode=_isSavenameMode'}
        add = urllib.request.Request(url=self.up_base_url, headers=inner_head, method='POST')
        response = urllib.request.urlopen(url=add, timeout=timeout, data=data)
        return response.read().decode('utf-8')


import re
import time


# 获取10位的时间戳  精度是秒(s)
def time_stamp_10():
    return int(time.time())


def add_one(match):
    val = match.groups()[0]
    return f"{match.group()[:-10]}{time_stamp_10()}"


def add_many(match):
    val = match.groups()[0]
    return f"{match.group()[:-10]}{time_stamp_10() + 1500}"


if __name__ == '__main__':
    p_base_url, p_url_data, p_cookie = sys.argv[1], sys.argv[2], sys.argv[3]
    p_save_path = "gitbook_search"
    new_ck = re.sub('Hm_lvt_.*?=(\d{10})', add_one, p_cookie)
    p_cookie = re.sub('Hm_lpvt_.*?=(\d{10})', add_many, new_ck)

    pic_server = HttpMethod(base_url=p_base_url, cookie=p_cookie, url_data=p_url_data, save_path=p_save_path)
    pic_server.delete_file()
    res = pic_server.upload_file()
    _, new_file_name = os.path.split(res)
    print(f"上传成功, 新的文件名为: {p_save_path}\{new_file_name}")
