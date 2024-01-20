# 类似原神,但是不具备计数器存储功能（就是程序每次运行计数器都是以0开始）
import random

# 设定概率
five_star_rate = 0.006  # 5星角色的概率
four_star_rate = 0.051  # 4星角色的概率
guaranteed_five_star = 90  # 保底90抽获得5星
guaranteed_four_star = 10  # 保底10抽获得4星

# 设定奖池
five_star_characters = ["角色A", "角色B", "角色C"]
four_star_characters = ["角色D", "角色E", "角色F"]
three_star_weapons = ["武器A", "武器B", "武器C"]

# 抽卡计数器
counter_five_star = 0
counter_four_star = 0

def draw_one():
    global counter_five_star, counter_four_star
    counter_five_star += 1
    counter_four_star += 1
    
    # 检查保底
    if counter_five_star >= guaranteed_five_star:
        counter_five_star = 0
        return random.choice(five_star_characters), 5
    if counter_four_star >= guaranteed_four_star:
        counter_four_star = 0
        return random.choice(four_star_characters), 4
    
    # 正常抽卡
    draw_chance = random.random()
    if draw_chance < five_star_rate:
        counter_five_star = 0
        return random.choice(five_star_characters), 5
    elif draw_chance < five_star_rate + four_star_rate:
        counter_four_star = 0
        return random.choice(four_star_characters), 4
    else:
        return random.choice(three_star_weapons), 3

def draw_ten():
    results = []
    for _ in range(10):
        results.append(draw_one())
    return results

# 抽一次
print("单抽结果：", draw_one())

# 抽十次
print("十连抽结果：")
for result in draw_ten():
    print(f"获得{result[1]}星：{result[0]}")
