# 곱하기 혹은 더하기
s = input()

result = 0
for c in s:
    n = int(c)
    if result > 1 and n > 1:
        result *= n
        continue
    result += n

print(result)