#!/usr/bin/env python3
import sys
import math
from functools import partial


def binary_search_monotonic(func, low, high, decr=False):
    if not decr:
        low -= 1
    else:
        high += 1
    while high - low > 1:
        mid = (low + high) // 2
        if func(mid) ^ decr:
            high = mid
        else:
            low = mid
    return high if not decr else low


# bin_search, divider_inclusion_exclusion
def main():
    N = int(input())
    # primes = []
    # is_prime = [True] * (65)
    # is_prime[0] = False
    # is_prime[1] = False
    # for i in range(2, 65):
    #     if is_prime[i]:
    #         primes.append(i)
    #         x = 2 * i
    #         while x <= 64:
    #             is_prime[x] = False
    #             x += i

    # print(f'primes={primes}', file=sys.stderr)
    # print(f'is_prime={is_prime}', file=sys.stderr)

    # ans = 1  # 1の分
    # for i in range(2, 64):
    #     if is_prime[i]:
    #         v = math.floor(math.pow(N, 1 / i)) - 1
    #         print(f'i={i} v={v}', file=sys.stderr)
    #         ans += v

    coeff = [1] * 65
    for i in range(2, 65):
        x = i * 2
        while x <= 64:
            coeff[x] -= coeff[i]
            x += i

    # print(f'coeff={coeff}', file=sys.stderr)

    def f(x, i):
        return pow(x, i) <= N

    ans = 1  # 1の分
    for i in range(2, 64):
        x = binary_search_monotonic(partial(f, i=i), 1, int(1e9), decr=True)
        v = (x - 1) * coeff[i]
        # print(f'i={i} v={v}', file=sys.stderr)
        ans += v

    print(ans)

if __name__ == '__main__':
    main()
