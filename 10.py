n = float(input())
cntt = 0

while True:
    n1 = float(input())
    if n1 == 0:
        break
    if n1 < n:
        cntt += 1
    n = n1
print(cntt)
