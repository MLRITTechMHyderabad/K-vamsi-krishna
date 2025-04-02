num = list(map(int, input().split()))
dict = {}
count = 0;
for i in num:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
