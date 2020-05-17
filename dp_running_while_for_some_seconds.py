"""
Description: Run a while loop for some seconds after which break it automatically.
Author: Divyesh Patel
Date: Sun 17 May, 2020
"""

import time
record_time = time.time()

while time.time() <= record_time + 5:
    print('running')

print('5 seconds elapsed')