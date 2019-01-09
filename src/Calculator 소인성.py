# coding : UTF-8
title = '''계산하려는 연산부호 항목입니다. 1번부터 4번까지 하나를 선택하세요.
1. 덧셈    2. 뺄셈    3. 곱셈    4. 나눗셈
'''
T_name = input(title)
result = ""
a = int(input("계산하려는 첫 번째 값을 입력하세요.\n\t-->\t"))
b = int(input("계산하려는 두 번째 값을 입력하세요.\n\t-->\t"))
if T_name == "1" :
    result = a + b
elif T_name == "2" :
    result = a - b
elif T_name == "3" :
    result = a * b
elif T_name == "4" :
    result = a / b
else :
    print("잘못 선택하셨습니다.")
print("선택한 숫자의 연산값은", result, "입니다.")