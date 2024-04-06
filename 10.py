n = float(input())
cnt = 0

while True:
    n1 = float(input())
    if n1 == 0:
        break
    if n1 < n:
        cnt += 1
    n = n1
print(cnt)
