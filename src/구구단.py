# coding:UTF-8
print("구구단 시작")
# d = int(input("출력할 단을 입력해주세요."))
for d in range(1, 10) :
    print(" ### %d 단 ### " % d)
    a = ''
    for i in range(1, 10) :
        a = a+str(("%d * %d = %d " % (d, i, (d*i) )))
    print(a)
        
