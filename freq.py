def most_frequent(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    z = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    for i in z:
        print(i[0]+"="+str(i[1]))

most_frequent('mississippi')
