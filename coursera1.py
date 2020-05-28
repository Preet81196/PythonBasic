def computepay(hrs,rate):
    if hrs > 40 :
        rate_1 = (rate * 1.5) * (hrs - 40)
    return ((hrs - 5) * rate) +  rate_1

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(45,10.50)
print("Pay",p)