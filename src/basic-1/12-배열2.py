# coding:UTF-8
이름목록 = ['문자',1, 0.2, False]
print(이름목록)
a, b, c, d = 이름목록
print(a, b, c, d)

# 데이터 추가
이름목록.append("추가")
print(이름목록)

이름목록.extend([1,2,3,4,5])
print(이름목록)

이름목록.insert(2, "중간")
print(이름목록)

# 데이터 삭제
del 이름목록[5]
print(이름목록)

이름목록.remove('중간')
print(이름목록)

# 데이터 변경
이름목록[3] = True
print(이름목록)