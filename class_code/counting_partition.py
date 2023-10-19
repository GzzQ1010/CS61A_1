def count_partition(n,m):
    """
    >>>count_partition(6,4)
    9

    """
    if n==0:
        return 1 
    if n<0:
        return 0
    if m==0:
        return 0 
    else: 
        with_m=count_partition(n-m,m)
        without_m=count_partition(n,m-1)
        return with_m+without_m
    


