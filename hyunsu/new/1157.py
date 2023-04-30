a = input().lower()
lst = list(set(a))
cnt = []

for i in lst:
    cnt.append(a.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(lst[cnt.index(max(cnt))].upper())
