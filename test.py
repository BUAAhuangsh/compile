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
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %6 = call i32 @getint()
  store i32 %6, i32* %2, align 4
  store i32 2, i32* %3, align 4
  %7 = load i32, i32* %2, align 4
  %8 = load i32, i32* %3, align 4
  %9 = add nsw i32 %7, %8
  call void @putint(i32 %9)
  %10 = call i32 @getint()
  store i32 %10, i32* %4, align 4
  %11 = load i32, i32* %4, align 4
  %12 = load i32, i32* %3, align 4
  %13 = add nsw i32 %11, %12
  call void @putint(i32 %13)
  %14 = load i32, i32* %2, align 4
  %15 = add nsw i32 %14, 2
  store i32 %15, i32* %5, align 4
  %16 = load i32, i32* %2, align 4
  %17 = load i32, i32* %5, align 4
  %18 = add nsw i32 %16, %17
  call void @putint(i32 %18)
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
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 1, i32* %2, align 4
  store i32 0, i32* %3, align 4
  store i32 2, i32* %4, align 4
  %11 = load i32, i32* %3, align 4
  %12 = load i32, i32* %4, align 4
  %13 = add nsw i32 %11, %12
  store i32 %13, i32* %3, align 4
  store i32 3, i32* %5, align 4
  %14 = load i32, i32* %3, align 4
  %15 = load i32, i32* %5, align 4
  %16 = add nsw i32 %14, %15
  store i32 %16, i32* %3, align 4
  %17 = load i32, i32* %3, align 4
  call void @putint(i32 %17)
  %18 = load i32, i32* %5, align 4
  call void @putint(i32 %18)
  call void @putch(i32 10)
  store i32 4, i32* %5, align 4
  %19 = load i32, i32* %3, align 4
  store i32 %19, i32* %6, align 4
  %20 = load i32, i32* %6, align 4
  %21 = load i32, i32* %5, align 4
  %22 = add nsw i32 %20, %21
  store i32 %22, i32* %7, align 4
  store i32 5, i32* %8, align 4
  %23 = load i32, i32* %7, align 4
  store i32 %23, i32* %9, align 4
  %24 = load i32, i32* %9, align 4
  %25 = load i32, i32* %8, align 4
  %26 = add nsw i32 %24, %25
  store i32 %26, i32* %10, align 4
  store i32 6, i32* %8, align 4
  %27 = load i32, i32* %10, align 4
  call void @putint(i32 %27)
  %28 = load i32, i32* %8, align 4
  call void @putint(i32 %28)
  call void @putch(i32 10)
  %29 = load i32, i32* %10, align 4
  %30 = load i32, i32* %8, align 4
  %31 = add nsw i32 %29, %30
  store i32 %31, i32* %10, align 4
  store i32 7, i32* %8, align 4
  %32 = load i32, i32* %10, align 4
  %33 = load i32, i32* %8, align 4
  %34 = add nsw i32 %32, %33
  store i32 %34, i32* %10, align 4
  %35 = load i32, i32* %10, align 4
  call void @putint(i32 %35)
  %36 = load i32, i32* %8, align 4
  call void @putint(i32 %36)
  %37 = load i32, i32* %10, align 4
  %38 = load i32, i32* %8, align 4
  %39 = add nsw i32 %37, %38
  store i32 %39, i32* %10, align 4
  call void @putch(i32 10)
  %40 = load i32, i32* %3, align 4
  call void @putint(i32 %40)
  %41 = load i32, i32* %4, align 4
  call void @putint(i32 %41)
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
  store i32 3389, i32* %2, align 4
  %7 = load i32, i32* %2, align 4
  %8 = icmp slt i32 %7, 10000
  br i1 %8, label %9, label %31

9:                                                ; preds = %0
  %10 = load i32, i32* %2, align 4
  %11 = add nsw i32 %10, 1
  store i32 %11, i32* %2, align 4
  store i32 112, i32* %3, align 4
  %12 = load i32, i32* %3, align 4
  %13 = icmp sgt i32 %12, 10
  br i1 %13, label %14, label %29

14:                                               ; preds = %9
  %15 = load i32, i32* %3, align 4
  %16 = sub nsw i32 %15, 88
  store i32 %16, i32* %3, align 4
  %17 = load i32, i32* %3, align 4
  %18 = icmp slt i32 %17, 1000
  br i1 %18, label %19, label %28

19:                                               ; preds = %14
  store i32 9, i32* %4, align 4
  store i32 11, i32* %5, align 4
  store i32 10, i32* %4, align 4
  %20 = load i32, i32* %3, align 4
  %21 = load i32, i32* %4, align 4
  %22 = sub nsw i32 %20, %21
  store i32 %22, i32* %3, align 4
  store i32 11, i32* %6, align 4
  %23 = load i32, i32* %3, align 4
  %24 = load i32, i32* %6, align 4
  %25 = add nsw i32 %23, %24
  %26 = load i32, i32* %5, align 4
  %27 = add nsw i32 %25, %26
  store i32 %27, i32* %3, align 4
  br label %28

28:                                               ; preds = %19, %14
  br label %29

29:                                               ; preds = %28, %9
  %30 = load i32, i32* %3, align 4
  call void @putint(i32 %30)
  br label %31

31:                                               ; preds = %29, %0
  ret i32 0
}
'''
s4='''
@a = dso_local constant i32 6, align 4
@b = dso_local global i32 7, align 4

