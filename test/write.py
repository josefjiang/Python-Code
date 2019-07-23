f1 = open('./test/1.txt','a',encoding='utf-8') 
#以追加的方式打开一个文件，尽管并不存在这个文件，但这行代码已经创建了一个txt文件了
f1.write('难念的经')
#写入'难念的经'的字符串
f1.close()           
#关闭文件 

f2 = open('./test/1.txt','r',encoding='utf-8')
#以读的方式打开这个文件
content = f2.read()
#把读取到的内容放在变量content里面
print(content)
#打印变量content
f2.close()
#关闭文件