# coding : UTF-8
file_nm = "D:/GDJ10/public/2018/201803/20180319/text.txt"
''' 파일 읽기
d = open(file_nm, "r", encoding="utf8")
print(d, d.read(), type(d))
d.close()
'''
''' 파일의 별명으로 파일 출력하기 (with 구문)
with open(file_nm, "r", encoding="utf8") as my_file:
    print(type(my_file), my_file.read(), type(my_file.read()))
'''
'''
with open(file_nm, "r", encoding="utf8") as my_file:
    print(my_file.read())
    #print(my_file.readline())
    #print(my_file.readlines())
    #print(l, l[1].strip())
'''
'''
d = open(file_nm, "r", encoding="utf8")
#print(d.read().split())
print(d.read().splitlines())
#print(d.readlines())
'''
''' readline를 이용하여 데이터 출력하기
with open(file_nm, "r", encoding="utf8") as my_file:
    i = 0
    while True:
        line = my_file.readline()
        if line.strip() != "" :
            print(str(i) + " === " + line.strip())
        if not line :
            break
        i += 1
'''
with open(file_nm, "r", encoding="utf8") as my_file:
    contents = my_file.read()
    print(contents.count("A"), contents.count("B"), contents.count("CD"))
    print(contents.split(" ").count("A"))
    print(contents.split("\n").count("A"))