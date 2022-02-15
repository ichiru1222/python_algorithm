k = int(input())
a, b = map(int, input().split())

ok = False

for i in range(a, b + 1):
    if i % k == 0:
        ok = True
if ok:
    print("OK")
else:
    print("NG")