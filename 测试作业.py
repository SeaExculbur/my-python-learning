import random
num = random.randint(1,100)
guess = int(input("输入你的猜想："))
i = 0
while guess != num:
    i += 1
    if guess < num:
        guess = int(input("你的猜想小于结果，已经尝试了%d次，请重新输入：" % i))
    elif guess > num:
        guess = int(input("你的猜想大于结果，已经尝试了%d次，请重新输入：" % i))
if guess == num:
    print("你的猜想正确，一共尝试了%d次" % i)