define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %4 = load i32, i32* @b, align 4
  store i32 %4, i32* %2, align 4
  store i32 8, i32* %3, align 4
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* %2, align 4
  %7 = add nsw i32 %5, %6
  call void @putint(i32 %7)
  ret i32 0
}
'''
s5='''
@t = dso_local global i32 4, align 4
@b = dso_local global i32 3, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  %4 = load i32, i32* %2, align 4
  store i32 %4, i32* %3, align 4
  %5 = load i32, i32* @t, align 4
  store i32 %5, i32* %2, align 4
  %6 = load i32, i32* %3, align 4
  store i32 %6, i32* @t, align 4
  %7 = load i32, i32* %2, align 4
  call void @putint(i32 %7)
  %8 = load i32, i32* %3, align 4
  call void @putint(i32 %8)
  %9 = load i32, i32* @t, align 4
  call void @putint(i32 %9)
  ret i32 0
}
'''
s6='''
@a = dso_local global i32 1, align 4
@b = dso_local global i32 3, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %2 = call i32 @getint()
  store i32 %2, i32* @a, align 4
  %3 = load i32, i32* @a, align 4
  store i32 %3, i32* @b, align 4
  %4 = load i32, i32* @b, align 4
  store i32 %4, i32* @a, align 4
  %5 = load i32, i32* @a, align 4
  store i32 %5, i32* @b, align 4
  %6 = load i32, i32* @a, align 4
  store i32 %6, i32* @b, align 4
  %7 = load i32, i32* @b, align 4
  store i32 %7, i32* @a, align 4
  %8 = load i32, i32* @a, align 4
  store i32 %8, i32* @b, align 4
  %9 = load i32, i32* @b, align 4
  store i32 %9, i32* @a, align 4
  %10 = load i32, i32* @b, align 4
  store i32 %10, i32* @a, align 4
  %11 = load i32, i32* @a, align 4
  store i32 %11, i32* @b, align 4
  %12 = call i32 @getint()
  store i32 %12, i32* @a, align 4
  %13 = load i32, i32* @a, align 4
  call void @putint(i32 %13)
  %14 = load i32, i32* @b, align 4
  call void @putint(i32 %14)
  ret i32 0
}
'''
s7='''
@a0 = common dso_local global i32 0, align 4
@a1 = common dso_local global i32 0, align 4
@a2 = common dso_local global i32 0, align 4
@a3 = common dso_local global i32 0, align 4
@a4 = common dso_local global i32 0, align 4
@a5 = common dso_local global i32 0, align 4
@a6 = common dso_local global i32 0, align 4
@a7 = common dso_local global i32 0, align 4
@a8 = common dso_local global i32 0, align 4
@a9 = common dso_local global i32 0, align 4
@a10 = common dso_local global i32 0, align 4
@a11 = common dso_local global i32 0, align 4
@a12 = common dso_local global i32 0, align 4
@a13 = common dso_local global i32 0, align 4
@a14 = common dso_local global i32 0, align 4
@a15 = common dso_local global i32 0, align 4
@a16 = common dso_local global i32 0, align 4
@a17 = common dso_local global i32 0, align 4
@a18 = common dso_local global i32 0, align 4
@a19 = common dso_local global i32 0, align 4
@a20 = common dso_local global i32 0, align 4
@a21 = common dso_local global i32 0, align 4
@a22 = common dso_local global i32 0, align 4
@a23 = common dso_local global i32 0, align 4
@a24 = common dso_local global i32 0, align 4
@a25 = common dso_local global i32 0, align 4
@a26 = common dso_local global i32 0, align 4
@a27 = common dso_local global i32 0, align 4
@a28 = common dso_local global i32 0, align 4
@a29 = common dso_local global i32 0, align 4
@a30 = common dso_local global i32 0, align 4
@a31 = common dso_local global i32 0, align 4
@a32 = common dso_local global i32 0, align 4
@a33 = common dso_local global i32 0, align 4
@a34 = common dso_local global i32 0, align 4
@a35 = common dso_local global i32 0, align 4
@a36 = common dso_local global i32 0, align 4
@a37 = common dso_local global i32 0, align 4
@a38 = common dso_local global i32 0, align 4
@a39 = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* @a0, align 4
  store i32 1, i32* @a1, align 4
  store i32 2, i32* @a2, align 4
  store i32 3, i32* @a3, align 4
  store i32 4, i32* @a4, align 4
  store i32 5, i32* @a5, align 4
  store i32 6, i32* @a6, align 4
  store i32 7, i32* @a7, align 4
  store i32 8, i32* @a8, align 4
  store i32 9, i32* @a9, align 4
  store i32 0, i32* @a10, align 4
  store i32 1, i32* @a11, align 4
  store i32 2, i32* @a12, align 4
  store i32 3, i32* @a13, align 4
  store i32 4, i32* @a14, align 4
  store i32 5, i32* @a15, align 4
  store i32 6, i32* @a16, align 4
  store i32 7, i32* @a17, align 4
  store i32 8, i32* @a18, align 4
  store i32 9, i32* @a19, align 4
  store i32 0, i32* @a20, align 4
  store i32 1, i32* @a21, align 4
  store i32 2, i32* @a22, align 4
  store i32 3, i32* @a23, align 4
  store i32 4, i32* @a24, align 4
  store i32 5, i32* @a25, align 4
  store i32 6, i32* @a26, align 4
  store i32 7, i32* @a27, align 4
  store i32 8, i32* @a28, align 4
  store i32 9, i32* @a29, align 4
  store i32 0, i32* @a30, align 4
  store i32 1, i32* @a31, align 4
  store i32 4, i32* @a32, align 4
  store i32 5, i32* @a33, align 4
  store i32 6, i32* @a34, align 4
  store i32 7, i32* @a35, align 4
  store i32 8, i32* @a36, align 4
  store i32 9, i32* @a37, align 4
  store i32 0, i32* @a38, align 4
  store i32 1, i32* @a39, align 4
  %2 = load i32, i32* @a0, align 4
  %3 = load i32, i32* @a1, align 4
  %4 = add nsw i32 %2, %3
  %5 = load i32, i32* @a2, align 4
  %6 = add nsw i32 %4, %5
  %7 = load i32, i32* @a3, align 4
  %8 = add nsw i32 %6, %7
  %9 = load i32, i32* @a4, align 4
  %10 = add nsw i32 %8, %9
  %11 = load i32, i32* @a5, align 4
  %12 = add nsw i32 %10, %11
  %13 = load i32, i32* @a6, align 4
  %14 = add nsw i32 %12, %13
  %15 = load i32, i32* @a7, align 4
  %16 = add nsw i32 %14, %15
  call void @putint(i32 %16)
  %17 = load i32, i32* @a0, align 4
  %18 = load i32, i32* @a1, align 4
  %19 = add nsw i32 %17, %18
  %20 = load i32, i32* @a2, align 4
  %21 = add nsw i32 %19, %20
  %22 = load i32, i32* @a3, align 4
  %23 = add nsw i32 %21, %22
  %24 = load i32, i32* @a4, align 4
  %25 = add nsw i32 %23, %24
  %26 = load i32, i32* @a5, align 4
  %27 = add nsw i32 %25, %26
  %28 = load i32, i32* @a6, align 4
  %29 = add nsw i32 %27, %28
  %30 = load i32, i32* @a7, align 4
  %31 = add nsw i32 %29, %30
  store i32 %31, i32* @a0, align 4
  %32 = load i32, i32* @a32, align 4
  %33 = load i32, i32* @a33, align 4
  %34 = add nsw i32 %32, %33
  %35 = load i32, i32* @a34, align 4
  %36 = add nsw i32 %34, %35
  %37 = load i32, i32* @a35, align 4
  %38 = sub nsw i32 %36, %37
  %39 = load i32, i32* @a36, align 4
  %40 = sub nsw i32 %38, %39
  %41 = load i32, i32* @a37, align 4
  %42 = sub nsw i32 %40, %41
  %43 = load i32, i32* @a38, align 4
  %44 = sub nsw i32 %42, %43
  %45 = load i32, i32* @a39, align 4
  %46 = sub nsw i32 %44, %45
  %47 = load i32, i32* @a8, align 4
  %48 = add nsw i32 %46, %47
  %49 = load i32, i32* @a9, align 4
  %50 = add nsw i32 %48, %49
  %51 = load i32, i32* @a10, align 4
  %52 = add nsw i32 %50, %51
  %53 = load i32, i32* @a11, align 4
  %54 = add nsw i32 %52, %53
  %55 = load i32, i32* @a12, align 4
  %56 = add nsw i32 %54, %55
  %57 = load i32, i32* @a13, align 4
  %58 = add nsw i32 %56, %57
  %59 = load i32, i32* @a14, align 4
  %60 = add nsw i32 %58, %59
  %61 = load i32, i32* @a15, align 4
  %62 = add nsw i32 %60, %61
  store i32 %62, i32* @a0, align 4
  %63 = load i32, i32* @a0, align 4
  call void @putint(i32 %63)
  %64 = load i32, i32* @a0, align 4
  %65 = load i32, i32* @a1, align 4
  %66 = add nsw i32 %64, %65
  %67 = load i32, i32* @a2, align 4
  %68 = add nsw i32 %66, %67
  %69 = load i32, i32* @a3, align 4
  %70 = add nsw i32 %68, %69
  %71 = load i32, i32* @a4, align 4
  %72 = add nsw i32 %70, %71
  %73 = load i32, i32* @a5, align 4
  %74 = add nsw i32 %72, %73
  %75 = load i32, i32* @a6, align 4
  %76 = add nsw i32 %74, %75
  %77 = load i32, i32* @a7, align 4
  %78 = add nsw i32 %76, %77
  %79 = load i32, i32* @a8, align 4
  %80 = add nsw i32 %78, %79
  %81 = load i32, i32* @a9, align 4
  %82 = add nsw i32 %80, %81
  %83 = load i32, i32* @a10, align 4
  %84 = add nsw i32 %82, %83
  %85 = load i32, i32* @a11, align 4
  %86 = add nsw i32 %84, %85
  %87 = load i32, i32* @a12, align 4
  %88 = add nsw i32 %86, %87
  %89 = load i32, i32* @a13, align 4
  %90 = add nsw i32 %88, %89
  %91 = load i32, i32* @a14, align 4
  %92 = add nsw i32 %90, %91
  %93 = load i32, i32* @a15, align 4
  %94 = add nsw i32 %92, %93
  %95 = load i32, i32* @a16, align 4
  %96 = add nsw i32 %94, %95
  %97 = load i32, i32* @a17, align 4
  %98 = add nsw i32 %96, %97
  %99 = load i32, i32* @a18, align 4
  %100 = sub nsw i32 %98, %99
  %101 = load i32, i32* @a19, align 4
  %102 = sub nsw i32 %100, %101
  %103 = load i32, i32* @a20, align 4
  %104 = sub nsw i32 %102, %103
  %105 = load i32, i32* @a21, align 4
  %106 = sub nsw i32 %104, %105
  %107 = load i32, i32* @a22, align 4
  %108 = sub nsw i32 %106, %107
  %109 = load i32, i32* @a23, align 4
  %110 = add nsw i32 %108, %109
  %111 = load i32, i32* @a24, align 4
  %112 = add nsw i32 %110, %111
  %113 = load i32, i32* @a25, align 4
  %114 = add nsw i32 %112, %113
  %115 = load i32, i32* @a26, align 4
  %116 = add nsw i32 %114, %115
  %117 = load i32, i32* @a27, align 4
  %118 = add nsw i32 %116, %117
  %119 = load i32, i32* @a28, align 4
  %120 = add nsw i32 %118, %119
  %121 = load i32, i32* @a29, align 4
  %122 = add nsw i32 %120, %121
  %123 = load i32, i32* @a30, align 4
  %124 = add nsw i32 %122, %123
  %125 = load i32, i32* @a31, align 4
  %126 = add nsw i32 %124, %125
  store i32 %126, i32* @a0, align 4
  %127 = load i32, i32* @a0, align 4
  call void @putint(i32 %127)
  ret i32 0
}
'''
s8='''
@a1 = dso_local global i32 1, align 4
@a2 = dso_local global i32 2, align 4
@a3 = dso_local global i32 3, align 4
@a4 = dso_local global i32 4, align 4
@a5 = dso_local global i32 5, align 4
@a6 = dso_local global i32 6, align 4
@a7 = dso_local global i32 7, align 4
@a8 = dso_local global i32 8, align 4
@a9 = dso_local global i32 9, align 4
@a10 = dso_local global i32 10, align 4
@a11 = dso_local global i32 11, align 4
@a12 = dso_local global i32 12, align 4
@a13 = dso_local global i32 13, align 4
@a14 = dso_local global i32 14, align 4
@a15 = dso_local global i32 15, align 4
@a16 = dso_local global i32 16, align 4
@a17 = dso_local global i32 1, align 4
@a18 = dso_local global i32 2, align 4
@a19 = dso_local global i32 3, align 4
@a20 = dso_local global i32 4, align 4
@a21 = dso_local global i32 5, align 4
@a22 = dso_local global i32 6, align 4
@a23 = dso_local global i32 7, align 4
@a24 = dso_local global i32 8, align 4
@a25 = dso_local global i32 9, align 4
@a26 = dso_local global i32 10, align 4
@a27 = dso_local global i32 11, align 4
@a28 = dso_local global i32 12, align 4
@a29 = dso_local global i32 13, align 4
@a30 = dso_local global i32 14, align 4
@a31 = dso_local global i32 15, align 4
@a32 = dso_local global i32 16, align 4

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
  %41 = call i32 @getint()
  store i32 %41, i32* %3, align 4
  %42 = load i32, i32* %3, align 4
  %43 = add nsw i32 %42, 18
  store i32 %43, i32* %4, align 4
  %44 = load i32, i32* %3, align 4
  %45 = load i32, i32* %4, align 4
  %46 = add nsw i32 %44, %45
  store i32 %46, i32* %2, align 4
  %47 = call i32 @getint()
  store i32 %47, i32* %5, align 4
  %48 = call i32 @getint()
  store i32 %48, i32* %6, align 4
  %49 = call i32 @getint()
  store i32 %49, i32* %7, align 4
  %50 = call i32 @getint()
  store i32 %50, i32* %8, align 4
  %51 = load i32, i32* %5, align 4
  %52 = add nsw i32 1, %51
  %53 = load i32, i32* @a1, align 4
  %54 = add nsw i32 %52, %53
  store i32 %54, i32* %9, align 4
  %55 = load i32, i32* %6, align 4
  %56 = add nsw i32 2, %55
  %57 = load i32, i32* @a2, align 4
  %58 = add nsw i32 %56, %57
  store i32 %58, i32* %10, align 4
  %59 = load i32, i32* %7, align 4
  %60 = add nsw i32 3, %59
  %61 = load i32, i32* @a3, align 4
  %62 = add nsw i32 %60, %61
  store i32 %62, i32* %11, align 4
  %63 = load i32, i32* %8, align 4
  %64 = add nsw i32 4, %63
  %65 = load i32, i32* @a4, align 4
  %66 = add nsw i32 %64, %65
  store i32 %66, i32* %12, align 4
  %67 = load i32, i32* %9, align 4
  %68 = add nsw i32 1, %67
  %69 = load i32, i32* @a5, align 4
  %70 = add nsw i32 %68, %69
  store i32 %70, i32* %13, align 4
  %71 = load i32, i32* %10, align 4
  %72 = add nsw i32 2, %71
  %73 = load i32, i32* @a6, align 4
  %74 = add nsw i32 %72, %73
  store i32 %74, i32* %14, align 4
  %75 = load i32, i32* %11, align 4
  %76 = add nsw i32 3, %75
  %77 = load i32, i32* @a7, align 4
  %78 = add nsw i32 %76, %77
  store i32 %78, i32* %15, align 4
  %79 = load i32, i32* %12, align 4
  %80 = add nsw i32 4, %79
  %81 = load i32, i32* @a8, align 4
  %82 = add nsw i32 %80, %81
  store i32 %82, i32* %16, align 4
  %83 = load i32, i32* %13, align 4
  %84 = add nsw i32 1, %83
  %85 = load i32, i32* @a9, align 4
  %86 = add nsw i32 %84, %85
  store i32 %86, i32* %17, align 4
  %87 = load i32, i32* %14, align 4
  %88 = add nsw i32 2, %87
  %89 = load i32, i32* @a10, align 4
  %90 = add nsw i32 %88, %89
  store i32 %90, i32* %18, align 4
  %91 = load i32, i32* %15, align 4
  %92 = add nsw i32 3, %91
  %93 = load i32, i32* @a11, align 4
  %94 = add nsw i32 %92, %93
  store i32 %94, i32* %19, align 4
  %95 = load i32, i32* %16, align 4
  %96 = add nsw i32 4, %95
  %97 = load i32, i32* @a12, align 4
  %98 = add nsw i32 %96, %97
  store i32 %98, i32* %20, align 4
  %99 = load i32, i32* %17, align 4
  %100 = add nsw i32 1, %99
  %101 = load i32, i32* @a13, align 4
  %102 = add nsw i32 %100, %101
  store i32 %102, i32* %21, align 4
  %103 = load i32, i32* %18, align 4
  %104 = add nsw i32 2, %103
  %105 = load i32, i32* @a14, align 4
  %106 = add nsw i32 %104, %105
  store i32 %106, i32* %22, align 4
  %107 = load i32, i32* %19, align 4
  %108 = add nsw i32 3, %107
  %109 = load i32, i32* @a15, align 4
  %110 = add nsw i32 %108, %109
  store i32 %110, i32* %23, align 4
  %111 = load i32, i32* %20, align 4
  %112 = add nsw i32 4, %111
  %113 = load i32, i32* @a16, align 4
  %114 = add nsw i32 %112, %113
  store i32 %114, i32* %24, align 4
  %115 = load i32, i32* %21, align 4
  %116 = add nsw i32 1, %115
  %117 = load i32, i32* @a17, align 4
  %118 = add nsw i32 %116, %117
  store i32 %118, i32* %25, align 4
  %119 = load i32, i32* %22, align 4
  %120 = add nsw i32 2, %119
  %121 = load i32, i32* @a18, align 4
  %122 = add nsw i32 %120, %121
  store i32 %122, i32* %26, align 4
  %123 = load i32, i32* %23, align 4
  %124 = add nsw i32 3, %123
  %125 = load i32, i32* @a19, align 4
  %126 = add nsw i32 %124, %125
  store i32 %126, i32* %27, align 4
  %127 = load i32, i32* %24, align 4
  %128 = add nsw i32 4, %127
  %129 = load i32, i32* @a20, align 4
  %130 = add nsw i32 %128, %129
  store i32 %130, i32* %28, align 4
  %131 = load i32, i32* %25, align 4
  %132 = add nsw i32 1, %131
  %133 = load i32, i32* @a21, align 4
  %134 = add nsw i32 %132, %133
  store i32 %134, i32* %29, align 4
  %135 = load i32, i32* %26, align 4
  %136 = add nsw i32 2, %135
  %137 = load i32, i32* @a22, align 4
  %138 = add nsw i32 %136, %137
  store i32 %138, i32* %30, align 4
  %139 = load i32, i32* %27, align 4
  %140 = add nsw i32 3, %139
  %141 = load i32, i32* @a23, align 4
  %142 = add nsw i32 %140, %141
  store i32 %142, i32* %31, align 4
  %143 = load i32, i32* %28, align 4
  %144 = add nsw i32 4, %143
  %145 = load i32, i32* @a24, align 4
  %146 = add nsw i32 %144, %145
  store i32 %146, i32* %32, align 4
  %147 = load i32, i32* %29, align 4
  %148 = add nsw i32 1, %147
  %149 = load i32, i32* @a25, align 4
  %150 = add nsw i32 %148, %149
  store i32 %150, i32* %33, align 4
  %151 = load i32, i32* %30, align 4
  %152 = add nsw i32 2, %151
  %153 = load i32, i32* @a26, align 4
  %154 = add nsw i32 %152, %153
  store i32 %154, i32* %34, align 4
  %155 = load i32, i32* %31, align 4
  %156 = add nsw i32 3, %155
  %157 = load i32, i32* @a27, align 4
  %158 = add nsw i32 %156, %157
  store i32 %158, i32* %35, align 4
  %159 = load i32, i32* %32, align 4
  %160 = add nsw i32 4, %159
  %161 = load i32, i32* @a28, align 4
  %162 = add nsw i32 %160, %161
  store i32 %162, i32* %36, align 4
  %163 = load i32, i32* %33, align 4
  %164 = add nsw i32 1, %163
  %165 = load i32, i32* @a29, align 4
  %166 = add nsw i32 %164, %165
  store i32 %166, i32* %37, align 4
  %167 = load i32, i32* %34, align 4
  %168 = add nsw i32 2, %167
  %169 = load i32, i32* @a30, align 4
  %170 = add nsw i32 %168, %169
  store i32 %170, i32* %38, align 4
  %171 = load i32, i32* %35, align 4
  %172 = add nsw i32 3, %171
  %173 = load i32, i32* @a31, align 4
  %174 = add nsw i32 %172, %173
  store i32 %174, i32* %39, align 4
  %175 = load i32, i32* %36, align 4
  %176 = add nsw i32 4, %175
  %177 = load i32, i32* @a32, align 4
  %178 = add nsw i32 %176, %177
  store i32 %178, i32* %40, align 4
  %179 = load i32, i32* %3, align 4
  %180 = load i32, i32* %4, align 4
  %181 = sub nsw i32 %179, %180
  %182 = add nsw i32 %181, 10
  store i32 %182, i32* %2, align 4
  %183 = load i32, i32* %33, align 4
  %184 = add nsw i32 1, %183
  %185 = load i32, i32* @a29, align 4
  %186 = add nsw i32 %184, %185
  store i32 %186, i32* %37, align 4
  %187 = load i32, i32* %34, align 4
  %188 = add nsw i32 2, %187
  %189 = load i32, i32* @a30, align 4
  %190 = add nsw i32 %188, %189
  store i32 %190, i32* %38, align 4
  %191 = load i32, i32* %35, align 4
  %192 = add nsw i32 3, %191
  %193 = load i32, i32* @a31, align 4
  %194 = add nsw i32 %192, %193
  store i32 %194, i32* %39, align 4
  %195 = load i32, i32* %36, align 4
  %196 = add nsw i32 4, %195
  %197 = load i32, i32* @a32, align 4
  %198 = add nsw i32 %196, %197
  store i32 %198, i32* %40, align 4
  %199 = load i32, i32* %29, align 4
  %200 = add nsw i32 1, %199
  %201 = load i32, i32* @a25, align 4
  %202 = add nsw i32 %200, %201
  store i32 %202, i32* %33, align 4
  %203 = load i32, i32* %30, align 4
  %204 = add nsw i32 2, %203
  %205 = load i32, i32* @a26, align 4
  %206 = add nsw i32 %204, %205
  store i32 %206, i32* %34, align 4
  %207 = load i32, i32* %31, align 4
  %208 = add nsw i32 3, %207
  %209 = load i32, i32* @a27, align 4
  %210 = add nsw i32 %208, %209
  store i32 %210, i32* %35, align 4
  %211 = load i32, i32* %32, align 4
  %212 = add nsw i32 4, %211
  %213 = load i32, i32* @a28, align 4
  %214 = add nsw i32 %212, %213
  store i32 %214, i32* %36, align 4
  %215 = load i32, i32* %25, align 4
  %216 = add nsw i32 1, %215
  %217 = load i32, i32* @a21, align 4
  %218 = add nsw i32 %216, %217
  store i32 %218, i32* %29, align 4
  %219 = load i32, i32* %26, align 4
  %220 = add nsw i32 2, %219
  %221 = load i32, i32* @a22, align 4
  %222 = add nsw i32 %220, %221
  store i32 %222, i32* %30, align 4
  %223 = load i32, i32* %27, align 4
  %224 = add nsw i32 3, %223
  %225 = load i32, i32* @a23, align 4
  %226 = add nsw i32 %224, %225
  store i32 %226, i32* %31, align 4
  %227 = load i32, i32* %28, align 4
  %228 = add nsw i32 4, %227
  %229 = load i32, i32* @a24, align 4
  %230 = add nsw i32 %228, %229
  store i32 %230, i32* %32, align 4
  %231 = load i32, i32* %21, align 4
  %232 = add nsw i32 1, %231
  %233 = load i32, i32* @a17, align 4
  %234 = add nsw i32 %232, %233
  store i32 %234, i32* %25, align 4
  %235 = load i32, i32* %22, align 4
  %236 = add nsw i32 2, %235
  %237 = load i32, i32* @a18, align 4
  %238 = add nsw i32 %236, %237
  store i32 %238, i32* %26, align 4
  %239 = load i32, i32* %23, align 4
  %240 = add nsw i32 3, %239
  %241 = load i32, i32* @a19, align 4
  %242 = add nsw i32 %240, %241
  store i32 %242, i32* %27, align 4
  %243 = load i32, i32* %24, align 4
  %244 = add nsw i32 4, %243
  %245 = load i32, i32* @a20, align 4
  %246 = add nsw i32 %244, %245
  store i32 %246, i32* %28, align 4
  %247 = load i32, i32* %17, align 4
  %248 = add nsw i32 1, %247
  %249 = load i32, i32* @a13, align 4
  %250 = add nsw i32 %248, %249
  store i32 %250, i32* %21, align 4
  %251 = load i32, i32* %18, align 4
  %252 = add nsw i32 2, %251
  %253 = load i32, i32* @a14, align 4
  %254 = add nsw i32 %252, %253
  store i32 %254, i32* %22, align 4
  %255 = load i32, i32* %19, align 4
  %256 = add nsw i32 3, %255
  %257 = load i32, i32* @a15, align 4
  %258 = add nsw i32 %256, %257
  store i32 %258, i32* %23, align 4
  %259 = load i32, i32* %20, align 4
  %260 = add nsw i32 4, %259
  %261 = load i32, i32* @a16, align 4
  %262 = add nsw i32 %260, %261
  store i32 %262, i32* %24, align 4
  %263 = load i32, i32* %13, align 4
  %264 = add nsw i32 1, %263
  %265 = load i32, i32* @a9, align 4
  %266 = add nsw i32 %264, %265
  store i32 %266, i32* %17, align 4
  %267 = load i32, i32* %14, align 4
  %268 = add nsw i32 2, %267
  %269 = load i32, i32* @a10, align 4
  %270 = add nsw i32 %268, %269
  store i32 %270, i32* %18, align 4
  %271 = load i32, i32* %15, align 4
  %272 = add nsw i32 3, %271
  %273 = load i32, i32* @a11, align 4
  %274 = add nsw i32 %272, %273
  store i32 %274, i32* %19, align 4
  %275 = load i32, i32* %16, align 4
  %276 = add nsw i32 4, %275
  %277 = load i32, i32* @a12, align 4
  %278 = add nsw i32 %276, %277
  store i32 %278, i32* %20, align 4
  %279 = load i32, i32* %9, align 4
  %280 = add nsw i32 1, %279
  %281 = load i32, i32* @a5, align 4
  %282 = add nsw i32 %280, %281
  store i32 %282, i32* %13, align 4
  %283 = load i32, i32* %10, align 4
  %284 = add nsw i32 2, %283
  %285 = load i32, i32* @a6, align 4
  %286 = add nsw i32 %284, %285
  store i32 %286, i32* %14, align 4
  %287 = load i32, i32* %11, align 4
  %288 = add nsw i32 3, %287
  %289 = load i32, i32* @a7, align 4
  %290 = add nsw i32 %288, %289
  store i32 %290, i32* %15, align 4
  %291 = load i32, i32* %12, align 4
  %292 = add nsw i32 4, %291
  %293 = load i32, i32* @a8, align 4
  %294 = add nsw i32 %292, %293
  store i32 %294, i32* %16, align 4
  %295 = load i32, i32* %5, align 4
  %296 = add nsw i32 1, %295
  %297 = load i32, i32* @a1, align 4
  %298 = add nsw i32 %296, %297
  store i32 %298, i32* %9, align 4
  %299 = load i32, i32* %6, align 4
  %300 = add nsw i32 2, %299
  %301 = load i32, i32* @a2, align 4
  %302 = add nsw i32 %300, %301
  store i32 %302, i32* %10, align 4
  %303 = load i32, i32* %7, align 4
  %304 = add nsw i32 3, %303
  %305 = load i32, i32* @a3, align 4
  %306 = add nsw i32 %304, %305
  store i32 %306, i32* %11, align 4
  %307 = load i32, i32* %8, align 4
  %308 = add nsw i32 4, %307
  %309 = load i32, i32* @a4, align 4
  %310 = add nsw i32 %308, %309
  store i32 %310, i32* %12, align 4
  %311 = load i32, i32* %5, align 4
  %312 = add nsw i32 1, %311
  %313 = load i32, i32* @a1, align 4
  %314 = add nsw i32 %312, %313
  store i32 %314, i32* %9, align 4
  %315 = load i32, i32* %6, align 4
  %316 = add nsw i32 2, %315
  %317 = load i32, i32* @a2, align 4
  %318 = add nsw i32 %316, %317
  store i32 %318, i32* %10, align 4
  %319 = load i32, i32* %7, align 4
  %320 = add nsw i32 3, %319
  %321 = load i32, i32* @a3, align 4
  %322 = add nsw i32 %320, %321
  store i32 %322, i32* %11, align 4
  %323 = load i32, i32* %8, align 4
  %324 = add nsw i32 4, %323
  %325 = load i32, i32* @a4, align 4
  %326 = add nsw i32 %324, %325
  store i32 %326, i32* %12, align 4
  %327 = load i32, i32* %2, align 4
  %328 = load i32, i32* %5, align 4
  %329 = add nsw i32 %327, %328
  %330 = load i32, i32* %6, align 4
  %331 = add nsw i32 %329, %330
  %332 = load i32, i32* %7, align 4
  %333 = add nsw i32 %331, %332
  %334 = load i32, i32* %8, align 4
  %335 = add nsw i32 %333, %334
  %336 = load i32, i32* %9, align 4
  %337 = sub nsw i32 %335, %336
  %338 = load i32, i32* %10, align 4
  %339 = sub nsw i32 %337, %338
  %340 = load i32, i32* %11, align 4
  %341 = sub nsw i32 %339, %340
  %342 = load i32, i32* %12, align 4
  %343 = sub nsw i32 %341, %342
  %344 = load i32, i32* %13, align 4
  %345 = add nsw i32 %343, %344
  %346 = load i32, i32* %14, align 4
  %347 = add nsw i32 %345, %346
  %348 = load i32, i32* %15, align 4
  %349 = add nsw i32 %347, %348
  %350 = load i32, i32* %16, align 4
  %351 = add nsw i32 %349, %350
  %352 = load i32, i32* %17, align 4
  %353 = sub nsw i32 %351, %352
  %354 = load i32, i32* %18, align 4
  %355 = sub nsw i32 %353, %354
  %356 = load i32, i32* %19, align 4
  %357 = sub nsw i32 %355, %356
  %358 = load i32, i32* %20, align 4
  %359 = sub nsw i32 %357, %358
  %360 = load i32, i32* %21, align 4
  %361 = add nsw i32 %359, %360
  %362 = load i32, i32* %22, align 4
  %363 = add nsw i32 %361, %362
  %364 = load i32, i32* %23, align 4
  %365 = add nsw i32 %363, %364
  %366 = load i32, i32* %24, align 4
  %367 = add nsw i32 %365, %366
  %368 = load i32, i32* %25, align 4
  %369 = sub nsw i32 %367, %368
  %370 = load i32, i32* %26, align 4
  %371 = sub nsw i32 %369, %370
  %372 = load i32, i32* %27, align 4
  %373 = sub nsw i32 %371, %372
  %374 = load i32, i32* %28, align 4
  %375 = sub nsw i32 %373, %374
  %376 = load i32, i32* %29, align 4
  %377 = add nsw i32 %375, %376
  %378 = load i32, i32* %30, align 4
  %379 = add nsw i32 %377, %378
  %380 = load i32, i32* %31, align 4
  %381 = add nsw i32 %379, %380
  %382 = load i32, i32* %32, align 4
  %383 = add nsw i32 %381, %382
  %384 = load i32, i32* %33, align 4
  %385 = sub nsw i32 %383, %384
  %386 = load i32, i32* %34, align 4
  %387 = sub nsw i32 %385, %386
  %388 = load i32, i32* %35, align 4
  %389 = sub nsw i32 %387, %388
  %390 = load i32, i32* %36, align 4
  %391 = sub nsw i32 %389, %390
  %392 = load i32, i32* %37, align 4
  %393 = add nsw i32 %391, %392
  %394 = load i32, i32* %38, align 4
  %395 = add nsw i32 %393, %394
  %396 = load i32, i32* %39, align 4
  %397 = add nsw i32 %395, %396
  %398 = load i32, i32* %40, align 4
  %399 = add nsw i32 %397, %398
  %400 = load i32, i32* @a1, align 4
  %401 = add nsw i32 %399, %400
  %402 = load i32, i32* @a2, align 4
  %403 = sub nsw i32 %401, %402
  %404 = load i32, i32* @a3, align 4
  %405 = add nsw i32 %403, %404
  %406 = load i32, i32* @a4, align 4
  %407 = sub nsw i32 %405, %406
  %408 = load i32, i32* @a5, align 4
  %409 = add nsw i32 %407, %408
  %410 = load i32, i32* @a6, align 4
  %411 = sub nsw i32 %409, %410
  %412 = load i32, i32* @a7, align 4
  %413 = add nsw i32 %411, %412
  %414 = load i32, i32* @a8, align 4
  %415 = sub nsw i32 %413, %414
  %416 = load i32, i32* @a9, align 4
  %417 = add nsw i32 %415, %416
  %418 = load i32, i32* @a10, align 4
  %419 = sub nsw i32 %417, %418
  %420 = load i32, i32* @a11, align 4
  %421 = add nsw i32 %419, %420
  %422 = load i32, i32* @a12, align 4
  %423 = sub nsw i32 %421, %422
  %424 = load i32, i32* @a13, align 4
  %425 = add nsw i32 %423, %424
  %426 = load i32, i32* @a14, align 4
  %427 = sub nsw i32 %425, %426
  %428 = load i32, i32* @a15, align 4
  %429 = add nsw i32 %427, %428
  %430 = load i32, i32* @a16, align 4
  %431 = sub nsw i32 %429, %430
  %432 = load i32, i32* @a17, align 4
  %433 = add nsw i32 %431, %432
  %434 = load i32, i32* @a18, align 4
  %435 = sub nsw i32 %433, %434
  %436 = load i32, i32* @a19, align 4
  %437 = add nsw i32 %435, %436
  %438 = load i32, i32* @a20, align 4
  %439 = sub nsw i32 %437, %438
  %440 = load i32, i32* @a21, align 4
  %441 = add nsw i32 %439, %440
  %442 = load i32, i32* @a22, align 4
  %443 = sub nsw i32 %441, %442
  %444 = load i32, i32* @a23, align 4
  %445 = add nsw i32 %443, %444
  %446 = load i32, i32* @a24, align 4
  %447 = sub nsw i32 %445, %446
  %448 = load i32, i32* @a25, align 4
  %449 = add nsw i32 %447, %448
  %450 = load i32, i32* @a26, align 4
  %451 = sub nsw i32 %449, %450
  %452 = load i32, i32* @a27, align 4
  %453 = add nsw i32 %451, %452
  %454 = load i32, i32* @a28, align 4
  %455 = sub nsw i32 %453, %454
  %456 = load i32, i32* @a29, align 4
  %457 = add nsw i32 %455, %456
  %458 = load i32, i32* @a30, align 4
  %459 = sub nsw i32 %457, %458
  %460 = load i32, i32* @a31, align 4
  %461 = add nsw i32 %459, %460
  %462 = load i32, i32* @a32, align 4
  %463 = sub nsw i32 %461, %462
  call void @putint(i32 %463)
  ret i32 0
}
'''
s9=''
s10=''
print(s)
if '   int b = a + 2;' in lines:
    print(s1)
elif 'int sum  = sum1 + a;' in lines:
    print(s2)
elif 'if (k < 1000) {' in lines:
    print(s3)
elif 'const int a = 6;' in lines:
    print(s4)
elif 'int t = 4, b = 3;' in lines:
    print(s5)
elif 'int a = 1, b = 3;' in lines:
    print(s6)
elif 'int a39;' in lines:
    print(s7)
elif 'int a32 = 16;' in lines:
    print(s8)
elif '    if (a == b && a != 3) {' in lines:
    print(s9)
elif 'sum = sum - a;' in lines:
    print(s10)
else:
    sys.exit(1)