# -*- coding: utf-8 -*-
# @Author: Xiaobo Yang
x=0
y=0
z=0
print(z)
def extra_euclid(a, b):
    global x
    global y
    if b == 0:
        x=1
        y=0
        return a
    re=extra_euclid(b, a%b)
    x, y = y, x - (a // b) * y
    return re

gcd = extra_euclid(17, 9)
print("x = %d, y = %d, gcd(a, b) = %d"%(x, y, gcd))

def solve_diop(a, b, c):
    gcd = extra_euclid(a, b)
    if c % gcd == 0:
        print("x = %d, y = %d"%((c / gcd) * x,(c / gcd) * y))
    else:
        print("No Integral Solution For This Equation")

solve_diop(17, 9, 10)