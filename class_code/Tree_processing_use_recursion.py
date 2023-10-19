from Tree import tree,label,branches,is_tree,is_leaf,fib_tree
#count leaf is often the baase case of a tree processing function

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_counts=[count_leaves(b) for b in branches(t)]
        return sum(branch_counts)
    
## Implement leaves, which returns a list of the leaf labels of a tree

def leaves(t):
    """
    >>>leaves(fib_tree(5))
    [1,0,1,0,1,1,0,1]
    """
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])
    
## A function that creates a tree from another tree is typicall also recursive
def increment_leaves(t):
    """
    Return a tree likt t but with leaf labels incremented
    """
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs=[increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)
    
def increment(t):
    """return a tree like t but with all labels incrmented"""
    return tree(label(t)+1,[increment(b) for b in branches(t)]) #when we reach a leave we are done

def print_tree(t,indent=0):
    print(" "*indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1)

def print_sums(t,so_far):
    so_far=so_far+label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b,so_far)

def count_paths(t,total):
    """
    Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.
    """
    if label(t)==total:
        found=1
    else:
        found=0
        return found+ sum([count_paths(b,total-label(t)) for b in branches(t)])


