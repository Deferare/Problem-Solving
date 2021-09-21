def solution(phone_number):
    start = ""
    for _ in range(len(phone_number)-4):
        start += "*"
    return start + phone_number[len(phone_number)-4:]
