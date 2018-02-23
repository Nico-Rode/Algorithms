#basically longest subarray of unique characters, right?
#initial thought is sliding window approach, think it would work similarly
#to smallest subarray under k, except max instead of min
def longest_ss_no_repeat(string):
    max_len, left = 0,0
    temp_array = {}
    for right, char in enumerate(s):
        if char in temp_array and left <= temp_array[char]:
            left = temp_array[char] + 1
        else:
            max_len = max(max_len, right - left + 1)

        temp_array[char] = right
    return max_len
