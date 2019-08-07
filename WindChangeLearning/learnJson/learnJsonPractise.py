import requests
from bs4 import BeautifulSoup
import re
def find_chinese(file):                       #定义筛选中文歌词的函数，函数的功能为去除所有非中文字符，每句中文之间保留一个逗号
    pattern = re.compile(r'[^\u4e00-\u9fa5]') #引入去除非中文的正则表达式
    chinese = re.sub(pattern, ' ', file)      #去除所有非中文并填补空格
    chinese='，'.join(chinese.split())        #把所有连续的空格替换为中文逗号
    return chinese

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers_music = {                         # 伪装请求头
    'origin':'https://y.qq.com',    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示    
    'referer':'https://y.qq.com/portal/search.html', # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示    
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', # 标记了请求从什么设备，什么浏览器上发出    
    }       
for x in range(5): # 将参数封装为字典
    params_music = {
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
    res_music = requests.get(url,headers=headers_music,params=params_music) # 调用get方法，下载这个字典    
    json_music = res_music.json() # 使用json()方法，将response对象，转为列表/字典    
    list_music = json_music['data']['song']['list'] # 一层一层地取字典，获取歌单列表    
    for music in list_music: # list_music是一个列表，music是它里面的元素    
        print(music['name']) # 以name为键，查找歌曲名        
        print('所属专辑：'+music['album']['name']) # 查找专辑名        
        print('播放时长：'+str(music['interval'])+'秒') # 查找播放时长              
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html') #查找播放链接
        song_url='https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
        res_song=requests.get(song_url)
        bs_song=BeautifulSoup(res_song.text,'html.parser')
        song_id=bs_song.find('a',class_='mod_btn js_more')['data-id']        
        song_lyric_url='https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        headers_song={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://y.qq.com',
            'Referer':'https://y.qq.com/n/yqq/song/'+music['mid']+'.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        params_song={
            'nobase64': '1',
            'musicid': song_id,
            '-': 'jsonp1',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0',
        }
        res_song_lyric=requests.get(song_lyric_url,headers=headers_song,params=params_song)
        json_song_lyric=res_song_lyric.json()
        song_lyric=json_song_lyric['lyric']
        print('歌词：'+find_chinese(song_lyric)+'\n\n')