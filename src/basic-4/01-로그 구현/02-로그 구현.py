# coding:UTF-8
datalist = []
with open("D:/GDJ10/public/2018/201803/20180322/test.csv", "r") as f :
    while 1 :
        data = f.readline()
        #print(data)

        if not data :
            break
        
        text = data.split(",")
        datalist.append(text)
print(datalist, datalist[1][1])