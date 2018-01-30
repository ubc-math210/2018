# poly.py

def poly_diff(p):
    '''Compute the derivative of a polynomial p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n.
    
    Input:
        p : list of length n+1 [a0,a1,a2,...,an] representing
            a polynomial p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n.
    Output:
        List [a1,2*a2,...,n*an] of length n (or [0] if n=0) representing the derivative p'(x).
    Example:
        >>> poly_diff([1,2,3,4])
        [2, 6, 12]
    '''
    deg_p = len(p) - 1
    if deg_p == 0:
        return [0]
    else:
        return [p[k]*k for k in range(1,deg_p+1)]

def poly_eval(p,a):
    '''Evaluate p(a) for p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n.
    
    Input:
        p : list of length n+1 [a0,a1,a2,...,an] representing
            a polynomial p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n.
        a : number
    Output:
        Polynomial p(x) evaluated at a.
    Example:
        >>> poly_eval([1,2,3,4],-2)
        -23
    '''
    return sum([p[k]*a**k for k in range(0,len(p))])

def poly_max(p,a,b,N):
    '''Approximate the maximum value of p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n in the interval [a,b].
    
    Input:
        p : list of length n+1 [a0,a1,a2,...,an] representing
            a polynomial p(x) = a0 + a1*x + a2*x**2 + ... + an*x**n.
        a,b : numbers defining the interval [a,b]
        N : positive integer defining the length of the partition x0 = a, x1, x2, ... , xN = b
    Output:
        Maximum value from the list of values p(x0), p(x1), p(x2), ... , p(xN).
    Example:
        >>> poly_max([1,0,-1],-1,1,10)
        1.0
    '''
    h = (b - a)/N # Length of each subinterval
    x_values = [a + h*k for k in range(0,N+1)] # Partition interval x0 = a, x1, x2, ... , xN = b
    y_values = [poly_eval(p,x) for x in x_values] # Compute y values y = p(x)
    return max(y_values)