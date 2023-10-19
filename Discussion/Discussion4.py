"""Conculusion. I'm still unfamilar with recursion. 
The question 2 and 5 was unsolved at the first try

On question 5, I made mistake on data structure
"""

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n, k):##unsolved
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        total=0
        for i in range(1,k+1):
            total+=count_k(n-i,k)
        return total 
    
"""
An altertive way:
"""

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    k,f=1,1
    def helper(m,n,k,f):
        if k==m or f==n:
            return 1
        else:
            return helper(m,n,k+1,f)+helper(m,n,k,f+1)
    return helper(m,n,k,f)

    
def max_product(s):## didn't got an efficient way 
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    #### My inefficient wat 
    # i=0
    # max_=1
    # def helper(s,i,max_):
    #     if s==[]:
    #         return max_
    #     elif len(s)<=2:
    #         return s.max()
    #     elif i+1==len(s):
    #         list=[s[i]*x for a,x in enumerate(s) if a!=i and a!=i+1 and a!=i-1]
    #         if max(list)>max_:
    #             max_=max(list)
    #         return max_           
    #     else:
    #         list=[s[i]*x for a,x in enumerate(s) if a!=i and a!=i+1 and a!=i-1]
    #         if max(list)>max_:
    #             max_=max(list)
    #         i+=1
    #         return helper(s,i,max_)
    # return helper(s,i,max_)
    if s==[]:
        return 1
    if len(s)==1:
        return s[0]
    else:
        return max(s[0]*max_product(s[2:]),max_product(s[1:]))
    

def flatten(s):## unsolved
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    "*** YOUR CODE HERE ***"
    if not any(isinstance(x, list) for x in s):
        return s
    else:
        # return [flatten(x) if type(x)==list else x for x in s] 
        """This doesn't work because the basic function returns a list
            it's not the way to change list """
    lst = []
    for elem in s:
        if type(elem) == list:
            lst += flatten(elem)
        else:
            lst += [elem]
    return lst        





