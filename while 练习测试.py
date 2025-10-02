a = 1
while a <= 9:
    b = 1
    while b <= a:
        result = a * b
        print(f"{b} x {a} = {result}\t ", end='')
        b += 1
    print()
    a += 1