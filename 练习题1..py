# 计算圆的面积和周长
import math
def circle_calculations():
    r = float(input("输入半径："))
    s = math.pi * r ** 2
    d = math.pi * 2 * r
    print("该圆的面积为%.1f，周长为%.1f" % (s, d))
circle_calculations()
# 计算闰年
k = int(input("输入你要计算的年份"))
def is_leap_year(year):
    if year % 4 == 0:
        print("是闰年")
    else:
        print("不是闰年")
is_leap_year(k)
# 字符串反转：  重点复习
k = input("输入你要反转的字符串")
def reverse_string(s):
    result = ""
    for i in s:
        result = i + result
    return result
s = reverse_string(k)
print(s)
# 斐波那契数列生成：
a = 0
b = 1
def k(x):
    global a , b
    for i in range(2 , x+1):
        temp = a + b
        a = b
        b = temp
        print(f"第{i}个斐波那契数为：{b}")
x = int(input("输入你要生成多少个斐波那契数列"))
if x == 1:
    print(f"第{x}个斐波那契数为：1")
elif x == 2:
    print(f"第1个斐波那契数为：2 \n第{x}个斐波那契数为：2")
else:
    k(x)
# 将列表内多余的元素删除
list = [1,2,3,4,5,5,5,5,6,7,8,8,8,8,9,10]
for i in list:
    while True:
        num = list.count(i)
        if num > 1:
            list.remove(i)
        elif num == 1:
            break
print(list)
# 质数的判断
def is_prime(num):
    if num >= 2:
        for i in range(2, num):
            if num % i != 0:
                if i == num - 1:
                    print(f"你输入的数据：{num}是素数")
                    break
            elif num % i == 0:
                    print(f"你输入的数据：{num}不是素数")
                    break
    else:
        print("请输入大于等于2的数据")
is_prime(int(input("请输入你要判断的数据：")))
# 数字分类统计
k = 0
for i in range(1,101):
    if i % 3 == 0:
        if (i-3) % 10 == 0:
            k += 1
            print(i)
print("一共有%d个数个位数为3，且能被3整除" % k)
# 模拟登录验证
def login(account, password):
    if account == "admin":
        if password == "12345":
            print("登录成功！")
        else:
            print("账号或密码错误，请重新输入！")
            account = input("输入账号：")
            password = input("输入密码:")
            login(account, password)
    else:
        print("账号或密码错误，请重新输入！")
        account = input("输入账号：")
        password = input("输入密码:")
        login(account, password)
account = input("输入账号：")
password = input("输入密码:")
login(account, password)
# 九九乘法表
i = 1
for i in range(1,10):
    t = 1
    while t <= i:
        print(f"{i} * {t} = {i * t}\t" , end="")
        t += 1
    print()