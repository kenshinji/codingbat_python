def front_times(str, n):
    if len(str) >= 3:
        return str[:3] * n
    else:
        return str * n