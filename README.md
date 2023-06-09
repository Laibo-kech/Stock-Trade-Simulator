# 股票交易模拟器

此项目是一个基于Python的股票交易模拟器。它旨在提供一种简单的方式，模拟股票市场的买卖行为。玩家可以买入和卖出三只不同的股票：腾讯、阿里巴巴和百度，而股票价格会根据预设的随机算法变动。

## 开发者

**shiwenxiang**

## 时间

开发日期：2023/4/16 22:17

## 代码结构

代码主要由两个类组成：`Stock`和`main()`。

### Stock类

该类定义了每一支股票的基本属性和方法。主要包括股票名称和价格，以及一个更新股票价格的方法。

### main函数

main函数是整个游戏的主要逻辑部分，玩家可以通过main函数来进行股票的买入和卖出，以及查看当前的股票价格。

## 使用方式

1. 运行代码，启动模拟器。
2. 根据提示，输入你想进行操作的股票名称（如“腾讯”）或输入'退出'来结束游戏。
3. 输入你想进行的操作类型，可以选择“买入”或者“卖出”。
4. 输入你想要交易的股票数量，然后按回车键确认。
5. 如果交易成功，你会看到交易成功的消息，包括交易的股票，数量和交易金额。如果交易失败（例如因为余额不足或输入的股票名称无效），你会收到一个错误消息。

## 注意事项

- 请确保输入的股票名称是正确的，否则你会收到一个错误消息。
- 在买入股票时，请确保你有足够的余额来支付股票的成本，否则交易将无法进行。
- 在卖出股票时，系统会假设你持有足够数量的股票来出售，但实际上，本程序并没有检查你是否拥有要卖出的股票。

## 免责声明

这只是一个股票交易模拟器，所有的股票价格都是随机生成的，与真实的股票价格无关。不应用此模拟器作为真实交易的依据。这是一个用于学习和娱乐的工具，而不是一个投资建议或策略。
