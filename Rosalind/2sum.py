
def twoSum(nums, target):

    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num] + 1, i + 1]
        lookup[num] = i
    return []



def main():
    len_list1, size = map(int, input().split())

    for i in range(len_list1):
        list1 = []
        string1 = input().split()
        for i in range(size):
            list1.append(int(string1[i]))
        ans = twoSum(list1, 0)
        if (len(ans)):
            print(ans[0], ans[1])
        else:
            print(-1)

main()
