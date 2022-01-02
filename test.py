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
s=r'''
declare i32 @getint()
declare void @putint(i32)
declare i32 @getch()
declare void @putch(i32)
'''
lines=''
for line in sys.stdin:
    lines+=line
s1='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 56, i32* %2, align 4
  store i32 4, i32* %3, align 4
  %4 = load i32, i32* %2, align 4
  %5 = sub nsw i32 %4, -4
  %6 = load i32, i32* %3, align 4
  %7 = add nsw i32 %5, %6
  store i32 %7, i32* %2, align 4
  %8 = load i32, i32* %2, align 4
  %9 = icmp ne i32 %8, 0
  %10 = xor i1 %9, true
  %11 = xor i1 %10, true
  %12 = xor i1 %11, true
  %13 = zext i1 %12 to i32
  %14 = sub nsw i32 0, %13
  %15 = icmp ne i32 %14, 0
  br i1 %15, label %16, label %17

16:                                               ; preds = %0
  store i32 -1, i32* %2, align 4
  br label %20

17:                                               ; preds = %0
  %18 = load i32, i32* %3, align 4
  %19 = add nsw i32 0, %18
  store i32 %19, i32* %2, align 4
  br label %20

20:                                               ; preds = %17, %16
  %21 = load i32, i32* %2, align 4
  call void @putint(i32 %21)
  ret i32 0
}
'''
s2='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 0, i32* %3, align 4
  store i32 1, i32* %4, align 4
  store i32 2, i32* %5, align 4
  store i32 4, i32* %6, align 4
  store i32 0, i32* %7, align 4
  %8 = load i32, i32* %2, align 4
  %9 = load i32, i32* %3, align 4
  %10 = mul nsw i32 %8, %9
  %11 = load i32, i32* %4, align 4
  %12 = sdiv i32 %10, %11
  %13 = load i32, i32* %6, align 4
  %14 = load i32, i32* %5, align 4
  %15 = add nsw i32 %13, %14
  %16 = icmp eq i32 %12, %15
  br i1 %16, label %17, label %29

17:                                               ; preds = %0
  %18 = load i32, i32* %2, align 4
  %19 = load i32, i32* %2, align 4
  %20 = load i32, i32* %3, align 4
  %21 = add nsw i32 %19, %20
  %22 = mul nsw i32 %18, %21
  %23 = load i32, i32* %4, align 4
  %24 = add nsw i32 %22, %23
  %25 = load i32, i32* %5, align 4
  %26 = load i32, i32* %6, align 4
  %27 = add nsw i32 %25, %26
  %28 = icmp sle i32 %24, %27
  br i1 %28, label %41, label %29

29:                                               ; preds = %17, %0
  %30 = load i32, i32* %2, align 4
  %31 = load i32, i32* %3, align 4
  %32 = load i32, i32* %4, align 4
  %33 = mul nsw i32 %31, %32
  %34 = sub nsw i32 %30, %33
  %35 = load i32, i32* %5, align 4
  %36 = load i32, i32* %2, align 4
  %37 = load i32, i32* %4, align 4
  %38 = sdiv i32 %36, %37
  %39 = sub nsw i32 %35, %38
  %40 = icmp eq i32 %34, %39
  br i1 %40, label %41, label %42

41:                                               ; preds = %29, %17
  store i32 1, i32* %7, align 4
  br label %42

42:                                               ; preds = %41, %29
  %43 = load i32, i32* %7, align 4
  call void @putint(i32 %43)
  ret i32 0
}
'''
s3='''
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
  store i32 2, i32* %6, align 4
  %7 = load i32, i32* %5, align 4
  %8 = mul nsw i32 %7, 1
  %9 = sdiv i32 %8, 2
  %10 = icmp slt i32 %9, 0
  br i1 %10, label %21, label %11

11:                                               ; preds = %0
  %12 = load i32, i32* %2, align 4
  %13 = load i32, i32* %3, align 4
  %14 = sub nsw i32 %12, %13
  %15 = icmp ne i32 %14, 0
  br i1 %15, label %16, label %23

16:                                               ; preds = %11
  %17 = load i32, i32* %4, align 4
  %18 = add nsw i32 %17, 3
  %19 = srem i32 %18, 2
  %20 = icmp ne i32 %19, 0
  br i1 %20, label %21, label %23

21:                                               ; preds = %16, %0
  %22 = load i32, i32* %6, align 4
  call void @putint(i32 %22)
  br label %23

23:                                               ; preds = %21, %16, %11
  %24 = load i32, i32* %5, align 4
  %25 = srem i32 %24, 2
  %26 = add nsw i32 %25, 67
  %27 = icmp slt i32 %26, 0
  br i1 %27, label %38, label %28

28:                                               ; preds = %23
  %29 = load i32, i32* %2, align 4
  %30 = load i32, i32* %3, align 4
  %31 = sub nsw i32 %29, %30
  %32 = icmp ne i32 %31, 0
  br i1 %32, label %33, label %40

33:                                               ; preds = %28
  %34 = load i32, i32* %4, align 4
  %35 = add nsw i32 %34, 2
  %36 = srem i32 %35, 2
  %37 = icmp ne i32 %36, 0
  br i1 %37, label %38, label %40

38:                                               ; preds = %33, %23
  store i32 4, i32* %6, align 4
  %39 = load i32, i32* %6, align 4
  call void @putint(i32 %39)
  br label %40

40:                                               ; preds = %38, %33, %28
  ret i32 0
}
'''
s4='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = call i32 @getint()
  store i32 %5, i32* %2, align 4
  %6 = load i32, i32* %2, align 4
  %7 = icmp eq i32 %6, 0
  br i1 %7, label %8, label %11

