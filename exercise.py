from math import sqrt


def quadraticSolver(a, b, c):
    """
    A simple function that uses the quadratic formula to compute the root of quadratic equations. Zero Division Error is also handled (Brownie expected! :-)
    param: a, b, c (int | float) - Inputs provided by the user
    return msg (list) - A list of the roots
    """
    try:
        if a == 0:
            raise ZeroDivisionError('zero divison error')
        else:
            root1 = (-b + sqrt((b*b) - (4 * a * c))) / 2*a
            root2 = (-b - sqrt((b*b) - (4 * a * c))) / 2*a
            msg = [root1, root2]
    except Exception as err:
        msg = f"An Error Occured: {err}".title()
    finally:
        return msg

a = 1
b = -2
c = -4

print(quadraticSolver(a, b, c))



