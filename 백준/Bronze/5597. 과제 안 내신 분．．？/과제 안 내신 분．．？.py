lst = []
for _ in range(28):
    num = int(input())
    lst.append(num)
    
dat = [0] * 31

for val in lst:
    dat[val] += 1

for i in range(1, 31):
    if dat[i] == 0:
        print(i)