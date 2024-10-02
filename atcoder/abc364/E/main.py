#!/usr/bin/env python3
import sys


# dp
def main():
    N, X, Y = list(map(int, input().split(" ")))
    A = [-1] * N
    B = [-1] * N
    for i in range(N):
        a, b = list(map(int, input().split(" ")))
        A[i] = a
        B[i] = b

    inf = int(1e18)
    cur = [[inf] * (N + 1) for _ in range(X + 1)]
    next = [[inf] * (N + 1) for _ in range(X + 1)]
    cur[0][0] = 0

    ans = 0
    for i in range(N):
        for x in range(X + 1):
            for j in range(N + 1):
                next[x][j] = cur[x][j]

        for x in range(X + 1):
            for j in range(i + 1):
                if cur[x][j] == inf:
                    continue
                nx = x + A[i]
                ny = cur[x][j] + B[i]
                # print(i, x, j, nx, ny, file=sys.stderr)
                if nx <= X and ny <= Y:
                    # print(i, x, j, nx, ny, file=sys.stderr)
                    next[nx][j + 1] = min(next[nx][j + 1], ny)
                    ans = max(ans, j + 1)

        # print(f'next={next}', file=sys.stderr)
        cur, next = next, cur

    ans = min(ans + 1, N)
    print(ans)

if __name__ == '__main__':
    main()
