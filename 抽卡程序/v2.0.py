import random


def draw_card(n):
    cards = ["Card1", "Card2", "Card3", "Card4", "Card5"]  # 替换为你的卡池内容
    results = []
    for i in range(n):
        card = random.choice(cards)
        results.append(card)
    return results


def main():
    num_draws = int(input("请输入要抽卡的次数："))
    draws = draw_card(num_draws)
    print("抽卡结果：", draws)


if __name__ == "__main__":
    main()
