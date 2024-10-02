#!/usr/bin/env python3
import sys

# digit_dp, 桁DP
def main():
    S = list(map(lambda x: ord(x) - ord('0'), input()))
    N = len(S)
    # TODO 戻す
    MAX = 150 # 14 * 9だけど適当に多めに取る

    ans = 0

    # 最終的な桁和を固定する
    for mod in range(1, MAX):
        dp = [[[[0] * 2 for _ in range(mod)] for _ in range(mod + 1)] for _ in range(N + 1)]  # (i, digit sum, sum, less)
        dp[0][0][0][0] = 1

        for i in range(N):
            for j in range(mod + 1):
                for k in range(mod):
                    for less in range(2):
                        if dp[i][j][k][less] == 0:
                            continue

                        for digit in range(10 if less == 1 else S[i] + 1):
                            nj = j + digit
                            if nj > mod:
                                continue

                            nk = (k * 10 + digit) % mod
                            nless = less | (digit < S[i])

                            dp[i + 1][nj][nk][nless] += dp[i][j][k][less]

        ans += sum(dp[N][mod][0])
    print(ans)


if __name__ == '__main__':
    main()
