class C1:
    def a(self):
        return "a"

class C2(C1):
    pass

c2 = C2()
print(c2.a())