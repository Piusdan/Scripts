#!python3.

import sys
import getopt
import pyperclip
import shelve
# A python program to store acount passwords
# for users using a single master key
# an insecure password locker program
# usage pw.pyw save <accountname> - copys content of clipboard as accountname password
#       pw.pyw copy <accountname> - copys account name password to clipboard
#		pw.pyw del  <account name> - deletes account name
# 		pw.pyw help - displays help information

class passwords:
    def __init__(self, argv):
        '''Dictionary to store passwords'''
        self.PASSWORDS = self.getPass()
        try:
            opts, args = getopt.getopt(argv, 'c:h',
                                       ['copy=', 'help', 'add=', 'del='])
        except getopt.GetoptError as e:
            print(str(e))
            print(self.usage(sys.argv[0]))
            print('use -h to view documentation on help')
            sys.exit(2)
        for o, arg in opts:
            if o in ('-h', '--help'):
                print('''Usage: pw.py [option] [value]
***********************************************************************
Options                 Value
[-c] [--copy]           [account name] - copy accounts password
[-h] [--help]            none - help doc
[--add]                 [account name] - To add new account and password
[--del]                  [account name] - delete existing account details
''')
                sys.exit(3)
            elif o in ('-c', '--copy'):
                self.account = arg
                try:
                    self.copy()
                except KeyError:
                    print('The account you entered does not exist')
                self.savePass()
            elif o in ('--add'):
                try:
                    self.account = arg
                    assert(arg not in self.PASSWORDS.keys())
                except AssertionError:
                    print('The account you trying to add already exists')
                    sys.exit(1)
                self.addAccount()
                self.savePass()
            elif o in ('--del '):
                self.account = arg
                try:
                    self.deleteAccount()
                except KeyError:
                    print('The account you entered does not exist')
                self.savePass()

    '''def __str__(self):
        for k, v in self.PASSWORDS.items():
            s = str(k) + ' : ' + str(v)
        return s'''

    '''def __doc__(self):
        s = 
A python program to store acount passwords
for users using a single master key
an insecure password locker program

        print (s)'''

    def usage(self, par):
        return 'Usage: ' + str(par) + '[option] [Value]'

    def copy(self):
        return pyperclip.copy(self.PASSWORDS[self.account])

    def addAccount(self):
        self.passW = input('Password: ')
        self.PASSWORDS[self.account] = self.passW

    def deleteAccount(self):
        del self.PASSWORDS[self.account]

    def savePass(self):
        f = open('pwd.bat', 'w')
        for k, v in self.PASSWORDS.items():
            s = str(k) + ' : ' + str(v) + '\n'
            f.write(s)
        f.close()

    def getPass(self):
        passwdict = {}
        try:
            f = open('pwd.bat', 'r')
            f.close()
        except IOError:
            f = open('pwd.bat', 'w')
            f.close()
        finally:
            f = open('pwd.bat', 'r')
        while True:
            text = f.readline()
            if len(text) == 0:
                break
            else:
                text = text.strip('\n')
                text = text.split(' : ')
                passwdict[text[0]] = text[1]
        f.close()
        return passwdict

if __name__ == '__main__':  # run module
    try:
        password = passwords(sys.argv[1:])
    except AttributeError:
        print('Use pw.py [option] [value] to view documentation on usage')
