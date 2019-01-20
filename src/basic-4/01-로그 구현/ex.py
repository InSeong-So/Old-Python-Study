# coding : UTF-8
DIR_NM = "D:/GDJ10/public/2018/201803/20180322/"
NEW_DIR_NM = ""
FILE_NM = ""
FULL_NM = ""
tempList = []

import file

while True :
    # 무엇을 할것인지 구분자 생성
    type_nm = input("무엇을 하실건가요?(1:신규 & 3:읽기)")
    type_key = ""
    if type_nm == "1" :
        type_key = "w"
        FULL_NM = file.신규(DIR_NM)
    elif type_nm == "3" :
        type_key = "r"
        for fn in tempList :
            print(fn)
        if len(tempList) > 0 :
            index = int(input("몇번째 파일를 읽을까요?"))
            FULL_NM = tempList[index-1]
        else :
            print("저장 되어 있는 목록이 없습니다.")
            continue
    else :
        break

    tempList = file.파일관리(FULL_NM, type_key, tempList)
