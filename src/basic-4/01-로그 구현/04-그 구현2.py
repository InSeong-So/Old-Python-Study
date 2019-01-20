# coding:UTF-8
with open("D:/GDJ10/public/2018/201803/20180322/test2.csv", "w", encoding="utf8") as f :
    data = ""
    while 1 :
        text = input("작성할 내용을 입력하세요.\t")
        # 가나
        if not text :
            data = data[:-1]
            data += "\n"
        elif text == "," :
            data = data[:-1]
            break
        else :
            data += text + ","
            # "" + "가나" + ","

    f.write(data)
