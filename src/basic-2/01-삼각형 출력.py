a = [5, [1,1,1,1,1,0,1,1,1,0,0,0,1,0,0]]
b = [5, [0,0,1,0,0,0,1,1,1,0,1,1,1,1,1]]
data = [a,b]
result = ""
n = 0
z = int(input("1과 2 중 하나를 입력하세요."))
for t in data[z-1][1] :
    if n%data[z-1][0] == 0 :
        result += "\n"
    if t == 1 :
        result += "O"
    elif t == 0 :
        result += " "
    n += 1
print(result)
