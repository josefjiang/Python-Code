import requests 
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
print(type(res))#输出结果为<class 'requests.models.Response'>

#学习第一个属性response.status_code
import requests 
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') 
print(res.status_code)#输出结果为200，这个数字代表服务器同意了请求，并返回了数据给我们

#学习第二个属性response.content
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') #发出请求，并把返回的结果放在变量res中
pic=res.content #把Reponse对象的内容以二进制数据的形式返回
photo = open(r'WindChangeLearning\LearnRequests\ppt.jpg','wb')
#新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
#图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo.write(pic) #获取pic的二进制内容
photo.close() #关闭文件

#学习第三个属性response.text
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md') #下载《三国演义》第一回，我们得到一个对象，它被命名为res
novel=res.text#把Response对象的内容以字符串的形式返回
print(novel[:100])#现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
with open(r'WindChangeLearning\LearnRequests\《三国演义》.txt','w',encoding='utf-8') as k: #如果'w'更换为'a+'，则表示指针放在文件末尾，追加内容
    k.write(novel)

#学习第四个属性response.encoding
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
print(res.encoding)#输出结果为utf-8，代表网页上的内容是以utf-8的模式编码的
res.encoding='gbk'#此处为改变下载下来的内容的编码模式为gbk
novel=res.text#把Response对象的内容以字符串的形式返回
print(novel[:100])#可以看到输出内容为乱码

#练习一，获取文章
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
article=res.text
with open(r'WindChangeLearning\LearnRequests\Article.txt','w',encoding='utf-8') as f:
    f.write(article)

#练习二，获取图片
res=requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
spider_web=res.content
with open(r'WindChangeLearning\LearnRequests\Spider_web.jpg','wb') as f:
    f.write(spider_web)

#练习三，获取音乐文件
res=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
music=res.content
with open(r'WindChangeLearning\LearnRequests\Rainbow.mp3','wb') as f:
    f.write(music)