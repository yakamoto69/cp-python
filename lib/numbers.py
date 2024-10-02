# 約数を昇順で返す
# O(sqrt(N))時間かかるので、１回だけなら10^12ぐらいまで大丈夫
def find_divisers(x: int) -> [int]:
    divisers = []
    post = []
    d = 1
    while d * d <= x:
        if x % d == 0:
            divisers.append(d)
            if d * d != x:
                post.append(x // d)
        d += 1

    for i in range(len(post) - 1, -1, -1):
        divisers.append(post[i])
    return divisers
