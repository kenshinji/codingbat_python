def xyz_there(str):
    i = 0
    while i < len(str) - 2:
        if str[i:i+3] == "xyz":
            if i - 1 < 0:
                return True
            elif i - 1 >= 0 and str[i-1:i] != ".":
                return True
        i += 1
    return False
