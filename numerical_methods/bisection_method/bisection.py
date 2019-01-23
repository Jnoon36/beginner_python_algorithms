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
                print('Number of iterations: ', n)
                return c
                break
            elif f(a) * f(c) < 0:
                b = c
                n = n + 1
            else:
                a = c
                n = n + 1
        return 'No root found within chosen tolerance. Max iterations exceeded.'
