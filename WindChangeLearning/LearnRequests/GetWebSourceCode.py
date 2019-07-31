import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
source_code=res.text
print(res.encoding)
with open(r'WindChangeLearning\LearnRequests\source code.txt','w',encoding='utf-8') as f:
    f.write(source_code)