import sys
from math import gcd
import random
from collections import Counter

input = sys.stdin.readline

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

def main():
    T =  int(input())
    for t in range(T):
        N = int(input())
        C = []
        for _ in range(N):
            x, y = list(map(int, input().split(" ")))
            C.append(Coordinate(x, y))

        n = min(N, 1000)
        samples = random.sample(C, n)
        fn_to_coord = {}
        cnt = Counter()

        for i in range(n):
            for j in range(n - 1):
                fn = calc_linear_function(samples[i].x, samples[i].y, samples[j].x, samples[j].y)
                cnt[fn] += 1
                fn_to_coord[fn] = samples[i]

        most_common: LinearFunction = cnt.most_common()[0][0]
        # print(f'most_common={most_common}', file=sys.stderr)
        base = fn_to_coord[most_common]
        cnt_same_as_most_common = 0
        for c in C:
            if c == base:
                cnt_same_as_most_common += 1
            else:
                fn = calc_linear_function(c.x, c.y, base.x, base.y)
                if fn == most_common:
                    cnt_same_as_most_common += 1

        estimate = (N - cnt_same_as_most_common)
        # print(f'cnt_same_as_most_common={cnt_same_as_most_common} estimate={estimate}', file=sys.stderr)

        ans = min(N, estimate * 3 // 2)
        print(f'Case #{t+1}: {ans}')


if __name__ == '__main__':
    main()
