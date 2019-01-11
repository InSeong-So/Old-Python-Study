# coding : UTF-8
file_nm = "D:/GDJ10/public/2018/201803/20180319/1.txt"
dataList = []
with open(file_nm, "r", encoding="utf8") as f :
    d = f.read()
    strList = list( set( d.upper().split() ) )
    strList.sort()
    tempList = []
    for i in range(len(strList)) :
        fn = strList[i]
        if len(tempList) == 0 : # 첫번째 데이터 부분
            tempList.append([fn, d.upper().count(fn)])
        elif fn[0:1] == tempList[0][0][0:1] : # 비교 대상 데이터가 동일 한 경우
            tempList.append([fn, d.upper().count(fn)])
        elif fn[0:1] != tempList[0][0][0:1] : # 비교 대상 데이터가 서로 다른 경우
            # 데이터 정렬 시작
            t = []
            for ii in range(len(tempList)) :
                t.append(tempList[ii][1])
            t.sort()

            dd = []
            for num in t :
                for ii in range(len(tempList)) :
                    if num == tempList[ii][1] :
                        dd.append(tempList[ii])
            # 데이터 정렬 종료

            dataList.extend(dd)
            tempList = []
            tempList.append([fn, d.upper().count(fn)])
            if i == (len(strList) - 1) : # 비교 대상 데이터가 마지막일 경우
                # 데이터 정렬 시작
                t = []
                for ii in range(len(tempList)) :
                    t.append(tempList[ii][1])
                t.sort()

                dd = []
                for num in t :
                    for ii in range(len(tempList)) :
                        if num == tempList[ii][1] :
                            dd.append(tempList[ii])
                # 데이터 정렬 종료
                
                dataList.extend(dd)
print(dataList)