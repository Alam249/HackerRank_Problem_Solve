n, m = map(int, input().split())

for i in range(n // 2):
    string = ".|." * (2 * i + 1)
    x = string.center(m, "-")
    print(x)

print("WELCOME".center(m, "-"))

for i in reversed(range(n // 2)):
    string = ".|." * (2 * i + 1)
    x = string.center(m, "-")
    print(x)