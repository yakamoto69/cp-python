#!/usr/bin/env python3
import sys


class Tank:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return f"height: {self.height}, width: {self.width}"


# histogram, monotonic_stack
def main():
    N = int(input())
    H = list(map(int, input().split(" ")))
    tanks: list[Tank] = []
    ans = [0] * (N + 1)
    ans[0] = 1
    for i in range(N):
        volume = H[i]
        width = 1
        remove = 0
        for j in range(len(tanks) - 1, -1, -1):
            tank = tanks[j]
            if tank.height <= H[i]:
                volume += (H[i] - tank.height) * tank.width
                width += tank.width
                remove += 1
            else:
                break
        del tanks[len(tanks)-remove:]
        # print(f'remove={remove} tanks={tanks}', file=sys.stderr)
        tanks.append(Tank(H[i], width))
        ans[i + 1] = ans[i] + volume

    print(*ans[1:], sep=' ')


if __name__ == '__main__':
    main()
