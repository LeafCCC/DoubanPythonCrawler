#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/cinema/later/chengdu/"  # 需要爬取的网站
response = requests.get(url)  # 请求网站

soup = BeautifulSoup(response.content.decode("utf8"), "lxml")  # 用beautifulsoup解析网站

all_movies = soup.find('div', id="showing-soon")  # 找到所有电影所在块

file=open("filmdata2.html","w",encoding="utf8")
file.write("""
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>豆瓣电影即将上映影片信息</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<h2 class="text-center">豆瓣电影即将上映影片信息</h2>
<table class="table table-striped table-hover mx-auto text-center">
    <thead>
        <tr>
            <th>电影名</th>
            <th>上映日期</th>
            <th>类型</th>
            <th>地区</th>
            <th>关注的人数</th>
        </tr>
    </thead>
    <tbody>   
    """)     #写入标题

for movie in all_movies.find_all("div", class_="item"):  # 找到每一个电影，接下来在所在代码块中找到需要的信息并输出
    name = movie.find_all("a")[1].text  # 电影名
    href = movie.find_all("a")[0]["href"]  # 海报链接
    date = movie.find_all("li")[0].text  # 上映日期
    type = movie.find_all("li")[1].text  # 类型
    area = movie.find_all("li")[2].text  # 地区
    lovers = movie.find_all("li")[3].text.replace("想看","")   # 关注的人数
    print("电影名:{} 海报链接:{} 上映日期:{} 类型:{} 地区:{} 关注的人数:{}\n".format(name, href, date, type, area, lovers))  # 将结果测试输出
    file.write("""
        <tr>
            <td><a href={}>{}</a></td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    """.format(href,name,date,type,area,lovers)) #写入所需的信息

file.write("""
 </tbody>
</table>
</body>
</html>
""")
file.close()

print("file finished!")


