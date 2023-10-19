## Rational number abstraction
pair=[1,2]

x,y=pair

##constructor of rational
from math import gcd

# def rational(n,d):
#     g=gcd(n,d)
#     return[n//g,d//g]
##alternative:
def rational(n,d):
    def select(name):
        if name == 'n':
            return n
        if name =='d':
            return d
    return select


# def numer(x):
#     return x[0]

# def denom(x):
#     return x[1]
##Alternative
def numer(x):
    return x('n')
def denom(x):
    return x('d')

def mul_rational(x,y):
    return rational(numer(x)*numer(y),
                    denom(x)*denom(y))

def add_rational(x,y):
    nx,dx=numer(x),denom(x)
    ny,dy=numer(y),denom(y)
    return rational(nx*dy+ny*dy,dx*dy)

def equal_rational(x,y):
    return numer(x)*denom(y)==numer(y)*denom(x)
