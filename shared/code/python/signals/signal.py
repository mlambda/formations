import os
import signal


def reload(signum, frame):
    print("Reloading config…")


signal.signal(signal.SIGUSR1, reload)
print(os.getpid())
while True:
    signal.pause()
