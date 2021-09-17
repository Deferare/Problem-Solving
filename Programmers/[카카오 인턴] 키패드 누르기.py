def solution(numbers, hand):
    left = [3,0]; right = [3,2]
    result = ""
    for number in numbers:
        number_cases = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0],
                        [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        number_point = number_cases[number]
        if number == 1 or number == 4 or number == 7:
            left = number_point
            result += "L"
            continue
        elif number == 3 or number == 6 or number == 9:
            right = number_point
            result += "R"
            continue
        left_distance = abs(left[0] - number_point[0]) + abs(left[1] - number_point[1])
        right_distance = abs(right[0] - number_point[0]) + abs(right[1] - number_point[1])
        if left_distance > right_distance:
            result += "R"
            right = number_point
        elif left_distance < right_distance:
            result += "L"
            left = number_point
        else:
            if hand == "left":
                result += "L"
                left = number_point
            if hand == "right":
                result += "R"
                right = number_point
    return result
