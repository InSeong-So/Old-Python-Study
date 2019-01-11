a = [[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
b = [[1,0,0],[1,1,0],[1,1,1],[1,1,0],[1,0,0]]
data = [a, b]
z = int(input("1, 2, 3, 4 중 하나를 입력하세요."))
p = ""
for t in data[int((z == 1 or z == 2) and "0" or "1")] :
    result = ""
    for tt in t :
        result = z == 4 and (tt == 1 and "O" + result or " " + result) or (tt == 1 and result + "O" or result + " ") 
    p = z%2 != 0 and p + result + "\n" or result + "\n" + p
print(p)
