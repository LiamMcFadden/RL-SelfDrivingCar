# This solution is from here -> Box Of Hats (https://github.com/Box-Of-Hats )
# Modified to to only look for the keys in key_list

import win32api as wapi
import time

# see https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
key_list = [0x01, 0x02, 0x57, 0x41, 0x53, 0x44, 0x10, 0x50, 0x51, 0x52, 0x46]
key_dic = {0x01:'Left Click', 0x02:'Right Click', 0x57:'w', 0x41:'a',
        0x53:'s', 0x44:'d', 0x10:'Shift', 0x50:'p', 0x51:'q', 0x52:'r', 0x46:'f'}

def key_check():
    keys = set()
    for key in key_list:
        if wapi.GetAsyncKeyState((key)):
            keys.add(key_dic[key])

    return keys
