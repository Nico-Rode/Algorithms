def fib(months, life):
    list_of_life = [0] * life
    list_of_life[0], list_of_life[1] = 0, 1
    for x in range(2, months):
        temp = list(list_of_life)
        list_of_life[0] = sum(list_of_life[1:])  # number of new born
        for i in range(1, life):
            list_of_life[i] = temp[i - 1]
    return sum(list_of_life)

def main():
    print(fib(96,20))


main()
