import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__math_code = """
import typing


def _is_prime(n: int) -> bool:
    '''
    Reference:
    M. Forisek and J. Jancina,
    Fast Primality Testing for Integers That Fit into a Machine Word
    '''

    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in (2, 7, 61):
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)


def _primitive_root(m: int) -> int:
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                break
        else:
            return g
        g += 1
"""

atcoder._math = types.ModuleType('atcoder._math')
exec(_atcoder__math_code, atcoder._math.__dict__)


_atcoder_modint_code = """
import typing

# import atcoder._math


class ModContext:
    context: typing.List[int] = []

    def __init__(self, mod: int) -> None:
        assert 1 <= mod

        self.mod = mod

    def __enter__(self) -> None:
        self.context.append(self.mod)

    def __exit__(self, exc_type: typing.Any, exc_value: typing.Any,
                 traceback: typing.Any) -> None:
        self.context.pop()

    @classmethod
    def get_mod(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._mod = ModContext.get_mod()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self._mod

    def mod(self) -> int:
        return self._mod

    def val(self) -> int:
        return self._v

    def __iadd__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v += rhs._v
        else:
            self._v += rhs
        if self._v >= self._mod:
            self._v -= self._mod
        return self

    def __isub__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v -= rhs._v
        else:
            self._v -= rhs
        if self._v < 0:
            self._v += self._mod
        return self

    def __imul__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            self._v = self._v * rhs._v % self._mod
        else:
            self._v = self._v * rhs % self._mod
        return self

    def __ifloordiv__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        self._v = self._v * inv % self._mod
        return self

    def __pos__(self) -> 'Modint':
        return self

    def __neg__(self) -> 'Modint':
        return Modint() - self

    def __pow__(self, n: int) -> 'Modint':
        assert 0 <= n

        return Modint(pow(self._v, n, self._mod))

    def inv(self) -> 'Modint':
        eg = atcoder._math._inv_gcd(self._v, self._mod)

        assert eg[0] == 1

        return Modint(eg[1])

    def __add__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            result = self._v + rhs._v
            if result >= self._mod:
                result -= self._mod
            return raw(result)
        else:
            return Modint(self._v + rhs)

    def __sub__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            result = self._v - rhs._v
            if result < 0:
                result += self._mod
            return raw(result)
        else:
            return Modint(self._v - rhs)

    def __mul__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            return Modint(self._v * rhs._v)
        else:
            return Modint(self._v * rhs)

    def __floordiv__(self, rhs: typing.Union['Modint', int]) -> 'Modint':
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = atcoder._math._inv_gcd(rhs, self._mod)[1]
        return Modint(self._v * inv)

    def __eq__(self, rhs: typing.Union['Modint', int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v == rhs._v
        else:
            return self._v == rhs

    def __ne__(self, rhs: typing.Union['Modint', int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v != rhs._v
        else:
            return self._v != rhs


def raw(v: int) -> Modint:
    x = Modint()
    x._v = v
    return x
"""

atcoder.modint = types.ModuleType('atcoder.modint')
atcoder.modint.__dict__['atcoder'] = atcoder
atcoder.modint.__dict__['atcoder._math'] = atcoder._math
exec(_atcoder_modint_code, atcoder.modint.__dict__)
Modint = atcoder.modint.Modint

ModContext = atcoder.modint.ModContext

#!/usr/bin/env python3
import sys
# from atcoder.modint import Modint, ModContext

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


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    g = [[False for _ in range(2*N)] for _ in range(2*N)]
    for i in range(M):
        u, v = A[i] - 1, B[i] - 1
        g[u][v] = True

    with ModContext(MOD):
        comb = BinomialCoefficients(2 * N)

        dp = [[Modint(0) for r in range(2*N + 1)] for l in range(2*N + 1)]
        for i in range(2*N + 1):
            dp[i][i] += 1

        for len in range(2, 2*N + 1, 2):
            for l in range(2*N - len + 1):
                r = l + len
                # print(l, r, file=sys.stderr)
                for k in range(l + 1, r, 2):
                    if not g[l][k]:
                        continue

                    a = (k - (l + 1)) // 2 + 1
                    b = (r - (k + 1)) // 2
                    # print("l r k", l, r, k, a, b, file=sys.stderr)
                    # print("dp", dp[l + 1][k].val(), dp[k + 1][r].val(), comb(a + b, a).val(), file=sys.stderr)
                    dp[l][r] += dp[l + 1][k] * dp[k + 1][r] * comb(a + b, a)
        print(dp[0][2*N].val())

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
