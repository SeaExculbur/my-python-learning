import random
num = random.randint(1, 10)
guess = int(input("输入你的猜想"))
if num == guess:
    print("你猜对了")
else:
    if num > guess:
        print("你猜小了")
    else:
        print("你猜大了")
    guess = int(input("输入你的第二次猜想"))
    if num == guess:
        print("你猜对了")
    else:
        if num < guess:
            print("你猜大了")
        else:
            print("你猜小了")
        guess = int(input("输入你的第三次猜想"))
        if num == guess:
            print("你猜对了")
        else:
            print("机会用完了，正确答案是:%d" % num)