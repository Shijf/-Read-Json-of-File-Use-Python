#!/bin/env python
#-*- encoding=utf8 -*-

# Author:Shijf
# Email：shijf_private@163.com
# Github: github.com/Shijf

import json
import os,sys
def resolveJson(path):
    '''
    读取json文件
    '''
    file = open(path)
    fileJson = json.load(file)
    return fileJson

def output():
    '''
    输出指定路径的json数据
    '''
    result = resolveJson(path)
    # print(result)
    for index, x in enumerate(result):
        '''
        以下输出格式,可自定义
        '''
        print('第' + str(index) + "组数据:")
        print ("---start----")
        print( "PM1.0:"  +  str(x.get('pm10')))
        print(  "PM2.5:" +  str(x.get('pm25')))
        print(  "time:"  +  str(x.get('time')) )
        print ("---end----")

# path 请换成实际 json 文件的路径例如 path = r"G:\demo\data.json" 
# 记得加 r
# 以下只是演示路径 

path = os.getcwd() + "\data.json" # 实际地址:G:\demo\data.json 

# 输出
output()           
