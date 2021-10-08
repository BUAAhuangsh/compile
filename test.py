import sys,re
n=[]
word=[]
j=0
num=""
ident=''
for line in sys.stdin:
    n.append(line)
dict={'if':'If',
      'else':'Else',
      'while':'While',
      'break':'Break',
      'continue':'Continue',
      'return':'Return',
      '=':'Assign',
      ';':'Semicolon',
      '(':'LPar',
      ')':'RPar',
      '{':'LBrace',
      '}':'RBrace',
      '+':'Plus',
      '*':'Mult',
      '/':'Div',
      '<':'Lt',
      '>':'Gt',
      '==':'Eq'}
for i in n:
    word=i.split()
    for j in word:
        if j in dict:
            print(dict[j])
        else:
            k=0
            while k<len(j):
                num=""
                ident=''
                if len(j)-k >=2 and j[k]=='=' and j[k+1]=='=':
                    print('Eq')
                    k+=2
                elif j[k] in dict:
                    print(dict[j[k]])
                    k+=1
                elif re.match('[0-9]',j[k]):
                    while k<len(j) and re.match('[0-9]',j[k]):
                        num+=j[k]
                        k+=1
                    print('Number('+num+')')
                elif re.match('[_a-zA-Z]',j[k]):
                    while k<len(j) and re.match('[_a-zA-Z0-9]',j[k]):
                        ident+=j[k]
                        k+=1
                    if ident in dict:
                        print(dict[ident])
                    else:
                        print('Ident('+ident+')')
                else:
                    print("Err")
                    sys.exit(0)

