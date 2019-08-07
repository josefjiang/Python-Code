import requests
'''
#json模块的简单示例
import json # 引入json模块
a = [1,2,3,4] # 创建一个列表a。
b = json.dumps(a) # 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
print(b) # 打印b。
print(type(b)) # 打印b的数据类型。

c = json.loads(b) # 使用loads()函数，将json格式的字符串b转为列表，赋值给c。
print(c) # 打印c。
print(type(c))  # 打印c的数据类型。

#爬取周杰伦歌曲列表，包含歌曲名、专辑名、播放时长和播放链接
#data-song-list-0-name
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 调用get方法，下载这个字典
json_music = res_music.json() # 使用json()方法，将response对象，转为列表/字典
list_music = json_music['data']['song']['list'] # 一层一层地取字典，获取歌单列表
for music in list_music: # list_music是一个列表，music是它里面的元素
    print(music['name']) # 以name为键，查找歌曲名    
    print('所属专辑：'+music['album']['name'])# 查找专辑名    
    print('播放时长：'+str(music['interval'])+'秒')# 查找播放时长    
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')# 查找播放链接

#爬去周杰伦歌曲七里香的热门评论
for i in range(5):
    res_comments = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(i)+'&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010')
    # 调用get方法，下载评论列表
    json_comments = res_comments.json() # 使用json()方法，将response对象，转为列表/字典
    list_comments = json_comments['comment']['commentlist'] # 一层一层地取字典，获取评论列表
    for comment in list_comments: # list_comments是一个列表，comment是它里面的元素
        print(comment['rootcommentcontent']) # 输出评论    
        print('-----------------------------------') # 将不同的评论分隔开来    
print(5*'\n')#for i in range(5):print()

#爬去周杰伦歌曲七里香的热门评论，使用requests.get()方法中的URL方法的参数params
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg' # 请求歌曲评论的url参数前面的部分
for i in range(5):   # 将参数封装为字典
    params = {
    'g_tk':'5381',
    'loginUin':'0', 
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'GB2312',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'cid':'205360772',
    'reqtype':'2',
    'biztype':'1',
    'topid':'102065756',
    'cmd':'6',
    'needmusiccrit':'0',
    'pagenum':str(i),
    'pagesize':'15',
    'lasthotcommentid':'song_102065756_3202544866_44059185',
    'domain':'qq.com',
    'ct':'24',
    'cv':'10101010'   
    }   
    res_comments = requests.get(url,params=params) # 调用get方法，下载这个字典    
    json_comments = res_comments.json()
    list_comments = json_comments['comment']['commentlist']
    for comment in list_comments:
        print(comment['rootcommentcontent'])
        print('-----------------------------------')  

#爬取周杰伦的所有歌曲，下面代码举例只爬取5页内容
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5): # 将参数封装为字典
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'10',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }    
    res_music = requests.get(url,params=params) # 调用get方法，下载这个字典    
    json_music = res_music.json() # 使用json()方法，将response对象，转为列表/字典    
    list_music = json_music['data']['song']['list'] # 一层一层地取字典，获取歌单列表    
    for music in list_music: # list_music是一个列表，music是它里面的元素    
        print(music['name']) # 以name为键，查找歌曲名        
        print('所属专辑：'+music['album']['name']) # 查找专辑名        
        print('播放时长：'+str(music['interval'])+'秒') # 查找播放时长        
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n') # 查找播放链接
'''
#如果服务器拒绝访问，请添加headers参数，以上一个例子举例如下
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {                         # 伪装请求头
    'origin':'https://y.qq.com',    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示    
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html', # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示    
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }       
for x in range(5): # 将参数封装为字典
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'10',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }    
    res_music = requests.get(url,headers=headers,params=params) # 调用get方法，下载这个字典    
    json_music = res_music.json() # 使用json()方法，将response对象，转为列表/字典    
    list_music = json_music['data']['song']['list'] # 一层一层地取字典，获取歌单列表  
    i=1  
    for music in list_music: # list_music是一个列表，music是它里面的元素  
        print('page=%d,number=%d'%(x+1,i))  
        print(music['name']) # 以name为键，查找歌曲名        
        print('所属专辑：'+music['album']['name']) # 查找专辑名        
        print('播放时长：'+str(music['interval'])+'秒') # 查找播放时长        
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n') # 查找播放链接 
        i=i+1