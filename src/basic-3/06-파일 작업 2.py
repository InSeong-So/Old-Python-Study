# coding : UTF-8
DIR_NM = "D:/GDJ10/public/2018/201803/20180320/"
FILE_NM = ""

while True :
    # 무엇을 할것인지 구분자 생성
    type_nm = input("무엇을 하실건가요?(1:신규 & 2:추가 & 3:읽기)")
    type_key = ""
    if type_nm == "1" :
        type_key = "w"
    elif type_nm == "2" :
        type_key = "a"
    elif type_nm == "3" :
        type_key = "r"
    else :
        break
    FILE_NM = input("파일 이름을 작성해주세요.")
    # 파일 처리부분
    with open(DIR_NM + FILE_NM + ".txt", type_key, encoding="utf8") as f:
        if type_key == "r" :
            text = f.read()
            print(text)
        else :
            while True :
                t = input("글 주세요~ 'ㅁ'a")
                if t == "":
                    break
                f.write(t + "\n")