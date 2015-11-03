#!/usr/bin/env python3

import hashlib
import getpass
import os
import binascii
import base64

home = os.getenv('HOME')

site = input('Site: ').encode('utf-8')
password = getpass.getpass().encode('utf-8')

with open(home + '/.PTPie', 'r') as file:
    seed = file.read().encode('utf-8')

new_password = hashlib.pbkdf2_hmac('sha512', site + password, seed, 200000)
output = base64.b64encode(new_password).decode('utf-8')[:26]

print(output)
