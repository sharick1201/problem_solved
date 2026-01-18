T = int(input())

for _ in range(T):
    string = input().strip()
    result = string[0] + string[-1]
    print(result)
