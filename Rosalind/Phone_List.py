number_of_sets = int(input())

while(number_of_sets):
    phone_numbers = int(input())
    list = []
    for i in range(phone_numbers):
        list.append(input())
    list.sort()
    answer = "YES"
    for num in range(phone_numbers-1):
        if (list[num] == list[num+1][:len(list[num])]):
            answer = "NO"
            break
    number_of_sets -= 1
    print(answer)
