count = 0
mn = min(i for i in range(100, 200) if i % 17 == 0)
for i in range(mn, 999+1, 17):
    count += 1
    print(i, end=' ')
print('\n', count)
