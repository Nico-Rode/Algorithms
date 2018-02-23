def subsequence(sequence):

    m = [None] * len(sequence)
    permutations = [None] * len(sequence)

    last = 1

    m[0] = 0

    for i in range(1, len(sequence)):
        lower = 0
        upper = last

        if sequence[m[upper - 1]] < sequence[i]:
            j = upper
        else:
            while (upper - lower) > 1:
                mid = (upper + lower) // 2
                if sequence[m[mid - 1]] < sequence[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower

        permutations[i] = m[j - 1]

        if j == last or sequence[i] < sequence[m[j]]:
            m[j] = i
            last = max(last, j + 1)

    result = []
    pos = m[last - 1]

    for _ in range(last):
        result.append(sequence[pos])
        pos = permutations[pos]

    return result[::-1]



def main():
    n = int(input())
    list1 = []
    string1 = input().split()
    for i in range(n):
        list1.append(int(string1[i]))

    increasing = subsequence(list1)
    decreasing = subsequence(list1[::-1])[::-1]
    print(str(increasing).strip('[]').replace(',', ''))
    print(str(decreasing).strip('[]').replace(',', ''))




if __name__ == '__main__':
	main()
