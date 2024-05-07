#!/usr/bin/env python

from decrypt import Decrypt

def main():
    """ 
        main method to test decrypt class
        this module runs as a script
    """
    dcrypt = Decrypt()
    dcrypt.getText() #default gets text from secret.txt in $CWD
    dcrypt.getKey() #default sets key to '13'
    dcrypt.decipherMessage(show_cleartext=True)

if __name__ == '__main__':
    main()
