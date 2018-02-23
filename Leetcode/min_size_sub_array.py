def min_size_sub(array, s):
    left, current_sum = 0,0
    min_len = len(array) + 1
    for right, num in array:
        current_sum += num
        while current_sum >= s:
            current_sum -= array[left]
            min_len = min(min_len, right - left + 1)
            left += 1
    return min_len if min_len <= len(array) else 0
