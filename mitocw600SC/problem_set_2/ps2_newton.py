# 6.00 Problem Set 2 - Newton (problem 1,2,3)
# Name: Sangwook Cheon
# Collaborators (Discussion): None
# Collaborators (Identical Solution): None
# Time: 1 hour 30 minutes

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    assert len(poly) > 0
    f = poly
    eval = 0.0
    input = float(x)

    for i in range(0, len(f)):
        eval += f[i] * (x ** i)

    return eval


# Code to execute evaluate_poly function
# f1 = (2,3,4,5,6,1,2)
# input = float(raw_input("Write the value of x: "))
# print "RESULT"
# print " "
# print "The polynomial given: " + str(f1)
# print "The input given: " + str(input)
# print "The evaluation: " + str(evaluate_poly(f1,input))

# poly = int(raw_input('Enter coefficients of a polynomial in order from highest to lowest: '))

def compute_deriv(origpoly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    assert len(origpoly) > 0
    inpoly = origpoly
    outpoly = ()

    for i in range(1, len(inpoly)):
        outpoly += (i * inpoly[i],)

    return outpoly


poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
print compute_deriv(poly)


# Way to flip a tuple: ex) (1,2,3) to (3,2,1)
# test = (1,2,3,4,5,6,7,8)
# new = ()
# for i in range(0,len(test)):
#     new += (test[-i-1],)
# print new

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    assert len(poly) > 0
    assert epsilon > 0.0

    inpoly = poly
    input = x_0
    result = 0.0
    outpoly = ()
    numiter = 0

    while True:
        result = evaluate_poly(inpoly, input)
        derivpoly = compute_deriv(inpoly)
        derivval = evaluate_poly(derivpoly,input)
        numiter += 1

        # Computing the result without implementing the function
        # for i in range(0,len(inpoly)):
        #     result += inpoly[i] * (input^i)

        if abs(result) <= epsilon:
            outpoly += (input,)
            outpoly += (numiter,)
            return outpoly
        else:
            input = input - (result/derivval)


poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
print compute_root(poly, x_0, epsilon)
