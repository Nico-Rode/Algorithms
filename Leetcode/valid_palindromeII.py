def valid_palindrome(string):
    left, right = 0, len(string)-1
    while left <= right and string[left] == string[right]:
        left += 1
        right -= 1
    opt1, opt2 = string[left:right], string[left+1:right+1]
    return opt1 == opt1[::-1] or opt2 == opt2[::-1]
