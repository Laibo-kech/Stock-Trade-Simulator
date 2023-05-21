# Developer：shiwenxiang
# Time:2023/4/16 22:17
import random

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        change = random.uniform(-0.1, 0.1) * self.price
        self.price += change
        self.price = round(self.price, 2)

def main():
    print("欢迎来到模拟股票交易游戏！")

    stocks = [
        Stock("腾讯", 200.00),
        Stock("阿里巴巴", 150.00),
        Stock("百度", 120.00),
    ]

    player_balance = 10000

    while True:
        print(f"\n您当前的本金为：{player_balance}元")
        print("股票行情：")
        for stock in stocks:
            stock.update_price()
            print(f"{stock.name}：{stock.price}元")

        choice = input("请输入您要操作的股票名字（腾讯、阿里巴巴、百度），或者输入'退出'来结束游戏：")
        if choice == "退出":
            print("感谢您的参与，再见！")
            break

        selected_stock = None
        for stock in stocks:
            if stock.name == choice:
                selected_stock = stock
                break

        if selected_stock is None:
            print("无效输入，请重新输入。")
            continue

        action = input("请输入您要执行的操作（买入、卖出）：")

        amount = int(input("请输入您要操作的股票数量："))

        if action == "买入":
            total_cost = amount * selected_stock.price
            if total_cost > player_balance:
                print("您的本金不足，无法购买。")
                continue
            player_balance -= total_cost
            print(f"您已成功购买{amount}股{selected_stock.name}，花费{total_cost}元。")
        elif action == "卖出":
            total_income = amount * selected_stock.price
            player_balance += total_income
            print(f"您已成功卖出{amount}股{selected_stock.name}，收入{total_income}元。")
        else:
            print("无效输入，请重新输入。")

if __name__ == "__main__":
    main()
