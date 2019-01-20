# coding:UTF-8
with open("D:/GDJ10/public/2018/201803/20180322/test2.csv", "w", encoding="utf8") as f :
    while 1 :
        text = input("작성할 내용을 입력하세요.\t")
        if not text :
            break

        f.write(text + ",")
