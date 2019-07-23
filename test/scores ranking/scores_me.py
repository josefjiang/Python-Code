#按行读出scores文件里的数据，每行数据变为数组里的一个元素
file1 = open(r'D:\Python Code\test\scores ranking\scores.txt','r',encoding='gbk')
file_lines = file1.readlines()
file1.close()
#初始化
final_scores=[]
list_scores=[]
list_temp=[]
#分解每行字符串里的数据，并把每行数据生成一个列表，把除名字外的分数相加生成新的列表
for i in file_lines:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
    list_temp.append(data[0])
    list_temp.append(sum)
    list_scores.append(list_temp)
    list_temp=[]
#对上述步骤中生成的列表进行冒泡排序 
for i in range(len(list_scores)-1):
    for j in range(len(list_scores)-1-i):
        if list_scores[j][1]<list_scores[j+1][1]:
            list_scores[j],list_scores[j+1]=list_scores[j+1],list_scores[j]       
#对排序后生成的列表每个元素的列表进行合并，子列表变成字符串        
for i in list_scores:
    i[1]=str(i[1])
    j=''.join(i)+'\n'
    final_scores.append(j)
#把排序好的列表写进txt文件中
winner=open(r'D:\Python Code\test\scores ranking\winner.txt','w',encoding='utf-8')
winner.writelines(final_scores)
winner.close()