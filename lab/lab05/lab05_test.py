from lab05 import tree,is_leaf,is_leaf,label,branches

def func1(t):
    if is_leaf(t):
        if label(t)=='a':
            return tree('b')
        else:
            return tree(t)

def print_sums(t,so_far):
    so_far=so_far+label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b,so_far)
