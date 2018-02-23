def reverse_integer(integer):
    result = 0
    while integer:
        result = result*10 + (intger%10)
        integer /= 10
    return result if result <= 0x7fffffff else 0
