##Extanding rationals
## Rational ADT 
from math import gcd

def make_rat(num,den):
    common_gcd=gcd(num,den)
    def select(name):
        if name=='n':
            return num//common_gcd
        elif name=='d':
            return den//common_gcd
    return select

def numer(rat):
    return rat('n')

def denom(rat):
    return rat('d')

##Divide rational number 
def div_rat(x,y):
    return make_rat(numer(x)*denom(y),numer(y)*denom(x))

##Less Than
def lt_rat(x,y):
    if numer(x)*denom(y)<numer(y)*denom(x):
        return True
    return False 

##Tree
##Tree ADT 
def tree(label,branches=[]):
    return [label]+list(branches)

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_leaf(t):
    return not branches(t)

def height(t):
    if is_leaf(t):
        return 0
    bs=[1+height(branches(t))]
    return max(bs)
"""Alternatives"""
    ## Non-list comprehension solution
    # if is_leaf(t):
    #     return 0
    # best_height = 0
    # for b in branches(t):
    #     best_height = max(height(b), best_height)
    # return best_height + 1

    ##
    #return 1 + max([-1] + [height(branch) for branch in branches(t)])
    #return max([1 + height(b) for b in branches(t)], default=0)

def find_path(t,x):
    """Write a function find_path that takes in a tree t with unique labels and a value x. It returns a list containing the labels of the nodes along the path from the root of t to the node labeled x.

If x is not a label in t, return None. Assume that the labels of t are unique.

For the following tree, find_path(t, 5) should return [2, 7, 6, 5].
>>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
>>> find_path(t, 5)
    [2, 7, 6, 5]
>>> find_path(t, 10)  # returns None
"""
    if label(t)==x:
        return [x]
    for b in branches(t):
        path = find_path(b,x)
        if path:
            return [label(t)]+path 

"""need to check again"""
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t),[tree(leaf) for leaf in leaves])
    return tree(label(t),[sprout_leaves(b,leaves) for b in branches(t)])

"""Need to check again """
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    total=0
    for b in branches(t):
        total+=sum_tree(b)
    return total+label(t)

def balanced(t):
    """
    if all paths are equal
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    path_sum=[]
    def helper(t,so_far=0):
        so_far+=label(t)
        if is_leaf(t):
            path_sum.append(so_far)
        else:
            for b in branches(t):
                helper(b,so_far)
        print(path_sum)
        return len(set(path_sum))==1
    return helper(t)

"""need to check again """
        
def perfect_balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    for b in branches(t):
        if sum_tree(branches(t)[0]) != sum_tree(b) or not perfect_balanced(b):
            return False
    return True

        





