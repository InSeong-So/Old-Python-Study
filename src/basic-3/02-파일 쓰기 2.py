# coding : UTF-8
FILE_NM = "D:/GDJ10/public/2018/201803/20180320/2.txt"
with open(FILE_NM, 'w', encoding="utf8") as f:
    for i in range(10):
        f.write(str(i) + "\n")
