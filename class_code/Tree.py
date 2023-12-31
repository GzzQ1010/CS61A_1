## creat a tree abstraction
def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    """
    1.a tree has a label and a list of branches-- its type is list
    2.each branch is a tree
    """
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)#check if its branches are empty 
    
##Fib tree
def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left, right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

