import collections

def threeSum(nums):
    nums, result, i = sorted(nums), [], 0
    while i < len(nums) - 2:
        if i == 0 or nums[i] != nums[i - 1]:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        i += 1
    return result

def main():
    len_list1, size = map(int, input().split())

    for i in range(len_list1):
        list1 = []
        string1 = input().split()
        for i in range(size):
            list1.append(int(string1[i]))
        dict = {}
        for index in range(len(list1)):
            dict[list1[index]] = index + 1

        ans = threeSum(list1)
        if (len(ans)):
            index1, index2, index3 = ans[0]
            print(dict[index1], dict[index2], dict[index3])
        else:
            print(-1)


main()
