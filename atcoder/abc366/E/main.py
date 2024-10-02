#!/usr/bin/env python3
import sys
from bisect import bisect_right


# bisect, binary-search, manhattan
def main():
    N, D = list(map(int, input().split(" ")))
    X = [0] * N
    Y = [0] * N

    offset = int(2e6)
    max = int(4e6)
    for i in range(N):
        dx, y = list(map(int, input().split(" ")))
        X[i] = dx + offset
        Y[i] = y + offset

    cnt_X = [0] * (max + 1)
    cnt_Y = [0] * (max + 1)
    for i in range(N):
        cnt_X[X[i]] += 1
        cnt_Y[Y[i]] += 1

    def calc(A, cnt_A):
        sum_A = sum(A)
        d_A = [0] * (max + 1)
        cnt = 0
        for a in range(max + 1):
            d_A[a] = sum_A
            cnt += cnt_A[a]
            sum_A += 2 * cnt - N
        return list(filter(lambda a: a <= D, d_A))

    d_X = calc(X, cnt_X)
    d_Y = calc(Y, cnt_Y)

    # print(d_X, d_Y, file=sys.stderr)

    ans = 0
    d_Y.sort()
    for dx in d_X:
        ans += bisect_right(d_Y, D - dx)

    print(ans)


if __name__ == '__main__':
    main()
