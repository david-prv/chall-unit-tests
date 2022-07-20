#!/usr/bin/env python3

import os
import subprocess
from colorama import Fore
from colorama import Style 
from colorama import init

def runExploits():
    # map unit test to corresponding exptected output
    tests = {
        'flag1.py': 'FLAG_HERE',
        'flag2.py': 'FLAG_HERE',
        'flag3.py': 'FLAG_HERE'
    }

    # count fails
    failed = 0

    # execute tests and examine output
    for i in tests:
        print(f"[{Fore.LIGHTCYAN_EX}INFO{Style.RESET_ALL}] Running test '{i}'...")

        r = subprocess.run(['python3', './tests/' + i], stdout=subprocess.PIPE)
        r = r.stdout.decode('ascii')
        exp = tests[i]

        if(exp in r):
            state = "PASSED"
            msg = "Unit test was successfully completed."
        else:
            failed += 1
            state = "FAILURE"
            msg = f"Unit test has failed. Expected '{exp}' but got '{r.rstrip()}'."

        print(f"[{Fore.GREEN if exp in r else Fore.RED}{state}{Style.RESET_ALL}] {msg}")

    print(f"[{Fore.LIGHTCYAN_EX}INFO{Style.RESET_ALL}] Tests failed: {failed} | Tests passed: {len(tests)-failed}")

if __name__ == '__main__':
    init(convert=True)
    os.chdir(os.path.dirname(__file__))
    if(os.path.isdir(os.getcwd() + "/tests")):
        runExploits()
    else:
        print(f"[{Fore.RED}ERROR{Style.RESET_ALL}] Could not find './tests'...")
