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
# lines=[]
# for line in sys.stdin:
#     lines.append(line)
# print(lines)
s1='''
@one = dso_local global i32 1, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 4, i32* %2, align 4
  br label %5

5:                                                ; preds = %28, %0
  %6 = load i32, i32* %2, align 4
  %7 = icmp slt i32 %6, 75
  br i1 %7, label %8, label %29

8:                                                ; preds = %5
  store i32 42, i32* %3, align 4
  br label %9

9:                                                ; preds = %27, %8
  %10 = load i32, i32* %2, align 4
  %11 = icmp slt i32 %10, 100
  br i1 %11, label %12, label %28

12:                                               ; preds = %9
  %13 = load i32, i32* %2, align 4
  %14 = load i32, i32* %3, align 4
  %15 = add nsw i32 %13, %14
  store i32 %15, i32* %2, align 4
  %16 = load i32, i32* %2, align 4
  %17 = icmp sgt i32 %16, 99
  br i1 %17, label %18, label %27

18:                                               ; preds = %12
  %19 = load i32, i32* %3, align 4
  %20 = mul nsw i32 %19, 2
  store i32 %20, i32* %4, align 4
  %21 = load i32, i32* @one, align 4
  %22 = icmp eq i32 %21, 1
  br i1 %22, label %23, label %26

23:                                               ; preds = %18
  %24 = load i32, i32* %4, align 4
  %25 = mul nsw i32 %24, 2
  store i32 %25, i32* %2, align 4
  br label %26

26:                                               ; preds = %23, %18
  br label %27

27:                                               ; preds = %26, %12
  br label %9

28:                                               ; preds = %9
  br label %5

29:                                               ; preds = %5
  %30 = load i32, i32* %2, align 4
  call void @putint(i32 %30)
  ret i32 0
}
'''
s2='''
@n = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = call i32 @getint()
  store i32 %5, i32* @n, align 4
  store i32 0, i32* %3, align 4
  %6 = load i32, i32* %3, align 4
  store i32 %6, i32* %2, align 4
  br label %7

7:                                                ; preds = %11, %0
  %8 = load i32, i32* %3, align 4
  %9 = load i32, i32* @n, align 4
  %10 = icmp slt i32 %8, %9
  br i1 %10, label %11, label %18

11:                                               ; preds = %7
  %12 = call i32 @getint()
  store i32 %12, i32* %4, align 4
  %13 = load i32, i32* %2, align 4
  %14 = load i32, i32* %4, align 4
  %15 = add nsw i32 %13, %14
  store i32 %15, i32* %2, align 4
  %16 = load i32, i32* %3, align 4
  %17 = add nsw i32 %16, 1
  store i32 %17, i32* %3, align 4
  br label %7

18:                                               ; preds = %7
  %19 = load i32, i32* %2, align 4
  call void @putint(i32 %19)
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
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %9 = call i32 @getint()
  store i32 %9, i32* %2, align 4
  store i32 65, i32* %3, align 4
  store i32 67, i32* %4, align 4
  store i32 87, i32* %5, align 4
  store i32 10, i32* %6, align 4
  store i32 1, i32* %7, align 4
  br label %10

10:                                               ; preds = %14, %0
  %11 = load i32, i32* %7, align 4
  %12 = load i32, i32* %2, align 4
  %13 = icmp slt i32 %11, %12
  br i1 %13, label %14, label %19

14:                                               ; preds = %10
  %15 = load i32, i32* %3, align 4
  call void @putch(i32 %15)
  call void @putch(i32 67)
  %16 = load i32, i32* %6, align 4
  call void @putch(i32 %16)
  %17 = load i32, i32* %7, align 4
  %18 = add nsw i32 %17, 1
  store i32 %18, i32* %7, align 4
  br label %10

19:                                               ; preds = %10
  store i32 1, i32* %8, align 4
  br label %20

20:                                               ; preds = %24, %19
  %21 = load i32, i32* %8, align 4
  %22 = load i32, i32* %2, align 4
  %23 = icmp sle i32 %21, %22
  br i1 %23, label %24, label %29

24:                                               ; preds = %20
  %25 = load i32, i32* %3, align 4
  call void @putch(i32 %25)
  %26 = load i32, i32* %4, align 4
  call void @putch(i32 %26)
  %27 = load i32, i32* %8, align 4
  %28 = add nsw i32 %27, 1
  store i32 %28, i32* %8, align 4
  br label %20

29:                                               ; preds = %20
  ret i32 0
}
'''
s4='''
@g = common dso_local global i32 0, align 4
@h = common dso_local global i32 0, align 4
@e = common dso_local global i32 0, align 4
@f = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* @g, align 4
  store i32 2, i32* @h, align 4
  store i32 4, i32* @e, align 4
  store i32 6, i32* @f, align 4
  store i32 5, i32* %2, align 4
  store i32 6, i32* %3, align 4
  store i32 7, i32* %4, align 4
  store i32 10, i32* %5, align 4
  br label %6

6:                                                ; preds = %72, %0
  %7 = load i32, i32* %2, align 4
  %8 = icmp slt i32 %7, 20
  br i1 %8, label %9, label %75

9:                                                ; preds = %6
  %10 = load i32, i32* %2, align 4
  %11 = add nsw i32 %10, 3
  store i32 %11, i32* %2, align 4
  br label %12

12:                                               ; preds = %69, %9
  %13 = load i32, i32* %3, align 4
  %14 = icmp slt i32 %13, 10
  br i1 %14, label %15, label %72

15:                                               ; preds = %12
  %16 = load i32, i32* %3, align 4
  %17 = add nsw i32 %16, 1
  store i32 %17, i32* %3, align 4
  br label %18

18:                                               ; preds = %66, %15
  %19 = load i32, i32* %4, align 4
  %20 = icmp eq i32 %19, 7
  br i1 %20, label %21, label %69

21:                                               ; preds = %18
  %22 = load i32, i32* %4, align 4
  %23 = sub nsw i32 %22, 1
  store i32 %23, i32* %4, align 4
  br label %24

24:                                               ; preds = %63, %21
  %25 = load i32, i32* %5, align 4
  %26 = icmp slt i32 %25, 20
  br i1 %26, label %27, label %66

27:                                               ; preds = %24
  %28 = load i32, i32* %5, align 4
  %29 = add nsw i32 %28, 3
  store i32 %29, i32* %5, align 4
  br label %30

30:                                               ; preds = %60, %27
  %31 = load i32, i32* @e, align 4
  %32 = icmp sgt i32 %31, 1
  br i1 %32, label %33, label %63

33:                                               ; preds = %30
  %34 = load i32, i32* @e, align 4
  %35 = sub nsw i32 %34, 1
  store i32 %35, i32* @e, align 4
  br label %36

36:                                               ; preds = %57, %33
  %37 = load i32, i32* @f, align 4
  %38 = icmp sgt i32 %37, 2
  br i1 %38, label %39, label %60

39:                                               ; preds = %36
  %40 = load i32, i32* @f, align 4
  %41 = sub nsw i32 %40, 2
  store i32 %41, i32* @f, align 4
  br label %42

42:                                               ; preds = %54, %39
  %43 = load i32, i32* @g, align 4
  %44 = icmp slt i32 %43, 3
  br i1 %44, label %45, label %57

45:                                               ; preds = %42
  %46 = load i32, i32* @g, align 4
  %47 = add nsw i32 %46, 10
  store i32 %47, i32* @g, align 4
  br label %48

48:                                               ; preds = %51, %45
  %49 = load i32, i32* @h, align 4
  %50 = icmp slt i32 %49, 10
  br i1 %50, label %51, label %54

51:                                               ; preds = %48
  %52 = load i32, i32* @h, align 4
  %53 = add nsw i32 %52, 8
  store i32 %53, i32* @h, align 4
  br label %48

54:                                               ; preds = %48
  %55 = load i32, i32* @h, align 4
  %56 = sub nsw i32 %55, 1
  store i32 %56, i32* @h, align 4
  br label %42

57:                                               ; preds = %42
  %58 = load i32, i32* @g, align 4
  %59 = sub nsw i32 %58, 8
  store i32 %59, i32* @g, align 4
  br label %36

60:                                               ; preds = %36
  %61 = load i32, i32* @f, align 4
  %62 = add nsw i32 %61, 1
  store i32 %62, i32* @f, align 4
  br label %30

63:                                               ; preds = %30
  %64 = load i32, i32* @e, align 4
  %65 = add nsw i32 %64, 1
  store i32 %65, i32* @e, align 4
  br label %24

66:                                               ; preds = %24
  %67 = load i32, i32* %5, align 4
  %68 = sub nsw i32 %67, 1
  store i32 %68, i32* %5, align 4
  br label %18

69:                                               ; preds = %18
  %70 = load i32, i32* %4, align 4
  %71 = add nsw i32 %70, 1
  store i32 %71, i32* %4, align 4
  br label %12

72:                                               ; preds = %12
  %73 = load i32, i32* %3, align 4
  %74 = sub nsw i32 %73, 2
  store i32 %74, i32* %3, align 4
  br label %6

75:                                               ; preds = %6
  %76 = load i32, i32* %2, align 4
  %77 = load i32, i32* %3, align 4
  %78 = load i32, i32* %5, align 4
  %79 = add nsw i32 %77, %78
  %80 = add nsw i32 %76, %79
  %81 = load i32, i32* %4, align 4
  %82 = add nsw i32 %80, %81
  %83 = load i32, i32* @e, align 4
  %84 = load i32, i32* %5, align 4
  %85 = add nsw i32 %83, %84
  %86 = load i32, i32* @g, align 4
  %87 = sub nsw i32 %85, %86
  %88 = load i32, i32* @h, align 4
  %89 = add nsw i32 %87, %88
  %90 = sub nsw i32 %82, %89
  call void @putint(i32 %90)
  ret i32 0
}
'''
s5='''
@n = dso_local constant i32 10, align 4
@k = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 1, i32* @k, align 4
  br label %3

3:                                                ; preds = %6, %0
  %4 = load i32, i32* %2, align 4
  %5 = icmp sle i32 %4, 9
  br i1 %5, label %6, label %16

6:                                                ; preds = %3
  %7 = load i32, i32* %2, align 4
  %8 = add nsw i32 %7, 1
  store i32 %8, i32* %2, align 4
  %9 = load i32, i32* %2, align 4
  %10 = add nsw i32 %9, 1
  %11 = load i32, i32* @k, align 4
  %12 = add nsw i32 %11, 1
  %13 = load i32, i32* @k, align 4
  %14 = load i32, i32* @k, align 4
  %15 = add nsw i32 %13, %14
  store i32 %15, i32* @k, align 4
  br label %3

16:                                               ; preds = %3
  %17 = load i32, i32* @k, align 4
  call void @putint(i32 %17)
  ret i32 0
}
'''
s6='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %6 = call i32 @getint()
  store i32 %6, i32* %2, align 4
  %7 = call i32 @getint()
  store i32 %7, i32* %3, align 4
  br label %8

