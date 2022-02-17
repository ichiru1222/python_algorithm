from traceback import print_tb


N, K = map(int, input().split())
h = list(map(int, input().split()))

# コスト
cost = [0] * N
# 初期条件
cost[0] = 0
# 次の足場は一通り
cost[1] = cost[0] + abs(h[1] - h[0])

for i in range(2, N):
    c = []
    for k in range(1, K+1):
        if i - k < 0:
            break
        n_c = cost[i - k] + abs(h[i] - h[i - k])
        c.append(n_c)
  
    cost[i] = min(c)
print(cost[N-1])