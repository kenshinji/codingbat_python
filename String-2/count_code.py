def count_code(str):
    count = 0
    i = 0
    while i < len(str) - 3:
        if str[i] == "c" and str[i+1] == "o" and str[i+3] == "3":
            count += 1
        i += 1
    return count
