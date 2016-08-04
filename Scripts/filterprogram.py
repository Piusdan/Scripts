#! python3
# filterprogram.py - filters a file ignoring lines starting with a # symbol
def filterfile(oldFile, newFile):
    f1 = open(oldFile, 'rw')
    f2 = open(newFile, 'w')
    while True:
        text = f1.readline()
        if text == '':
            break
        elif '#' in text:
            if text[0] == '#':
                continue
            else:
                count = 0
                for i in text:
                    if i != '#':
                        count = count + 1
                    else:
                        f2.write(text[:count])
                        continue
        else:
            f2.write(text)
    f1.close()
    f2.close()
    return
if __name__ == '__main__':
    filterfile('test.bin', 'newtest2.bin')
