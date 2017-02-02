def make_chocolate(small, big, goal):
    if goal / 5 >= big:
        rest = goal - big * 5
        if rest > small:
            return -1
        elif rest == small:
            return small
        else:
            return rest
    else:
        rest = goal - goal / 5 * 5
        if rest > small:
            return -1
        elif rest == small:
            return small
        else:
            return rest
