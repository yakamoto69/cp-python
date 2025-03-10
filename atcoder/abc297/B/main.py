#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    b = []
    k = []
    r = []
    for i in range(len(S)):
        c = S[i]
        if c == "B1":
            b.append(i)
        elif c == "K":
            k.append(i)
        elif c == "R":
            r.append(i)
    cond1 = (b[0] % 2) != (b[1] % 2)
    r0 = min(r)
    r1 = max(r)
    cond2 = r0 < k[0] < r1
    if cond1 and cond2:
        print(YES)
    else:
        print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
