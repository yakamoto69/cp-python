#!/usr/bin/env python3
import sys
import heapq


# priority_queue, greedy
def main():
    N = int(input())
    A = list(map(int, input().split(" ")))
    D = [1] * N
    heap = []
    for i in range(N):
        heapq.heappush(heap, (A[i] * (2 * D[i] + 1), i))

    remain = 2 * (N - 1) - N

    while remain > 0:
        remain -= 1
        _, i = heapq.heappop(heap)
        D[i] += 1
        heapq.heappush(heap, (A[i] * (2 * D[i] + 1), i))

    # print(f'D={D}', file=sys.stderr)

    ans = 0
    for i in range(N):
        ans += A[i] * D[i] * D[i]
    print(ans)

if __name__ == '__main__':
    main()
