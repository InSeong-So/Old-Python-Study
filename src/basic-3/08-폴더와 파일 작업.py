# coding : UTF-8
DIR_NM = "D:/GDJ10/public/2018/201803/20180320/"
NEW_DIR_NM = ""
FILE_NM = ""
FULL_NM = ""
tempList = []

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
    import os

    if type_key == "w" :
        NEW_DIR_NM = input("선택할 폴더 이름을 입력하세요.")
        if not os.path.isdir(DIR_NM + NEW_DIR_NM) : # 폴더 유무 확인
            os.mkdir(DIR_NM + NEW_DIR_NM)
        FILE_NM = input("파일 이름을 작성해주세요.")
        FULL_NM = DIR_NM + NEW_DIR_NM +"/"+ FILE_NM + ".txt"
    elif type_key == "r" :
        for fn in tempList :
            print(fn)
        if len(tempList) > 0 :
            index = int(input("몇번째 파일를 읽을까요?"))
            FULL_NM = tempList[index-1]
        else :
            print("저장 되어 있는 목록이 없습니다.")
            continue
    # 파일 처리부분
    with open(FULL_NM, type_key, encoding="utf8") as f:
        if type_key == "r" :
            text = f.read()
            print(text)
        else :
            if type_key == "w" :
                tempList.append(FULL_NM)
            while True :
                t = input("글 주세요~ 'ㅁ'a")
                if t == "":
                    break
                f.write(t + "\n")