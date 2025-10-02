money = 5000
def main():
    name = input("输入你的名字")
    def second():
        global money
        print("-------------主菜单------------- \n %s，欢迎使用ATM，请选择你的操作：" % name)
        keyboard = int(input("查询余额 [输入1] \n 存款  [输入2] \n 取款  [输入3] \n 退出  [输入4]\n 输入你的选择："))
        while True:
            if keyboard == 1:
                print("你的余额为：%d" % money)
                second()
            elif keyboard == 2:
                save = int(input("输入你要存入的钱："))
                money += save
                print("存款成功，你的余额为：%d" % money)
                second()
            elif keyboard == 3:
                cost = int(input("输入你要取出的钱："))
                money = money - cost
                print("取钱成功，你的余额为：%d" % money)
                second()
            else:
                print("您已退出")
                main()
    second()
main()