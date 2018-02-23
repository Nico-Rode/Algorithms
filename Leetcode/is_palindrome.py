def is_palindrome(string):
    left, right = 0, (len(string)-1)
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome(string):
    return str(string) == str(string)[::-1]
