#!/usr/bin/env python3
import sys

MOD = 998244353

# dp, mod
def main():
    N = int(input())
    A = list(map(int, input().split(" ")))
    to_idx = dict()
    inf = int(1e12) # 幅1のときのdiff
    to_value = [inf]
    for i in range(N):
        for j in range(i):
            d = A[i] - A[j]
            if d not in to_idx:
                to_idx[d] = len(to_idx)
                to_value.append(d)

    # print(f'to_idx={to_idx}', file=sys.stderr)
    # print(f'to_value={to_value}', file=sys.stderr)

    M = len(to_value)
    dp = [[[0 for _ in range(M)] for _ in range(N + 1)] for _ in range(N)] # (i, 個数, idx)

    for i in range(N):
        # 幅=1
        dp[i][1][0] = 1
        for j in range(i):
            for n in range(1, j + 2):
                diff = A[i] - A[j]
                idx = to_idx[diff]
                if n == 1:
                    dp[i][n + 1][idx] = (dp[i][n + 1][idx] + dp[j][1][0]) % MOD
                else:
                    dp[i][n + 1][idx] = (dp[i][n + 1][idx] + dp[j][n][idx]) % MOD

    ans = [0 for _ in range(N)]
    for i in range(N):
        for n in range(N):
            ans[n] = (ans[n] + sum(dp[i][n + 1])) % MOD
    print(*ans, sep=' ')

if __name__ == '__main__':
    main()
