#!/usr/bin/env python3
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# priority_queue
def main():
    H, W, Y = list(map(int, input().split(" ")))
    grid = [list(map(int, input().split(" "))) for _ in range(H)]
    dry = [[True] * W for _ in range(H)]
    heap = []

    for h in range(H):
        for w in range(W):
            if h == 0 or h == H - 1 or w == 0 or w == W - 1:
                dry[h][w] = False
                heappush(heap, ((grid[h][w] << 32) + (h << 16) + w))

    D = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    ans = H * W
    mask = ((1 << 16) - 1)
    for y in range(1, Y + 1):
        while heap and (heap[0] >> 32) <= y:
            ans -= 1
            v = heappop(heap)
            h = v >> 16 & mask
            w = v & mask
            for dh, dw in D:
                nh = dh + h
                nw = dw + w
                if 0 <= nh < H and 0 <= nw < W:
                    if dry[nh][nw]:
                        dry[nh][nw] = False
                        heappush(heap, ((grid[nh][nw] << 32) + (nh << 16) + nw))

        print(ans)



if __name__ == '__main__':
    main()
