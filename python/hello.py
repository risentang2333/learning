from urllib import request
from bs4 import BeautifulSoup
# 抓取地址
url = 'http://news.baidu.com/'
# 网页对象
htmlObject = request.urlopen(url)
# 解析对象
html = htmlObject.read()
# beautifulSoup格式化数据
soup = BeautifulSoup(html, 'html.parser')
# 筛出所有a标签
# div = soup.find_all(name='div',attrs={"class":"mod-tab-pane active"})
shenYangNews = soup.find(name='ul',attrs={"class":"ulist focuslistnews"})
a = shenYangNews.find_all('a')
for val in a:
    string = val.string
    href = val.get('href')
    print('标题：'+string)
    print('地址：'+href)
# ul = div.find_next('ul')

# for link in a:
#     # url = link.get('href')
#     string = link.string
#     print(string)
#     html = f.read()
#     soup = BeautifulSoup(html, 'html.parser')
#     arr = soup.find_all('a')
#     for link2 in arr:
#         print(link2.get('href'))
# print(arr)
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# f = request.urlopen(req)
# print('Status:', f.status, f.reason)
# for k, v in f.getheaders():
#     print('%s: %s' % (k, v))
# print('Data:', f.read().decode('utf-8'))