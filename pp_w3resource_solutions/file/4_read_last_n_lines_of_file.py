
with open("preet.txt","r") as fh:
    line = fh.readlines()
    last_line = line[-2]
    for line in last_line:
        print(last_line)
        break


        fh.close()