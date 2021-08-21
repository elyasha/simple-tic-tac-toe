a = input()
b = input()
result = ""
for i in range(len(a)):
    result += a[i]
    if i == len(b) - 1 and len(a) > len(b):
        result += b[i]
        break
    for j in range(len(b)):
        if j == len(b) and len(b) > len(a):
            result += b[j, :]
        if i == j:
            result += b[j]


print(result)
