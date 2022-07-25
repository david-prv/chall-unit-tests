#!/usr/bin/env python3

"""
Correctness testing for services often means
trying to find flags over and over again by exploiting vulnerabilities
after each major feature update. Thus, we check, if the intended vulnerabilities still
work, of if any unintended bug breaks them and makes the challenge unsolvable or at least much
harder to solve.
"""

import requests
import sys
import re

# Host specifications
# (HTTP auth is necessary of my service test-system)
TARGET_HOST = "xxx.xxx.xxx.xxx"
TARGET_PORT = "80"
TARGET_USER = "secretUser"
TARGET_PASS = "secretPass"

# Initialize session
sess = requests.Session()
sess.auth = (TARGET_USER, TARGET_PASS)

"""
printFlag:

Takes @input as input and filter the contained flag
"""
def printFlag(input):
    m = re.search('FLAG{[A-Za-z0-9\/\\+_]*}', input)
    print(f"Found flag: {m.group(0)}" if m else "Nope, there wasn't a flag :(")
    return

"""
test:

Takes @target ip and @port and runs main attack
methods on specified host
"""
def test(target, port):
    # TODO: Write your test here
    pass

if __name__ == '__main__':
    test(sys.argv[1] if len(sys.argv) > 1 else TARGET_HOST, sys.argv[2] if len(sys.argv) > 2 else TARGET_PORT)
