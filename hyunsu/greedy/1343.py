k = input()

k = k.replace('XXXX', 'AAAA')
k = k.replace('XX', 'BB')

if 'X' in k:
    print(-1)
else:
    print(k)