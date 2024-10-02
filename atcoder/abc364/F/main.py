#!/usr/bin/env python3
import sys
from sortedcontainers import SortedSet


# tree, binary-search
def main():
    N, Q = list(map(int, input().split(" ")))
    queries = [list(map(int, input().split(" "))) for _ in range(Q)]
    tree = SortedSet([i + 1 for i in range(N)])
    queries.sort(key=lambda x: x[2])
    # print(f'queries={queries}', file=sys.stderr)
    ans = 0
    for q in queries:
        l, r, c = q
        cur = r
        prev_segment = None
        while cur >= l:
            idx = tree.bisect_right(cur)
            if idx == 0:
                break
            segment = tree[idx - 1]
            # print(f'segment={segment} prev_segment={prev_segment} idx={idx} q={q}', file=sys.stderr)
            if prev_segment is not None:
                tree.remove(prev_segment)
            ans += c
            prev_segment = segment
            cur = segment - 1
    ans = ans if len(tree) == 1 else -1
    print(ans)


if __name__ == '__main__':
    main()
