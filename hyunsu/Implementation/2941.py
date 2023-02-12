k = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    k = k.replace(i, '!')

print(len(k))