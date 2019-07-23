import csv
#读取原始CSV文件
with open(r'D:\Python Code\WindChangeLearning\LearnCSVMoudule\test1.csv', newline = '', encoding = 'gbk')  as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
    print('数据读取完毕')
#复制并粘贴新的CSV文件
import shutil
shutil.copyfile(r'D:\Python Code\WindChangeLearning\LearnCSVMoudule\test1.csv', r'D:\Python Code\WindChangeLearning\LearnCSVMoudule\test1_1.csv')
#修改新的CSV文件
with open(r'D:\Python Code\WindChangeLearning\LearnCSVMoudule\test1_1.csv','a', newline='',encoding='gbk') as f:
    writer  = csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])
#读取修改后新的CSV文件
with open(r'D:\Python Code\WindChangeLearning\LearnCSVMoudule\test1_1.csv','r', newline='',encoding='gbk') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)
    print('数据改动完毕')