#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", k: "List[int]"):
    return


# Generated by 2.14.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    k = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        b[i] = int(next(tokens))
        k[i] = int(next(tokens))
    solve(N, Q, a, b, k)

if __name__ == '__main__':
    main()
