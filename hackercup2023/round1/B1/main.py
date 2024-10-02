import sys
input = sys.stdin.readline


def calc(P, S, p0, stack, i, ans):
    if S == 0 and P == 1:
        if ans is None or len(ans) > i:
            return stack[:i]
        else:
            return ans
    for p in range(p0, S + 1):
        if P % p == 0:
            stack[i] = p
            ans = calc(P // p, S - p, p, stack, i + 1, ans)

    return ans


def main():
    T = int(input())
    for test_num in range(T):
        P = int(input())
        stack = [0] * 42
        ans = calc(P, 41, 1, stack, 0, None)
        if ans is None:
            print(f'Case #{test_num + 1}: -1')
        else:
            print(f'Case #{test_num + 1}: {len(ans)}', end=' ')
            print(*ans)


if __name__ == '__main__':
    main()