def make_bricks(small, big, goal):
    if goal / 5 >= big:
        rest = goal - big * 5
        return rest <= small
    else:
        rest = goal - goal / 5 * 5
        return rest <= small
    
