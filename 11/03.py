# 문자열 뒤집기
S = input()

counts = {
    0: 0,
    1: 0,
}

cur_num = int(S[0])
counts[cur_num] += 1
for i in S[1:]:
    num = int(i)
    if cur_num != num:
        cur_num = num
        counts[num] += 1

print(min(counts[0], counts[1]))
