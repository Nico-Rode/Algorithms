def binarySearch(list1, floor, ceiling, x):
    # Check base case
    if ceiling >= floor:
        guess_index = int(floor + ((ceiling - floor) / 2))
        if list1[guess_index] == x:
            return guess_index + 1
        elif list1[guess_index] > x:
            return binarySearch(list1, floor, guess_index - 1, x)
        else:
            return binarySearch(list1, guess_index + 1, ceiling, x)
    return -1

def main(list1):
    answer_dict = {}
    answer_list = []
    size = len(list1)/2
    for x in list1:
        if x in answer_dict:
            answer_dict[x] += 1
        else:
            answer_dict[x] = 1
    for key in answer_dict.keys():
        if answer_dict[key] > size:
            answer_list.append(key)
    if len(answer_list):
        for k in answer_list:
            print(k)
            return 0
    print(-1)


len_list1, len_list2 = map(int, input().split())

for i in range(len_list1):
    string1 = ''
    list1 = []
    string1 = input().split()
    for i in range(len_list2):
        list1.append(int(string1[i]))
    main(list1)
