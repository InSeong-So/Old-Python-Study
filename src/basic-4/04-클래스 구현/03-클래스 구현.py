# coding:UTF-8
class C1: # 클래스(부모)
    def a(self):
        return "a"

class C2(C1):
    def b(self):
        return "b"

class C3(C2):
    def c(self):
        return "c"
    def a(self):
        return "A"
    def superA(self):
        return super().a()

c3 = C3()
c3.a()
c3.b()
c3.c()
c3.superA()