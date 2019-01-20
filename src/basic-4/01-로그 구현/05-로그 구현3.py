# coding:UTF-8
with open("D:/GDJ10/public/2018/201803/20180322/test2.csv", "w", encoding="utf8") as f :
    data = []
    temp = []
    while 1 :
        text = input("작성할 내용을 입력하세요.\t")
        
        if not text : #다음 행으로 이동 [[],[],[]]
            data.append(temp)
            temp = []
        elif text == "," :
            data.append(temp)
            break
        else :
            temp.append(text)

    #print(data)
    #f.write(text + ",")
    for i in range(len(data)) :
        d = ""
        for j in range(len(data[i])) :
            if len(data[i]) == (j + 1) :
                d += data[i][j]
            else :                
                d += data[i][j] + ","
        f.write(d+"\n")