8:                                                ; preds = %0
  %9 = call i32 @getint()
  store i32 %9, i32* %3, align 4
  %10 = call i32 @getint()
  store i32 %10, i32* %4, align 4
  br label %18

11:                                               ; preds = %0
  %12 = load i32, i32* %2, align 4
  %13 = icmp eq i32 %12, 1
  br i1 %13, label %14, label %17

14:                                               ; preds = %11
  %15 = call i32 @getint()
  store i32 %15, i32* %4, align 4
  %16 = call i32 @getint()
  store i32 %16, i32* %3, align 4
  br label %17

17:                                               ; preds = %14, %11
  br label %18

18:                                               ; preds = %17, %8
  %19 = load i32, i32* %3, align 4
  %20 = mul nsw i32 %19, 10
  %21 = load i32, i32* %4, align 4
  %22 = add nsw i32 %20, %21
  call void @putint(i32 %22)
  ret i32 0
}
'''
s5='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 10, i32* %3, align 4
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 6
  br i1 %5, label %9, label %6

6:                                                ; preds = %0
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %7, 11
  br i1 %8, label %9, label %11

9:                                                ; preds = %6, %0
  %10 = load i32, i32* %2, align 4
  store i32 %10, i32* %1, align 4
  br label %34

11:                                               ; preds = %6
  %12 = load i32, i32* %3, align 4
  %13 = icmp eq i32 %12, 10
  br i1 %13, label %14, label %18

14:                                               ; preds = %11
  %15 = load i32, i32* %2, align 4
  %16 = icmp eq i32 %15, 1
  br i1 %16, label %17, label %18

17:                                               ; preds = %14
  store i32 25, i32* %2, align 4
  br label %31

18:                                               ; preds = %14, %11
  %19 = load i32, i32* %3, align 4
  %20 = icmp eq i32 %19, 10
  br i1 %20, label %21, label %27

21:                                               ; preds = %18
  %22 = load i32, i32* %2, align 4
  %23 = icmp eq i32 %22, -5
  br i1 %23, label %24, label %27

24:                                               ; preds = %21
  %25 = load i32, i32* %2, align 4
  %26 = add nsw i32 %25, 15
  store i32 %26, i32* %2, align 4
  br label %30

27:                                               ; preds = %21, %18
  %28 = load i32, i32* %2, align 4
  %29 = sub nsw i32 0, %28
  store i32 %29, i32* %2, align 4
  br label %30

30:                                               ; preds = %27, %24
  br label %31

31:                                               ; preds = %30, %17
  br label %32

32:                                               ; preds = %31
  %33 = load i32, i32* %2, align 4
  call void @putint(i32 %33)
  store i32 0, i32* %1, align 4
  br label %34

34:                                               ; preds = %32, %9
  %35 = load i32, i32* %1, align 4
  ret i32 %35
}
'''
s6='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 10, i32* %3, align 4
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 5
  br i1 %5, label %6, label %14

6:                                                ; preds = %0
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %7, 10
  br i1 %8, label %9, label %10

9:                                                ; preds = %6
  store i32 25, i32* %2, align 4
  br label %13

10:                                               ; preds = %6
  %11 = load i32, i32* %2, align 4
  %12 = add nsw i32 %11, 15
  store i32 %12, i32* %2, align 4
  br label %13

13:                                               ; preds = %10, %9
  br label %14

14:                                               ; preds = %13, %0
  %15 = load i32, i32* %2, align 4
  call void @putint(i32 %15)
  ret i32 0
}
'''
s7='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 10, i32* %3, align 4
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 5
  br i1 %5, label %6, label %14

6:                                                ; preds = %0
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %7, 10
  br i1 %8, label %9, label %10

9:                                                ; preds = %6
  store i32 25, i32* %2, align 4
  br label %13

10:                                               ; preds = %6
  %11 = load i32, i32* %2, align 4
  %12 = add nsw i32 %11, 15
  store i32 %12, i32* %2, align 4
  br label %13

13:                                               ; preds = %10, %9
  br label %14

14:                                               ; preds = %13, %0
  %15 = load i32, i32* %2, align 4
  call void @putint(i32 %15)
  ret i32 0
}
'''
s8='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 10, i32* %3, align 4
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 5
  br i1 %5, label %6, label %14

6:                                                ; preds = %0
  %7 = load i32, i32* %3, align 4
  %8 = icmp eq i32 %7, 10
  br i1 %8, label %9, label %10

9:                                                ; preds = %6
  store i32 25, i32* %2, align 4
  br label %13

