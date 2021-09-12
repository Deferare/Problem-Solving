import datetime
def solution(a, b):
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    day_index = datetime.date(2016, a, b).weekday()
    return days[day_index]
