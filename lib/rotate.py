# NxN行列を回転する
# ２次元配列を生成したくないときはni, njの計算方法だけコピペして使うこと
# @param d: 反時計回りに回転する。0 => 0°, 1 => 90°, 2 => 180°, 3 => 270°
# @return NxN行列
def rotate(N: int, d: int, grid: list[list[int]]):
    res = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):        
        for j in range(N):
            ni, nj = 0, 0
            if d == 0:
                ni, nj = i, j
            elif d == 1:
                ni, nj = N - j, i
            elif d == 2:
                ni, nj = N - i, N - j
            elif d == 3:
                ni, nj = j, N - i
            res[i][j] = grid[ni][nj]
            
    return res
