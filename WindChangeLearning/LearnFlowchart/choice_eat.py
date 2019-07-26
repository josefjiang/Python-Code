import random,time
list_snack=['桂林米粉','云南过桥米线','杭州小笼包','天津狗不理包子','柳州螺蛳粉','长沙臭豆腐','新疆羊肉串','南昌米粉','山东煎饼','成都担担面']
list_chinesefood=['小炒牛肉','红烧肉','糖醋排骨','清蒸武昌鱼','北京烤鸭','西红柿炒鸡蛋','蒜香排骨','鱼香茄子','土豆炖牛肉','新疆大盘鸡']
list_westernfood=['法式羊排','土豆泥','米饭披萨','无花果萨拉米沙拉','炸鸡三明治','炸薯条','洋葱烧猪扒','鸡肉起司卷','培根芝士意面','牛肉汉堡']
list_all=list_snack+list_chinesefood+list_westernfood
    
print('今天想吃什么？')
while True:
    recommend_choice=input('是否需要随机推荐？需要推荐请输入y，不需要时请随意输入：')
    if recommend_choice=='y':
        result=''.join(random.choice(list_all))
        print('给你推荐%s'%result)
        time.sleep(1)
        agree_recommend=input('对系统推荐的菜系是否满意？满意请输入y,不满意时请随意输入：')
        if agree_recommend=='y':
            break
        else:
            continue
    else:
        print("系统推荐有三个类别可选，你想吃'小吃'、'中餐'还是'西餐'?")
        time.sleep(1)
        food_type=input('请输入以上三个类别中的一个，不带标点符号：')
        if food_type=='小吃':
            result=random.choice(list_snack)
            print('给你推荐%s'%result)
            time.sleep(1)
            agree_recommend=input('对系统推荐的菜系是否满意？满意请输入y,不满意时请随意输入：')
            if agree_recommend=='y':
                break
            else:
                continue
        elif food_type=='中餐':
            result=random.choice(list_chinesefood)
            print('给你推荐%s'%result)
            time.sleep(1)
            agree_recommend=input('对系统推荐的菜系是否满意？满意请输入y,不满意时请随意输入：')
            if agree_recommend=='y':
                break
            else:
                continue
        elif food_type=='西餐':
            result=random.choice(list_westernfood)
            print('给你推荐%s'%result)
            time.sleep(1)
            agree_recommend=input('对系统推荐的菜系是否满意？满意请输入y,不满意时请随意输入：')
            if agree_recommend=='y':
                break
            else:
                continue
        else:
            continue

print('程序结果，感谢使用')