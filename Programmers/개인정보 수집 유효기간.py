def solution(today, terms, privacies):
    def getDateValue(date: [int]) -> int:
        return date[0] * (12 * 28) + (date[1] * 28) + date[2]

    def caclulate(date:[int], turm_kind:str ) -> bool:
        date_value = getDateValue(date)
        turm_value = terms_v2[turm_kind]*28
        if (date_value + turm_value) <= today_value: return True
        return False

    today2 = today.split(".")
    today = [int(today2[0]), int(today2[1]), int(today2[2])]
    today_value = getDateValue(today)

    terms_v2 = dict()
    for term in terms:
        t = term.split(" ")
        terms_v2[t[0]] = int(t[1])

    answer = []
    for i in range(len(privacies)):
        arr = privacies[i].split(" ")
        date = arr[0].split(".")
        date2 = [int(date[0]), int(date[1]), int(date[2])]
        if caclulate(date2, arr[1]):
            answer.append(i+1)
            
    return answer
