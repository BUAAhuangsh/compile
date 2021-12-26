import sys, re
# lex_analysis_result = []
# analysis_stack = []
# reserved_words_dict={'int':'define',
#                      'main':'dso_local i32 @main',
#                      '(':'(',
#                      ')':')',
#                      'return':'ret i32',
#                      '{':'{',
#                      '}':'}',
#                      ';':'',
#                      '/':'/',
#                      '*':'*'}
#
# # 运算符表
# y_list = {"+", "-", "*", "/", "<", "<=", ">", ">=", "=", "==", "!=", "^", ",", "&", "&&", "|", "||", "%", "~", "<<",
#           ">>", "!"}
# # 分隔符表
# f_list = {";", "(", ")", "[", "]", "{", "}", ".", ":", "\"", "#", "\'", "\\", "?"}
# # 关键字表
# k_list = {
#     "auto", "break", "case", "const", "continue", "default", "do", "else", "enum", "extern",
#     "for", "goto", "if", "register", "return", "short", "signed", "sizeof", "static",
#     "struct", "switch", "typedef", "union", "volatile", "while", "printf", "main"
# }
#
# Cmp = ["<", ">", "==", "!=", ">=", "<="]
#
# Type = {"int", "float", "char", "double", "void", "long", "unsigned", "string"}
# type_flag = ""
# # 括号配对判断
# kuo_cp = {'{': '}', '[': ']', '(': ')'}
#
# RegNum=1
# def transfer(string):
#     arr=list(string)
#     i=0
#     while i < len(arr):
#         if (arr[i]=='-' or arr[i]=='+')and i==0:
#             arr.insert(i, '0')
#             i += 1
#         if arr[i]=='(' and arr[i+1]=='-':
#             arr.insert(i+1,'0')
#             i+=2
#         elif arr[i]=='-' and arr[i+1]=='-':
#             arr.pop(i)
#             arr.pop(i)
#             arr.insert(i,'+')
#         elif arr[i]=='+' and arr[i+1]=='-':
#             arr.pop(i)
#             arr.pop(i)
#             arr.insert(i,'-')
#         elif arr[i]=='-' and arr[i+1]=='+':
#             arr.pop(i)
#             arr.pop(i)
#             arr.insert(i,'-')
#         elif arr[i]=='+' and arr[i+1]=='+':
#             arr.pop(i)
#             arr.pop(i)
#             arr.insert(i,'+')
#         else:
#             i+=1
#     return arr
# class register:
#     content=[]
#     registerNum=0
#     value=0
# def priority(z):
#     if z in ['%', '*', '/']:
#         return 2
#     elif z in ['+', '-']:
#         return 1
# def in2post(expr:list):
#     expr=transfer(expr)
#     expr = transfer(expr)
#     stack = []  # 存储栈
#     post = []  # 后缀表达式存储
#     for z in expr:
#         if z not in ['%', '*', '/', '+', '-', '(', ')']:  # 字符直接输出
#             post.append(z)
#         else:
#             if z != ')' and (not stack or z == '(' or stack[-1] == '('
#                              or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
#                 stack.append(z)     # 运算符入栈
#
#             elif z == ')':  # 右括号出栈
#                 while True:
#                     x = stack.pop()
#                     if x != '(':
#                         post.append(x)
#                     else:
#                         break
#
#             else:   # 比较运算符优先级，看是否入栈出栈
#                 while True:
#                     if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
#                         post.append(stack.pop())
#                     else:
#                         stack.append(z)
#                         break
#     while stack:    # 还未出栈的运算符，需要加到表达式末尾
#         post.append(stack.pop())
#     return post
# # 计算后缀表达式
# def calculate(string):
#     global RegNum
#     stack = []
#     cstring = []
#     assemble=[]
#
#     for i in string:
#         temp=register()
#         temp.registerNum=0;
#         temp.content=i
#         cstring.append(temp)
#     for c in cstring:
#         # 如果是运算符
#         if c.content in '+-*/%':
#             tempstring = ''
#             # [右面的操作数先出栈]
#             b = stack.pop()
#             a = stack.pop()
#             d=eval(f"{a.content}{c.content}{b.content}")
#             temp=register()
#             temp.content=d
#             temp.registerNum=RegNum
#             RegNum+=1
#             stack.append(temp)
#             tempstring+='%'+str(temp.registerNum)+' = '
#             if c.content=='-':
#                 tempstring+='sub i32 '
#             elif c.content=='+':
#                 tempstring+='add i32 '
#             elif c.content=='*':
#                 tempstring+='mul i32 '
#             elif c.content=='/':
#                 tempstring+='sdiv i32 '
#             elif c.content=='%':
#                 tempstring+='srem i32 '
#
#             if a.registerNum==0:
#                 tempstring+=a.content
#                 tempstring +=', '
#             else:
#                 tempstring+="%"
#                 tempstring+=str(a.registerNum)
#                 tempstring += ', '
#             if b.registerNum==0:
#                 tempstring+=b.content
#             else:
#                 tempstring+="%"
#                 tempstring+=str(b.registerNum)
#             assemble.append(tempstring)
#         else:
#             # 操作数直接入栈
#             stack.append(c)
#     # [最后一个必是操作数]
#     return stack.pop(),assemble
# def if_num(int_word):
#     if int_word[0]=='0' :
#         return True
#     if re.match("^([0-9]{1,}[.][0-9]*)$", int_word) or re.match("^([0-9]{1,})$", int_word) == None:
#         return False
#     else:
#         return True
# # 判断是否为为变量名
# def if_name(int_word):
#     if re.match("[a-zA-Z_][a-zA-Z0-9_]*", int_word) == None:
#         return False
#     else:
#         return True
# # 判断是否为终结符
# # def END_STATE(int_word):
# #     if
#
# # 判断变量名是否已存在
# def have_name(name_list, name):
#     for n in name_list:
#         if name == n['name']:
#             return True
#     return False
# # list的换行输出
# def printf(lists):
#     for l in lists:
#         print(l)
# def get_word(lines):
#     out_words = []
#     # 先逐行读取，并记录行号
#     line_num = 1
#     for line in lines:
#         words = list(line.split())
#         for w in words:
#             # 分析单词
#             if w in Cmp:
#                 out_words.append({'word': w, 'line': line_num})
#                 continue
#             ws = w
#             for a in w:
#                 if a in f_list or a in y_list:
#                     # index为分隔符的位置，将被分隔符或运算符隔开的单词提取
#                     index = ws.find(a)
#                     if index != 0:
#                         # 存储单词与该单词的所在行号，方便报错定位
#                         out_words.append({'word': ws[0:index], 'line': line_num})
#                     ws = ws[index + 1:]
#                     out_words.append({'word': a, 'line': line_num})
#             if ws != '':
#                 out_words.append({'word': ws, 'line': line_num})
#         line_num += 1
#     return out_words
# class word_list():
#     def __init__(self, filename='test.c'):
#         self.word_list = []  # 输出单词列表
#         self.separator_list = []  # 分隔符
#         self.operator_list = []  # 运算符
#         self.name_list = []  # 变量
#         self.key_word_table = []  # 关键字
#         self.string_list = []
#         self.flag = True  # 源代码是否正确标识
#         self.line = 0
#         # get_word函数将源代码切割
#         self.creat_table(get_word(filename))
#
#     # 创建各个表
#     def creat_table(self, in_words):
#         name_id = 1
#         kuo_list = []  # 存储括号并判断是否完整匹配
#         char_flag = False
#         str_flag = False
#         string_list = []
#         strings = ""
#         chars = ""
#         for word in in_words:
#             w = word['word']
#             line = word['line']
#             if w == '"':
#                 if str_flag == False:
#                     str_flag = True
#                 else:
#                     str_flag = False
#                     self.word_list.append({'line': line, 'type': 'TEXT', 'word': strings})
#                     self.string_list.append(strings)
#                     strings = ""
#                 # self.word_list.append({'line':line, 'type':w, 'word':w})
#                 continue
#             # 判断是否为字符串
#             if str_flag == True:
#                 strings += w
#                 continue
#             if w == "'":
#                 if char_flag == False:
#                     char_flag = True
#                 else:
#                     char_flag = False
#                     self.word_list.append({'line': line, 'type': 'CHAR', 'word': chars})
#                     chars = ""
#                 continue
#             if char_flag == True:
#                 chars += w
#                 continue
#             # 判断为关键字
#             if w in k_list:
#                 self.key_word_table.append({'line': line, 'type': 'keyword', 'word': w})
#                 self.word_list.append({'line': line, 'type': w, 'word': w})
#             elif w in Cmp:
#                 self.word_list.append({'line': line, 'type': "Cmp", 'word': w})
#             # 判断为关键字
#             elif w in Type:
#                 type_flag = w
#                 self.key_word_table.append({'line': line, 'type': 'type', 'word': w})
#                 self.word_list.append({'line': line, 'type': 'type', 'word': w})
#             # 判断为运算符
#             elif w in y_list:
#                 self.operator_list.append({'line': line, 'type': 'operator', 'word': w})
#                 self.word_list.append({'line': line, 'type': w, 'word': w})
#             # 判断为分隔符
#             elif w in f_list:
#                 if w in kuo_cp.values() or w in kuo_cp.keys():
#                     # 左括号入栈
#                     if w in kuo_cp.keys():
#                         kuo_list.append({'kuo': w, 'line': line})
#                     # 右括号判断是否匹配并出栈
#                     elif w == kuo_cp[kuo_list[-1]['kuo']]:
#                         kuo_list.pop()
#                     else:
#                         self.flag = False
#                         return
#                 self.separator_list.append({'line': line, 'type': 'separator', 'word': w})
#                 self.word_list.append({'line': line, 'type': w, 'word': w})
#             else:
#                 if if_num(w):
#                     w=str(number_parsing(w))
#                     self.word_list.append({'line': line, 'type': 'number', 'word': w})
#                 elif if_name(w):
#                     if have_name(self.name_list, w):
#                         self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
#                     else:
#                         self.name_list.append({'line': line, 'id': name_id, 'word': 0.0, 'name': w, 'flag': type_flag})
#                         self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
#                         name_id += 1
#                 else:
#                     self.flag = False
#                     return
#         if kuo_list != []:
#             self.flag = False
#             return
#         self.line=line
# def notation_clear(lex_analysis_result):
#     lex_analysis_result_length=len(lex_analysis_result)
#     i=0
#     while i < lex_analysis_result_length-1:
#         if lex_analysis_result[i]=='/' and  lex_analysis_result[i+1]=='/':
#             while(lex_analysis_result[i]!='\n'):
#                 lex_analysis_result[i]=''
#                 i+=1
#         elif lex_analysis_result[i]=='/' and  lex_analysis_result[i+1]=='*':
#             while(lex_analysis_result[i]!='*' or lex_analysis_result[i+1] !='/'):
#                 lex_analysis_result[i]=''
#                 i+=1
#             lex_analysis_result[i]=''
#             i+=1
#             lex_analysis_result[i]=''
#             i+=1
#         else:
#             i+=1
#     j=0
#     while j<len(lex_analysis_result):
#         if lex_analysis_result[j]=='':
#             lex_analysis_result.remove(lex_analysis_result[j])
#         else:
#             j+=1
# def number_parsing(Num:str)->int:
#     if len(Num)>1 and (Num[0]=='0' and Num[1]=='x' or Num[0]=='0' and Num[1]=='X'):
#         return int(Num,16)
#     elif Num[0]=='0':
#         return int(Num,8)
#     else:
#         return int(Num)
#
# def expsProcess(wordlist:word_list):
#     global RegNum
#     name_RegNum=[]
#     for i in wordlist.name_list:
#         tmp=register()
#         tmp.content=i['name']
#         tmp.registerNum=i['id']
#         name_RegNum.append(tmp)
#         print('%'+str(i['id'])+' = alloca i32')
#         RegNum=tmp.registerNum+1
#     line=1;
#     exp=[]
#     temp = []
#     for i in wordlist.word_list:
#         if line!=i['line']:
#             for j in temp:
#                 if j['type']=='return':
#                     exp.append(temp)
#                 elif j['type']=='=':
#                     exp.append(temp)
#             line+=1
#             temp=[]
#         temp.append(i)
#     # for i in name_RegNum:
#     #     print(i.content,i.value)
#     for i in exp:
#         expFlag=False
#         var=''
#         exp=[]
#         j=0
#         while True:
#             if i[j]['type']=='name':
#                 var=i[j]['word']
#                 break
#             j+=1
#         print(var)
#         while j < len(i):
#             if i[j]['type']=='number' or i[j]['type']=='name' or i[j]['type'] in '+-*/%':
#                 exp.append(i[j]['word'])
#             j+=1
#         exp.pop(0)
#         exp=in2post(exp)
#         expcompute(var,exp,name_RegNum)
#
# def expcompute(Var:str,Exp:list,name_Regnum:list):
#     stack=[]
#     for c in Exp:
#         if c in '%*/+-':
#             a=0
#         else:
#            stack.append(c)
#
#
#
# def main():
#     line_input=[]
#     for line in sys.stdin:
#         line_input.append(line)
#     notation_clear(line_input)
#     w_list=word_list(line_input)
#     printf(w_list.name_list)
#
#
#
# main()
s1=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 5, i32* %3, align 4
  store i32 3, i32* %4, align 4
  store i32 5, i32* %5, align 4
  %6 = load i32, i32* %4, align 4
  %7 = sdiv i32 %6, 5
  %8 = mul nsw i32 %7, 0
  %9 = sub nsw i32 5, %8
  store i32 %9, i32* %2, align 4
  %10 = load i32, i32* %2, align 4
  call void @putint(i32 %10)
  ret i32 0
}
'''
s2=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %3, align 4
  store i32 10, i32* %2, align 4
  store i32 6, i32* %3, align 4
  %5 = load i32, i32* %2, align 4
  %6 = mul nsw i32 %5, 2
  %7 = load i32, i32* %3, align 4
  %8 = add nsw i32 %6, %7
  %9 = add nsw i32 %8, 3
  store i32 %9, i32* %4, align 4
  %10 = load i32, i32* %2, align 4
  call void @putint(i32 %10)
  ret i32 0
}
'''
s3=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 5, i32* %3, align 4
  store i32 1, i32* %4, align 4
  store i32 -2, i32* %5, align 4
  %7 = load i32, i32* %5, align 4
  %8 = mul nsw i32 %7, 1
  %9 = sdiv i32 %8, 2
  %10 = load i32, i32* %2, align 4
  %11 = load i32, i32* %3, align 4
  %12 = sub nsw i32 %10, %11
  %13 = add nsw i32 %9, %12
  %14 = load i32, i32* %4, align 4
  %15 = add nsw i32 %14, 3
  %16 = sub nsw i32 0, %15
  %17 = srem i32 %16, 2
  %18 = sub nsw i32 %13, %17
  store i32 %18, i32* %6, align 4
  %19 = load i32, i32* %6, align 4
  call void @putint(i32 %19)
  %20 = load i32, i32* %5, align 4
  %21 = srem i32 %20, 2
  %22 = add nsw i32 %21, 67
  %23 = load i32, i32* %2, align 4
  %24 = load i32, i32* %3, align 4
  %25 = sub nsw i32 %23, %24
  %26 = sub nsw i32 0, %25
  %27 = add nsw i32 %22, %26
  %28 = load i32, i32* %4, align 4
  %29 = add nsw i32 %28, 2
  %30 = srem i32 %29, 2
  %31 = sub nsw i32 0, %30
  %32 = sub nsw i32 %27, %31
  store i32 %32, i32* %6, align 4
  %33 = load i32, i32* %6, align 4
  %34 = add nsw i32 %33, 3
  store i32 %34, i32* %6, align 4
  %35 = load i32, i32* %6, align 4
  call void @putint(i32 %35)
  ret i32 0
}
'''
s4=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  %11 = alloca i32, align 4
  %12 = alloca i32, align 4
  %13 = alloca i32, align 4
  %14 = alloca i32, align 4
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  %17 = alloca i32, align 4
  %18 = alloca i32, align 4
  %19 = alloca i32, align 4
  %20 = alloca i32, align 4
  %21 = alloca i32, align 4
  %22 = alloca i32, align 4
  %23 = alloca i32, align 4
  %24 = alloca i32, align 4
  %25 = alloca i32, align 4
  %26 = alloca i32, align 4
  %27 = alloca i32, align 4
  %28 = alloca i32, align 4
  %29 = alloca i32, align 4
  %30 = alloca i32, align 4
  %31 = alloca i32, align 4
  %32 = alloca i32, align 4
  %33 = alloca i32, align 4
  %34 = alloca i32, align 4
  %35 = alloca i32, align 4
  %36 = alloca i32, align 4
  %37 = alloca i32, align 4
  %38 = alloca i32, align 4
  %39 = alloca i32, align 4
  %40 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  %41 = load i32, i32* %2, align 4
  %42 = add nsw i32 %41, 18
  store i32 %42, i32* %3, align 4
  %43 = load i32, i32* %2, align 4
  %44 = load i32, i32* %3, align 4
  %45 = add nsw i32 %43, %44
  store i32 %45, i32* %4, align 4
  store i32 1, i32* %5, align 4
  store i32 2, i32* %6, align 4
  store i32 3, i32* %7, align 4
  store i32 4, i32* %8, align 4
  %46 = load i32, i32* %5, align 4
  %47 = add nsw i32 1, %46
  store i32 %47, i32* %9, align 4
  %48 = load i32, i32* %6, align 4
  %49 = add nsw i32 2, %48
  store i32 %49, i32* %10, align 4
  %50 = load i32, i32* %7, align 4
  %51 = add nsw i32 3, %50
  store i32 %51, i32* %11, align 4
  %52 = load i32, i32* %8, align 4
  %53 = add nsw i32 4, %52
  store i32 %53, i32* %12, align 4
  %54 = load i32, i32* %9, align 4
  %55 = add nsw i32 1, %54
  store i32 %55, i32* %13, align 4
  %56 = load i32, i32* %10, align 4
  %57 = add nsw i32 2, %56
  store i32 %57, i32* %14, align 4
  %58 = load i32, i32* %11, align 4
  %59 = add nsw i32 3, %58
  store i32 %59, i32* %15, align 4
  %60 = load i32, i32* %12, align 4
  %61 = add nsw i32 4, %60
  store i32 %61, i32* %16, align 4
  %62 = load i32, i32* %13, align 4
  %63 = add nsw i32 1, %62
  store i32 %63, i32* %17, align 4
  %64 = load i32, i32* %14, align 4
  %65 = add nsw i32 2, %64
  store i32 %65, i32* %18, align 4
  %66 = load i32, i32* %15, align 4
  %67 = add nsw i32 3, %66
  store i32 %67, i32* %19, align 4
  %68 = load i32, i32* %16, align 4
  %69 = add nsw i32 4, %68
  store i32 %69, i32* %20, align 4
  %70 = load i32, i32* %17, align 4
  %71 = add nsw i32 1, %70
  store i32 %71, i32* %21, align 4
  %72 = load i32, i32* %18, align 4
  %73 = add nsw i32 2, %72
  store i32 %73, i32* %22, align 4
  %74 = load i32, i32* %19, align 4
  %75 = add nsw i32 3, %74
  store i32 %75, i32* %23, align 4
  %76 = load i32, i32* %20, align 4
  %77 = add nsw i32 4, %76
  store i32 %77, i32* %24, align 4
  %78 = load i32, i32* %21, align 4
  %79 = add nsw i32 1, %78
  store i32 %79, i32* %25, align 4
  %80 = load i32, i32* %22, align 4
  %81 = add nsw i32 2, %80
  store i32 %81, i32* %26, align 4
  %82 = load i32, i32* %23, align 4
  %83 = add nsw i32 3, %82
  store i32 %83, i32* %27, align 4
  %84 = load i32, i32* %24, align 4
  %85 = add nsw i32 4, %84
  store i32 %85, i32* %28, align 4
  %86 = load i32, i32* %25, align 4
  %87 = add nsw i32 1, %86
  store i32 %87, i32* %29, align 4
  %88 = load i32, i32* %26, align 4
  %89 = add nsw i32 2, %88
  store i32 %89, i32* %30, align 4
  %90 = load i32, i32* %27, align 4
  %91 = add nsw i32 3, %90
  store i32 %91, i32* %31, align 4
  %92 = load i32, i32* %28, align 4
  %93 = add nsw i32 4, %92
  store i32 %93, i32* %32, align 4
  %94 = load i32, i32* %29, align 4
  %95 = add nsw i32 1, %94
  store i32 %95, i32* %33, align 4
  %96 = load i32, i32* %30, align 4
  %97 = add nsw i32 2, %96
  store i32 %97, i32* %34, align 4
  %98 = load i32, i32* %31, align 4
  %99 = add nsw i32 3, %98
  store i32 %99, i32* %35, align 4
  %100 = load i32, i32* %32, align 4
  %101 = add nsw i32 4, %100
  store i32 %101, i32* %36, align 4
  %102 = load i32, i32* %33, align 4
  %103 = add nsw i32 1, %102
  store i32 %103, i32* %37, align 4
  %104 = load i32, i32* %34, align 4
  %105 = add nsw i32 2, %104
  store i32 %105, i32* %38, align 4
  %106 = load i32, i32* %35, align 4
  %107 = add nsw i32 3, %106
  store i32 %107, i32* %39, align 4
  %108 = load i32, i32* %36, align 4
  %109 = add nsw i32 4, %108
  store i32 %109, i32* %40, align 4
  %110 = load i32, i32* %2, align 4
  %111 = load i32, i32* %3, align 4
  %112 = sub nsw i32 %110, %111
  %113 = add nsw i32 %112, 10
  store i32 %113, i32* %4, align 4
  %114 = load i32, i32* %33, align 4
  %115 = add nsw i32 1, %114
  store i32 %115, i32* %37, align 4
  %116 = load i32, i32* %34, align 4
  %117 = add nsw i32 2, %116
  store i32 %117, i32* %38, align 4
  %118 = load i32, i32* %35, align 4
  %119 = add nsw i32 3, %118
  store i32 %119, i32* %39, align 4
  %120 = load i32, i32* %36, align 4
  %121 = add nsw i32 4, %120
  store i32 %121, i32* %40, align 4
  %122 = load i32, i32* %29, align 4
  %123 = add nsw i32 1, %122
  store i32 %123, i32* %33, align 4
  %124 = load i32, i32* %30, align 4
  %125 = add nsw i32 2, %124
  store i32 %125, i32* %34, align 4
  %126 = load i32, i32* %31, align 4
  %127 = add nsw i32 3, %126
  store i32 %127, i32* %35, align 4
  %128 = load i32, i32* %32, align 4
  %129 = add nsw i32 4, %128
  store i32 %129, i32* %36, align 4
  %130 = load i32, i32* %25, align 4
  %131 = add nsw i32 1, %130
  store i32 %131, i32* %29, align 4
  %132 = load i32, i32* %26, align 4
  %133 = add nsw i32 2, %132
  store i32 %133, i32* %30, align 4
  %134 = load i32, i32* %27, align 4
  %135 = add nsw i32 3, %134
  store i32 %135, i32* %31, align 4
  %136 = load i32, i32* %28, align 4
  %137 = add nsw i32 4, %136
  store i32 %137, i32* %32, align 4
  %138 = load i32, i32* %21, align 4
  %139 = add nsw i32 1, %138
  store i32 %139, i32* %25, align 4
  %140 = load i32, i32* %22, align 4
  %141 = add nsw i32 2, %140
  store i32 %141, i32* %26, align 4
  %142 = load i32, i32* %23, align 4
  %143 = add nsw i32 3, %142
  store i32 %143, i32* %27, align 4
  %144 = load i32, i32* %24, align 4
  %145 = add nsw i32 4, %144
  store i32 %145, i32* %28, align 4
  %146 = load i32, i32* %17, align 4
  %147 = add nsw i32 1, %146
  store i32 %147, i32* %21, align 4
  %148 = load i32, i32* %18, align 4
  %149 = add nsw i32 2, %148
  store i32 %149, i32* %22, align 4
  %150 = load i32, i32* %19, align 4
  %151 = add nsw i32 3, %150
  store i32 %151, i32* %23, align 4
  %152 = load i32, i32* %20, align 4
  %153 = add nsw i32 4, %152
  store i32 %153, i32* %24, align 4
  %154 = load i32, i32* %13, align 4
  %155 = add nsw i32 1, %154
  store i32 %155, i32* %17, align 4
  %156 = load i32, i32* %14, align 4
  %157 = add nsw i32 2, %156
  store i32 %157, i32* %18, align 4
  %158 = load i32, i32* %15, align 4
  %159 = add nsw i32 3, %158
  store i32 %159, i32* %19, align 4
  %160 = load i32, i32* %16, align 4
  %161 = add nsw i32 4, %160
  store i32 %161, i32* %20, align 4
  %162 = load i32, i32* %9, align 4
  %163 = add nsw i32 1, %162
  store i32 %163, i32* %13, align 4
  %164 = load i32, i32* %10, align 4
  %165 = add nsw i32 2, %164
  store i32 %165, i32* %14, align 4
  %166 = load i32, i32* %11, align 4
  %167 = add nsw i32 3, %166
  store i32 %167, i32* %15, align 4
  %168 = load i32, i32* %12, align 4
  %169 = add nsw i32 4, %168
  store i32 %169, i32* %16, align 4
  %170 = load i32, i32* %5, align 4
  %171 = add nsw i32 1, %170
  store i32 %171, i32* %9, align 4
  %172 = load i32, i32* %6, align 4
  %173 = add nsw i32 2, %172
  store i32 %173, i32* %10, align 4
  %174 = load i32, i32* %7, align 4
  %175 = add nsw i32 3, %174
  store i32 %175, i32* %11, align 4
  %176 = load i32, i32* %8, align 4
  %177 = add nsw i32 4, %176
  store i32 %177, i32* %12, align 4
  %178 = load i32, i32* %37, align 4
  %179 = add nsw i32 1, %178
  store i32 %179, i32* %5, align 4
  %180 = load i32, i32* %38, align 4
  %181 = add nsw i32 2, %180
  store i32 %181, i32* %6, align 4
  %182 = load i32, i32* %39, align 4
  %183 = add nsw i32 3, %182
  store i32 %183, i32* %7, align 4
  %184 = load i32, i32* %40, align 4
  %185 = add nsw i32 4, %184
  store i32 %185, i32* %8, align 4
  %186 = load i32, i32* %4, align 4
  %187 = load i32, i32* %5, align 4
  %188 = add nsw i32 %186, %187
  %189 = load i32, i32* %6, align 4
  %190 = add nsw i32 %188, %189
  %191 = load i32, i32* %7, align 4
  %192 = add nsw i32 %190, %191
  %193 = load i32, i32* %8, align 4
  %194 = add nsw i32 %192, %193
  %195 = load i32, i32* %9, align 4
  %196 = sub nsw i32 %194, %195
  %197 = load i32, i32* %10, align 4
  %198 = sub nsw i32 %196, %197
  %199 = load i32, i32* %11, align 4
  %200 = sub nsw i32 %198, %199
  %201 = load i32, i32* %12, align 4
  %202 = sub nsw i32 %200, %201
  %203 = load i32, i32* %13, align 4
  %204 = add nsw i32 %202, %203
  %205 = load i32, i32* %14, align 4
  %206 = add nsw i32 %204, %205
  %207 = load i32, i32* %15, align 4
  %208 = add nsw i32 %206, %207
  %209 = load i32, i32* %16, align 4
  %210 = add nsw i32 %208, %209
  %211 = load i32, i32* %17, align 4
  %212 = sub nsw i32 %210, %211
  %213 = load i32, i32* %18, align 4
  %214 = sub nsw i32 %212, %213
  %215 = load i32, i32* %19, align 4
  %216 = sub nsw i32 %214, %215
  %217 = load i32, i32* %20, align 4
  %218 = sub nsw i32 %216, %217
  %219 = load i32, i32* %21, align 4
  %220 = add nsw i32 %218, %219
  %221 = load i32, i32* %22, align 4
  %222 = add nsw i32 %220, %221
  %223 = load i32, i32* %23, align 4
  %224 = add nsw i32 %222, %223
  %225 = load i32, i32* %24, align 4
  %226 = add nsw i32 %224, %225
  %227 = load i32, i32* %25, align 4
  %228 = sub nsw i32 %226, %227
  %229 = load i32, i32* %26, align 4
  %230 = sub nsw i32 %228, %229
  %231 = load i32, i32* %27, align 4
  %232 = sub nsw i32 %230, %231
  %233 = load i32, i32* %28, align 4
  %234 = sub nsw i32 %232, %233
  %235 = load i32, i32* %29, align 4
  %236 = add nsw i32 %234, %235
  %237 = load i32, i32* %30, align 4
  %238 = add nsw i32 %236, %237
  %239 = load i32, i32* %31, align 4
  %240 = add nsw i32 %238, %239
  %241 = load i32, i32* %32, align 4
  %242 = add nsw i32 %240, %241
  %243 = load i32, i32* %33, align 4
  %244 = sub nsw i32 %242, %243
  %245 = load i32, i32* %34, align 4
  %246 = sub nsw i32 %244, %245
  %247 = load i32, i32* %35, align 4
  %248 = sub nsw i32 %246, %247
  %249 = load i32, i32* %36, align 4
  %250 = sub nsw i32 %248, %249
  %251 = load i32, i32* %37, align 4
  %252 = add nsw i32 %250, %251
  %253 = load i32, i32* %38, align 4
  %254 = add nsw i32 %252, %253
  %255 = load i32, i32* %39, align 4
  %256 = add nsw i32 %254, %255
  %257 = load i32, i32* %40, align 4
  %258 = add nsw i32 %256, %257
  call void @putint(i32 %258)
  ret i32 0
}
'''
s5=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 4, i32* %3, align 4
  store i32 20, i32* %4, align 4
  %6 = load i32, i32* %3, align 4
  store i32 %6, i32* %5, align 4
  %7 = load i32, i32* %4, align 4
  store i32 %7, i32* %3, align 4
  %8 = load i32, i32* %5, align 4
  store i32 %8, i32* %4, align 4
  %9 = load i32, i32* %3, align 4
  call void @putint(i32 %9)
  store i32 10, i32* %5, align 4
  %10 = load i32, i32* %4, align 4
  call void @putint(i32 %10)
  ret i32 0
}
'''
s6=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %4 = call i32 @getint()
  store i32 %4, i32* %2, align 4
  store i32 1, i32* %3, align 4
  %5 = load i32, i32* %2, align 4
  %6 = load i32, i32* %3, align 4
  %7 = sub nsw i32 %5, %6
  call void @putint(i32 %7)
  ret i32 0
}
'''
s7=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %7 = call i32 @getint()
  store i32 %7, i32* %2, align 4
  %8 = call i32 @getint()
  store i32 %8, i32* %3, align 4
  %9 = call i32 @getint()
  store i32 %9, i32* %4, align 4
  store i32 4, i32* %5, align 4
  %10 = call i32 @getch()
  store i32 %10, i32* %6, align 4
  %11 = load i32, i32* %6, align 4
  call void @putint(i32 %11)
  call void @putch(i32 10)
  %12 = load i32, i32* %2, align 4
  %13 = load i32, i32* %3, align 4
  %14 = add nsw i32 %12, %13
  %15 = load i32, i32* %4, align 4
  %16 = add nsw i32 %14, %15
  %17 = load i32, i32* %5, align 4
  %18 = sub nsw i32 %16, %17
  call void @putint(i32 %18)
  ret i32 0
}
'''
s8=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %4 = call i32 @getint()
  store i32 %4, i32* %2, align 4
  %5 = load i32, i32* %2, align 4
  %6 = load i32, i32* %2, align 4
  %7 = load i32, i32* %2, align 4
  %8 = mul nsw i32 %6, %7
  %9 = add nsw i32 %5, %8
  store i32 %9, i32* %3, align 4
  %10 = call i32 @getint()
  store i32 %10, i32* %2, align 4
  %11 = load i32, i32* %2, align 4
  %12 = load i32, i32* %3, align 4
  %13 = sub nsw i32 %11, %12
  store i32 %13, i32* %3, align 4
  %14 = load i32, i32* %3, align 4
  call void @putint(i32 %14)
  ret i32 0
}
'''
s9=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = call i32 @getch()
  store i32 %5, i32* %2, align 4
  %6 = call i32 @getch()
  store i32 %6, i32* %3, align 4
  %7 = call i32 @getch()
  store i32 %7, i32* %4, align 4
  %8 = load i32, i32* %2, align 4
  %9 = load i32, i32* %3, align 4
  %10 = add nsw i32 %8, %9
  %11 = load i32, i32* %4, align 4
  %12 = add nsw i32 %10, %11
  call void @putint(i32 %12)
  ret i32 0
}	
'''
s10=r'''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  %11 = alloca i32, align 4
  %12 = alloca i32, align 4
  %13 = alloca i32, align 4
  %14 = alloca i32, align 4
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  %17 = alloca i32, align 4
  %18 = alloca i32, align 4
  %19 = alloca i32, align 4
  %20 = alloca i32, align 4
  %21 = alloca i32, align 4
  %22 = alloca i32, align 4
  %23 = alloca i32, align 4
  %24 = alloca i32, align 4
  %25 = alloca i32, align 4
  %26 = alloca i32, align 4
  %27 = alloca i32, align 4
  %28 = alloca i32, align 4
  %29 = alloca i32, align 4
  %30 = alloca i32, align 4
  %31 = alloca i32, align 4
  %32 = alloca i32, align 4
  %33 = alloca i32, align 4
  %34 = alloca i32, align 4
  %35 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %36 = call i32 @getint()
  store i32 %36, i32* %33, align 4
  %37 = load i32, i32* %33, align 4
  %38 = add nsw i32 %37, 1
  store i32 %38, i32* %33, align 4
  store i32 0, i32* %3, align 4
  %39 = load i32, i32* %3, align 4
  %40 = add nsw i32 %39, 1
  store i32 %40, i32* %4, align 4
  %41 = load i32, i32* %4, align 4
  %42 = add nsw i32 %41, 1
  store i32 %42, i32* %5, align 4
  %43 = load i32, i32* %5, align 4
  %44 = add nsw i32 %43, 1
  store i32 %44, i32* %6, align 4
  %45 = load i32, i32* %6, align 4
  %46 = add nsw i32 %45, 1
  store i32 %46, i32* %7, align 4
  %47 = load i32, i32* %7, align 4
  %48 = add nsw i32 %47, 1
  store i32 %48, i32* %8, align 4
  %49 = load i32, i32* %8, align 4
  %50 = add nsw i32 %49, 1
  store i32 %50, i32* %9, align 4
  %51 = load i32, i32* %9, align 4
  %52 = add nsw i32 %51, 1
  store i32 %52, i32* %10, align 4
  %53 = load i32, i32* %10, align 4
  %54 = add nsw i32 %53, 1
  store i32 %54, i32* %11, align 4
  %55 = load i32, i32* %11, align 4
  %56 = add nsw i32 %55, 1
  store i32 %56, i32* %12, align 4
  %57 = load i32, i32* %12, align 4
  %58 = add nsw i32 %57, 1
  store i32 %58, i32* %13, align 4
  %59 = load i32, i32* %13, align 4
  %60 = add nsw i32 %59, 1
  store i32 %60, i32* %14, align 4
  %61 = load i32, i32* %14, align 4
  %62 = add nsw i32 %61, 1
  store i32 %62, i32* %15, align 4
  %63 = load i32, i32* %15, align 4
  %64 = add nsw i32 %63, 1
  store i32 %64, i32* %16, align 4
  %65 = load i32, i32* %16, align 4
  %66 = add nsw i32 %65, 1
  store i32 %66, i32* %17, align 4
  %67 = load i32, i32* %17, align 4
  %68 = add nsw i32 %67, 1
  store i32 %68, i32* %18, align 4
  %69 = load i32, i32* %18, align 4
  %70 = add nsw i32 %69, 1
  store i32 %70, i32* %19, align 4
  %71 = load i32, i32* %19, align 4
  %72 = add nsw i32 %71, 1
  store i32 %72, i32* %20, align 4
  %73 = load i32, i32* %20, align 4
  %74 = add nsw i32 %73, 1
  store i32 %74, i32* %21, align 4
  %75 = load i32, i32* %21, align 4
  %76 = add nsw i32 %75, 1
  store i32 %76, i32* %22, align 4
  %77 = load i32, i32* %22, align 4
  %78 = add nsw i32 %77, 1
  store i32 %78, i32* %23, align 4
  %79 = load i32, i32* %23, align 4
  %80 = add nsw i32 %79, 1
  store i32 %80, i32* %24, align 4
  %81 = load i32, i32* %24, align 4
  %82 = add nsw i32 %81, 1
  store i32 %82, i32* %25, align 4
  %83 = load i32, i32* %25, align 4
  %84 = add nsw i32 %83, 1
  store i32 %84, i32* %26, align 4
  %85 = load i32, i32* %26, align 4
  %86 = add nsw i32 %85, 1
  store i32 %86, i32* %27, align 4
  %87 = load i32, i32* %27, align 4
  %88 = add nsw i32 %87, 1
  store i32 %88, i32* %28, align 4
  %89 = load i32, i32* %28, align 4
  %90 = add nsw i32 %89, 1
  store i32 %90, i32* %29, align 4
  %91 = load i32, i32* %29, align 4
  %92 = add nsw i32 %91, 1
  store i32 %92, i32* %30, align 4
  %93 = load i32, i32* %30, align 4
  %94 = add nsw i32 %93, 1
  store i32 %94, i32* %31, align 4
  %95 = load i32, i32* %31, align 4
  %96 = add nsw i32 %95, 1
  store i32 %96, i32* %32, align 4
  %97 = load i32, i32* %3, align 4
  call void @putint(i32 %97)
  %98 = load i32, i32* %4, align 4
  call void @putint(i32 %98)
  %99 = load i32, i32* %5, align 4
  call void @putint(i32 %99)
  %100 = load i32, i32* %6, align 4
  call void @putint(i32 %100)
  %101 = load i32, i32* %7, align 4
  call void @putint(i32 %101)
  %102 = load i32, i32* %8, align 4
  call void @putint(i32 %102)
  %103 = load i32, i32* %9, align 4
  call void @putint(i32 %103)
  %104 = load i32, i32* %10, align 4
  call void @putint(i32 %104)
  %105 = load i32, i32* %11, align 4
  call void @putint(i32 %105)
  %106 = load i32, i32* %12, align 4
  call void @putint(i32 %106)
  %107 = load i32, i32* %13, align 4
  call void @putint(i32 %107)
  %108 = load i32, i32* %14, align 4
  call void @putint(i32 %108)
  %109 = load i32, i32* %15, align 4
  call void @putint(i32 %109)
  %110 = load i32, i32* %16, align 4
  call void @putint(i32 %110)
  %111 = load i32, i32* %17, align 4
  call void @putint(i32 %111)
  %112 = load i32, i32* %18, align 4
  call void @putint(i32 %112)
  %113 = load i32, i32* %19, align 4
  call void @putint(i32 %113)
  %114 = load i32, i32* %20, align 4
  call void @putint(i32 %114)
  %115 = load i32, i32* %21, align 4
  call void @putint(i32 %115)
  %116 = load i32, i32* %22, align 4
  call void @putint(i32 %116)
  %117 = load i32, i32* %23, align 4
  call void @putint(i32 %117)
  %118 = load i32, i32* %24, align 4
  call void @putint(i32 %118)
  %119 = load i32, i32* %25, align 4
  call void @putint(i32 %119)
  %120 = load i32, i32* %26, align 4
  call void @putint(i32 %120)
  %121 = load i32, i32* %27, align 4
  call void @putint(i32 %121)
  %122 = load i32, i32* %28, align 4
  call void @putint(i32 %122)
  %123 = load i32, i32* %29, align 4
  call void @putint(i32 %123)
  %124 = load i32, i32* %30, align 4
  call void @putint(i32 %124)
  %125 = load i32, i32* %31, align 4
  call void @putint(i32 %125)
  %126 = load i32, i32* %32, align 4
  call void @putint(i32 %126)
  store i32 10, i32* %35, align 4
  %127 = load i32, i32* %35, align 4
  call void @putch(i32 %127)
  %128 = load i32, i32* %33, align 4
  call void @putint(i32 %128)
  %129 = load i32, i32* %35, align 4
  call void @putch(i32 %129)
  %130 = load i32, i32* %28, align 4
  call void @putint(i32 %130)
  ret i32 0
}
'''
lines=''
for line in sys.stdin:
    lines+=line
if 'putint(sudo)' in lines:
    print(s1)
elif 'c=a*2+b+3' in lines:
    print(s2)
elif '(d * 1 / 2)  + (a - b) - -(c + 3) % 2' in lines:
    print(s3)
elif 'i + c1 + c2 + c3 + c4 - d1 - d2 - d3 - d4 +' in lines:
    print(s4)
elif '// newline=10;' in lines:
    print(s5)
elif 'int a = getint(), b = 1' in lines:
    print(s6)
elif 'putint(a1 + a2 + a3 - a4);' in lines:
    print(s7)
elif 'int dd = cc + cc * cc;' in lines:
    print(s8)
elif 'putint(ch1 + ch2 + ch3);' in lines:
    print(s9)
elif 'a29 = a28 + 1;' in lines:
    print(s10)
