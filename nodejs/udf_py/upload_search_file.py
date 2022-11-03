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
import random
import sys
import time
import urllib.parse
import urllib.parse
import urllib.request
import urllib.request
from http import cookiejar

time_lst = [1200, 1500, 2000, 2200]


def time_stamp_10():
    return int(time.time())


def update_time(match):
    return f"{match.group()[:-10]}{time_stamp_10()}"


def update_time_last(match):
    return f"{match.group()[:-10]}{time_stamp_10() + time_lst[random.randint(0, 3)]}"


class HttpMethod:
    def __init__(self, base_url: str, user_name: str, user_pwd: str, url_data: str = None, save_path: str = None):
        """
        @param base_url: 图床根路径
        @param url_data: 需要上传的文件
        @param save_path: 保存的路径, 默认保存到 "gitbook_search"
        """
        self.base_url = base_url
        self.save_path = save_path or "gitbook_search"

        self.user_name = user_name
        self.user_pwd = user_pwd

        self.referer = f'{self.base_url}/url.php'
        self.url_data = url_data or "https://raw.githubusercontent.com/hycBook/hycBlog/gh-pages/search.txt"
        self.post_data = {"urlData": self.url_data, 'savePath': self.save_path}

        self.up_base_url = f'{self.base_url}/url-up-savename.php'
        _, file_name = os.path.split(self.url_data)
        self.delete_url = f"{base_url}/fileNameModeManager.php?p={self.save_path}&del={file_name}"
        self.del_referer = f'{base_url}/fileNameModeManager.php?p={self.save_path}'

        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"

    def get_cookie(self):
        login_url = f"{self.base_url}/fileNameModeManager.php"
        login_form_data = {"fm_usr": self.user_name, "fm_pwd": self.user_pwd}
        login_form_data_final = urllib.parse.urlencode(login_form_data)
        headers = {
            "referer": f"{self.base_url}/fileNameModeManager.php",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"self.base_url",
            "Users-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
        # 1.3 发送登录请求POST，
        # 自动保存cookie
        cook_jar = cookiejar.MozillaCookieJar()
        # 定义有添加 cookie功能的处理器
        cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)
        # 根据处理器生成opener
        opener = urllib.request.build_opener(cook_handler)
        # add = urllib.request.Request(url=login_url, headers=headers, method='POST')
        # 此时headers里面还没有cookie，还没有登录
        login_request = urllib.request.Request(login_url, headers=headers, data=login_form_data_final.encode("utf-8"))
        # 如果登录成功。cookjar自动保存cookie，opener里面有cookjar，所以opener里有cookie
        # 下面一步不需要返回数据，只要成功登陆就行
        resp = opener.open(login_request)
        return cook_jar

    def delete_file(self, timeout: float = 100):
        cook_jar = self.get_cookie()
        # 创建管理器
        cookie_handler = urllib.request.HTTPCookieProcessor(cook_jar)
        http_handler = urllib.request.HTTPHandler()
        https_handler = urllib.request.HTTPSHandler()
        opener = urllib.request.build_opener(cookie_handler, http_handler, https_handler)
        inner_head = {'user-agent': self.ua, 'Referer': self.del_referer}
        req = urllib.request.Request(url=self.delete_url, headers=inner_head, method='GET')
        # response = urllib.request.urlopen(url=add, timeout=timeout)
        response = opener.open(req, timeout=timeout)

    def upload_file(self, timeout: float = 100):
        data = urllib.parse.urlencode(self.post_data)
        data = data.encode('ascii')
        inner_head = {'user-agent': self.ua, 'Referer': self.referer, 'cookie': 'name-mode=_isSavenameMode'}
        add = urllib.request.Request(url=self.up_base_url, headers=inner_head, method='POST')
        response = urllib.request.urlopen(url=add, timeout=timeout, data=data)
        return response.read().decode('utf-8')


def start_run(base_url: str, user_name: str, user_pwd: str, url_data: str or None, save_path: str):
    # new_ck = re.sub('Hm_lvt_.*?=(\d{10})', update_time, cookie)
    # cookie = re.sub('Hm_lpvt_.*?=(\d{10})', update_time_last, new_ck)
    pic_server = HttpMethod(base_url=base_url, user_name=user_name, user_pwd=user_pwd, url_data=url_data,
                            save_path=save_path)
    pic_server.delete_file()
    res = pic_server.upload_file()
    _, new_file_name = os.path.split(res)
    print(f"上传成功: {save_path}\{new_file_name}")


if __name__ == '__main__':
    p_base_url, p_url_data, p_user_name, p_user_pwd = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    p_save_path = "gitbook_search"
    start_run(base_url=p_base_url, user_name=p_user_name, user_pwd=p_user_pwd, url_data=p_url_data,
              save_path=p_save_path)
    print("上传结束")
