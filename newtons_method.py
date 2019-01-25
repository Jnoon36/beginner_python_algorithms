"""
Here we will look at a root finding algorithm called Newton's method. This involves a reasonable initial guess, xinit, for the 
root of a function f (that is continuous on an interval [a, b], and differentiable on the interval (a, b)) and derivatives of 
that function. More info can be found on wikipedia: [I'm an inline-style link](https://en.wikipedia.org/wiki/Newton%27s_method)
"""


def newton(f, xinit, tol, N):
    """
    f is our function, xinit is our intial guess, tol is the accuracy for the root, and N is the number of iterations.
    """
    if f(xinit) < tol:
        return xinit
    else:
        n = 1
        while n < N:
            xnew = xinit - (f(xinit) / derivative(f, xinit))
            if abs(f(xnew)) < tol:
                print('Root found. Number of iterations: ', n)
                return xnew
                break
            else:
                xinit = xnew
                n = n + 1
        else:
            return 'Max iterations reached. No root found within chosen tolerance.'
