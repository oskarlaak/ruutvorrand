def quadratic_formula(a, b, c):
    if a == 0:
        return False
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return False
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            return x1, x2