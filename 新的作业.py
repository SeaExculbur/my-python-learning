n = 0
def k(x,y):
    global n
    if x == y:
        print("相等")
    elif x < y:
        print("x小于y")
    else:
        print("x大于y")
x = int(input("输入x"))
y = int(input("输入y"))
m = k(x,y)
print(m)
print(type(m))