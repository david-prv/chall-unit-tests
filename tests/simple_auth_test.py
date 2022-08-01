import requests
import sys

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

EXPECTED: "True"
"""
def test(target, port):
    r = sess.get(f"http://{target}:{port}/admin").text
    print("401 Unauthorized" not in r)

if __name__ == '__main__':
    test(sys.argv[1] if len(sys.argv) > 1 else TARGET_HOST, sys.argv[2] if len(sys.argv) > 2 else TARGET_PORT)
