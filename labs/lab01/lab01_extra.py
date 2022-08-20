"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    fact=1
    while n>0 and k>0:
        k=k-1
        fact=fact*n
        n=n-1   
    return  fact


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    abl_a5r_rakam=False
    while n>0:
        a5r_rakam=n % 10
        
        if a5r_rakam==8 and abl_a5r_rakam:
            return True
        elif a5r_rakam==8:
            abl_a5r_rakam=True
        else:
            abl_a5r_rakam=False
        n=n//10
    return False
        
            
    
