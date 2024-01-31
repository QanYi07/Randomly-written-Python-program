ver = 1
while ver == 1:
    import random

# 设定概率
    five_star_rate: float = 0.006  # 5星角色的概率
    four_star_rate: float = 0.051  # 4星角色的概率
    guaranteed_five_star: int = 90  # 保底90抽获得5星
    guaranteed_four_star: int = 10  # 保底10抽获得4星

# 设定奖池
    five_star_characters = ["1"]
    four_star_characters = ["A", "B", "C"]
    three_star_weapons = ["a", "b", "c", "d"]

# 抽卡计数器
    already_drawn = []  # 已经抽到的角色或武器
    counter_five_star = 0
    counter_four_star = 0

    try:
        with open("计数器(勿删)", "r") as f:
            lines = f.readlines()
        if len(lines) == 2:
            counter_five_star = int(lines[0])
            counter_four_star = int(lines[1])
    except FileNotFoundError:
        pass  # 如果文件不存在，则忽略错误


    def draw_one():
        global counter_five_star, counter_four_star, already_drawn
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
            while True:
                choice = random.choice(five_star_characters)
                if choice not in already_drawn:
                    already_drawn.append(choice)
                    return choice, 5
        elif draw_chance < five_star_rate + four_star_rate:
            counter_four_star = 0
            while True:
                choice = random.choice(four_star_characters)
                if choice not in already_drawn:
                    already_drawn.append(choice)
                    return choice, 4
        else:
            return random.choice(three_star_weapons), 3


    def draw_ten():
        results = []
        for _ in range(10):
            results.append(draw_one())
        return results


    draw = input("是否十连抽?(yes/no):")

    if draw == "no":
        print("单抽结果：", draw_one())  # 抽一次
    else:
        print("十连抽结果：")  # 抽十次
        for result in draw_ten():
            print(f"获得{result[1]}星：{result[0]}")

    with open("计数器(勿删).txt", "w") as f:
        f.write(str(counter_five_star) + "\n")
        f.write(str(counter_four_star) + "\n")  # 将计数器写入文件
