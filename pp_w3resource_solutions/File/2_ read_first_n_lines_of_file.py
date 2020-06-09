fh = open("preet.txt")
n = 1
line_count = 0

for line in fh:
    if line_count == n:
        break
    line_count += 1
    print(line,end="")
