import time, itertools, sys

spinner = itertools.cycle(["|", "/", "-", "\\"])

for _ in range(50):
    sys.stdout.write("\rLoading " + next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
