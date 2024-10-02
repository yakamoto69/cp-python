#!/usr/bin/env python3
import sys
from functools import cache


# probability
def main():
    N, A, X, Y = list(map(int, input().split(" ")))

    @cache
    def calc(n):
        if n == 0:
            return 0

        nn = n // A
        use_x = calc(nn) + X
        sigma = 0
        for i in range(2, 7):
            sigma += calc(n // i) / 6
        use_y = (sigma + Y) * 6 / 5
        return min(use_y, use_x)

    ans = calc(N)
    print(f'{ans:.10f}')


if __name__ == '__main__':
    main()
