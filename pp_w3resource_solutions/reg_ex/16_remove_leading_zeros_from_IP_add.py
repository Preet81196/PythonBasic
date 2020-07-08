import re

my_ip = '103.103.056.460'

"""update_ip = re.sub("0","",my_ip)"""
update_ip = re.sub(r'\b0+(\d)', r'\1', my_ip)
    # splits the ip by "."
    # converts the words to integeres to remove leading removeZeros
    # convert back the integer to string and join them back to a string
print(update_ip)