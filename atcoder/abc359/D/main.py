#!/usr/bin/env python3
import sys

from atcoder.modint import Modint, ModContext


# dp, bit
def main():
    N, K = list(map(int, input().split(" ")))
    S = input()
    palindromes = [False] * (1 << K)
    for i in range(1 << K):
        yes = True
        for j in range((K + 1) // 2):
            if (i >> j & 1) != (i >> (K - 1 - j) & 1):
                yes = False
        palindromes[i] = yes

    # print(f'palindromes={palindromes}', file=sys.stderr)

    def possible(i):
        nonlocal S
        if S[i] == 'A':
            return [0]
        if S[i] == 'B':
            return [1]
        else:
            return [0, 1]

    mask = (1 << K) - 1


    with ModContext(998244353):
        dp = [[Modint(0) for _ in range(1 << K)] for _ in range(N + 1)]
        dp[0][0] = Modint(1)

        for i in range(N):
            for c in possible(i):
                for s in range(1 << K):
                    ns = (s << 1 & mask) | c

                    # K未満か、回分でなければOK
                    if i < K - 1 or not palindromes[ns]:
                        dp[i + 1][ns] += dp[i][s]

        ans = Modint(0)
        for s in range(1 << K):
            ans += dp[N][s]

        print(ans.val())


if __name__ == '__main__':
    main()
