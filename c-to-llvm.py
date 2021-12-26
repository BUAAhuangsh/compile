from __future__ import print_function
import sys,re
import cparser
import llvmlite_generator
def _zz_test_translate(src:str):
    parser = cparser.CParser()
    ast = parser.parse(src)
    generator = llvmlite_generator.LLVMGenerator()

    return generator.generate(ast)


def getinput(arr:list):
    ans1=[]
    ans2=[]
    ch_arr=[]
    int_arr=[]
    # for i in sys.stdin:
    #     arr.append(i)
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
    p = 0
    for i in range(len(int_arr) - 1):
        if int_arr[i] == int_arr[i + 1]:
            p += 1
            int_arr[i + 1] += '.' + str(p)
        else:
            p = 0
    return int_arr,ch_arr

if __name__ == "__main__":
    src=r"""
    void putint(int a) { printf("%d", a); }
    void putch(int a) { printf("%c", a); }

    """
    for i in sys.stdin:
        src+=i
    arr = src.split('\n')
    tmp1,tmp2=getinput(arr)

    src = src.replace("= getint()", "")
    src = src.replace("= getch()", "")
    src = src.replace("=getint()", "")
    src = src.replace("=getch()", "")
    ans=str(_zz_test_translate(src))

    ans2=ans.split('\n')
    tmpstr1="  %\"tmp\" = call i32 @getint()"
    tmpstr2 = "  %\"tmp\" = call i32 @getch()"
    p=''
    for i in range(len(ans2)):
        for j in tmp2:
            j='%\"'+j+'\"'
            if j in ans2[i] and '= alloca' in ans2[i] :
                ans2.insert(i+1,tmpstr2)
                p = '  store i32 %\"tmp\", i32* ' + j
                ans2.insert(i+2,p)
        for j in tmp1:
            j = '%\"' + j + '\"'
            if j in ans2[i] and '= alloca' in ans2[i] :
                ans2.insert(i + 1, tmpstr1)
                p='  store i32 %\"tmp\", i32* '+j
                ans2.insert(i+2,p)
    for i in ans2:
        print(i)
    # print(tmp1,tmp2)

