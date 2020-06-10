with open("preet.txt","r") as fh:
    lines = fh.readlines()
    lines = [line.strip() for line in lines]
    print(lines)