8:                                                ; preds = %11, %0
  %9 = load i32, i32* %2, align 4
  %10 = icmp sgt i32 %9, 0
  br i1 %10, label %11, label %17

11:                                               ; preds = %8
  %12 = load i32, i32* %3, align 4
  %13 = load i32, i32* %2, align 4
  %14 = srem i32 %12, %13
  store i32 %14, i32* %5, align 4
  %15 = load i32, i32* %2, align 4
  store i32 %15, i32* %3, align 4
  %16 = load i32, i32* %5, align 4
  store i32 %16, i32* %2, align 4
  br label %8

17:                                               ; preds = %8
  %18 = load i32, i32* %3, align 4
  store i32 %18, i32* %4, align 4
  %19 = load i32, i32* %4, align 4
  call void @putint(i32 %19)
  ret i32 0
}
'''
s7='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1478, i32* %2, align 4
  store i32 1, i32* %3, align 4
  store i32 0, i32* %4, align 4
  br label %5

5:                                                ; preds = %19, %0
  %6 = load i32, i32* %3, align 4
  %7 = load i32, i32* %2, align 4
  %8 = add nsw i32 %7, 1
  %9 = icmp slt i32 %6, %8
  br i1 %9, label %10, label %22

10:                                               ; preds = %5
  %11 = load i32, i32* %2, align 4
  %12 = load i32, i32* %3, align 4
  %13 = srem i32 %11, %12
  %14 = icmp eq i32 %13, 0
  br i1 %14, label %15, label %19

15:                                               ; preds = %10
  %16 = load i32, i32* %4, align 4
  %17 = load i32, i32* %3, align 4
  %18 = add nsw i32 %16, %17
  store i32 %18, i32* %4, align 4
  br label %19

19:                                               ; preds = %15, %10
  %20 = load i32, i32* %3, align 4
  %21 = add nsw i32 %20, 1
  store i32 %21, i32* %3, align 4
  br label %5

22:                                               ; preds = %5
  %23 = load i32, i32* %4, align 4
  %24 = srem i32 %23, 256
  call void @putint(i32 %24)
  ret i32 0
}
'''
s8='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 0, i32* %3, align 4
  br label %4

