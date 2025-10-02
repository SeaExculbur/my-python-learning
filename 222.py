import random
num = random.randint(1, 10)
guess = int(input("输入你的第一次猜想"))
if num == guess:
    print("你猜对了")
elif num < guess:
    print("你猜大了")
    guess = int(input("输入你的第二次猜想"))
    if num == guess:
        print("你猜对了")
    elif num > guess:
        print("你猜小了")
        guess = int(input("输入你的第三次猜想"))
        if num == guess:
            print("你猜对了")
        elif num < guess:
            print("你猜大了,正确答案是%d" % num)
        elif num > guess:
            print("你猜小了，正确答案是%d" % num)
    elif num < guess:
        print("你猜大了")
        guess = int(input("输入你的第三次猜想"))
        if num == guess:
            print("你猜对了")
        elif num < guess:
            print("你猜大了,正确答案是%d" % num)
        elif num > guess:
            print("你猜小了，正确答案是%d" % num)
elif num > guess:
    print("你猜小了")
    guess = int(input("输入你的第二次猜想"))
    if num == guess:
        print("你猜对了")
    elif num > guess:
        print("你猜小了")
        guess = int(input("输入你的第三次猜想"))
        if num == guess:
            print("你猜对了")
        elif num < guess:
            print("你猜大了,正确答案是%d" % num)
        elif num > guess:
            print("你猜小了，正确答案是%d" % num)