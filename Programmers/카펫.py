def solution(brown, yellow):
    area = brown + yellow
    width = 3
    while True:
        while True:
            if area%width == 0:
                height = area//width
                break
            width += 1
        if width < height: width += 1
        else:
            y_num = area - ((width*2) + ((height*2) - 4))
            if y_num == yellow: return [width, height]
            else: width += 1
