def add_all_odd(a,b):
    sum = 0
    for i in range(a,b):
        if (i%2 == 1):
            sum += i
    print(sum)

add_all_odd(4459,9150+1)

