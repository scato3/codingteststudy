'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
알파벳 문자열을 입력받아 각 알파벳을 1부터 26까지 숫자로 변환하여 출력
'''

dic = {"A":1, "B":2, "C": 3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24 , "Y":25, "Z":26}

arr = list(input())
for c in arr:
    if c==arr[-1]:
        print(dic[c])
    else:
        print(dic[c], sep=" ", end=" ")