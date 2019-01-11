# coding : UTF-8
FILE_NM = "D:/GDJ10/public/2018/201803/20180320/3.txt"
with open(FILE_NM, 'w', encoding="utf8") as f:
    while True :
        t = input("글 주세요~ 'ㅁ'a")
        if t == "":
            break
        f.write(t + "\n")
