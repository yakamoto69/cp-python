#!/usr/bin/env python3
import sys


# math, dp
def main():
    N, K = list(map(int, input().split(" ")))
    A = [0] * N
    B = [0] * N

    for i in range(N):
        a, b = list(map(int, input().split(" ")))
        A[i] = a
        B[i] = b

    I = [i for i in range(N)]
    I.sort(key=lambda i: (A[i] - 1) / B[i]) # 小数点が気になるが数値が小さいから大丈夫だろう
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            if dp[i][j] == 0:
                continue

            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j < K:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] * A[I[i]] + B[I[i]])

    ans = dp[N][K]
    print(ans)

if __name__ == '__main__':
    main()
