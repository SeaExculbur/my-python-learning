money = 5000000
def main():
    name = input("输入你的名字")
    return name
name = main()
def second():
    print("-----------------主菜单------------------")
    print(f"{name},您好！欢迎使用ATM机，请选择操作：")
    x = int(input("查询余额 [输入1] \n 存款   [输入2] \t\n 取款   [输入3] \t\n 退出   [输入4]  \t\n 请输入你的选择：\t"))
    if x == 1:
        the_rest()
    elif x == 2:
        save()
    elif x == 3:
        cost()
    else:
        print("程序已经退出")
def the_rest():
    print("-----------------查询余额------------------ \n 您的余额为%d" % money)
    second()
def save():
    global money
    money = money + int(input("输入你要存入的现金"))
    print("存款成功！\n 你的存款还剩%d" % money)
    second()
def cost():
    global money
    money = money - int(input("输入你要取出的现金"))
    print("取款成功！\n 你的存款还剩%d" % money)
    second()
second()