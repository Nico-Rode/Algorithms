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

def main(list1, list2):
    answer_dict = {}
    for x in list2:
        if x in answer_dict:
            continue
        print(binarySearch(list1, 0, len(list1) - 1, x))

len_list1 = int(input())
len_list2 = int(input())
list1 = []
list2 = []
string1 = input().split()
string2 = input().split()
for i in range(len_list1):
    list1.append(int(string1[i]))
for i in range(len_list2):
    list2.append(int(string2[i]))


main(list1, list2)
