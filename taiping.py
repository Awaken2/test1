from bs4 import BeautifulSoup
# from urllib import  parse
import requests
response = requests.get("http://life.cntaiping.com/info-bxcp/")
response.encoding = response.apparent_encoding #中文乱码转换
html = response.text
soup = BeautifulSoup(html,"html.parser")
all_lian = soup.findAll("a",attrs={"target":"_blank"})
all_name = soup.find("td")
for price in all_lian:
    price = "http://life.cntaiping.com"+price.get('href')#添加http进链接,去掉标签只获取标签内的内容
    if "条款PDF文档" in price :
        print(all_name,price)
