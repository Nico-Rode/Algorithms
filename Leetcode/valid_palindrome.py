def valid_palindrome(string):
    left, right = 0, len(string)-1
    while left <= right:
        if not string[left].isalnum():
            left +=1
        elif not string[right].isalum():
            right -= 1
        else:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -=1

    return True
