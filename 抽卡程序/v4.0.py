import random

# 定义抽卡物品和概率
weapon_probability = 0.3  # 武器抽卡概率为30%
character_probability = 0.5  # 角色抽卡概率为50%

# 定义抽卡次数和保底机制
draw_times = 10  # 每次抽卡最多抽取10次
bonus_times = 5  # 连续抽取5次未获得稀有物品赠送
bonus_item = '武器'  # 赠送的稀有物品为武器

# 初始化抽卡次数和已获得的稀有物品
draw_count = 0
bonus_count = 0
has_bonus = False

# 模拟抽卡过程
for i in range(draw_times):
    # 生成随机数
    random_num = random.random()
    
    # 判断是否抽到物品
    if random_num <= weapon_probability:
        print('抽到了武器！')
        draw_count += 1
    elif random_num <= character_probability:
        print('抽到了角色！')
        draw_count += 1
    else:
        print('没有抽到任何物品。')
        
    # 判断是否达到保底机制
    if not has_bonus and draw_count >= bonus_times:
        print(f'恭喜您，连续抽取{bonus_times}次未获得{bonus_item}，赠送您一个{bonus_item}！')
        has_bonus = True
        bonus_count += 1

# 输出抽卡结果
print(f'本次抽卡共抽取了{draw_count}次，其中赠送了{bonus_count}个{bonus_item}。')