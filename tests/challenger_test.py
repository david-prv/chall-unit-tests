import requests
import sys
import random
import string

# Host specifications
TARGET_HOST = "xxx.xxx.xxx.xxx"
TARGET_PORT = "80"
TARGET_USER = "secretUser"
TARGET_PASS = "secretPass"

# Initialize session
sess = requests.Session()
sess.auth = (TARGET_USER, TARGET_PASS)

"""
test:
Takes @target ip and @port and runs main attack
methods on specified host

EXPECTED: "contenttype: image/png | status: 200 | random input resulted in: 403"
"""
def test(target, port):
    try:
        # General check-up
        r = sess.get(f"http://{target}:{port}/func/captcha.php")
        contenttype = r.headers['Content-Type']
        status = r.status_code

        # Check random input
        chars = string.ascii_uppercase
        inp = str(random.randint(0,255))
        for _ in range(6):
            inp += str(random.choice(chars))
        
        chall_r = sess.post(f"http://{target}:{port}/func/captcha.php", data={"user_challenge": inp}).status_code

        print(f"contenttype: {contenttype} | status: {status} | random input resulted in: {chall_r}")
    except Exception as err:
        print(f"ERROR: {err}")
        exit()

if __name__ == '__main__':
    test(sys.argv[1] if len(sys.argv) > 1 else TARGET_HOST, sys.argv[2] if len(sys.argv) > 2 else TARGET_PORT)
