# -*- coding: utf-8 -*-
###############################################################
# Author:  karlzpsong
# Date:    2023-06-13
# Contact: https://github.com/KARLSZP/Chevereto-Uploader
###############################################################

import json
import mimetypes
import os
import sys
from functools import partial

import requests
import yaml

CONFIG_FILE = 'config.yml'


class ChevertoUploader(object):
    def __init__(self, initialize=False) -> None:
        self.REQUEST_URL = None
        self.uploader = None

        if initialize:
            self.init_config_file()
        self.build_url()
        self.set_uploader_params()

    def check_if_conf_exist(self):
        if not os.path.exists(CONFIG_FILE):
            raise ValueError('No config file found. Please run `python upload.py init` first.')

    def build_url(self):
        self.check_if_conf_exist()
        KEY, BASE_URL = self.load_cfg()
        self.REQUEST_URL = "{}/api/1/upload/?key={}&format=json".format(BASE_URL, KEY)

    def set_uploader_params(self):
        proxies = {'http': None, 'https': None}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                    (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
        self.uploader = partial(requests.post, url=self.REQUEST_URL, proxies=proxies, headers=headers)

    def upload(self, img_list):
        for img in img_list:
            try:
                resp = self.uploader(files=self.build_file(img))
                json_cnt = json.loads(resp.text)
                print(json_cnt["image"]["url"])
            except all:
                print('Error: Network Issue.')

    @staticmethod
    def init_config_file():
        BASE_URL = input("Enter the url of cheverto: ")
        if not BASE_URL.startswith('https') or not BASE_URL.startswith('http'):
            raise ValueError("Please enter full url. E.g.: https://example.com")
        KEY = input(f"Enter the API key (https://{BASE_URL}/dashboard/settings/api): ")

        with open(CONFIG_FILE, 'w') as f:
            yaml.safe_dump({'USER_CFG': {'KEY': KEY, 'BASE_URL': BASE_URL}}, f)
        print("Initialized.")
        exit()

    @staticmethod
    def load_cfg():
        with open(CONFIG_FILE, "r") as f:
            cfg = yaml.safe_load(f)
        return cfg['USER_CFG']['KEY'], cfg['USER_CFG']['BASE_URL']

    @staticmethod
    def build_file(filename):
        mime_type = mimetypes.guess_type(filename)[0]
        return [('source', (filename, open(filename, 'rb'), mime_type))]


if __name__ == '__main__':
    uploader = ChevertoUploader(initialize=(sys.argv[1] == 'init'))

    img_list = sys.argv[1:]
    uploader.upload(img_list)