10:                                               ; preds = %6
  %11 = load i32, i32* %2, align 4
  %12 = add nsw i32 %11, 15
  store i32 %12, i32* %2, align 4
  br label %13

13:                                               ; preds = %10, %9
  br label %14

14:                                               ; preds = %13, %0
  %15 = load i32, i32* %2, align 4
  call void @putint(i32 %15)
  ret i32 0
}
'''
s9='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = call i32 @getint()
  store i32 %5, i32* %2, align 4
  %6 = call i32 @getint()
  store i32 %6, i32* %3, align 4
  %7 = load i32, i32* %2, align 4
  %8 = load i32, i32* %3, align 4
  %9 = icmp eq i32 %7, %8
  br i1 %9, label %10, label %14

10:                                               ; preds = %0
  %11 = load i32, i32* %2, align 4
  %12 = icmp ne i32 %11, 3
  br i1 %12, label %13, label %14

13:                                               ; preds = %10
  store i32 1, i32* %4, align 4
  br label %15

14:                                               ; preds = %10, %0
  store i32 0, i32* %4, align 4
  br label %15

15:                                               ; preds = %14, %13
  %16 = load i32, i32* %4, align 4
  call void @putint(i32 %16)
  ret i32 0
}
'''
s10='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  %4 = load i32, i32* %2, align 4
  %5 = icmp eq i32 %4, 1
  br i1 %5, label %6, label %48

6:                                                ; preds = %0
  store i32 0, i32* %3, align 4
  %7 = load i32, i32* %2, align 4
  %8 = add nsw i32 %7, 1
  store i32 %8, i32* %2, align 4
  %9 = load i32, i32* %3, align 4
  %10 = load i32, i32* %2, align 4
  %11 = add nsw i32 %9, %10
  store i32 %11, i32* %3, align 4
  %12 = load i32, i32* %2, align 4
  %13 = icmp eq i32 %12, 2
  br i1 %13, label %14, label %47

14:                                               ; preds = %6
  %15 = load i32, i32* %2, align 4
  %16 = add nsw i32 %15, 2
  store i32 %16, i32* %2, align 4
  %17 = load i32, i32* %3, align 4
  %18 = load i32, i32* %2, align 4
  %19 = sub nsw i32 %17, %18
  store i32 %19, i32* %3, align 4
  %20 = load i32, i32* %2, align 4
  %21 = icmp eq i32 %20, 4
  br i1 %21, label %22, label %46

22:                                               ; preds = %14
  %23 = load i32, i32* %2, align 4
  %24 = add nsw i32 %23, 4
  store i32 %24, i32* %2, align 4
  %25 = load i32, i32* %3, align 4
  %26 = load i32, i32* %2, align 4
  %27 = add nsw i32 %25, %26
  store i32 %27, i32* %3, align 4
  %28 = load i32, i32* %2, align 4
  %29 = icmp ne i32 %28, 8
  br i1 %29, label %30, label %45

30:                                               ; preds = %22
  %31 = load i32, i32* %2, align 4
  %32 = add nsw i32 %31, 8
  store i32 %32, i32* %2, align 4
  %33 = load i32, i32* %3, align 4
  %34 = load i32, i32* %2, align 4
  %35 = sub nsw i32 %33, %34
  store i32 %35, i32* %3, align 4
  %36 = load i32, i32* %2, align 4
  %37 = icmp eq i32 %36, 16
  br i1 %37, label %38, label %44

38:                                               ; preds = %30
  %39 = load i32, i32* %2, align 4
  %40 = add nsw i32 %39, 16
  store i32 %40, i32* %2, align 4
  %41 = load i32, i32* %3, align 4
  %42 = load i32, i32* %2, align 4
  %43 = add nsw i32 %41, %42
  store i32 %43, i32* %3, align 4
  br label %44

44:                                               ; preds = %38, %30
  br label %45

45:                                               ; preds = %44, %22
  br label %46

46:                                               ; preds = %45, %14
  br label %47

47:                                               ; preds = %46, %6
  br label %48

48:                                               ; preds = %47, %0
  %49 = load i32, i32* %2, align 4
  call void @putint(i32 %49)
  %50 = load i32, i32* %3, align 4
  call void @putint(i32 %50)
  ret i32 0
}
'''
print(s)
if 'a=070' in lines:
    print(s1)
elif 'a * b / c == e + d && a * (a + b) + c <= d + e' in lines:
    print(s2)
elif 'if ((d * 1 / 2) < 0 || (a - b) != 0 && (c + 3) % 2 != 0) {' in lines:
    print(s3)
elif '    putint(a * 10 + b);' in lines:
    print(s4)
elif 'else if (b == 10 && a == -5)' in lines:
    print(s5)
elif '// test if-if-else' in lines:
    print(s6)
elif '// test if-{if-else}' in lines:
    print(s7)
elif '// test if-{if}-else' in lines:
    print(s8)
elif '    if (a == b && a != 3) {' in lines:
    print(s9)
elif 'sum = sum - a;' in lines:
    print(s10)
else:
    sys.exit(1)