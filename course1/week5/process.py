import time
import os
import sys

for i in range(5):
    pid = os.fork()
    if pid == 0:
        for j in range(3):
            print("child: ", i, " ", os.getpid(), " iter - ", j)
            time.sleep(5)
        sys.exit()
    else:
        print("parent: ", i, " ", os.getpid())
os.wait()
