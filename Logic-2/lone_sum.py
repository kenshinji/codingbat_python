def lone_sum(a, b, c):
    if(a == b and b != c):
        return c
    elif(a != b and b == c):
        return a
    elif(a == c and a != b):
        return b
    elif(a == b and b == c):
        return 0
    else:
        return a + b + c
