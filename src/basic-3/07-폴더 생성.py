# coding : UTF-8
DIR_NM = "D:/GDJ10/public/2018/201803/20180320/"
NEW_DIR_NM = ""
FILE_NM = ""

import os
NEW_DIR_NM = input("생성할 폴더 이름을 입력하세요.")
os.mkdir(DIR_NM + NEW_DIR_NM)

FILE_NM = input("파일 이름을 입력하세요.")
with open(DIR_NM + NEW_DIR_NM +"/"+ FILE_NM + ".txt", "w", encoding="utf8") as f :
    txt = input("작성할 내용을 입력하세요.")
    f.write(txt)