def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2 != 0):
        return sortedLst[index]   # if not divisible
    else:
        return (sortedLst[index] + sortedLst[index + 1]) / 2.0 # if divisible 


