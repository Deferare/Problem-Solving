n = int(input())
card_arr = list(map(int, input().split(" ")))
m = int(input())
query_arr = list(map(int, input().split(" ")))

dict = {}
for key in card_arr:
    dict[key] = 1
result = ""
for key in query_arr:
    if key in dict:
        result += "1"
    else:
        result += "0"
    result += " "
    
print(result)
