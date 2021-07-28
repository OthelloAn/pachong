import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

'''
抓取知乎发现页信息
'''
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('ExploreRoundtableCard-questionTitle.*?question.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,r.text)
# print(titles)

'''
抓取二进制数据，GitHub站点图标
'''
r = requests.get('https://github.com/favicon.ico',headers=headers,verify=False)
print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)