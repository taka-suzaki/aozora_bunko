from bs4 import BeautifulSoup
import urllib.request as req

#1---No入力
num = 879
#芥川竜之介
#2---URL指定
url = "http://www.aozora.gr.jp/index_pages/person"+str(num)+".html"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
#4---抽出
li_list = soup.select("ol>li")
print(len(li_list), li_list[0])