# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:05:42 2018

@author: lenovo
"""

import urllib.request as r
import time
a=open('state.txt','r').readline()
if a=='1':
    print("欢迎使用全球天气APP")
else:
    print("欢迎第一次使用全球天气APP")
    input("请登记你的名称:")
    open('state.txt','w').write('1')
time.sleep(1)
city_pinyin=input("请输入城市拼音:")
address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
import json
data=json.loads(info)
#print(data)
print("1.查看当前城市天气,2.查看其它城市天气，3.保存当前城市")
time.sleep(1)
menno=input("请输入菜单：")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
    time.sleep(1)
    city_pinyin=input("请输入城市拼音:")
    address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
    info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    import json
    data=json.loads(info)   
if menno=="3":
    print("3.保存当前城市")   
days=[0,9,17,25,33]
def prinywea(data,day):
    tm=data["list"][day]["dt_txt"]
    temp=data["list"][day]["main"]["temp"]
    temp_max=data["list"][day]["main"]["temp_max"]
    pressure=data["list"][day]["main"]["pressure"]
    description=data["list"][day]["weather"][0]["description"]
    print("日期："+str(tm)+"\n"+"天气温度："+str(temp)+"\n"+"最大温度:"+str(temp_max)+"\n"+"气压:"+str(pressure)+"\n"+"天气情况:"+str(description))
for day in days:
    prinywea(data,day)
    time.sleep(2)
