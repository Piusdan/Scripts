def find(str, ch, start=0, end=7):
    index = start
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1
