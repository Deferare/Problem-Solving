from sys import stdin as st

N = int(st.readline())
scores_counter = dict()
scores_counter[1] = [0, 0, 0, 0, 1]
scores_counter[2] = [0, 0, 0, 0, 2]
scores_counter[3] = [0, 0, 0, 0, 3]

for _ in range(N):
    scores = list(map(int, st.readline().split(" ")))
    scores_counter[1][scores[0]] += 1
    scores_counter[2][scores[1]] += 1
    scores_counter[3][scores[2]] += 1
results = list()
scores_counter[1][0] = (scores_counter[1][1] * 1) + (scores_counter[1][2] * 2) + (scores_counter[1][3] * 3)
results.append(scores_counter[1])
scores_counter[2][0] = (scores_counter[2][1] * 1) + (scores_counter[2][2] * 2) + (scores_counter[2][3] * 3)
results.append(scores_counter[2])
scores_counter[3][0] = (scores_counter[3][1] * 1) + (scores_counter[3][2] * 2) + (scores_counter[3][3] * 3)
results.append(scores_counter[3])
results.sort(key=lambda x:(x[0],x[3],x[2],x[1]), reverse=True)
if results[0][0] > results[1][0] or results[0][3] > results[1][3] or results[0][2] > results[1][2] or results[0][1] > results[1][1]:
    print(f"{results[0][-1]} {results[0][0]}")
else:
    print(f"0 {results[0][0]}")
