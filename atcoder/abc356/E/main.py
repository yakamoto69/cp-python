#!/usr/bin/env python3
import sys


# sum
def main():
    _ = int(input())
    A = list(map(int, input().split(" ")))
    A.sort()

    MAX = int(1e6)
    cnt_sum = [0] * (MAX * 2 + 1)
    cnt = [0] * (MAX + 1)

    for a in A:
        cnt[a] += 1

    for i in range(1, len(cnt_sum)):
        cnt_sum[i] += cnt_sum[i - 1] + (cnt[i] if i <= MAX else 0)

    # print(f'cnt_sum={cnt_sum}', file=sys.stderr)

    ans = 0
    for a in range(1, MAX + 1):
        b = a
        c = 1
        if cnt[a] == 0:
            continue

        while b <= MAX:
            cnt_b = cnt_sum[b + a - 1] - cnt_sum[b - 1]
            v = cnt_b * c * cnt[a]
            # print(f'(a, b)=({a},{b}) v={v}', file=sys.stderr)
            ans += v
            b += a
            c += 1

    # n*(n-1)/2 であるところがn*nになっているので、調整する
    for i in range(len(cnt)):
        n = cnt[i]
        # print(f'n={n}', file=sys.stderr)
        ans -= n*n - (n*(n-1)//2)

    print(ans)

if __name__ == '__main__':
    main()
