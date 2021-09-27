def solution(phone_book):
    prefixs = dict()
    for number in phone_book:
        save_str = ""
        for i in range(len(number)):
            save_str += number[i]
            if save_str not in prefixs:
                prefixs[save_str] = 1
            else:
                prefixs[save_str] += 1
    for number in phone_book:
        if prefixs[number] > 1:
            return False
    return True
