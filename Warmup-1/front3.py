def front3(str):
    if len(str) < 3:
        return 3 * str
    else:
        return 3 * str[0:3]