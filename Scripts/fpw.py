#! python2.7
from pw import *


class fhandle(passwords):
    '''file handling for the passwords'''
    def savePass(self):
        f = open('pwd.bat', 'w')
        for k,v in self.PASSWORDS.items():
            s = str(k) + ' : ' + str(v) + '\n'
            f.write(s)
        f.close()

    def getPass(self):
        f = open('pwd.bat', 'r')
        while True:
            text = f.readline()
            if len(text) == 0:
                break
            else:
                text = text.strip('\n')
                text = text.split(' : ')
                self.PASSWORDS[text[0]] = text[1]
        print self.PASSWORDS
        f.close()

if __name__ == '__main__':
    Handle = fhandle(sys.argv[1:])
    #Handle.savePass()
    Handle.getPass();