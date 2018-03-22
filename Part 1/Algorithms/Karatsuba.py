
from math import pow
from math import ceil
def karatsuba(x,y):
    if x<10 and y<10:
        return x*y
    else:
        n=ceil(max(len(str(x)),len(str(y)))/2)
        a = int(x // pow(10, n))
        b = int(x % pow(10, n))
        c = int(y // pow(10, n))
        d = int(y % pow(10, n))
        ac=karatsuba(a,c)
        bd=karatsuba(b,d)
        prod=karatsuba(a+b,c+d) - ac - bd
        return ac*pow(10,2*n)+prod*pow(10,n) + bd

result=karatsuba(2450,12322)
print(result)


