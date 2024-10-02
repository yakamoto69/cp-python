#!/usr/bin/env python3
import sys

MOD = 998244353


# bin_coef, dp, GPT
# TLEが出たからChat-GPTに任せたらModint使わないバージョンになって速くなった
# 1000万オブジェクト生成は無謀だったか
def main():
    K = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    N_LETTERS = 26
    MAX_N = 2 * K + N_LETTERS  # H(n, k)で必要な最大値

    # 階乗と逆元の前計算
    fact = [1] * (MAX_N + 1)
    for i in range(1, MAX_N + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (MAX_N + 1)
    inv_fact[MAX_N] = pow(fact[MAX_N], MOD - 2, MOD)
    for i in range(MAX_N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def comb(n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    # H(n, k)の前計算
    MAX_H_N = K + N_LETTERS + 1
    MAX_H_K = K
    H = [[0] * (MAX_H_K + 1) for _ in range(MAX_H_N)]
    for n in range(MAX_H_N):
        for k in range(MAX_H_K + 1):
            H[n][k] = comb(n + k - 1, k) if n + k - 1 >= 0 else 0

    dp = [ [0] * (K + 1) for _ in range(N_LETTERS + 1) ]
    dp[0][0] = 1

    for i in range(N_LETTERS):
        Ci = C[i]
        for s0 in range(K + 1):
            val = dp[i][s0]
            if val == 0:
                continue
            max_use = min(K - s0, Ci)
            for use in range(0, max_use + 1):
                s1 = s0 + use
                coef = H[s0 + 1][use]
                dp[i + 1][s1] = (dp[i + 1][s1] + val * coef) % MOD

    ans = sum(dp[N_LETTERS][1:]) % MOD
    print(ans)

if __name__ == '__main__':
    main()
