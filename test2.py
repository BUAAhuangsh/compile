import sys,re,collections
def getinput():
    arr=[]
    ans1=[]
    ans2=[]
    ch_arr=[]
    int_arr=[]
    for i in sys.stdin:
        arr.append(i)
    for i in arr:
        i=i.replace(" ",'')
        p=re.findall('[a-zA-Z_][a-zA-Z0-9_]*=getint\(\)',i)
        ans1.append(p)
        p = re.findall('[a-zA-Z_][a-zA-Z0-9_]*=getch\(\)', i)
        ans2.append(p)
    for i in ans1:
        for j in i:
            j=j.replace("int","",1)
            j = j.replace("=getint()", "")
            int_arr.append(j)
    for i in ans2:
        for j in i:
            j=j.replace("int","")
            j = j.replace("=getch()", "")
            ch_arr.append(j)
    int_arr.sort()
    ch_arr.sort()
    p=0
    for i in range(len(int_arr)-1):
        if int_arr[i]==int_arr[i+1]:
            p+=1
            int_arr[i+1]+='.'+str(p)
        else:
            p=0
    return int_arr,ch_arr

a,b=getinput()
print(a,b)
