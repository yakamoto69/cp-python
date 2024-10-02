import sys


input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        N, G = list(map(int, input().split(" ")))
        E = [int(input()) for _ in range(N)]
        MAX = int(1e6)
        cnt = [0] * (MAX + 1)
        for i in range(N):
            cnt[E[i]] += 1

        cnt_sum = [0] * (MAX + 1)
        for i in range(MAX):
            cnt_sum[i + 1] = cnt_sum[i] + cnt[i + 1]

        ans = min([abs(e - G) for e in E])

        # Gの右側にclosestがあるときはそちらを優先する
        if cnt[G + ans] > 0:
            idx = N - cnt_sum[G + ans] + 1
        else:
            idx = N - cnt_sum[G - ans] + 1

        print(f'Case #{t+1}: {idx} {ans}')


if __name__ == '__main__':
    main()
