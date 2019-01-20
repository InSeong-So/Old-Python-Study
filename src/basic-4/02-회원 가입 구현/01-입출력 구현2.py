# coding:UTF-8
''' 파일에서 관리 할것!
    1. 입력값 -> 출력 -> 파일에 저장
    2. 파일에서 목록에 대하여 전체 출력하기
    3. 목록에서 선택한 모양 출력하기
'''
파일목록 = "D:/GDJ10/public/2018/201803/20180323/file.csv"

# 1. 입력값 -> 출력 -> 파일에 저장
'''
입력값 = int(input("입력값을 넣어주세요."))
for i in range(입력값) :
    blank = ("-" * (입력값 - i))
    figure = ("O" * int((i * 2) + 1))
    print(blank + figure + blank)
with open(파일목록, "a", encoding="utf8") as f :
    f.write(str(입력값) + ",")
'''

def 도형(높이, 행) :
    blank = (" " * (높이 - 행))
    figure = ("O" * int((행 * 2) + 1))
    return blank + figure + blank

def 도형연결(출력행, 전체높이, 도형목록, 연결수) :
    result = ""
    for i in range(전체높이) :
        for 위치값 in range(연결수) :
            if int(도형목록[출력행 + 위치값]) <= i :
                result += " " * (int(도형목록[출력행 + 위치값])*2 + 1) + "\t"
            else :
                result += 도형(int(도형목록[출력행 + 위치값]), i) + "\t"
        result += "\n"
    print(result)

# 2. 파일에서 목록에 대하여 전체 출력하기
with open(파일목록, "r", encoding="utf8") as f :
    d = f.read()[:-1].split(",")
    #print(d)
    for row in range(0, len(d), 3) :
        check = [d[row+0], d[row+1], d[row+2]]
        m = 0
        # 가장 큰 수 구하기
        for temp in check :
            if m < int(temp) :
                m = int(temp)
        #print(check, m)
        
        #result = ""
        도형연결(row, m, d, 3)

        #print(result)
