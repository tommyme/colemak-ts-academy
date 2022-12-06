import sys
import time

stream = sys.stdout
for i in range(137):
    stream.write("\b" * (len(str(i)) + 20))
    stream.write("\b" * (len(str(i)) + 20))
    stream.write("a\nMessage : " + str(i))
    stream.flush()
    time.sleep(0.3)
