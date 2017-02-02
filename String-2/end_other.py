def end_other(a, b):
    if len(a) > len(b):
        if a[-len(b):].lower() == b.lower():
            return True
        else:
            return False
    elif len(a) < len(b):
        if b[-len(a):].lower() == a.lower():
            return True
        else:
            return False
    elif a.lower() == b.lower():
        return True
    else:
        return False
