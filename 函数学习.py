def check(x):
    if x <= 37.5:
        print("您的体温是%.1f，欢迎进入" % x)
    else:
        print("您的体温是%.1f，需要隔离" % x)
check(float(input("欢迎，请输入你的体温")))