age = int(input("输入你的年龄："))
if age >= 18 :
    print("你已经成年，请继续答题")
    if age < 30 :
        print("请输入以下问题")
        if int(input("请输入你的级别")) >= 3:
            print("你可以获得礼物，级别大于等于三")
        elif int(input("请输入你的在职时长：")) >= 2:
            print("你可以获得礼物，在职时长大于2年")
    else:
        print("你的年龄高于30，无法获得礼物")
else:
    print("未成年无法获得礼物")