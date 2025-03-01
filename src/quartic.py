from src.cubic import find_cubic_roots
from src.polynomial import make_polynomial
from src.search import find_root_in_range, search_root_left, search_root_right

epsilon = 0.0000001


def find_quartic_roots(a, b, c, d, e):
    """If P(x) is a quartic polynomial of the form
    P(x) = ax^4 + bx^3 + cx^2 + dx + e,
    then it has up to 4 roots.  I.e., there are at most 4 real numbers, x
    for which p(x) = 0.
    The goal of this function, find_quartic_roots, is to return a sorted list
    of as many of those roots as possible.
    """
    if abs(a) < epsilon:
        # Since a=0, then the polynomial can be solved by the previous solution in cubic.py.
        # The student should insert a return and function call to the previously defined
        # function with the correct coefficients of the cubic polynomial.
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    if a < 0:
        # Since the leading coefficient of P(x) = ax^4 + bx^3 + cx^2 + dx + e,
        # is negative, we instead want to compute the roots of -P(x) = -ax^4 - bx^3 - cx^2 - dx - e.
        # We need to make a recursive call with the arguments negated.
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    def find_one_root():
        if abs(e) < epsilon:
            # if e=0 (or very close to zero), then x is a factor of the polynomial
            # and consequently 0 is a root.
            # return the root zero.
            # CHALLENGE: student must complete the implementation.
            # HINT: goal = 1 line of code
            raise NotImplementedError()

        P = make_polynomial([a, b, c, d, e])
        if e < 0:
            # if e < 0, then P(0) = e < 0, therefore
            # there is a root to the right of x=0,
            # and a root to the left of x=0.
            # use the function search_root_right or search_root_right
            # to find and return it.
            # CHALLENGE: student must complete the implementation.
            # HINT: goal = 1 line of code
            raise NotImplementedError()

        ips = (
            # The derivative of a degree 4 polynomial is a degree 3 polynomial.
            # The roots of the degree 3 tells us the inflection points of the
            # degree 4 polynomial.
            # Here the goal is to compute the roots of the degree 3 (cubic)
            # polynomial using functions developed earlier in cubic.py
            # Recall the derivative of ax^4 + bx^3 + cx^2 + dx +e
            #  = 4ax^3 + 3bx^2 + 2cx + d
            #
            # CHALLENGE: student must complete the implementation.
            # HINT: goal = 1 line of code
            raise NotImplementedError()

        )

        for ip in ips:
            # if the polynomial is 0 at one of the inflection points,
            # then the inflection point is the root, return it.
            # CHALLENGE: student must complete the implementation.
            # HINT: goal <= 2 lines of code
            raise NotImplementedError()

        for ip in ips:
            if P(ip) < 0:
                # if the polynomial is negative at one of the inflection points,
                # then there is a root to the right (and also to the left)
                # use the search_root_right or search_root_left function
                # to approximate it and return that approximated root.
                # CHALLENGE: student must complete the implementation.
                # HINT: goal = 1 line of code
                raise NotImplementedError()

    r = find_one_root()

    A = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for A?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    B = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for B?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    C = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for C?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    D = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for D?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    return [r] + find_cubic_roots(A, B, C, D)
