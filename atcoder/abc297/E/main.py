#!/usr/bin/env python3
import heapq
import sys


def solve(N: int, K: int, A: "List[int]"):
    A.sort()
    heap = [0]
    visit = set()
    K += 1
    while True:
        u = heapq.heappop(heap)
        if u not in visit:
            visit.add(u)
            for a in A:
                heapq.heappush(heap, u + a)
            K -= 1
            if K == 0:
                print(u)
                return
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
