s = list(input())
a = sorted(s)
for i in range(len(s)):
    if s[i] != a[i]:
        for j in range(len(s) - 1, -1, -1):
            if s[j] == a[i]:
                s[i], s[j] = s[j], s[i]
                break
        break
print(''.join(s))
