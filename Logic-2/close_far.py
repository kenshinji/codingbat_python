def close_far(a, b, c):
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            return True
        else:
            return False
    elif abs(a - c) <= 1:
        if abs(a - b) >= 2 and abs(b - c) >= 2:
            return True
        else:
            return False
    else:
        return False
