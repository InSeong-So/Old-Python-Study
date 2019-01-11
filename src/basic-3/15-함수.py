def a() :
    print("함수 실행!")

def b() :
    return "함수2 실행"

def c(v) :
    return v

def e(a, b, c) :
    return a + b + c
'''
d = a()
d = b()
d = c(True)
'''
d = e(5, 3, 1)
print("d : ", d, type(d))