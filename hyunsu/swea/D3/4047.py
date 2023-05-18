t = int(input())

for tc in range(1, t+1):
    my_card = {
        'S': [],
        'D': [],
        'H': [],
        'C': []
    }

    cards = input()

    print('#{}'.format(tc),end=' ')
    for i in range(0, len(cards), 3):
        card = cards[i]
        n = cards[i+1:i+3]

        if n not in my_card[card]:
            my_card[card].append(n)
        else:
            print('ERROR',end=' ')
            print()
            break

    else:
        for key, value in my_card.items():
            print(13 - len(value),end=' ')
        print()
