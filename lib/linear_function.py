from math import gcd


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x ^ self.y

    def __str__(self):
        return f'({self.x},{self.y})'


class LinearFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __hash__(self):
        return self.a ^ self.b ^ self.c

    def __str__(self):
        return f'({self.a},{self.b},{self.c})'

# Y = b/a・X + c/a の形式の１次関数
# Y軸に並行な場合は a=0, b=1, c=X
# X軸に並行な場合は a=1, b=0, c=Y
# 同じ点については考慮する必要がない
# a >= 0
def calc_linear_function(x1, y1, x2, y2) -> LinearFunction:
    a = x1 - x2
    b = y1 - y2
    if a < 0:
        a *= -1
        b *= -1

    if a != 0 and b != 0:
        d = gcd(a, b)
        a //= d
        b //= d
        c = y1 * a - x1 * b
        return LinearFunction(a, b, c)
    else:
        if a == 0:
            return LinearFunction(0, 1, x1)
        else:
            return LinearFunction(1, 0, y1)
