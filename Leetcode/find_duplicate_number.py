def find_duplicate(array):
    slow = array[0]
    fast = array[array[0]]
    while fast != slow:
        slow = array[slow]
        fast = array[array[fast]]
    fast = 0
    while fast != slow:
        fast = array[fast]
        slow = array[slow]
    return slow
