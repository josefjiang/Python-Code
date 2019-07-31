import requests #调用requests库
from bs4 import BeautifulSoup #调用BS4库
import re

remove_symbol=re.compile(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\t|\r')#导入清除特殊字符
#课堂练习
url='https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res = requests.get(url) #获取网页源代码，得到的res是response对象          #print(res.status_code)，检查请求是否正确响应
html = res.text #把res的内容以字符串的形式返回                            #print(html)#打印html，检查html内容是否成功获取
soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象  #print(type(soup))查看soup类型，print(soup)查看soup内容
items = soup.find_all(class_='books') #通过标签匹配我们需要的数据         #print(type(items))查看items类型，print(items)查看items内容
for item in items:                    #遍历items内的Tag对象              #print(item)  查看item类型，print(item)查看item内容
    kind = item.find('h2')            # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='title') #  在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info')  # 在列表中的每个元素里，匹配属性class_='info'提取出数据
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)
    print()
#练习一，提取网页里的评论数据
url='https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
res=requests.get(url)
html=res.text
soup=BeautifulSoup(html,'html.parser')
items=soup.find_all(class_='comment-content')
#清除文件内容
with open(r'WindChangeLearning\LearBeautifulSoup\comment.txt','w',encoding='utf-8') as f:
    f.write('')
i=0
for item in items:  #遍历找到的评论数据，并把每个数据按行写入txt文件    
    #保存所有数据到txt文件
    with open(r'WindChangeLearning\LearBeautifulSoup\comment.txt','a+',encoding='utf-8') as f:
        f.writelines(remove_symbol.sub('',item.text))
    #打印前10个数据
    if i<10:
        print(remove_symbol.sub('',item.text))
        i+=1

#练习二，提取网页左侧的栏目
url='http://books.toscrape.com/'
res=requests.get(url)
html=res.text
soup=BeautifulSoup(html,'html.parser')
nav=soup.find(class_='nav nav-list')
items=nav.find_all('li')
for item in items:
    element=item.find('a')    
    print(element.text.strip())#element.text.strip() #remove_symbol.sub('',element.text) #去除字符串首位空白的方法

#练习三，提取网页中的书名和评分
keyword=re.compile('.*star-rating.*')
url='http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res=requests.get(url)
print(res.status_code)
html=res.text
soup=BeautifulSoup(html,'html.parser')
books=soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    book_name=book.find('h3').find('a')    
    book_star=book.find('p')['class']
    book_price=book.find(class_='product_price').find(class_='price_color')   
    print(book_name['title'],'\n',book_star[0],book_star[1],'\n',book_price.text[1:],'\n')    

#练习四
url='https://spidermen.cn/'
res=requests.get(url)
html=res.text
soup=BeautifulSoup(html,'html.parser')
items=soup.find_all('article')
for item in items:
    article_name=item.find('h2').find('a')
    article_time=item.find(class_='entry-meta').find('a').find('time')
    article_link=item.find(class_='entry-meta').find('a')
    print(article_name.text,article_time.text,article_link['href'])