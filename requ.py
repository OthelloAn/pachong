import requests

# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

'''
GET请求
'''
# r = requests.get('http://httpbin.org/get')
# print(r.text)

data = {
    'name': 'axt',
    'age':'26'
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)