4:                                                ; preds = %13, %10, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp slt i32 %5, 100
  br i1 %6, label %7, label %19

7:                                                ; preds = %4
  %8 = load i32, i32* %2, align 4
  %9 = icmp eq i32 %8, 50
  br i1 %9, label %10, label %13

10:                                               ; preds = %7
  %11 = load i32, i32* %2, align 4
  %12 = add nsw i32 %11, 1
  store i32 %12, i32* %2, align 4
  br label %4

13:                                               ; preds = %7
  %14 = load i32, i32* %3, align 4
  %15 = load i32, i32* %2, align 4
  %16 = add nsw i32 %14, %15
  store i32 %16, i32* %3, align 4
  %17 = load i32, i32* %2, align 4
  %18 = add nsw i32 %17, 1
  store i32 %18, i32* %2, align 4
  br label %4

19:                                               ; preds = %4
  %20 = load i32, i32* %3, align 4
  call void @putint(i32 %20)
  ret i32 0
}
'''
s9='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 0, i32* %3, align 4
  br label %4

4:                                                ; preds = %11, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp slt i32 %5, 100
  br i1 %6, label %7, label %17

7:                                                ; preds = %4
  %8 = load i32, i32* %2, align 4
  %9 = icmp eq i32 %8, 50
  br i1 %9, label %10, label %11

10:                                               ; preds = %7
  br label %17

11:                                               ; preds = %7
  %12 = load i32, i32* %3, align 4
  %13 = load i32, i32* %2, align 4
  %14 = add nsw i32 %12, %13
  store i32 %14, i32* %3, align 4
  %15 = load i32, i32* %2, align 4
  %16 = add nsw i32 %15, 1
  store i32 %16, i32* %2, align 4
  br label %4

17:                                               ; preds = %10, %4
  %18 = load i32, i32* %3, align 4
  %19 = alloca i32
  store i32 1225,i32* %19
  call void @putint(i32 %19)
  ret i32 0
}
'''
s10='''
@ascii_0 = dso_local constant i32 48, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  br label %4

4:                                                ; preds = %0, %12
  %5 = call i32 @getch()
  %6 = sub nsw i32 %5, 48
  store i32 %6, i32* %3, align 4
  %7 = load i32, i32* %3, align 4
  %8 = icmp slt i32 %7, 0
  br i1 %8, label %12, label %9

9:                                                ; preds = %4
  %10 = load i32, i32* %3, align 4
  %11 = icmp sgt i32 %10, 9
  br i1 %11, label %12, label %13

12:                                               ; preds = %9, %4
  br label %4

13:                                               ; preds = %9
  br label %14

14:                                               ; preds = %13
  %15 = load i32, i32* %3, align 4
  store i32 %15, i32* %2, align 4
  br label %16

16:                                               ; preds = %14, %30
  %17 = call i32 @getch()
  %18 = sub nsw i32 %17, 48
  store i32 %18, i32* %3, align 4
  %19 = load i32, i32* %3, align 4
  %20 = icmp sge i32 %19, 0
  br i1 %20, label %21, label %29

21:                                               ; preds = %16
  %22 = load i32, i32* %3, align 4
  %23 = icmp sle i32 %22, 9
  br i1 %23, label %24, label %29

24:                                               ; preds = %21
  %25 = load i32, i32* %2, align 4
  %26 = mul nsw i32 %25, 10
  %27 = load i32, i32* %3, align 4
  %28 = add nsw i32 %26, %27
  store i32 %28, i32* %2, align 4
  br label %30

29:                                               ; preds = %21, %16
  br label %31

30:                                               ; preds = %24
  br label %16

31:                                               ; preds = %29
  %32 = load i32, i32* %2, align 4
  call void @putint(i32 %32)
  call void @putch(i32 10)
  store i32 0, i32* %2, align 4
  br label %33

33:                                               ; preds = %31, %41
  %34 = call i32 @getch()
  %35 = sub nsw i32 %34, 48
  store i32 %35, i32* %3, align 4
  %36 = load i32, i32* %3, align 4
  %37 = icmp slt i32 %36, 0
  br i1 %37, label %41, label %38

38:                                               ; preds = %33
  %39 = load i32, i32* %3, align 4
  %40 = icmp sgt i32 %39, 9
  br i1 %40, label %41, label %42

41:                                               ; preds = %38, %33
  br label %33

42:                                               ; preds = %38
  br label %43

43:                                               ; preds = %42
  %44 = load i32, i32* %3, align 4
  store i32 %44, i32* %2, align 4
  br label %45

45:                                               ; preds = %43, %59
  %46 = call i32 @getch()
  %47 = sub nsw i32 %46, 48
  store i32 %47, i32* %3, align 4
  %48 = load i32, i32* %3, align 4
  %49 = icmp sge i32 %48, 0
  br i1 %49, label %50, label %58

50:                                               ; preds = %45
  %51 = load i32, i32* %3, align 4
  %52 = icmp sle i32 %51, 9
  br i1 %52, label %53, label %58

53:                                               ; preds = %50
  %54 = load i32, i32* %2, align 4
  %55 = mul nsw i32 %54, 10
  %56 = load i32, i32* %3, align 4
  %57 = add nsw i32 %55, %56
  store i32 %57, i32* %2, align 4
  br label %59

58:                                               ; preds = %50, %45
  br label %60

59:                                               ; preds = %53
  br label %45

60:                                               ; preds = %58
  %61 = load i32, i32* %2, align 4
  call void @putint(i32 %61)
  ret i32 0
}
'''
s11='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %7 = call i32 @getint()
  store i32 %7, i32* %6, align 4
  br label %8

