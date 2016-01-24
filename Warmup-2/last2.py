
def last2(str):
    count = 0
    target = str[-2:]
    for i in range(len(str)-2):
        if(str[i:i+2]) == target:
            count = count + 1
    return count
print last2('hixxhi')
print last2('xaxxaxaxx')
print last2('axxxaaxx')