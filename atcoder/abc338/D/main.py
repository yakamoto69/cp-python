#!/usr/bin/env python3
import sys

# imos, 回転
def main():
    N, M = list(map(int, input().split(" ")))
    X = list(map(int, input().split(" ")))
    for i in range(M):
        X[i] -= 1

    cost2 = [0] * (2 * N + 1)  # i - (i + 1)%N への道。回転を考慮するのが難しいので２倍で確保する

    best = 0

    # clockwiseで進む
    def add_penalty(penalty, origin, dest):
        dest2 = dest if dest > origin else dest + N
        cost2[origin] += penalty
        cost2[dest2] -= penalty

    for i in range(M - 1):
        clockwise = (N + X[i + 1] - X[i]) % N
        counter_clockwise = (N + X[i] - X[i + 1]) % N
        if clockwise < counter_clockwise:
            add_penalty(counter_clockwise - clockwise, X[i], X[i + 1]) # clockwiseが安い => clockwiseのルートにpenaltyを追加する

        elif clockwise > counter_clockwise:
            add_penalty(clockwise - counter_clockwise, X[i + 1], X[i])

        # 同じ場合はpenaltyなし

        best += min(clockwise, counter_clockwise)

    # imos
    for i in range(2 * N):
        cost2[i + 1] += cost2[i]

    # costはcost2をmodしたものと考えられる
    cost = [0] * N
    for i in range(2 * N):
        cost[i % N] += cost2[i]

    ans = best + min(cost)
    print(ans)

if __name__ == '__main__':
    main()
