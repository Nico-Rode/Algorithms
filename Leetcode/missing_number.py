def find_missing_num(array):
    size = len(array)
    total = ((size*size)+size)/2
    calc = 0
    for num in array:
        calc += num
    return total - calc
