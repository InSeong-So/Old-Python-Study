# coding : UTF-8
FILE_NM = "D:/GDJ10/public/2018/201803/20180320/3.txt"
# 무엇을 할것인지 구분자 생성
type_nm = input("무엇을 하실건가요?(1:신규 & 2:추가)")
type_key = ""
if type_nm == "1" :
    type_key = "w"
elif type_nm == "2" :
    type_key = "a"
# 파일 처리부분 (신규&추가)
with open(FILE_NM, type_key, encoding="utf8") as f:
    while True :
        t = input("글 주세요~ 'ㅁ'a")
        if t == "":
            break
        f.write(t + "\n")