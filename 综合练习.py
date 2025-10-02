money = 10000
for i in range(1,21):
    import random
    grade = random.randint(1, 10)
    if grade < 5:
        print(f"员工{i}，绩效分{grade}，低于5，不发放工资，下一位。")
        continue
    else:
        money = money - 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩{money}元。")
        if money == 0:
            print("工资发放完毕")
            break