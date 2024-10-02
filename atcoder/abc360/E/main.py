#!/usr/bin/env python3
import sys

from atcoder.modint import Modint, ModContext


def main():
    N, K = list(map(int, input().split(" ")))
    with (((ModContext(998244353)))):
        dp = [[Modint(0)] * 2 for _ in range(K + 1)]
        dp[0][0] = Modint(1)
        inv_n = Modint(N).inv()
        all = inv_n * inv_n  # 全事象
        not_select = all * (N - 1) * (N - 1)

        for i in range(K):
            dp[i + 1][0] = dp[i][0] * (not_select + Modint(1) * 1 * all)
            + dp[i][1] * Modint(1) * 2 * all

            dp[i + 1][1] = dp[i][0] * Modint(1) * (N - 1) * 2 * all
            + dp[i][1] * (not_select + Modint(1) * (N - 1) * 2 * all)

        sum_after1 = Modint(N) * Modint(N + 1) // 2 - Modint(1)
        ans = (Modint(1) * dp[K][0] + sum_after1 * dp[K][1]) * inv_n
        print(ans.val())

if __name__ == '__main__':
    main()
