def first_missing_positive(array):
    i = 0
    size = len(array)
    while i < size:
        pos = array[i]-1
        if pos < 0 or pos > (size-1) or array[pos] == array[i]:
            i+=1
        else:
            array[pos], array[i] = array[i], array[pos]
    i = 0
    while i < size and array[i] == i+1:
        i += 1
    return i+1
