"""
動的計画法の問題

方針
ある足場までにかかるコスト
今いる足場までのコスト + そこから目標までのコスト

"""

N = int(input())
h = list(map(int, input().split()))

# cost[i]: 足場i にたどり着くまでのコスト、大きさN
cost = [0] * N

# 初期条件
cost[0] = 0
# 二つ目の足場はジャンプ元が一通り
cost[1] = cost[0] + abs(h[0] - h[1])

# それ以降はジャンプ元がふた通り、小さい方を採用
for i in range(2, N):
    cost[i] = min(cost[i-1]+abs(h[i] - h[i-1]), cost[i-2]+ abs(h[i] - h[i-2]))
print(cost[N-1])