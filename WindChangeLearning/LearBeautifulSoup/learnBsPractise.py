import requests
from bs4 import BeautifulSoup


#练习一，提取豆瓣电影的序号、电影名称、评分、推荐语和链接(方法一，提取共同的父标签)
list_all=[]
for i in range(1,11):
    print('i=%d'%i)
    link_number=str((i-1)*25)
    res_movie=requests.get('https://movie.douban.com/top250?start='+link_number+'&filter=')
    bs_movie=BeautifulSoup(res_movie.text,'html.parser')
    list_movie=bs_movie.find('ol',class_='grid_view').find_all('li')
    list_page=[]
    for movie in list_movie:
        movie_ranking=movie.find('div',class_='pic').find('em').text
        movie_name=movie.find('div',class_='pic').find('a').find('img')['alt']
        movie_score=movie.find('span',class_='rating_num').text
        try:
            movie_comment=movie.find('p',class_='quote').text
        except AttributeError:
            movie_comment=''
        movie_link=movie.find('div',class_='pic').find('a')['href']
        list_page.append([movie_ranking,movie_name,movie_score,movie_comment,movie_link])        
    #print(list_page)
    list_all=list_all+list_page
print(list_all)

#练习一，提取豆瓣电影的序号、电影名称、评分、推荐语和链接(方法二，提取所有的子标签)
list_all=[]
for i in range(1,11):
    print('i=%d'%i)
    list_page=[]
    link_number=str((i-1)*25)
    res_movie=requests.get('https://movie.douban.com/top250?start='+link_number+'&filter=')
    bs_movie=BeautifulSoup(res_movie.text,'html.parser')
    tag_head=bs_movie.find_all('div',class_='pic')
    tag_score=bs_movie.find_all('span',class_='rating_num')
    if i!=6:
        tag_comment=bs_movie.find_all('span',class_='inq')
    else:
        tag_comment=bs_movie.find_all('span',class_='inq') #第135名的<我不是药神>没有推荐语,需单独处理
        tag_comment.insert(9,tag_comment[9]) #第135名的<我不是药神>没有推荐语,需单独处理       
    for x in range(len(tag_head)):
        print('x=%d'%x)
        list_movie=[tag_head[x].find('em').text,tag_head[x].find('a').find('img')['alt'],tag_score[x].text,tag_comment[x].text,tag_head[x].find('a')['href']]
        list_page.append(list_movie)
    list_all=list_all+list_page
list_all[134][3]='' #第135名的<我不是药神>没有推荐语,需单独处理
print(list_all)

#练习二，提取电影天堂的下载链接
from urllib.parse import quote
movie_name=input('请输入你要看的电影名称：')
movie_nameURL=quote(movie_name.encode('gbk'))
movie_URL='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+movie_nameURL
print(movie_URL)
res=requests.get(movie_URL)
bs=BeautifulSoup(res.text,'html.parser')
try:
    movie_link='https://www.ygdy8.com'+bs.find('div',class_='co_content8').find('td',width='55%').find('a')['href']
    print('《'+movie_name+'》电影的主页面为:    '+movie_link)
    res_movie=requests.get(movie_link)
    res_movie.encoding='gb2312'
    bs_movie=BeautifulSoup(res_movie.text,'html.parser')
    download_link=bs_movie.find('td',style='WORD-WRAP: break-word').text
    print('《'+movie_name+'》电影的下载链接为:    '+download_link+'\n备注:请复制以上地址并使用迅雷或磁力链下载')
except AttributeError:
    print('找不到《'+movie_name+'》电影的主页面，请换一个关键词再试试')
