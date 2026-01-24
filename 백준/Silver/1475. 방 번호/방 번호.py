lst = map(int, input())
# 딕셔너리를 사용해보자
dat = {i:0 for i in range(10)}

for item in lst:
    dat[item] += 1

balance = int((dat[6] + dat[9]) / 2 + 0.5)
dat[6] = balance
dat[9] = balance

print(max(dat.values()))