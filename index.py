a, b, c, d, e = map(int, input().split(' '))
x = min(a, b, c, d, e)
min_s = a+b+c+d+e-x
x = max(a, b, c, d, e)
max_s = a+b+c+d+e-x
print(f'{max_s} {min_s}')
