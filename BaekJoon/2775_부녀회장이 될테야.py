test_case = int(input())
for _ in range(test_case):
    line = int(input())
    block = int(input())
    zero_line = [i for i in range(1, block+1)]
    block_line = [0 for _ in range(block)]
    for _ in range(line):
        for j in range(block):
            add = 0
            if j != 0:
                add = block_line[j-1]
            block_line[j] = zero_line[j] + add
        zero_line = block_line
    print(block_line[block-1])
