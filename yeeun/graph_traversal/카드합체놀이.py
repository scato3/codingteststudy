'''
https://www.acmicpc.net/problem/15903
1. x번 카드와 y번 카드를 골라 더함
2. x+y =x x+y = y

카드합치기 m번하면 놀이가 끝

총 점수 : m번 합체 후 n개 카드 모두 합한 값
가장 작은 총 점수 구해라
'''

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
#오름차순 정렬 하고 / 카드 값 업데이트 하고 / 다시 정렬 / 카드 값 업데이트 ....

def solution(cards):

    update = cards[0]+cards[1]
    cards[0] =update
    cards[1]= update
    cards.sort()
    return cards
cards.sort()

for i in range(m):
    solution(cards)
for card in cards:
    ans += card
print(ans)