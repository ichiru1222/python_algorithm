# 幅優先探索
from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

S = []
for i in range(R):
    s = input()
    S.append(s)

# 1始まりを0始まりに直す
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# 始点からの最小移動回数を管理する２次元配列
# -1 は未訪問
dist = []
for i in range(R):
    dist.append([-1]*C)

# キューに始点を入れる
Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

# キューを取り出しながら探索
while len(Q) > 0:
    i, j = Q.popleft()
    # 4つの隣マスを確認
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # 盤面の範囲外であれば無視
        if not (0 <= i2 < R and 0 <= j2 < C):
            continue
        # 壁マスであれば無視
        if S[i][j] == "#":
            continue
        # もし未訪問であれば、距離を更新してキューにいれる
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])
print(dist[gy][gx])

