import re

my_ip = '103.103.56.46'

update_ip = re.sub("0","",my_ip)
print(update_ip)