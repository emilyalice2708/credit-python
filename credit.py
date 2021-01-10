from cs50 import get_int
from cs50 import get_string
from sys import exit

while True:
    n = get_string("Number: ")
    if len(n) == 13 or len(n) == 15 or len(n) == 16:
        break
    print("INVALID")
    exit(1)

num = int(n)
index = len(n) - 1
rev = n[::-1]

total_double = 0
totals = 0

for i in range(len(n)):
    if i % 2 != 0:
        double = int(rev[i]) * 2
        sum = 0
        if len(str(double)) > 1:
            for i in range(len(str(double))):
                sum += int((str(double)[i]))
            double = sum
        total_double += double
    if i % 2 == 0:
        totals += int(rev[i])

total_sum = total_double + totals
if (str(total_sum)[-1]) != '0':
    print("INVALID")
    exit(1)

if n[0] == '4':
    print("VISA")
    exit(0)
else:
    str = n[0] + n[1]
    if str == '34' or str == '37':
        print("AMEX")
        exit(0)
    elif str == '51' or str == '52' or str == '53' or str == '54' or str == '55':
        print("MASTERCARD")
        exit(0)
