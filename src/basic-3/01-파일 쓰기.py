# coding : UTF-8
FILE_NM = "D:/GDJ10/public/2018/201803/20180320/1.txt"
f = open(FILE_NM, 'w', encoding="utf8")

for i in range(10):
    f.write(str(i) + "\n")

f.close()