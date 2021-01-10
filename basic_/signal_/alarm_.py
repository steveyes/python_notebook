import signal
import time

signal.alarm(4)  # process will be exited 4 seconds later

while True:
    time.sleep(1)
    print("still running...")
