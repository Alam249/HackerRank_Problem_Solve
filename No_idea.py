n, m = [input().split() for _ in range(2)]
A = set(input().split())
B = set(input().split())

happiness = 0

for i in m:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)