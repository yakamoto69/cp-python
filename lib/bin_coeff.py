from atcoder.modint import Modint


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
