#!/usr/bin/env python3

import requests
import sys
import re

# Host specifications
TARGET_HOST = "xxx.xxx.xxx.xxx"
TARGET_PORT = "80"
TARGET_USER = "secretUser"
TARGET_PASS = "secretPass"

"""
TARGET_USER and TARGET_PASS are necessary, since my service uses a simple http authentication
during testings
"""

# Initialize session
sess = requests.Session()
sess.auth = (TARGET_USER, TARGET_PASS)

"""
printFlags:

Takes @input as input and filters all contained flags
"""
def printFlags(input):
    m = re.search('FLAG{[A-Za-z0-9\/\\+_]*}', input)
    print(f"Found flag: {m.group(0)}" if m else "Nope, there wasn't a flag :(")
    return

"""
exploit:

Takes @target ip and @port and runs main attack
methods on specified host
"""
def exploit(target, port):
    # TODO: Write your test here
    pass

if __name__ == '__main__':
    exploit(sys.argv[1] if len(sys.argv) > 1 else TARGET_HOST, sys.argv[2] if len(sys.argv) > 2 else TARGET_PORT)
