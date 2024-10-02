import sys
input = sys.stdin.readline


def main():
    T =  int(input())
    for t in range(T):
        A, B, C = list(map(int, input().split()))
        all_single = C // A
        all_double = (C // B) * 2 - 1  # ダブルが安い時、最後の一個にシングルの代わりにダブルを使う
        D = (C - A) // B  # シングル１個分を確保して、できるだけダブルで
        S = (C - B * D) // A
        assert(S > 0)
        assert(A * S + B * D <= C)
        almost_double = D * 2 + S
        ans = max(max(all_single, all_double), almost_double)
        print(f'Case #{t+1}: {ans}')


if __name__ == '__main__':
    main()