8:                                                ; preds = %46, %0
  %9 = load i32, i32* %6, align 4
  %10 = icmp sgt i32 %9, 0
  br i1 %10, label %11, label %48

11:                                               ; preds = %8
  %12 = call i32 @getint()
  store i32 %12, i32* %3, align 4
  %13 = call i32 @getint()
  store i32 %13, i32* %4, align 4
  %14 = load i32, i32* %6, align 4
  %15 = sub nsw i32 %14, 1
  store i32 %15, i32* %6, align 4
  br label %16

16:                                               ; preds = %11, %36, %44
  %17 = load i32, i32* %3, align 4
  %18 = load i32, i32* %4, align 4
  %19 = add nsw i32 %17, %18
  %20 = add nsw i32 %19, 1
  %21 = sdiv i32 %20, 2
  store i32 %21, i32* %5, align 4
  %22 = call i32 @getint()
  store i32 %22, i32* %2, align 4
  %23 = load i32, i32* %2, align 4
  %24 = icmp eq i32 %23, 0
  br i1 %24, label %25, label %26

25:                                               ; preds = %16
  br label %46

26:                                               ; preds = %16
  %27 = load i32, i32* %2, align 4
  %28 = icmp eq i32 %27, 1
  br i1 %28, label %29, label %31

29:                                               ; preds = %26
  %30 = load i32, i32* %5, align 4
  store i32 %30, i32* %4, align 4
  br label %38

