# coding:UTF-8
a = input("사칙연산 기호를 입력하세요!\n")
b = 4
c = 3
if a == "+" :
    print("덧셈 입니다.", b+c)
elif a == "-" :
    print("뺄셈 입니다.", b-c)
elif a == "*" :
    print("곱셈 입니다.", b*c)
elif a == "/" :
    print("나누기 입니다.", b/c)
else :
    print("입력하신 기호는 사칙연산 기호가 아닙니다.")