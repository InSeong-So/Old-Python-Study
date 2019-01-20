class C1:
    v1 = 0
    v2 = ""
    def getV1(self):
        return self.v1
    def setV1(self, v1):
        self.v1 = v1
    
    def getV2(self):
        return self.v2
    def setV2(self, v2):
        self.v2 = v2
    
    def getResult(self):
        return "C1 : " + str(self.v1) + ", " + self.v2

c1 = C1()
print(c1.getResult())
#print(c1.getV1())
#print(c1.getV2())
c1.setV1(10)
c1.setV2("값")
#print(c1.getV1())
#print(c1.getV2())
print(c1.getResult())