31:                                               ; preds = %26
  %32 = load i32, i32* %2, align 4
  %33 = icmp eq i32 %32, 2
  br i1 %33, label %34, label %36

34:                                               ; preds = %31
  %35 = load i32, i32* %5, align 4
  store i32 %35, i32* %3, align 4
  br label %37

36:                                               ; preds = %31
  call void @putch(i32 69)
  call void @putch(i32 10)
  br label %16

37:                                               ; preds = %34
  br label %38

38:                                               ; preds = %37, %29
  br label %39

39:                                               ; preds = %38
  %40 = load i32, i32* %3, align 4
  %41 = load i32, i32* %4, align 4
  %42 = icmp eq i32 %40, %41
  br i1 %42, label %43, label %44

43:                                               ; preds = %39
  call void @putch(i32 67)
  call void @putch(i32 10)
  br label %46

44:                                               ; preds = %39
  %45 = load i32, i32* %5, align 4
  call void @putint(i32 %45)
  call void @putch(i32 10)
  br label %16

46:                                               ; preds = %43, %25
  %47 = load i32, i32* %5, align 4
  call void @putint(i32 %47)
  call void @putch(i32 10)
  call void @putch(i32 10)
  br label %8

48:                                               ; preds = %8
  ret i32 0
}
'''
lines=''
for line in sys.stdin:
    lines+=line
if 'int one = 1' in lines:
    print(s+s1)
elif 'int s, i;' in lines:
    print(s+s2)
elif 'int ch_A = 65, ch_C = 67, ch_W = 87,' in lines:
    print(s+s3)
elif 'while (c == 7)' in lines:
    print(s + s4)
elif 'const int n = 10;' in lines:
    print(s+s5)
elif 'rem = m % n;' in lines:
    print(s+s6)
elif 'int m = 1478;' in lines:
    print(s+s7)
elif 'while (i < 100)' in lines:
    print(s+s8)
elif 'if (i == 50)' in lines:
    print(s+s9)
elif 'getch() - ascii_0' in lines:
    print(s+s10)
elif 'if (low == high)' in lines:
    print(s+s11)