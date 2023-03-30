def solution(today, terms, privacies):
    result = []
    today = list(map(int, today.split('.')))
    today = today[2] + today[1] * 28 + today[0] * 28 * 12

    dic = dict()
    for term in terms:
        k, v = term.split()
        dic[k] = int(v) * 28

    for i in range(len(privacies)):
        datetime, category = privacies[i].split()
        datetime = list(map(int, datetime.split('.')))
        datetime = datetime[2] + datetime[1] * 28 + datetime[0] * 28 * 12
        if datetime + dic[category] <= today:
            result.append(i+1)

    return result


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))