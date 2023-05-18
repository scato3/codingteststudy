t = int(input())

for tc in range(1, t+1):
    n = int(input())
    speed = 0
    ans = 0

    for i in range(n):
        a = input().split()
        if a[0] == '1':
            speed += int(a[1])
            ans += speed
        elif a[0] == '0':
            ans += speed
        elif a[0] == '2':
            speed -= int(a[1])
            if speed < 0:
                speed = 0
            ans += speed

    print('#{} {}'.format(tc, ans))
