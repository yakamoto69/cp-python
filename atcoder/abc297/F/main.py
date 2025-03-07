#!/usr/bin/env python3
import sys
from atcoder.modint import Modint, ModContext

MOD = 998244353  # type: int

class BinomialCoefficients:
    def __init__(self, N: int):
        self.F: list[Modint] = [None] * (N + 1)
        self.I: list[Modint] = [None] * (N + 1)
        self.F[0] = Modint(1)
        self.F[1] = Modint(1)
        for i in range(2, N + 1):
            self.F[i] = self.F[i - 1] * i

        self.I[N] = self.F[N].inv()
        for i in range(N - 1, -1, -1):
            self.I[i] = self.I[i + 1] * (i + 1)

    def __call__(self, n: int, k: int) -> Modint:
        if n < k:
            return Modint(0)
        return self.F[n] * self.I[k] * self.I[n - k]

    # nグループの中からkこ選ぶ
    def H(self, n: int, k: int) -> Modint:
        return self(n + k - 1, k)

def solve(H: int, W: int, K: int):
    if K == 1:
        print(1)
        return

    with ModContext(MOD):
        comb = BinomialCoefficients(H * W + 100)

        dp = [[Modint(0)] * (W + 1) for _ in range(H + 1)]

        def g(h: int, w: int):
            res = comb((h * w) - 1, K - 1)
            print(f'g({h},{w})={res.val()}', file=sys.stderr)
            return res

        def f(h: int, w: int):
            res = g(h, w) + g(h - 1, w - 1) - (g(h, w - 1) + g(h - 1, w))
            print(f'f({h},{w})={res.val()}', file=sys.stderr)
            return res

        for h in range(1, H + 1):
            for w in range(1, W + 1):
                v = f(h, w)
                dp[h][w] = dp[h - 1][w] + dp[h][w - 1] - dp[h - 1][w - 1] + v * h * w
                print((h, w), v.val(), dp[h][w].val(), file=sys.stderr)

        ans = Modint(0)
        for h in range(1, H + 1):
            for w in range(1, W + 1):
                ans += dp[h][w]

        ans *= comb(H*W, K).inv()
        print(ans.val())
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(H, W, K)

if __name__ == '__main__':
    main()
