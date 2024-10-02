#!/usr/bin/env python3
import sys


# functional_graph, directed_graph
def main():
    N = int(input())
    F = list(map(lambda x: x - 1, map(int, input().split(" "))))

    visited = [False] * N
    cnt = [0] * N

    # dfs相当の処理をループでやるよ
    # 関数グラフなので終端がcycleで処理が楽 => visitedを0, 1, 2の３状態で管理する必要がない
    def dfs(u):
        # print(f'dfs({u})', file=sys.stderr)
        visited[u] = True
        route = [u]
        while not visited[F[u]]:
            v = F[u]
            route.append(v)
            visited[v] = True
            u = v

        # print(f'route={route}', file=sys.stderr)

        def reverse_route(len):
            for i in range(len - 1, -1, -1):
                u = route[i]
                v = F[u]
                cnt[u] = cnt[v] + 1 # v以降はすでに処理されている

        # routeがcycleを含むケース
        if F[u] in route:
            # cycle部分の処理
            s_cycle = route.index(F[u])
            len_cycle = len(route) - s_cycle
            for i in range(s_cycle, len(route)):
                u = route[i]
                cnt[u] = len_cycle

            # cycle以外の処理
            reverse_route(len(route) - len_cycle)

        # cycleを処理済みのケース
        else:
            reverse_route(len(route))

    for v in range(N):
        if not visited[v]:
            dfs(v)
            # print(f'cnt={cnt}', file=sys.stderr)

    ans = sum(cnt)
    print(ans)


if __name__ == '__main__':
    main()
