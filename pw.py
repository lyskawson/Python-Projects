#! /usr/bin/env python3

passwords = {'email': 'rhrhw3423', 'blog': 'aw382ddw', 'luggae': '1234'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Using: python pw.py [account] - copying password for stated account')
    sys.exit()
account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(account.capitalize() + ' password has been copied to clipboard.')
else:
    print(account.capitalize() + ' account doesn\'t exist.')

