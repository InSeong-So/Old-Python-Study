# coding:UTF-8
x = int(input("입력값을 넣어주세요."))
n = 1
while n < 10 : # 입력값 만큼 반복 실행
    d = 1
    while d < 10 : # 1 ~ 9까지 덧셈 실행
        result = ""
        j = 0
        while j < x : # 입력값 만큼 나열하기
            dd = (n + j) # 단 생성
            if dd == 10 : # 9단 이상 시 멈추기
                break
            result += "%d * %d = %d\t" % (dd, d, (dd * d))
            j += 1
        print(result)
        d += 1
    n += x
print("End")