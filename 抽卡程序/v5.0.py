import random

# 定义角色和武器的名称
CHARACTER = ['旅行者', '迪卢克', '钟离']
WEAPON = ['天空之刃', '苍古自由之誓', '雾切之笛']

# 定义抽卡结果
DRAW_RESULT = {
    0: 'NONE',
    1: 'CHARACTER',
    2: 'WEAPON',
    3: 'DUPLICATE'
}


# 产生随机数
def randnum():
    return random.randint(1, 100)


# 判断是否保底
def is_bonus(count):
    return count >= 60


# 抽卡
def draw():
    count = 0
    while True:
        num = randnum()
        count += 1

        if num <= 50:
            # 抽到角色
            return DRAW_RESULT[1]
        elif num <= 70:
            # 抽到武器
            return DRAW_RESULT[2]
        elif num <= 80:
            # 重复物品
            return DRAW_RESULT[3]
        else:
            # 未抽到物品
            return DRAW_RESULT[0]


# 输出抽卡结果
def print_result(result):
    if result == DRAW_RESULT[1]:
        print('抽到了一个角色：', random.choice(CHARACTER))
    elif result == DRAW_RESULT[2]:
        print('抽到了一个武器：', random.choice(WEAPON))
    elif result == DRAW_RESULT[3]:
        print('抽到了一个重复的物品。')
    else:
        print('没有抽到任何物品。')


# 抽卡主函数
def main():
    count = 0

    while True:
        print('第', count, '次抽卡：')
        result = draw()
        print_result(result)
        count += 1

        if result == DRAW_RESULT[0]:
            break

    print('总共抽卡：', count, '次，平均抽卡次数：', count / 100)


if __name__ == '__main__':
    main()
