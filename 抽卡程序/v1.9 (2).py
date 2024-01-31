ver = 1
while ver == 1:
    import random

    # 设定概率
    six_star_rate: float = 0.001  # 6星角色的概率
    five_star_rate: float = 0.006  # 5星角色的概率
    four_star_rate: float = 0.051  # 4星角色的概率
    guaranteed_six_star: int = 180
    guaranteed_five_star: int = 90  # 保底90抽获得5星
    guaranteed_four_star: int = 10  # 保底10抽获得4星

    # 设定奖池
    six_star_characters = ["灰太狼-SXD"]
    five_star_characters = ["李品傲"]
    four_star_characters = ["沈镇南", "王锐", "黄瑞", "马超跃", "袁凤琦", "赵晓羽", "付杰", "胡淼", "胡峻豪", "罗艳",
                            "汪晓曼"]
    three_star_weapons = ["许家乐", "王方欣", "丁瑞鑫", "刘杨", "刘一君", "陈方婷", "王恩琦", "金生城", "胡志运",
                          "马超",
                          "路畅", "吴诗诺", "李耀", "张紫轩", "胡宇", "赵孝坤", "胡深", "刘花", "邓茂森", "张嘉鑫",
                          "雷鑫怡", "王帅", "刘灿", "张奇", "王郁涛", "唐靓星", "熊晓枫", "冯羽阳", "许振宇", "姜树柏",
                          "耿良冬", "史玉卓", "王祥旭", "戚怡曦", "钟家丽", "顾李研", "胡涛涛", "周亮", "王欣宇",
                          "罗越越",
                          "钱凯旋", "刘子恒"]

    # 抽卡计数器
    already_drawn = []  # 已经抽到的角色
    counter_six_star = 0
    counter_five_star = 0
    counter_four_star = 0

    try:
        with open("计数器(勿删)", "r") as f:
            lines = f.readlines()
        if len(lines) == 2:
            counter_six_star = int(lines[0])
            counter_five_star = int(lines[1])
            counter_four_star = int(lines[2])
    except FileNotFoundError:
        pass  # 如果文件不存在，则忽略错误


    def draw_one():
        global counter_six_star, counter_five_star, counter_four_star, already_drawn
        counter_six_star += 1
        counter_five_star += 1
        counter_four_star += 1

        # 检查保底
        if counter_six_star >= guaranteed_six_star:
            counter_six_star = 0
            return random.choice(six_star_characters), 6
        if counter_five_star >= guaranteed_five_star:
            counter_five_star = 0
            return random.choice(five_star_characters), 5
        if counter_four_star >= guaranteed_four_star:
            counter_four_star = 0
            return random.choice(four_star_characters), 4

        # 正常抽卡
        draw_chance = random.random()
        if draw_chance < six_star_rate:
            counter_six_star = 0
            while True:
                choice = random.choice(six_star_characters)
                if choice not in already_drawn:
                    already_drawn.append(choice)
                    return choice, 6
        elif draw_chance < six_star_rate + five_star_rate:
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
        f.write(str(counter_six_star) + "\n")
        f.write(str(counter_five_star) + "\n")
        f.write(str(counter_four_star) + "\n")  # 将计数器写入文件
