# 모험가 길드
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = 0
temp = []
while len(arr) > 0:
    temp.append(arr.pop())
    if len(temp) >= temp[-1]:
        result += 1
        temp = []

print(result)