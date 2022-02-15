"""
問題のリンク
https://atcoder.jp/contests/atc001/tasks/dfs_a



高橋君の住む街は長方形の形をしており、格子状の区画に区切られています。 長方形の各辺は東西及び南北に並行です。 各区画は道または塀のどちらかであり、高橋君は道を東西南北に移動できますが斜めには移動できません。 また、塀の区画は通ることができません。

高橋君が、塀を壊したりすることなく道を通って魚屋にたどり着けるかどうか判定してください。


"""
import sys
sys.setrecursionlimit(10**7) # 再帰回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w

def dfs(x, y):
    # 範囲外 or 壁ならば終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == "#":
        return
    # ゴールなら終了
    if maze[x][y] == "g":
        print("Yes")
        exit()
    maze[x][y] == "#" # 確認したルートは壁に
    
    # 上下左右に再帰
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
dfs(sx, sy)
print("No")


