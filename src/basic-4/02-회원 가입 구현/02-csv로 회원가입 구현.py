# coding:UTF-8
''' csv 파일에서 관리 할것!
    1. 회원가입
    2. 로그인
    3. 종료
'''

회원정보 = "D:/GDJ10/public/2018/201803/20180323/users.csv"
회원가입질의 = ["아이디를 입력하세요.", "비밀번호를 입력하세요.", "이름을 입력하세요."]
로그인후 = ["님 환영합니다.","누구냐 넌?"]

# 1. 회원가입 CSV(아이디, 비밀번호, 이름)
def 회원가입() :
    with open(회원정보, "a", encoding="utf8") as f:
        user = []
        i = 0
        while 1 :
            if len(회원가입질의) == i :
                break
            입력값 = input(회원가입질의[i])
            user.append(입력값)
            i += 1
        for jj in range(len(user)) :
            result = ""
            if len(user) == (jj + 1) :
                result += user[jj] + "\n"
            else :
                result += user[jj] + ","
            f.write(result)

# 2. 로그인
def 로그인() :
    with open(회원정보, "r", encoding="utf8") as f:
        users = []
        user = []
        while 1 :
            data = f.readline()
            if not data :
                break
            users.append(data[:-1].split(","))
        
        id = input(회원가입질의[0])
        pw = input(회원가입질의[1])
        user = [id, pw]

        check = False
        for u in users :
            if u[0] == user[0] and u[1] == user[1] :
                user.append(u[2])
                check = True
        print(check and user[2] + 로그인후[0] or 로그인후[1])

# 회원관리
while 1 :
    key = int(input("회원가입(1), 로그인(2), 종료(3) 중 하나를 입력하세요."))
    if key == 1 :
        회원가입()
    elif key == 2 :
        로그인()
    elif key == 3 :
        break
    else :
        print("다시 입력해주세요.")
