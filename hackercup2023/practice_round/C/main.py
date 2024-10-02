import sys
input = sys.stdin.readline


def calc_candidate(cand0, cand1):
    if cand0 == 0:
        assert (cand1 != 0)
        return cand1
    elif cand1 == 0:
        assert (cand0 != 0)
        return cand0
    else:
        return cand0 if cand0 == cand1 else -1


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        if N == 1:
            print(f'Case #{t + 1}: 1')
            continue
        A.sort()

        inf = 1e18
        ans = inf
        outer = [0] * N
        for i in range(N - 1):  # [0, N - 1)
            outer[i] = A[i] + A[-1 - i]
            if i > 0 and outer[i] != outer[i - 1]:
                outer[i] = -1
                
        inner_minus = [0] * N
        for i in reversed(range(N - 1)):  # [0, N - 1)
            inner_minus[i] = A[i] + A[-1 - i - 1]
            if i < N - 1 and inner_minus[i] != inner_minus[i + 1]:
                inner_minus[i] = -1
                
        inner_plus = [0] * N
        for i in reversed(range(1, N)):  # [1, N)
            inner_plus[i] = A[i] + A[-1 - i + 1]
            if i < N - 1 and inner_plus[i] != inner_plus[i + 1]:
                inner_plus[i] = -1

        # print(f'outer: {outer} inner_minus: {inner_minus} inner_plus: {inner_plus}', file=sys.stderr)

        for i in range(N):
            # iを買う
            cand0 = outer[i - 1] if i > 0 else 0
            cand1 = inner_minus[i] if i < N - 1 else 0
            candidate = calc_candidate(cand0, cand1)
            pair = A[-1 - i]
            if candidate != -1 and candidate - pair > 0:
                # print(f'case1(i={i}) candidate: {candidate}, pair: {pair}', file=sys.stderr)
                ans = min(ans, candidate - pair)

            # -1 - i を買う
            cand0 = outer[i - 1] if i > 0 else 0
            cand1 = inner_plus[i + 1] if i < N - 1 else 0
            candidate = calc_candidate(cand0, cand1)

            pair = A[i]
            if candidate != -1 and candidate - pair > 0:
                # print(f'case2(i={i}) candidate: {candidate}, pair: {pair}', file=sys.stderr)
                ans = min(ans, candidate - pair)

        ans = -1 if ans == inf else ans
        print(f'Case #{t + 1}: {ans}')

if __name__ == '__main__':
    main()