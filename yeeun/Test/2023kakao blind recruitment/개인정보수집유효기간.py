'''
각 약관마다 개인정보 보관 유효기간 정해져 있음 유효기간이 지나면 파기
ex 22.01.05에 수집된 약관 12달 유효기간 -> 23.01.04까지 유효 23.01.05에 파기


- 모든 달은 28일까지 있다고 가정
- 매개변수(입력) today, terms, privaces
- 출력 : 파기해야 할 개인정보 번호 오름차순
* terms: "약관종류(A,B,C) 유효기간" 유효기간: 달
* privaces:
    1 ≤ privacies의 길이 ≤ 100
    privacies[i] : i+1번 "개인정보의 수집 일자/ 공백 /약관 종류"
    ->  "YYYY.MM.DD  A"
*terms, privaces속 날짜 YYYY.MM.DD
    2000 ≤ YYYY ≤ 2022
    1 ≤ MM ≤ 12
    1 ≤ DD ≤ 28
    한 자릿수인 경우 앞에 0

 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요

'''



def solution(today, terms, privacies):
    today = dateConversion(today)
    terms = termDictionary(terms)

    answer = []
    for i in range(len(privacies)):
        privacyDate, termType = privacies[i].split(' ')
        privacyDate = dateConversion(privacyDate)
        validDateList = validDate(privacyDate, terms[termType])
        print(isValid(today, validDateList))
        if isValid(today, validDateList): answer.append(i +1)

    return answer


def dateConversion(date):
    y, m, d =date.split('.')
    y = int(y)
    m = int(m)
    d = int(d)
    dateList = [y,m,d]
    return dateList


def termDictionary(terms):
    terms_d = {}
    for term in terms:
        terms_type, terms_m = term.split(' ')
        terms_m = int(terms_m)
        terms_d[terms_type] = terms_m
    return (terms_d)
def validDate(date, term_m):
    sum_m = date[1]+term_m

    if sum_m > 12:
        if sum_m % 12 == 0:
            date[1] = 12
            date[0] += (sum_m // 12) -1
        else:
            date[0] += sum_m // 12
            date[1] = sum_m % 12
    else:
        date[1] = sum_m

    validDateList=[date[0], date[1], date[2]]
    print(validDateList)
    return (validDateList)

def isValid(today, validDate):
    if today[0] > validDate[0] : return True
    elif today[0] == validDate[0]:
        if today[1] > validDate[1] : return True
        elif today[1] == validDate[1]:
            if today[2] >= validDate[2] : return True
    return False


today = "2021.12.08"
terms = ["A 18", "B 12", "C 3", "D 9"]
privacies = ["2020.06.08 A"]
# 24 -> 2 가 플러스 ...

# 2021.6.8 12개월 뒤
# 2021.12.8 6개월 뒤

# 2021.06. 08
# 12
# 6+12 > 12 -> 21 -> 22 / 6 -> 18%12=6
print(solution(today,terms,privacies))