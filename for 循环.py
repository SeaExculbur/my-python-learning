for i in range(1 , 10):
    for j in range(1, i+1):
        result = i * j
        print(f"{j} * {i} = {result}\t" , end='')
        j += 1
    print()