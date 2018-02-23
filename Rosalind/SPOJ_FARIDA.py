def max_coins(map_of_monsters, case):
    using_coin = 0
    not_using_coin = 0

    for current_coin in map_of_monsters:
        # Current max excluding i
        new_not_using_coin = max(using_coin, not_using_coin)
        # Current coin count including current coin
        using_coin = not_using_coin + current_coin
        not_using_coin = new_not_using_coin

    print("Case {}: {}".format(case, max(not_using_coin, using_coin)))



def input_spoj():
    while (1):
        test_cases = int(input())
        if test_cases == 0:
            break
        for test_case in range(test_cases):
            num_monsters = int(input())
            map_of_monsters = []
            string1 = input().split()
            for i in range(num_monsters):
                map_of_monsters.append(int(string1[i]))
            max_coins(map_of_monsters, (test_case + 1))

        return 0

def main():
    input_spoj()

    return 0


if __name__ == '__main__':
    main()
