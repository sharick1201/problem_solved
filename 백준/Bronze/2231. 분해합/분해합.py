N = int(input())

for M in range(1, N):
    digitsum = sum(int(digit) for digit in str(M))
    if M + digitsum == N:
        print(M)
        break
else:
    print(0)