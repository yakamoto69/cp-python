#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    [N, Q] = list(map(int, input().split()))
    i = 0
    j = 0
    called = [False] * N
    for q in range(Q):
        line = list(map(int, input().split()))
        type = line[0]
        if type == 1:
            i += 1
        elif type == 2:
            x = line[1] - 1
            called[x] = True
        else:
            while called[j]:
                j += 1
            print(j + 1)

    pass

if __name__ == '__main__':
    main()
