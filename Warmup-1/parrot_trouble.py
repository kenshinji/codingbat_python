def parrot_trouble(talking, hour):
    if hour<7 or hour>20:
        return talking
    elif hour>=7 and hour<=20:
        return False