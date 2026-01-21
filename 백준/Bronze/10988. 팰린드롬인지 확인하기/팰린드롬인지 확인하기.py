txt = input()
ans = 1

for i in range(len(txt)//2):
    if txt[i] != txt[len(txt)-1-i]:
        ans = 0
        break

print(ans)