def count_hi(str):
    count = 0
    i = 0
    while i < len(str) - 1:
        if str[i:i+2] == "hi":
            count += 1
        i += 1
    return count

