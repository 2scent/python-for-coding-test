n, m = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(n)]

result = 0

for row in cards:
    result = max(result, min(row))

print(result)
