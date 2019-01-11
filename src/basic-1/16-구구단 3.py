# coding:UTF-8
print("구구단 시작!")
'''
for d in range(1, 10, 3) :
    for i in range(1, 10) :
        print( "%d * %d = %d\t%d * %d = %d\t%d * %d = %d" % (d, i, (d * i),d+1, i, ((d+1) * i),d+2, i, ((d+2) * i)) )
'''

n = int(input("옆으로 보여줄 단의 수를 입력하세요."))
for d in range(1, 10, n) :
    for i in range(1, 10) :
        result = ""
        for nn in range(0, n) :
            result += "%d * %d = %d\t" % (d + nn, i, ((d + nn) * i))
        print(result)