import os
def 신규(DIR_NM) :
    NEW_DIR_NM = input("선택할 폴더 이름을 입력하세요.")
    if not os.path.isdir(DIR_NM + NEW_DIR_NM) : # 폴더 유무 확인
        os.mkdir(DIR_NM + NEW_DIR_NM)
    FILE_NM = input("파일 이름을 작성해주세요.")
    return DIR_NM + NEW_DIR_NM +"/"+ FILE_NM + ".txt"

def 파일관리(FULL_NM, type_key, tempList) :
    # 파일 처리부분
    with open(FULL_NM, type_key, encoding="utf8") as f:
        if type_key == "r" :
            text = f.read()
            print(text)
            check = input("내용을 추가 할까요?(Y/N)")
            if check == "Y" :
                파일관리(FULL_NM, "a", tempList)
            elif check == "N" :
                print("읽기를 종료합니다.")
        else :
            if type_key == "w" :
                tempList.append(FULL_NM)
            while True :
                t = input("글 주세요~ 'ㅁ'a")
                if t == "":
                    break
                f.write(t + "\n")
    return tempList