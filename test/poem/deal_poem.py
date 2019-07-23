with open('test\poem\poem1.txt','r',encoding='gbk') as f:
    lines=f.readlines()
print(lines)

newlines=[]
with open(r'test\poem\test.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in ['一弦一柱思华年。\n','蓝田日暖玉生烟。\n']:
            line='______________\n'
        newlines.append(line)
    new.writelines(newlines)
print(newlines)