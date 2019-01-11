# coding:UTF-8
title = '''Why do you want to learn programming?
1. For my kids
2. Make money
1 & 2 ?
'''
T_name = input(title)
result = ""

if T_name == "1" :
    result = "아이들 교육"
elif T_name == "2" :
    result = "돈 벌기 위해서"
else :
    result = "잘못 선택 되었습니다."

print("선택한 내용은?", result)