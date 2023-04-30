    vowels = 'aeiou'

    while True:
        a = input()
        if a == 'end':
            break
        check1 = 1
        check2 = 0

        for i in a:
            if i in vowels:
                check1 = 0

        if check1 == 0:
            for i in range(len(a) - 1):
                if a[i] == a[i+1] and a[i] not in 'eo':
                    check2 = 1
        for i in range(len(a) -  2):
            if a[i] in vowels and a[i+1] in vowels and a[i+2] in vowels:
                check2 = 1
            elif a[i] not in vowels and a[i+1] not in vowels and a[i+2] not in vowels:
                check2 = 1

        if check1 == 0 and check2 == 0:
            print('<' + a  + '> is acceptable.')
        else:
            print('<' + a  + '> is not acceptable.')

