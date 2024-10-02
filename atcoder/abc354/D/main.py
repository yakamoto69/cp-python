#!/usr/bin/env python3
import sys


# mod
def main():
    A, B, C, D = list(map(int, input().split(" ")))
    C -= 1
    D -= 1
    black = [
        [2, 1, 0, 1],
        [1, 2, 1, 0],
        [2, 1, 0, 1],
        [1, 2, 1, 0]
    ]

    def find_after(x, i):
        for j in range(4):
            if (x + j) % 4 == i:
                return x + j

    def find_before(x, i):
        for j in range(4):
            if (x - j) % 4 == i:
                return x - j

    def cnt(i, j):
        a = find_after(A, j)
        c = find_before(C, j)
        b = find_after(B, i)
        d = find_before(D, i)
        # print(f'i,j={i},{j} a={a} b={b} c={c}, d={d}', file=sys.stderr)
        if a > c or b > d:
            return 0
        width = (c - a) // 4 + 1
        height = (d - b) // 4 + 1
        return width * height * black[i][j]

    ans = sum([cnt(i, j) for j in range(4) for i in range(4)])
    print(ans)


if __name__ == '__main__':
    main()
