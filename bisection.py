"""
When we want to find the zero (root) of a function f(x) in the plane, it is not always possible to set f equal to zero 
and analytically solve for x. Just try f(x) = cos(x) - x. Therefore, we need what's called a root-finding algorithm. The 
bisection method is one of the most common ways to find a zero of a function. If a function f(x) is continuous on a closed
interval [a, b], and f(a)*f(b)<0 (f has opposite signs at the endpoints), then there exists a c in [a, b] such that f(c) = 0.
More can be found on this method and further generalizations of this method at https://en.wikipedia.org/wiki/Bisection_method


Feel free to use this method and play around with it!!!
"""

def bisection(f, a, b, tol, N):
    """
    N is the maximum number of iterations, tol is the tolerance (how accurate of a solution you want).
    Generally, as the tolerance becomes smaller, the number of iterations N must grow. a and b are the endpoints of the close interval, while f is your function.
    """
    if f(a) * f(b) > 0:
        return 'No real roots contained within the chosen interval.'
    else:
        n = 1
        while n <= N:
            c = (b + a) / 2
            if abs(f(c)) < tol:
                print('Root found. Number of iterations: ', n)
                return c
                break
            elif f(a) * f(c) < 0:
                b = c
                n = n + 1
            else:
                a = c
                n = n + 1
        return 'No root found within chosen tolerance. Max iterations exceeded.'
