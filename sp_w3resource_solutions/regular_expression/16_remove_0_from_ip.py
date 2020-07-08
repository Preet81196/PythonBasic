"""Write a Python program to remove leading zeros from an IP address."""
import re

ip = '192.168.031.130'

update = re.sub(r'\b0+(\d)', r'\1', ip)
print(update)