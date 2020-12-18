from math import sqrt


def find_roots(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    k = float(b * b - 4 * a * c)
    if k >= 0:
        sk = sqrt(k)
        x1 = (-b + sk) / (2 * a)
        x2 = (-b - sk) / (2 * a)
        x = (x1, x2)
    else:
        pass

    return x


print(find_roots(2, 10, 8));