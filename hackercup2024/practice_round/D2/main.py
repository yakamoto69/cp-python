import sys


input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        N, G = list(map(int, input().split(" ")))
        E = [int(input()) for _ in range(N)]

        # treeを使う必要がない
        res = []
        offset = 0
        for i in range(N):
            res.append(E[i] + offset)
            offset += 1
        res.sort()
        # print(f'res={res}', file=sys.stderr)
        positions = []
        for i in range(N):
            positions.append(res[i] - offset + i + 1)
        # print(f'positions={positions}', file=sys.stderr)

        MAX = int(2e6)
        cnt = [0] * (MAX + 1)
        for i in range(N):
            cnt[positions[i]] += 1

        cnt_sum = [0] * (MAX + 1)
        for i in range(MAX):
            cnt_sum[i + 1] = cnt_sum[i] + cnt[i + 1]

        ans = min([abs(position - G) for position in positions])

        # Gの右側にclosestがあるときはそちらを優先する
        if cnt[G + ans] > 0:
            idx = N - cnt_sum[G + ans] + 1
        else:
            idx = N - cnt_sum[G - ans] + 1

        print(f'Case #{t+1}: {idx} {ans}')


if __name__ == '__main__':
    main()
