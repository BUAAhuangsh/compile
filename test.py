import sys, re
lex_analysis_result = []
analysis_stack = []
reserved_words_dict={'int':'define',
                     'main':'dso_local i32 @main',
                     '(':'(',
                     ')':')',
                     'return':'ret i32',
                     '{':'{',
                     '}':'}',
                     ';':'',
                     '/':'/',
                     '*':'*'}

def Lexical_analysis(line_input):

    for i in line_input:
        word= i.split()
        for j in word:
            if j in reserved_words_dict:
                lex_analysis_result.append(j)
            else:
                k=0
                num=''
                ident=''
                while k<len(j):
                    if re.match('[-0-9]', j[k]):
                        while k < len(j) and re.match('[-0-9a-fA-FXx]', j[k]):
                            num += j[k]
                            k += 1
                        lex_analysis_result.append(num)
                        num=''
                    elif re.match('[_A-Za-z]', j[k]):
                        while k < len(j) and re.match('[_a-zA-Z0-9]', j[k]):
                            ident += j[k]
                            k += 1
                        lex_analysis_result.append(ident)
                        ident=''
                    elif j[k] in reserved_words_dict:
                        lex_analysis_result.append(j[k])
                        k+=1

        lex_analysis_result.append('\n')

def main():
    line_input=[]
    for line in sys.stdin:
        line_input.append(line)
    Lexical_analysis(line_input)
    notation_clear(lex_analysis_result)
    parsing()
    for i in lex_analysis_result:
        if i in reserved_words_dict:
            print(reserved_words_dict[i],end=' ')
        else:
            print(i,end=' ')

def notation_clear(lex_analysis_result):
    lex_analysis_result_length=len(lex_analysis_result)
    i=0
    while i < lex_analysis_result_length-1:
        if lex_analysis_result[i]=='/' and  lex_analysis_result[i+1]=='/':
            while(lex_analysis_result[i]!='\n'):
                lex_analysis_result[i]=''
                i+=1
        elif lex_analysis_result[i]=='/' and  lex_analysis_result[i+1]=='*':
            while(lex_analysis_result[i]!='*' or lex_analysis_result[i+1] !='/'):
                lex_analysis_result[i]=''
                i+=1
            lex_analysis_result[i]=''
            i+=1
            lex_analysis_result[i]=''
            i+=1
        else:
            i+=1
    j=0
    while j<len(lex_analysis_result):
        if lex_analysis_result[j]=='':
            lex_analysis_result.remove(lex_analysis_result[j])
        else:
            j+=1

def parsing():
    temp=''
    j=0
    for i in lex_analysis_result:
        if i in reserved_words_dict:
            temp+=i
        elif i!='\n':
            lex_analysis_result[j]=number_parsing(i)
        j+=1
    check='intmain(){return;}'
    if temp!=check:
        print(temp)
        sys.exit(1)

def number_parsing(Num:str)->int:
    if len(Num)>1 and (Num[0]=='0' and Num[1]=='x' or Num[0]=='0' and Num[1]=='X'):
        return int(Num,16)
    elif Num[0]=='0':
        return int(Num,8)
    else:
        return int(Num)
main()