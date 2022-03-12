
from email import contentmanager
from flask import request
import requests
import os
import sys
import douban_crawler

now_path = os.getcwd()
add_path = now_path + r"/../conf/"
sys.path.append(add_path)

import yaml_reader
import data_parser

# 采用策略设计模式，对在配置中开关开启的url进行分发解析
class UrlHandleManager:
  def __init__(self):
    data = yaml_reader.ReadYaml(add_path + 'tag_recommend_system.yaml')
    self.config = data_parser.DataParser(data)
    print('UrlHandleManager init complete!')
    
  # 对已在配置中注册的网站进行遍历
  def Handle(self):
    for web_config in self.config.website:
      if(web_config['switch'] == 1):
        self.Dispatch(web_config)
      
  # 对需要爬取网站content进行分发解析
  def Dispatch(self, web_config):
    if(web_config['name'] == 'douban'):
      movie_list =  douban_crawler.CrawlDouban(web_config)
    elif(web_config['name'] == 'zhihu'):
      pass