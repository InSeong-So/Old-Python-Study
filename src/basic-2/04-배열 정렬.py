d = [['A', 45], ['ALL', 1], ['AN', 4], ['AS', 5], ['AWAY', 3]]
t = []

for i in range(len(d)) :
    t.append([d[i][1]])
t.sort()
print(t)

dd = []
for num in t :
    print(num)
    for i in range(len(d)) :
        if num == d[i][1] :
            dd.extend(d[i])
print(dd)
