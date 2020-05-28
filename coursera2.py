largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        if largest is None or largest < num :
            largest = num
        if smallest is None or smallest > num :
            smallest = num
    except:
        print("INvalid input")
        continue
print("Maximum", largest)
print("minimun", smallest)