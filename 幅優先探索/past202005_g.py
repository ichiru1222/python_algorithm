from collections import deque

N, X, Y = map(int, input().split())

# 障害物の位置
obstacles = []
for _ in range(N):
    x_o, y_o = map(int, input().split())
    obstacles.append([x_o+201, y_o+201])

# 最小移動回数,未訪問は-1
dist = []
for i in range(403):
    dist.append([-1]*403)

Q = deque()
Q.append([201, 201])
dist[201][201] = 0

# キューを取り出しながら散策
while len(Q):
    i, j = Q.popleft()
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1], [i+1, j+1], [i-1, j+1]]:
        if not (0 <= i2 < 403 and 0 <= j2 < 403):
            continue
        if [i2, j2] in obstacles:
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            Q.append([i2, j2])
print(dist[X+201][Y+201])

