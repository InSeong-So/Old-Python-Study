# coding : UTF-8
import os
#폴더 확인 후 처리
dir_nm="D:/GDJ10/public/2018/201803/20180322/"

def log():
    if not os.path.isdir(dir_nm+"log"):
        os.mkdir(dir_nm+"log")
    #없을때가 true 없으면 만들겠다~ 라는 거

    #파일이 있는지 확인 후 처리
    if not os.path.exists(dir_nm+"log/log.txt"):
        f=open(dir_nm+"log/log.txt","w",encoding="utf8")
        f.write("기록을 시작하겠습니다.\n")
        f.close()
    else :
    #만약에 있으면
        f=open(dir_nm+"log/log.txt","a",encoding="utf8")
        f.write("다시 기록을 남기겠습니다.\n")
        f.close()

    #로그 파일에 남길 내용 적용하기
    with open(dir_nm+"log/log.txt","a",encoding="utf8") as f:
        import datetime
    #시간...을 남기는거
        stamp=str(datetime.datetime.now())
        f.write(stamp+"\n")

def log_key(key):
    if not os.path.isdir(dir_nm+"log"):
        os.mkdir(dir_nm+"log")
    if not os.path.exists(dir_nm+"log/log.txt"):
        f=open(dir_nm+"log/log.txt","w",encoding="utf8")
        f.write("기록을 시작하겠습니다.\n")
        f.close()
    else :
        f=open(dir_nm+"log/log.txt","a",encoding="utf8")
        f.write("다시 기록을 남기겠습니다.\n")
        f.close()

    # 로그내용 변경 부분
    if key == "w" :
        result = "쓰기"
    elif key == "r" :
        result = "읽기"
    elif key == "a" :
        result = "추가"

    with open(dir_nm+"log/log.txt","a",encoding="utf8") as f:
        import datetime
        stamp=str(datetime.datetime.now())
        f.write(result+"\t"+stamp+"\n")