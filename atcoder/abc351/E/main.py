#!/usr/bin/env python3
import sys


# マンハッタン距離, manhattan_distance
def main():
    N0 = int(input())
    X = [-1] * N0
    Y = [-1] * N0
    for i in range(N0):
        x, y = list(map(int, input().split(" ")))
        X[i] = x
        Y[i] = y

    def calc1(V):
        n = len(V)
        V.sort()
        sum = 0
        cnt = 0
        res = 0
        for i in range(n):
            res += cnt * V[i] - sum
            sum += V[i]
            cnt += 1
        # print(f'V={V} res={res}', file=sys.stderr)
        return res

    def calc2(A, B):
        return calc1(A) + calc1(B)

    def calc():
        A0, B0 = [], []
        A1, B1 = [], []
        for i in range(N0):
            if (X[i] + Y[i]) % 2 == 0:
                A0.append(X[i] + Y[i])
                B0.append(X[i] - Y[i])
            else:
                A1.append(X[i] + Y[i])
                B1.append(X[i] - Y[i])
        return calc2(A0, B0) + calc2(A1, B1)

    print(calc() // 2)




if __name__ == '__main__':
    main()
