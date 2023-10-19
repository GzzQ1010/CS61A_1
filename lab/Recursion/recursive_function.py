def multiply(x,n):
    if n==1:
        return x
    else:
        n-=1
        return x+multiply(x,n)
    
##find the bug 
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)
    
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def check_prime(x):
        if x==n:
            return True
        elif n%x==0 :
            return False
        return check_prime(x+1)
    return check_prime(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    step=0
    def f(n,step):
        if n==1:
            step+=1
            return step
        elif n%2==0:
            n/=2
            print(n)
            step+=1
            return f(n,step)
        else: 
            n=n*3+1
            print(n)
            step+=1 
            return f(n,step)
    return f(n,step)

def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1==0:
        return n2 
    elif n2==0:
        return n1 
    elif n1%10<n2%10:
        return merge(n1//10,n2)*10+n1%10
    else:
        return merge(n1,n2//10)*10+n2%10
    

