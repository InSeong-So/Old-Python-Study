# coding:UTF-8
print("구구단 시작!")
# d = int(input("출력할 단를 입력해주세요."))
for d in range(1, 10, 3) :
    for i in range(1, 10) :
        print("%d * %d = %d\t%d * %d = %d\t%d * %d = %d" % (d, i, (d * i), d+1, i, ((d+1) * i), d+2, i, ((d+2) * i) ) )