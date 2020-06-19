"""def srp(s):
    for x in range(s):
        print(' '*(s-x-1)+'*'*(2*x+1))
    for x in sorted(range(3), reverse=True):
            print(' ' * (s - x - 1) + '*' * (2 * x + 1))

srp(4)

def srp(s):
    for each in sorted(range(1, s+1), reverse=True):
        print('*'*each)


srp(5)"""

score = float(input("Enter Score: "))
while score > 0.0 and score < 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score <= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    quit()