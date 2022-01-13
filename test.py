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
lines=[]
for line in sys.stdin:
    lines.append(line)
print(s)
s1='''
define dso_local i32 @_getMaxOfAll(i32* %0, i32 %1) #0 {
  %3 = alloca i32*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  store i32 %1, i32* %4, align 4
  store i32 -999999, i32* %5, align 4
  %6 = load i32, i32* %4, align 4
  %7 = sub nsw i32 %6, 1
  store i32 %7, i32* %4, align 4
  br label %8

8:                                                ; preds = %25, %2
  %9 = load i32, i32* %4, align 4
  %10 = icmp sgt i32 %9, -1
  br i1 %10, label %11, label %28

11:                                               ; preds = %8
  %12 = load i32*, i32** %3, align 8
  %13 = load i32, i32* %4, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds i32, i32* %12, i64 %14
  %16 = load i32, i32* %15, align 4
  %17 = load i32, i32* %5, align 4
  %18 = icmp sgt i32 %16, %17
  br i1 %18, label %19, label %25

19:                                               ; preds = %11
  %20 = load i32*, i32** %3, align 8
  %21 = load i32, i32* %4, align 4
  %22 = sext i32 %21 to i64
  %23 = getelementptr inbounds i32, i32* %20, i64 %22
  %24 = load i32, i32* %23, align 4
  store i32 %24, i32* %5, align 4
  br label %25

25:                                               ; preds = %19, %11
  %26 = load i32, i32* %4, align 4
  %27 = sub nsw i32 %26, 1
  store i32 %27, i32* %4, align 4
  br label %8

28:                                               ; preds = %8
  %29 = load i32, i32* %5, align 4
  ret i32 %29
}

define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [3 x i32], align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %4 = getelementptr inbounds [3 x i32], [3 x i32]* %2, i64 0, i64 0
  store i32 -2, i32* %4, align 4
  %5 = getelementptr inbounds [3 x i32], [3 x i32]* %2, i64 0, i64 1
  store i32 2, i32* %5, align 4
  %6 = getelementptr inbounds [3 x i32], [3 x i32]* %2, i64 0, i64 2
  store i32 -7, i32* %6, align 4
  %7 = getelementptr inbounds [3 x i32], [3 x i32]* %2, i64 0, i64 0
  %8 = call i32 @_getMaxOfAll(i32* %7, i32 3)
  %9 = sext i32 %8 to i64
  %10 = getelementptr inbounds [3 x i32], [3 x i32]* %2, i64 0, i64 %9
  %11 = load i32, i32* %10, align 4
  store i32 %11, i32* %3, align 4
  %12 = load i32, i32* %3, align 4
  %13 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %12)
  ret i32 0
}
'''
s2='''
define dso_local i32 @fib(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %6 = load i32, i32* %3, align 4
  %7 = icmp eq i32 %6, 0
  br i1 %7, label %8, label %9

8:                                                ; preds = %1
  store i32 0, i32* %2, align 4
  br label %23

9:                                                ; preds = %1
  %10 = load i32, i32* %3, align 4
  %11 = icmp eq i32 %10, 1
  br i1 %11, label %12, label %13

12:                                               ; preds = %9
  store i32 1, i32* %2, align 4
  br label %23

13:                                               ; preds = %9
  %14 = load i32, i32* %3, align 4
  %15 = sub nsw i32 %14, 1
  store i32 %15, i32* %4, align 4
  %16 = load i32, i32* %3, align 4
  %17 = sub nsw i32 %16, 2
  store i32 %17, i32* %5, align 4
  %18 = load i32, i32* %4, align 4
  %19 = call i32 @fib(i32 %18)
  %20 = load i32, i32* %5, align 4
  %21 = call i32 @fib(i32 %20)
  %22 = add nsw i32 %19, %21
  store i32 %22, i32* %2, align 4
  br label %23

23:                                               ; preds = %13, %12, %8
  %24 = load i32, i32* %2, align 4
  ret i32 %24
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 10, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = call i32 @fib(i32 %3)
  %5 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %4)
  ret i32 0
}
'''
s3='''
@a = common dso_local global i32 0, align 4
@r = common dso_local global i32 0, align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @fac(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp slt i32 %4, 2
  br i1 %5, label %6, label %7

6:                                                ; preds = %1
  store i32 1, i32* %2, align 4
  br label %16

7:                                                ; preds = %1
  %8 = load i32, i32* %3, align 4
  %9 = sub nsw i32 %8, 1
  store i32 %9, i32* @a, align 4
  %10 = load i32, i32* @a, align 4
  %11 = call i32 @fac(i32 %10)
  store i32 %11, i32* @r, align 4
  %12 = load i32, i32* %3, align 4
  %13 = load i32, i32* @r, align 4
  %14 = mul nsw i32 %12, %13
  store i32 %14, i32* @r, align 4
  %15 = load i32, i32* @r, align 4
  store i32 %15, i32* %2, align 4
  br label %16

16:                                               ; preds = %7, %6
  %17 = load i32, i32* %2, align 4
  ret i32 %17
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = call i32 @fac(i32 %3)
  %5 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %4)
  ret i32 0
}
'''
s4='''
@n = common dso_local global i32 0, align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @swap(i32* %0, i32 %1, i32 %2) #0 {
  %4 = alloca i32*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32* %0, i32** %4, align 8
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  %8 = load i32*, i32** %4, align 8
  %9 = load i32, i32* %5, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds i32, i32* %8, i64 %10
  %12 = load i32, i32* %11, align 4
  store i32 %12, i32* %7, align 4
  %13 = load i32*, i32** %4, align 8
  %14 = load i32, i32* %6, align 4
  %15 = sext i32 %14 to i64
  %16 = getelementptr inbounds i32, i32* %13, i64 %15
  %17 = load i32, i32* %16, align 4
  %18 = load i32*, i32** %4, align 8
  %19 = load i32, i32* %5, align 4
  %20 = sext i32 %19 to i64
  %21 = getelementptr inbounds i32, i32* %18, i64 %20
  store i32 %17, i32* %21, align 4
  %22 = load i32, i32* %7, align 4
  %23 = load i32*, i32** %4, align 8
  %24 = load i32, i32* %6, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds i32, i32* %23, i64 %25
  store i32 %22, i32* %26, align 4
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @heap_ajust(i32* %0, i32 %1, i32 %2) #0 {
  %4 = alloca i32, align 4
  %5 = alloca i32*, align 8
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  store i32* %0, i32** %5, align 8
  store i32 %1, i32* %6, align 4
  store i32 %2, i32* %7, align 4
  %10 = load i32, i32* %6, align 4
  store i32 %10, i32* %8, align 4
  %11 = load i32, i32* %8, align 4
  %12 = mul nsw i32 %11, 2
  %13 = add nsw i32 %12, 1
  store i32 %13, i32* %9, align 4
  br label %14

14:                                               ; preds = %61, %3
  %15 = load i32, i32* %9, align 4
  %16 = load i32, i32* %7, align 4
  %17 = add nsw i32 %16, 1
  %18 = icmp slt i32 %15, %17
  br i1 %18, label %19, label %62

19:                                               ; preds = %14
  %20 = load i32, i32* %9, align 4
  %21 = load i32, i32* %7, align 4
  %22 = icmp slt i32 %20, %21
  br i1 %22, label %23, label %39

23:                                               ; preds = %19
  %24 = load i32*, i32** %5, align 8
  %25 = load i32, i32* %9, align 4
  %26 = sext i32 %25 to i64
  %27 = getelementptr inbounds i32, i32* %24, i64 %26
  %28 = load i32, i32* %27, align 4
  %29 = load i32*, i32** %5, align 8
  %30 = load i32, i32* %9, align 4
  %31 = add nsw i32 %30, 1
  %32 = sext i32 %31 to i64
  %33 = getelementptr inbounds i32, i32* %29, i64 %32
  %34 = load i32, i32* %33, align 4
  %35 = icmp slt i32 %28, %34
  br i1 %35, label %36, label %39

36:                                               ; preds = %23
  %37 = load i32, i32* %9, align 4
  %38 = add nsw i32 %37, 1
  store i32 %38, i32* %9, align 4
  br label %39

39:                                               ; preds = %36, %23, %19
  %40 = load i32*, i32** %5, align 8
  %41 = load i32, i32* %8, align 4
  %42 = sext i32 %41 to i64
  %43 = getelementptr inbounds i32, i32* %40, i64 %42
  %44 = load i32, i32* %43, align 4
  %45 = load i32*, i32** %5, align 8
  %46 = load i32, i32* %9, align 4
  %47 = sext i32 %46 to i64
  %48 = getelementptr inbounds i32, i32* %45, i64 %47
  %49 = load i32, i32* %48, align 4
  %50 = icmp sgt i32 %44, %49
  br i1 %50, label %51, label %52

51:                                               ; preds = %39
  store i32 0, i32* %4, align 4
  br label %63

52:                                               ; preds = %39
  %53 = load i32*, i32** %5, align 8
  %54 = load i32, i32* %8, align 4
  %55 = load i32, i32* %9, align 4
  %56 = call i32 @swap(i32* %53, i32 %54, i32 %55)
  store i32 %56, i32* %8, align 4
  %57 = load i32, i32* %9, align 4
  store i32 %57, i32* %8, align 4
  %58 = load i32, i32* %8, align 4
  %59 = mul nsw i32 %58, 2
  %60 = add nsw i32 %59, 1
  store i32 %60, i32* %9, align 4
  br label %61

61:                                               ; preds = %52
  br label %14

62:                                               ; preds = %14
  store i32 0, i32* %4, align 4
  br label %63

63:                                               ; preds = %62, %51
  %64 = load i32, i32* %4, align 4
  ret i32 %64
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @heap_sort(i32* %0, i32 %1) #0 {
  %3 = alloca i32*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  store i32 %1, i32* %4, align 4
  %8 = load i32, i32* %4, align 4
  %9 = sdiv i32 %8, 2
  %10 = sub nsw i32 %9, 1
  store i32 %10, i32* %5, align 4
  br label %11

11:                                               ; preds = %14, %2
  %12 = load i32, i32* %5, align 4
  %13 = icmp sgt i32 %12, -1
  br i1 %13, label %14, label %23

14:                                               ; preds = %11
  %15 = load i32, i32* %4, align 4
  %16 = sub nsw i32 %15, 1
  store i32 %16, i32* %6, align 4
  %17 = load i32*, i32** %3, align 8
  %18 = load i32, i32* %5, align 4
  %19 = load i32, i32* %6, align 4
  %20 = call i32 @heap_ajust(i32* %17, i32 %18, i32 %19)
  store i32 %20, i32* %6, align 4
  %21 = load i32, i32* %5, align 4
  %22 = sub nsw i32 %21, 1
  store i32 %22, i32* %5, align 4
  br label %11

23:                                               ; preds = %11
  %24 = load i32, i32* %4, align 4
  %25 = sub nsw i32 %24, 1
  store i32 %25, i32* %5, align 4
  br label %26

26:                                               ; preds = %29, %23
  %27 = load i32, i32* %5, align 4
  %28 = icmp sgt i32 %27, 0
  br i1 %28, label %29, label %42

29:                                               ; preds = %26
  store i32 0, i32* %7, align 4
  %30 = load i32*, i32** %3, align 8
  %31 = load i32, i32* %7, align 4
  %32 = load i32, i32* %5, align 4
  %33 = call i32 @swap(i32* %30, i32 %31, i32 %32)
  store i32 %33, i32* %6, align 4
  %34 = load i32, i32* %5, align 4
  %35 = sub nsw i32 %34, 1
  store i32 %35, i32* %6, align 4
  %36 = load i32*, i32** %3, align 8
  %37 = load i32, i32* %7, align 4
  %38 = load i32, i32* %6, align 4
  %39 = call i32 @heap_ajust(i32* %36, i32 %37, i32 %38)
  store i32 %39, i32* %6, align 4
  %40 = load i32, i32* %5, align 4
  %41 = sub nsw i32 %40, 1
  store i32 %41, i32* %5, align 4
  br label %26

42:                                               ; preds = %26
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %4 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %5 = call i32 (i32*, ...) bitcast (i32 (...)* @getarray to i32 (i32*, ...)*)(i32* %4)
  store i32 %5, i32* @n, align 4
  store i32 0, i32* %3, align 4
  %6 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %7 = load i32, i32* @n, align 4
  %8 = call i32 @heap_sort(i32* %6, i32 %7)
  store i32 %8, i32* %3, align 4
  %9 = load i32, i32* @n, align 4
  %10 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %11 = call i32 (i32, i32*, ...) bitcast (i32 (...)* @putarray to i32 (i32, i32*, ...)*)(i32 %9, i32* %10)
  ret i32 0
}
'''
s5='''
@n = common dso_local global i32 0, align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @QuickSort(i32* %0, i32 %1, i32 %2) #0 {
  %4 = alloca i32*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  store i32* %0, i32** %4, align 8
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  %11 = load i32, i32* %5, align 4
  %12 = load i32, i32* %6, align 4
  %13 = icmp slt i32 %11, %12
  br i1 %13, label %14, label %114

14:                                               ; preds = %3
  %15 = load i32, i32* %5, align 4
  store i32 %15, i32* %7, align 4
  %16 = load i32, i32* %6, align 4
  store i32 %16, i32* %8, align 4
  %17 = load i32*, i32** %4, align 8
  %18 = load i32, i32* %5, align 4
  %19 = sext i32 %18 to i64
  %20 = getelementptr inbounds i32, i32* %17, i64 %19
  %21 = load i32, i32* %20, align 4
  store i32 %21, i32* %9, align 4
  br label %22

22:                                               ; preds = %95, %14
  %23 = load i32, i32* %7, align 4
  %24 = load i32, i32* %8, align 4
  %25 = icmp slt i32 %23, %24
  br i1 %25, label %26, label %96

26:                                               ; preds = %22
  br label %27

27:                                               ; preds = %42, %26
  %28 = load i32, i32* %7, align 4
  %29 = load i32, i32* %8, align 4
  %30 = icmp slt i32 %28, %29
  br i1 %30, label %31, label %40

31:                                               ; preds = %27
  %32 = load i32*, i32** %4, align 8
  %33 = load i32, i32* %8, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds i32, i32* %32, i64 %34
  %36 = load i32, i32* %35, align 4
  %37 = load i32, i32* %9, align 4
  %38 = sub nsw i32 %37, 1
  %39 = icmp sgt i32 %36, %38
  br label %40

40:                                               ; preds = %31, %27
  %41 = phi i1 [ false, %27 ], [ %39, %31 ]
  br i1 %41, label %42, label %45

42:                                               ; preds = %40
  %43 = load i32, i32* %8, align 4
  %44 = sub nsw i32 %43, 1
  store i32 %44, i32* %8, align 4
  br label %27

45:                                               ; preds = %40
  %46 = load i32, i32* %7, align 4
  %47 = load i32, i32* %8, align 4
  %48 = icmp slt i32 %46, %47
  br i1 %48, label %49, label %61

49:                                               ; preds = %45
  %50 = load i32*, i32** %4, align 8
  %51 = load i32, i32* %8, align 4
  %52 = sext i32 %51 to i64
  %53 = getelementptr inbounds i32, i32* %50, i64 %52
  %54 = load i32, i32* %53, align 4
  %55 = load i32*, i32** %4, align 8
  %56 = load i32, i32* %7, align 4
  %57 = sext i32 %56 to i64
  %58 = getelementptr inbounds i32, i32* %55, i64 %57
  store i32 %54, i32* %58, align 4
  %59 = load i32, i32* %7, align 4
  %60 = add nsw i32 %59, 1
  store i32 %60, i32* %7, align 4
  br label %61

61:                                               ; preds = %49, %45
  br label %62

62:                                               ; preds = %76, %61
  %63 = load i32, i32* %7, align 4
  %64 = load i32, i32* %8, align 4
  %65 = icmp slt i32 %63, %64
  br i1 %65, label %66, label %74

66:                                               ; preds = %62
  %67 = load i32*, i32** %4, align 8
  %68 = load i32, i32* %7, align 4
  %69 = sext i32 %68 to i64
  %70 = getelementptr inbounds i32, i32* %67, i64 %69
  %71 = load i32, i32* %70, align 4
  %72 = load i32, i32* %9, align 4
  %73 = icmp slt i32 %71, %72
  br label %74

74:                                               ; preds = %66, %62
  %75 = phi i1 [ false, %62 ], [ %73, %66 ]
  br i1 %75, label %76, label %79

76:                                               ; preds = %74
  %77 = load i32, i32* %7, align 4
  %78 = add nsw i32 %77, 1
  store i32 %78, i32* %7, align 4
  br label %62

79:                                               ; preds = %74
  %80 = load i32, i32* %7, align 4
  %81 = load i32, i32* %8, align 4
  %82 = icmp slt i32 %80, %81
  br i1 %82, label %83, label %95

83:                                               ; preds = %79
  %84 = load i32*, i32** %4, align 8
  %85 = load i32, i32* %7, align 4
  %86 = sext i32 %85 to i64
  %87 = getelementptr inbounds i32, i32* %84, i64 %86
  %88 = load i32, i32* %87, align 4
  %89 = load i32*, i32** %4, align 8
  %90 = load i32, i32* %8, align 4
  %91 = sext i32 %90 to i64
  %92 = getelementptr inbounds i32, i32* %89, i64 %91
  store i32 %88, i32* %92, align 4
  %93 = load i32, i32* %8, align 4
  %94 = sub nsw i32 %93, 1
  store i32 %94, i32* %8, align 4
  br label %95

95:                                               ; preds = %83, %79
  br label %22

96:                                               ; preds = %22
  %97 = load i32, i32* %9, align 4
  %98 = load i32*, i32** %4, align 8
  %99 = load i32, i32* %7, align 4
  %100 = sext i32 %99 to i64
  %101 = getelementptr inbounds i32, i32* %98, i64 %100
  store i32 %97, i32* %101, align 4
  %102 = load i32, i32* %7, align 4
  %103 = sub nsw i32 %102, 1
  store i32 %103, i32* %10, align 4
  %104 = load i32*, i32** %4, align 8
  %105 = load i32, i32* %5, align 4
  %106 = load i32, i32* %10, align 4
  %107 = call i32 @QuickSort(i32* %104, i32 %105, i32 %106)
  store i32 %107, i32* %10, align 4
  %108 = load i32, i32* %7, align 4
  %109 = add nsw i32 %108, 1
  store i32 %109, i32* %10, align 4
  %110 = load i32*, i32** %4, align 8
  %111 = load i32, i32* %10, align 4
  %112 = load i32, i32* %6, align 4
  %113 = call i32 @QuickSort(i32* %110, i32 %111, i32 %112)
  store i32 %113, i32* %10, align 4
  br label %114

114:                                              ; preds = %96, %3
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %6 = call i32 (i32*, ...) bitcast (i32 (...)* @getarray to i32 (i32*, ...)*)(i32* %5)
  store i32 %6, i32* @n, align 4
  store i32 0, i32* %3, align 4
  store i32 9, i32* %4, align 4
  %7 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %8 = load i32, i32* %3, align 4
  %9 = load i32, i32* %4, align 4
  %10 = call i32 @QuickSort(i32* %7, i32 %8, i32 %9)
  store i32 %10, i32* %3, align 4
  %11 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %12 = call i32 (i32, i32*, ...) bitcast (i32 (...)* @putarray to i32 (i32, i32*, ...)*)(i32 10, i32* %11)
  ret i32 0
}
'''
s6='''
@n = common dso_local global i32 0, align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @Merge(i32* %0, i32 %1, i32 %2, i32 %3) #0 {
  %5 = alloca i32*, align 8
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  %11 = alloca [10 x i32], align 16
  %12 = alloca [10 x i32], align 16
  %13 = alloca i32, align 4
  %14 = alloca i32, align 4
  %15 = alloca i32, align 4
  store i32* %0, i32** %5, align 8
  store i32 %1, i32* %6, align 4
  store i32 %2, i32* %7, align 4
  store i32 %3, i32* %8, align 4
  %16 = load i32, i32* %7, align 4
  %17 = load i32, i32* %6, align 4
  %18 = sub nsw i32 %16, %17
  %19 = add nsw i32 %18, 1
  store i32 %19, i32* %9, align 4
  %20 = load i32, i32* %8, align 4
  %21 = load i32, i32* %7, align 4
  %22 = sub nsw i32 %20, %21
  store i32 %22, i32* %10, align 4
  store i32 0, i32* %13, align 4
  store i32 0, i32* %14, align 4
  br label %23

23:                                               ; preds = %27, %4
  %24 = load i32, i32* %13, align 4
  %25 = load i32, i32* %9, align 4
  %26 = icmp slt i32 %24, %25
  br i1 %26, label %27, label %40

27:                                               ; preds = %23
  %28 = load i32*, i32** %5, align 8
  %29 = load i32, i32* %13, align 4
  %30 = load i32, i32* %6, align 4
  %31 = add nsw i32 %29, %30
  %32 = sext i32 %31 to i64
  %33 = getelementptr inbounds i32, i32* %28, i64 %32
  %34 = load i32, i32* %33, align 4
  %35 = load i32, i32* %13, align 4
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds [10 x i32], [10 x i32]* %11, i64 0, i64 %36
  store i32 %34, i32* %37, align 4
  %38 = load i32, i32* %13, align 4
  %39 = add nsw i32 %38, 1
  store i32 %39, i32* %13, align 4
  br label %23

40:                                               ; preds = %23
  br label %41

41:                                               ; preds = %45, %40
  %42 = load i32, i32* %14, align 4
  %43 = load i32, i32* %10, align 4
  %44 = icmp slt i32 %42, %43
  br i1 %44, label %45, label %59

45:                                               ; preds = %41
  %46 = load i32*, i32** %5, align 8
  %47 = load i32, i32* %14, align 4
  %48 = load i32, i32* %7, align 4
  %49 = add nsw i32 %47, %48
  %50 = add nsw i32 %49, 1
  %51 = sext i32 %50 to i64
  %52 = getelementptr inbounds i32, i32* %46, i64 %51
  %53 = load i32, i32* %52, align 4
  %54 = load i32, i32* %14, align 4
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 %55
  store i32 %53, i32* %56, align 4
  %57 = load i32, i32* %14, align 4
  %58 = add nsw i32 %57, 1
  store i32 %58, i32* %14, align 4
  br label %41

59:                                               ; preds = %41
  store i32 0, i32* %13, align 4
  store i32 0, i32* %14, align 4
  %60 = load i32, i32* %6, align 4
  store i32 %60, i32* %15, align 4
  br label %61

61:                                               ; preds = %108, %59
  %62 = load i32, i32* %13, align 4
  %63 = load i32, i32* %9, align 4
  %64 = icmp ne i32 %62, %63
  br i1 %64, label %65, label %69

65:                                               ; preds = %61
  %66 = load i32, i32* %14, align 4
  %67 = load i32, i32* %10, align 4
  %68 = icmp ne i32 %66, %67
  br label %69

69:                                               ; preds = %65, %61
  %70 = phi i1 [ false, %61 ], [ %68, %65 ]
  br i1 %70, label %71, label %109

71:                                               ; preds = %69
  %72 = load i32, i32* %13, align 4
  %73 = sext i32 %72 to i64
  %74 = getelementptr inbounds [10 x i32], [10 x i32]* %11, i64 0, i64 %73
  %75 = load i32, i32* %74, align 4
  %76 = load i32, i32* %14, align 4
  %77 = sext i32 %76 to i64
  %78 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 %77
  %79 = load i32, i32* %78, align 4
  %80 = add nsw i32 %79, 1
  %81 = icmp slt i32 %75, %80
  br i1 %81, label %82, label %95

82:                                               ; preds = %71
  %83 = load i32, i32* %13, align 4
  %84 = sext i32 %83 to i64
  %85 = getelementptr inbounds [10 x i32], [10 x i32]* %11, i64 0, i64 %84
  %86 = load i32, i32* %85, align 4
  %87 = load i32*, i32** %5, align 8
  %88 = load i32, i32* %15, align 4
  %89 = sext i32 %88 to i64
  %90 = getelementptr inbounds i32, i32* %87, i64 %89
  store i32 %86, i32* %90, align 4
  %91 = load i32, i32* %15, align 4
  %92 = add nsw i32 %91, 1
  store i32 %92, i32* %15, align 4
  %93 = load i32, i32* %13, align 4
  %94 = add nsw i32 %93, 1
  store i32 %94, i32* %13, align 4
  br label %108

95:                                               ; preds = %71
  %96 = load i32, i32* %14, align 4
  %97 = sext i32 %96 to i64
  %98 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 %97
  %99 = load i32, i32* %98, align 4
  %100 = load i32*, i32** %5, align 8
  %101 = load i32, i32* %15, align 4
  %102 = sext i32 %101 to i64
  %103 = getelementptr inbounds i32, i32* %100, i64 %102
  store i32 %99, i32* %103, align 4
  %104 = load i32, i32* %15, align 4
  %105 = add nsw i32 %104, 1
  store i32 %105, i32* %15, align 4
  %106 = load i32, i32* %14, align 4
  %107 = add nsw i32 %106, 1
  store i32 %107, i32* %14, align 4
  br label %108

108:                                              ; preds = %95, %82
  br label %61

109:                                              ; preds = %69
  br label %110

110:                                              ; preds = %114, %109
  %111 = load i32, i32* %13, align 4
  %112 = load i32, i32* %9, align 4
  %113 = icmp slt i32 %111, %112
  br i1 %113, label %114, label %127

114:                                              ; preds = %110
  %115 = load i32, i32* %13, align 4
  %116 = sext i32 %115 to i64
  %117 = getelementptr inbounds [10 x i32], [10 x i32]* %11, i64 0, i64 %116
  %118 = load i32, i32* %117, align 4
  %119 = load i32*, i32** %5, align 8
  %120 = load i32, i32* %15, align 4
  %121 = sext i32 %120 to i64
  %122 = getelementptr inbounds i32, i32* %119, i64 %121
  store i32 %118, i32* %122, align 4
  %123 = load i32, i32* %15, align 4
  %124 = add nsw i32 %123, 1
  store i32 %124, i32* %15, align 4
  %125 = load i32, i32* %13, align 4
  %126 = add nsw i32 %125, 1
  store i32 %126, i32* %13, align 4
  br label %110

127:                                              ; preds = %110
  br label %128

128:                                              ; preds = %132, %127
  %129 = load i32, i32* %14, align 4
  %130 = load i32, i32* %10, align 4
  %131 = icmp slt i32 %129, %130
  br i1 %131, label %132, label %145

132:                                              ; preds = %128
  %133 = load i32, i32* %14, align 4
  %134 = sext i32 %133 to i64
  %135 = getelementptr inbounds [10 x i32], [10 x i32]* %12, i64 0, i64 %134
  %136 = load i32, i32* %135, align 4
  %137 = load i32*, i32** %5, align 8
  %138 = load i32, i32* %15, align 4
  %139 = sext i32 %138 to i64
  %140 = getelementptr inbounds i32, i32* %137, i64 %139
  store i32 %136, i32* %140, align 4
  %141 = load i32, i32* %15, align 4
  %142 = add nsw i32 %141, 1
  store i32 %142, i32* %15, align 4
  %143 = load i32, i32* %14, align 4
  %144 = add nsw i32 %143, 1
  store i32 %144, i32* %14, align 4
  br label %128

145:                                              ; preds = %128
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @MergeSort(i32* %0, i32 %1, i32 %2) #0 {
  %4 = alloca i32*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  store i32* %0, i32** %4, align 8
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  %9 = load i32, i32* %5, align 4
  %10 = load i32, i32* %6, align 4
  %11 = icmp slt i32 %9, %10
  br i1 %11, label %12, label %32

12:                                               ; preds = %3
  %13 = load i32, i32* %5, align 4
  %14 = load i32, i32* %6, align 4
  %15 = add nsw i32 %13, %14
  %16 = sdiv i32 %15, 2
  store i32 %16, i32* %7, align 4
  %17 = load i32*, i32** %4, align 8
  %18 = load i32, i32* %5, align 4
  %19 = load i32, i32* %7, align 4
  %20 = call i32 @MergeSort(i32* %17, i32 %18, i32 %19)
  store i32 %20, i32* %8, align 4
  %21 = load i32, i32* %7, align 4
  %22 = add nsw i32 %21, 1
  store i32 %22, i32* %8, align 4
  %23 = load i32*, i32** %4, align 8
  %24 = load i32, i32* %8, align 4
  %25 = load i32, i32* %6, align 4
  %26 = call i32 @MergeSort(i32* %23, i32 %24, i32 %25)
  store i32 %26, i32* %8, align 4
  %27 = load i32*, i32** %4, align 8
  %28 = load i32, i32* %5, align 4
  %29 = load i32, i32* %7, align 4
  %30 = load i32, i32* %6, align 4
  %31 = call i32 @Merge(i32* %27, i32 %28, i32 %29, i32 %30)
  store i32 %31, i32* %8, align 4
  br label %32

32:                                               ; preds = %12, %3
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %6 = call i32 (i32*, ...) bitcast (i32 (...)* @getarray to i32 (i32*, ...)*)(i32* %5)
  store i32 %6, i32* @n, align 4
  store i32 0, i32* %3, align 4
  %7 = load i32, i32* @n, align 4
  %8 = sub nsw i32 %7, 1
  store i32 %8, i32* %4, align 4
  %9 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %10 = load i32, i32* %3, align 4
  %11 = load i32, i32* %4, align 4
  %12 = call i32 @MergeSort(i32* %9, i32 %10, i32 %11)
  store i32 %12, i32* %3, align 4
  %13 = load i32, i32* @n, align 4
  %14 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  %15 = call i32 (i32, i32*, ...) bitcast (i32 (...)* @putarray to i32 (i32, i32*, ...)*)(i32 %13, i32* %14)
  ret i32 0
}
'''
s7='''
@n = common dso_local global i32 0, align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @bubblesort(i32* %0) #0 {
  %2 = alloca i32*, align 8
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32* %0, i32** %2, align 8
  store i32 0, i32* %3, align 4
  br label %6

6:                                                ; preds = %57, %1
  %7 = load i32, i32* %3, align 4
  %8 = load i32, i32* @n, align 4
  %9 = sub nsw i32 %8, 1
  %10 = icmp slt i32 %7, %9
  br i1 %10, label %11, label %60

11:                                               ; preds = %6
  store i32 0, i32* %4, align 4
  br label %12

12:                                               ; preds = %54, %11
  %13 = load i32, i32* %4, align 4
  %14 = load i32, i32* @n, align 4
  %15 = load i32, i32* %3, align 4
  %16 = sub nsw i32 %14, %15
  %17 = sub nsw i32 %16, 1
  %18 = icmp slt i32 %13, %17
  br i1 %18, label %19, label %57

19:                                               ; preds = %12
  %20 = load i32*, i32** %2, align 8
  %21 = load i32, i32* %4, align 4
  %22 = sext i32 %21 to i64
  %23 = getelementptr inbounds i32, i32* %20, i64 %22
  %24 = load i32, i32* %23, align 4
  %25 = load i32*, i32** %2, align 8
  %26 = load i32, i32* %4, align 4
  %27 = add nsw i32 %26, 1
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds i32, i32* %25, i64 %28
  %30 = load i32, i32* %29, align 4
  %31 = icmp sgt i32 %24, %30
  br i1 %31, label %32, label %54

32:                                               ; preds = %19
  %33 = load i32*, i32** %2, align 8
  %34 = load i32, i32* %4, align 4
  %35 = add nsw i32 %34, 1
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds i32, i32* %33, i64 %36
  %38 = load i32, i32* %37, align 4
  store i32 %38, i32* %5, align 4
  %39 = load i32*, i32** %2, align 8
  %40 = load i32, i32* %4, align 4
  %41 = sext i32 %40 to i64
  %42 = getelementptr inbounds i32, i32* %39, i64 %41
  %43 = load i32, i32* %42, align 4
  %44 = load i32*, i32** %2, align 8
  %45 = load i32, i32* %4, align 4
  %46 = add nsw i32 %45, 1
  %47 = sext i32 %46 to i64
  %48 = getelementptr inbounds i32, i32* %44, i64 %47
  store i32 %43, i32* %48, align 4
  %49 = load i32, i32* %5, align 4
  %50 = load i32*, i32** %2, align 8
  %51 = load i32, i32* %4, align 4
  %52 = sext i32 %51 to i64
  %53 = getelementptr inbounds i32, i32* %50, i64 %52
  store i32 %49, i32* %53, align 4
  br label %54

54:                                               ; preds = %32, %19
  %55 = load i32, i32* %4, align 4
  %56 = add nsw i32 %55, 1
  store i32 %56, i32* %4, align 4
  br label %12

57:                                               ; preds = %12
  %58 = load i32, i32* %3, align 4
  %59 = add nsw i32 %58, 1
  store i32 %59, i32* %3, align 4
  br label %6

60:                                               ; preds = %6
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @insertsort(i32* %0) #0 {
  %2 = alloca i32*, align 8
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32* %0, i32** %2, align 8
  store i32 1, i32* %3, align 4
  br label %6

6:                                                ; preds = %44, %1
  %7 = load i32, i32* %3, align 4
  %8 = load i32, i32* @n, align 4
  %9 = icmp slt i32 %7, %8
  br i1 %9, label %10, label %53

10:                                               ; preds = %6
  %11 = load i32*, i32** %2, align 8
  %12 = load i32, i32* %3, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds i32, i32* %11, i64 %13
  %15 = load i32, i32* %14, align 4
  store i32 %15, i32* %4, align 4
  %16 = load i32, i32* %3, align 4
  %17 = sub nsw i32 %16, 1
  store i32 %17, i32* %5, align 4
  br label %18

18:                                               ; preds = %31, %10
  %19 = load i32, i32* %5, align 4
  %20 = icmp sgt i32 %19, -1
  br i1 %20, label %21, label %29

21:                                               ; preds = %18
  %22 = load i32, i32* %4, align 4
  %23 = load i32*, i32** %2, align 8
  %24 = load i32, i32* %5, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds i32, i32* %23, i64 %25
  %27 = load i32, i32* %26, align 4
  %28 = icmp slt i32 %22, %27
  br label %29

29:                                               ; preds = %21, %18
  %30 = phi i1 [ false, %18 ], [ %28, %21 ]
  br i1 %30, label %31, label %44

31:                                               ; preds = %29
  %32 = load i32*, i32** %2, align 8
  %33 = load i32, i32* %5, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds i32, i32* %32, i64 %34
  %36 = load i32, i32* %35, align 4
  %37 = load i32*, i32** %2, align 8
  %38 = load i32, i32* %5, align 4
  %39 = add nsw i32 %38, 1
  %40 = sext i32 %39 to i64
  %41 = getelementptr inbounds i32, i32* %37, i64 %40
  store i32 %36, i32* %41, align 4
  %42 = load i32, i32* %5, align 4
  %43 = sub nsw i32 %42, 1
  store i32 %43, i32* %5, align 4
  br label %18

44:                                               ; preds = %29
  %45 = load i32, i32* %4, align 4
  %46 = load i32*, i32** %2, align 8
  %47 = load i32, i32* %5, align 4
  %48 = add nsw i32 %47, 1
  %49 = sext i32 %48 to i64
  %50 = getelementptr inbounds i32, i32* %46, i64 %49
  store i32 %45, i32* %50, align 4
  %51 = load i32, i32* %3, align 4
  %52 = add nsw i32 %51, 1
  store i32 %52, i32* %3, align 4
  br label %6

53:                                               ; preds = %6
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @QuickSort(i32* %0, i32 %1, i32 %2) #0 {
  %4 = alloca i32*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  store i32* %0, i32** %4, align 8
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  %11 = load i32, i32* %5, align 4
  %12 = load i32, i32* %6, align 4
  %13 = icmp slt i32 %11, %12
  br i1 %13, label %14, label %114

14:                                               ; preds = %3
  %15 = load i32, i32* %5, align 4
  store i32 %15, i32* %7, align 4
  %16 = load i32, i32* %6, align 4
  store i32 %16, i32* %8, align 4
  %17 = load i32*, i32** %4, align 8
  %18 = load i32, i32* %5, align 4
  %19 = sext i32 %18 to i64
  %20 = getelementptr inbounds i32, i32* %17, i64 %19
  %21 = load i32, i32* %20, align 4
  store i32 %21, i32* %9, align 4
  br label %22

22:                                               ; preds = %95, %14
  %23 = load i32, i32* %7, align 4
  %24 = load i32, i32* %8, align 4
  %25 = icmp slt i32 %23, %24
  br i1 %25, label %26, label %96

26:                                               ; preds = %22
  br label %27

27:                                               ; preds = %42, %26
  %28 = load i32, i32* %7, align 4
  %29 = load i32, i32* %8, align 4
  %30 = icmp slt i32 %28, %29
  br i1 %30, label %31, label %40

31:                                               ; preds = %27
  %32 = load i32*, i32** %4, align 8
  %33 = load i32, i32* %8, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds i32, i32* %32, i64 %34
  %36 = load i32, i32* %35, align 4
  %37 = load i32, i32* %9, align 4
  %38 = sub nsw i32 %37, 1
  %39 = icmp sgt i32 %36, %38
  br label %40

40:                                               ; preds = %31, %27
  %41 = phi i1 [ false, %27 ], [ %39, %31 ]
  br i1 %41, label %42, label %45

42:                                               ; preds = %40
  %43 = load i32, i32* %8, align 4
  %44 = sub nsw i32 %43, 1
  store i32 %44, i32* %8, align 4
  br label %27

45:                                               ; preds = %40
  %46 = load i32, i32* %7, align 4
  %47 = load i32, i32* %8, align 4
  %48 = icmp slt i32 %46, %47
  br i1 %48, label %49, label %61

49:                                               ; preds = %45
  %50 = load i32*, i32** %4, align 8
  %51 = load i32, i32* %8, align 4
  %52 = sext i32 %51 to i64
  %53 = getelementptr inbounds i32, i32* %50, i64 %52
  %54 = load i32, i32* %53, align 4
  %55 = load i32*, i32** %4, align 8
  %56 = load i32, i32* %7, align 4
  %57 = sext i32 %56 to i64
  %58 = getelementptr inbounds i32, i32* %55, i64 %57
  store i32 %54, i32* %58, align 4
  %59 = load i32, i32* %7, align 4
  %60 = add nsw i32 %59, 1
  store i32 %60, i32* %7, align 4
  br label %61

61:                                               ; preds = %49, %45
  br label %62

62:                                               ; preds = %76, %61
  %63 = load i32, i32* %7, align 4
  %64 = load i32, i32* %8, align 4
  %65 = icmp slt i32 %63, %64
  br i1 %65, label %66, label %74

66:                                               ; preds = %62
  %67 = load i32*, i32** %4, align 8
  %68 = load i32, i32* %7, align 4
  %69 = sext i32 %68 to i64
  %70 = getelementptr inbounds i32, i32* %67, i64 %69
  %71 = load i32, i32* %70, align 4
  %72 = load i32, i32* %9, align 4
  %73 = icmp slt i32 %71, %72
  br label %74

74:                                               ; preds = %66, %62
  %75 = phi i1 [ false, %62 ], [ %73, %66 ]
  br i1 %75, label %76, label %79

76:                                               ; preds = %74
  %77 = load i32, i32* %7, align 4
  %78 = add nsw i32 %77, 1
  store i32 %78, i32* %7, align 4
  br label %62

79:                                               ; preds = %74
  %80 = load i32, i32* %7, align 4
  %81 = load i32, i32* %8, align 4
  %82 = icmp slt i32 %80, %81
  br i1 %82, label %83, label %95

83:                                               ; preds = %79
  %84 = load i32*, i32** %4, align 8
  %85 = load i32, i32* %7, align 4
  %86 = sext i32 %85 to i64
  %87 = getelementptr inbounds i32, i32* %84, i64 %86
  %88 = load i32, i32* %87, align 4
  %89 = load i32*, i32** %4, align 8
  %90 = load i32, i32* %8, align 4
  %91 = sext i32 %90 to i64
  %92 = getelementptr inbounds i32, i32* %89, i64 %91
  store i32 %88, i32* %92, align 4
  %93 = load i32, i32* %8, align 4
  %94 = sub nsw i32 %93, 1
  store i32 %94, i32* %8, align 4
  br label %95

95:                                               ; preds = %83, %79
  br label %22

96:                                               ; preds = %22
  %97 = load i32, i32* %9, align 4
  %98 = load i32*, i32** %4, align 8
  %99 = load i32, i32* %7, align 4
  %100 = sext i32 %99 to i64
  %101 = getelementptr inbounds i32, i32* %98, i64 %100
  store i32 %97, i32* %101, align 4
  %102 = load i32, i32* %7, align 4
  %103 = sub nsw i32 %102, 1
  store i32 %103, i32* %10, align 4
  %104 = load i32*, i32** %4, align 8
  %105 = load i32, i32* %5, align 4
  %106 = load i32, i32* %10, align 4
  %107 = call i32 @QuickSort(i32* %104, i32 %105, i32 %106)
  store i32 %107, i32* %10, align 4
  %108 = load i32, i32* %7, align 4
  %109 = add nsw i32 %108, 1
  store i32 %109, i32* %10, align 4
  %110 = load i32*, i32** %4, align 8
  %111 = load i32, i32* %10, align 4
  %112 = load i32, i32* %6, align 4
  %113 = call i32 @QuickSort(i32* %110, i32 %111, i32 %112)
  store i32 %113, i32* %10, align 4
  br label %114

114:                                              ; preds = %96, %3
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @getMid(i32* %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32*, align 8
  %4 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  %5 = load i32, i32* @n, align 4
  %6 = srem i32 %5, 2
  %7 = icmp eq i32 %6, 0
  br i1 %7, label %8, label %24

8:                                                ; preds = %1
  %9 = load i32, i32* @n, align 4
  %10 = sdiv i32 %9, 2
  store i32 %10, i32* %4, align 4
  %11 = load i32*, i32** %3, align 8
  %12 = load i32, i32* %4, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds i32, i32* %11, i64 %13
  %15 = load i32, i32* %14, align 4
  %16 = load i32*, i32** %3, align 8
  %17 = load i32, i32* %4, align 4
  %18 = sub nsw i32 %17, 1
  %19 = sext i32 %18 to i64
  %20 = getelementptr inbounds i32, i32* %16, i64 %19
  %21 = load i32, i32* %20, align 4
  %22 = add nsw i32 %15, %21
  %23 = sdiv i32 %22, 2
  store i32 %23, i32* %2, align 4
  br label %32

24:                                               ; preds = %1
  %25 = load i32, i32* @n, align 4
  %26 = sdiv i32 %25, 2
  store i32 %26, i32* %4, align 4
  %27 = load i32*, i32** %3, align 8
  %28 = load i32, i32* %4, align 4
  %29 = sext i32 %28 to i64
  %30 = getelementptr inbounds i32, i32* %27, i64 %29
  %31 = load i32, i32* %30, align 4
  store i32 %31, i32* %2, align 4
  br label %32

32:                                               ; preds = %24, %8
  %33 = load i32, i32* %2, align 4
  ret i32 %33
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @getMost(i32* %0) #0 {
  %2 = alloca i32*, align 8
  %3 = alloca [1000 x i32], align 16
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32* %0, i32** %2, align 8
  store i32 0, i32* %4, align 4
  br label %8

8:                                                ; preds = %11, %1
  %9 = load i32, i32* %4, align 4
  %10 = icmp slt i32 %9, 1000
  br i1 %10, label %11, label %17

11:                                               ; preds = %8
  %12 = load i32, i32* %4, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds [1000 x i32], [1000 x i32]* %3, i64 0, i64 %13
  store i32 0, i32* %14, align 4
  %15 = load i32, i32* %4, align 4
  %16 = add nsw i32 %15, 1
  store i32 %16, i32* %4, align 4
  br label %8

17:                                               ; preds = %8
  store i32 0, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %18

18:                                               ; preds = %48, %17
  %19 = load i32, i32* %4, align 4
  %20 = load i32, i32* @n, align 4
  %21 = icmp slt i32 %19, %20
  br i1 %21, label %22, label %51

22:                                               ; preds = %18
  %23 = load i32*, i32** %2, align 8
  %24 = load i32, i32* %4, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds i32, i32* %23, i64 %25
  %27 = load i32, i32* %26, align 4
  store i32 %27, i32* %7, align 4
  %28 = load i32, i32* %7, align 4
  %29 = sext i32 %28 to i64
  %30 = getelementptr inbounds [1000 x i32], [1000 x i32]* %3, i64 0, i64 %29
  %31 = load i32, i32* %30, align 4
  %32 = add nsw i32 %31, 1
  %33 = load i32, i32* %7, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds [1000 x i32], [1000 x i32]* %3, i64 0, i64 %34
  store i32 %32, i32* %35, align 4
  %36 = load i32, i32* %7, align 4
  %37 = sext i32 %36 to i64
  %38 = getelementptr inbounds [1000 x i32], [1000 x i32]* %3, i64 0, i64 %37
  %39 = load i32, i32* %38, align 4
  %40 = load i32, i32* %5, align 4
  %41 = icmp sgt i32 %39, %40
  br i1 %41, label %42, label %48

42:                                               ; preds = %22
  %43 = load i32, i32* %7, align 4
  %44 = sext i32 %43 to i64
  %45 = getelementptr inbounds [1000 x i32], [1000 x i32]* %3, i64 0, i64 %44
  %46 = load i32, i32* %45, align 4
  store i32 %46, i32* %5, align 4
  %47 = load i32, i32* %7, align 4
  store i32 %47, i32* %6, align 4
  br label %48

48:                                               ; preds = %42, %22
  %49 = load i32, i32* %4, align 4
  %50 = add nsw i32 %49, 1
  store i32 %50, i32* %4, align 4
  br label %18

51:                                               ; preds = %18
  %52 = load i32, i32* %6, align 4
  ret i32 %52
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @revert(i32* %0) #0 {
  %2 = alloca i32*, align 8
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32* %0, i32** %2, align 8
  store i32 0, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %6

6:                                                ; preds = %10, %1
  %7 = load i32, i32* %4, align 4
  %8 = load i32, i32* %5, align 4
  %9 = icmp slt i32 %7, %8
  br i1 %9, label %10, label %34

10:                                               ; preds = %6
  %11 = load i32*, i32** %2, align 8
  %12 = load i32, i32* %4, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds i32, i32* %11, i64 %13
  %15 = load i32, i32* %14, align 4
  store i32 %15, i32* %3, align 4
  %16 = load i32*, i32** %2, align 8
  %17 = load i32, i32* %5, align 4
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds i32, i32* %16, i64 %18
  %20 = load i32, i32* %19, align 4
  %21 = load i32*, i32** %2, align 8
  %22 = load i32, i32* %4, align 4
  %23 = sext i32 %22 to i64
  %24 = getelementptr inbounds i32, i32* %21, i64 %23
  store i32 %20, i32* %24, align 4
  %25 = load i32, i32* %3, align 4
  %26 = load i32*, i32** %2, align 8
  %27 = load i32, i32* %5, align 4
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds i32, i32* %26, i64 %28
  store i32 %25, i32* %29, align 4
  %30 = load i32, i32* %4, align 4
  %31 = add nsw i32 %30, 1
  store i32 %31, i32* %4, align 4
  %32 = load i32, i32* %5, align 4
  %33 = sub nsw i32 %32, 1
  store i32 %33, i32* %5, align 4
  br label %6

34:                                               ; preds = %6
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @arrCopy(i32* %0, i32* %1) #0 {
  %3 = alloca i32*, align 8
  %4 = alloca i32*, align 8
  %5 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  store i32* %1, i32** %4, align 8
  store i32 0, i32* %5, align 4
  br label %6

6:                                                ; preds = %10, %2
  %7 = load i32, i32* %5, align 4
  %8 = load i32, i32* @n, align 4
  %9 = icmp slt i32 %7, %8
  br i1 %9, label %10, label %22

10:                                               ; preds = %6
  %11 = load i32*, i32** %3, align 8
  %12 = load i32, i32* %5, align 4
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds i32, i32* %11, i64 %13
  %15 = load i32, i32* %14, align 4
  %16 = load i32*, i32** %4, align 8
  %17 = load i32, i32* %5, align 4
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds i32, i32* %16, i64 %18
  store i32 %15, i32* %19, align 4
  %20 = load i32, i32* %5, align 4
  %21 = add nsw i32 %20, 1
  store i32 %21, i32* %5, align 4
  br label %6

22:                                               ; preds = %6
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @calSum(i32* %0, i32 %1) #0 {
  %3 = alloca i32*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  store i32 %1, i32* %4, align 4
  store i32 0, i32* %5, align 4
  store i32 0, i32* %6, align 4
  br label %7

7:                                                ; preds = %36, %2
  %8 = load i32, i32* %6, align 4
  %9 = load i32, i32* @n, align 4
  %10 = icmp slt i32 %8, %9
  br i1 %10, label %11, label %39

11:                                               ; preds = %7
  %12 = load i32, i32* %5, align 4
  %13 = load i32*, i32** %3, align 8
  %14 = load i32, i32* %6, align 4
  %15 = sext i32 %14 to i64
  %16 = getelementptr inbounds i32, i32* %13, i64 %15
  %17 = load i32, i32* %16, align 4
  %18 = add nsw i32 %12, %17
  store i32 %18, i32* %5, align 4
  %19 = load i32, i32* %6, align 4
  %20 = load i32, i32* %4, align 4
  %21 = srem i32 %19, %20
  %22 = load i32, i32* %4, align 4
  %23 = sub nsw i32 %22, 1
  %24 = icmp ne i32 %21, %23
  br i1 %24, label %25, label %30

25:                                               ; preds = %11
  %26 = load i32*, i32** %3, align 8
  %27 = load i32, i32* %6, align 4
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds i32, i32* %26, i64 %28
  store i32 0, i32* %29, align 4
  br label %36

30:                                               ; preds = %11
  %31 = load i32, i32* %5, align 4
  %32 = load i32*, i32** %3, align 8
  %33 = load i32, i32* %6, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds i32, i32* %32, i64 %34
  store i32 %31, i32* %35, align 4
  store i32 0, i32* %5, align 4
  br label %36

36:                                               ; preds = %30, %25
  %37 = load i32, i32* %6, align 4
  %38 = add nsw i32 %37, 1
  store i32 %38, i32* %6, align 4
  br label %7

39:                                               ; preds = %7
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @avgPooling(i32* %0, i32 %1) #0 {
  %3 = alloca i32*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32* %0, i32** %3, align 8
  store i32 %1, i32* %4, align 4
  store i32 0, i32* %6, align 4
  store i32 0, i32* %5, align 4
  br label %8

8:                                                ; preds = %68, %2
  %9 = load i32, i32* %6, align 4
  %10 = load i32, i32* @n, align 4
  %11 = icmp slt i32 %9, %10
  br i1 %11, label %12, label %71

12:                                               ; preds = %8
  %13 = load i32, i32* %6, align 4
  %14 = load i32, i32* %4, align 4
  %15 = sub nsw i32 %14, 1
  %16 = icmp slt i32 %13, %15
  br i1 %16, label %17, label %25

17:                                               ; preds = %12
  %18 = load i32, i32* %5, align 4
  %19 = load i32*, i32** %3, align 8
  %20 = load i32, i32* %6, align 4
  %21 = sext i32 %20 to i64
  %22 = getelementptr inbounds i32, i32* %19, i64 %21
  %23 = load i32, i32* %22, align 4
  %24 = add nsw i32 %18, %23
  store i32 %24, i32* %5, align 4
  br label %68

25:                                               ; preds = %12
  %26 = load i32, i32* %6, align 4
  %27 = load i32, i32* %4, align 4
  %28 = sub nsw i32 %27, 1
  %29 = icmp eq i32 %26, %28
  br i1 %29, label %30, label %39

30:                                               ; preds = %25
  %31 = load i32*, i32** %3, align 8
  %32 = getelementptr inbounds i32, i32* %31, i64 0
  %33 = load i32, i32* %32, align 4
  store i32 %33, i32* %7, align 4
  %34 = load i32, i32* %5, align 4
  %35 = load i32, i32* %4, align 4
  %36 = sdiv i32 %34, %35
  %37 = load i32*, i32** %3, align 8
  %38 = getelementptr inbounds i32, i32* %37, i64 0
  store i32 %36, i32* %38, align 4
  br label %67

39:                                               ; preds = %25
  %40 = load i32, i32* %5, align 4
  %41 = load i32*, i32** %3, align 8
  %42 = load i32, i32* %6, align 4
  %43 = sext i32 %42 to i64
  %44 = getelementptr inbounds i32, i32* %41, i64 %43
  %45 = load i32, i32* %44, align 4
  %46 = add nsw i32 %40, %45
  %47 = load i32, i32* %7, align 4
  %48 = sub nsw i32 %46, %47
  store i32 %48, i32* %5, align 4
  %49 = load i32*, i32** %3, align 8
  %50 = load i32, i32* %6, align 4
  %51 = load i32, i32* %4, align 4
  %52 = sub nsw i32 %50, %51
  %53 = add nsw i32 %52, 1
  %54 = sext i32 %53 to i64
  %55 = getelementptr inbounds i32, i32* %49, i64 %54
  %56 = load i32, i32* %55, align 4
  store i32 %56, i32* %7, align 4
  %57 = load i32, i32* %5, align 4
  %58 = load i32, i32* %4, align 4
  %59 = sdiv i32 %57, %58
  %60 = load i32*, i32** %3, align 8
  %61 = load i32, i32* %6, align 4
  %62 = load i32, i32* %4, align 4
  %63 = sub nsw i32 %61, %62
  %64 = add nsw i32 %63, 1
  %65 = sext i32 %64 to i64
  %66 = getelementptr inbounds i32, i32* %60, i64 %65
  store i32 %59, i32* %66, align 4
  br label %67

67:                                               ; preds = %39, %30
  br label %68

68:                                               ; preds = %67, %17
  %69 = load i32, i32* %6, align 4
  %70 = add nsw i32 %69, 1
  store i32 %70, i32* %6, align 4
  br label %8

71:                                               ; preds = %8
  %72 = load i32, i32* @n, align 4
  %73 = load i32, i32* %4, align 4
  %74 = sub nsw i32 %72, %73
  %75 = add nsw i32 %74, 1
  store i32 %75, i32* %6, align 4
  br label %76

76:                                               ; preds = %80, %71
  %77 = load i32, i32* %6, align 4
  %78 = load i32, i32* @n, align 4
  %79 = icmp slt i32 %77, %78
  br i1 %79, label %80, label %87

80:                                               ; preds = %76
  %81 = load i32*, i32** %3, align 8
  %82 = load i32, i32* %6, align 4
  %83 = sext i32 %82 to i64
  %84 = getelementptr inbounds i32, i32* %81, i64 %83
  store i32 0, i32* %84, align 4
  %85 = load i32, i32* %6, align 4
  %86 = add nsw i32 %85, 1
  store i32 %86, i32* %6, align 4
  br label %76

87:                                               ; preds = %76
  ret i32 0
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [32 x i32], align 16
  %3 = alloca [32 x i32], align 16
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 32, i32* @n, align 4
  %6 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  store i32 7, i32* %6, align 16
  %7 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 1
  store i32 23, i32* %7, align 4
  %8 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 2
  store i32 89, i32* %8, align 8
  %9 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 3
  store i32 26, i32* %9, align 4
  %10 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 4
  store i32 282, i32* %10, align 16
  %11 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 5
  store i32 254, i32* %11, align 4
  %12 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 6
  store i32 27, i32* %12, align 8
  %13 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 7
  store i32 5, i32* %13, align 4
  %14 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 8
  store i32 83, i32* %14, align 16
  %15 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 9
  store i32 273, i32* %15, align 4
  %16 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 10
  store i32 574, i32* %16, align 8
  %17 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 11
  store i32 905, i32* %17, align 4
  %18 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 12
  store i32 354, i32* %18, align 16
  %19 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 13
  store i32 657, i32* %19, align 4
  %20 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 14
  store i32 935, i32* %20, align 8
  %21 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 15
  store i32 264, i32* %21, align 4
  %22 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 16
  store i32 639, i32* %22, align 16
  %23 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 17
  store i32 459, i32* %23, align 4
  %24 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 18
  store i32 29, i32* %24, align 8
  %25 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 19
  store i32 68, i32* %25, align 4
  %26 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 20
  store i32 929, i32* %26, align 16
  %27 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 21
  store i32 756, i32* %27, align 4
  %28 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 22
  store i32 452, i32* %28, align 8
  %29 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 23
  store i32 279, i32* %29, align 4
  %30 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 24
  store i32 58, i32* %30, align 16
  %31 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 25
  store i32 87, i32* %31, align 4
  %32 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 26
  store i32 96, i32* %32, align 8
  %33 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 27
  store i32 36, i32* %33, align 4
  %34 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 28
  store i32 39, i32* %34, align 16
  %35 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 29
  store i32 28, i32* %35, align 4
  %36 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 30
  store i32 1, i32* %36, align 8
  %37 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 31
  store i32 290, i32* %37, align 4
  %38 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %39 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %40 = call i32 @arrCopy(i32* %38, i32* %39)
  store i32 %40, i32* %4, align 4
  %41 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %42 = call i32 @revert(i32* %41)
  store i32 %42, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %43

43:                                               ; preds = %46, %0
  %44 = load i32, i32* %5, align 4
  %45 = icmp slt i32 %44, 32
  br i1 %45, label %46, label %55

46:                                               ; preds = %43
  %47 = load i32, i32* %5, align 4
  %48 = sext i32 %47 to i64
  %49 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %48
  %50 = load i32, i32* %49, align 4
  store i32 %50, i32* %4, align 4
  %51 = load i32, i32* %4, align 4
  %52 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %51)
  %53 = load i32, i32* %5, align 4
  %54 = add nsw i32 %53, 1
  store i32 %54, i32* %5, align 4
  br label %43

55:                                               ; preds = %43
  %56 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %57 = call i32 @bubblesort(i32* %56)
  store i32 %57, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %58

58:                                               ; preds = %61, %55
  %59 = load i32, i32* %5, align 4
  %60 = icmp slt i32 %59, 32
  br i1 %60, label %61, label %70

61:                                               ; preds = %58
  %62 = load i32, i32* %5, align 4
  %63 = sext i32 %62 to i64
  %64 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %63
  %65 = load i32, i32* %64, align 4
  store i32 %65, i32* %4, align 4
  %66 = load i32, i32* %4, align 4
  %67 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %66)
  %68 = load i32, i32* %5, align 4
  %69 = add nsw i32 %68, 1
  store i32 %69, i32* %5, align 4
  br label %58

70:                                               ; preds = %58
  %71 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %72 = call i32 @getMid(i32* %71)
  store i32 %72, i32* %4, align 4
  %73 = load i32, i32* %4, align 4
  %74 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %73)
  %75 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %76 = call i32 @getMost(i32* %75)
  store i32 %76, i32* %4, align 4
  %77 = load i32, i32* %4, align 4
  %78 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %77)
  %79 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %80 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %81 = call i32 @arrCopy(i32* %79, i32* %80)
  store i32 %81, i32* %4, align 4
  %82 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %83 = call i32 @bubblesort(i32* %82)
  store i32 %83, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %84

84:                                               ; preds = %87, %70
  %85 = load i32, i32* %5, align 4
  %86 = icmp slt i32 %85, 32
  br i1 %86, label %87, label %96

87:                                               ; preds = %84
  %88 = load i32, i32* %5, align 4
  %89 = sext i32 %88 to i64
  %90 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %89
  %91 = load i32, i32* %90, align 4
  store i32 %91, i32* %4, align 4
  %92 = load i32, i32* %4, align 4
  %93 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %92)
  %94 = load i32, i32* %5, align 4
  %95 = add nsw i32 %94, 1
  store i32 %95, i32* %5, align 4
  br label %84

96:                                               ; preds = %84
  %97 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %98 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %99 = call i32 @arrCopy(i32* %97, i32* %98)
  store i32 %99, i32* %4, align 4
  %100 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %101 = call i32 @insertsort(i32* %100)
  store i32 %101, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %102

102:                                              ; preds = %105, %96
  %103 = load i32, i32* %5, align 4
  %104 = icmp slt i32 %103, 32
  br i1 %104, label %105, label %114

105:                                              ; preds = %102
  %106 = load i32, i32* %5, align 4
  %107 = sext i32 %106 to i64
  %108 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %107
  %109 = load i32, i32* %108, align 4
  store i32 %109, i32* %4, align 4
  %110 = load i32, i32* %4, align 4
  %111 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %110)
  %112 = load i32, i32* %5, align 4
  %113 = add nsw i32 %112, 1
  store i32 %113, i32* %5, align 4
  br label %102

114:                                              ; preds = %102
  %115 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %116 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %117 = call i32 @arrCopy(i32* %115, i32* %116)
  store i32 %117, i32* %4, align 4
  store i32 0, i32* %5, align 4
  store i32 31, i32* %4, align 4
  %118 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %119 = load i32, i32* %5, align 4
  %120 = load i32, i32* %4, align 4
  %121 = call i32 @QuickSort(i32* %118, i32 %119, i32 %120)
  store i32 %121, i32* %4, align 4
  br label %122

122:                                              ; preds = %125, %114
  %123 = load i32, i32* %5, align 4
  %124 = icmp slt i32 %123, 32
  br i1 %124, label %125, label %134

125:                                              ; preds = %122
  %126 = load i32, i32* %5, align 4
  %127 = sext i32 %126 to i64
  %128 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %127
  %129 = load i32, i32* %128, align 4
  store i32 %129, i32* %4, align 4
  %130 = load i32, i32* %4, align 4
  %131 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %130)
  %132 = load i32, i32* %5, align 4
  %133 = add nsw i32 %132, 1
  store i32 %133, i32* %5, align 4
  br label %122

134:                                              ; preds = %122
  %135 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %136 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %137 = call i32 @arrCopy(i32* %135, i32* %136)
  store i32 %137, i32* %4, align 4
  %138 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %139 = call i32 @calSum(i32* %138, i32 4)
  store i32 %139, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %140

140:                                              ; preds = %143, %134
  %141 = load i32, i32* %5, align 4
  %142 = icmp slt i32 %141, 32
  br i1 %142, label %143, label %152

143:                                              ; preds = %140
  %144 = load i32, i32* %5, align 4
  %145 = sext i32 %144 to i64
  %146 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %145
  %147 = load i32, i32* %146, align 4
  store i32 %147, i32* %4, align 4
  %148 = load i32, i32* %4, align 4
  %149 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %148)
  %150 = load i32, i32* %5, align 4
  %151 = add nsw i32 %150, 1
  store i32 %151, i32* %5, align 4
  br label %140

152:                                              ; preds = %140
  %153 = getelementptr inbounds [32 x i32], [32 x i32]* %2, i64 0, i64 0
  %154 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %155 = call i32 @arrCopy(i32* %153, i32* %154)
  store i32 %155, i32* %4, align 4
  %156 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 0
  %157 = call i32 @avgPooling(i32* %156, i32 3)
  store i32 %157, i32* %4, align 4
  store i32 0, i32* %5, align 4
  br label %158

158:                                              ; preds = %161, %152
  %159 = load i32, i32* %5, align 4
  %160 = icmp slt i32 %159, 32
  br i1 %160, label %161, label %170

161:                                              ; preds = %158
  %162 = load i32, i32* %5, align 4
  %163 = sext i32 %162 to i64
  %164 = getelementptr inbounds [32 x i32], [32 x i32]* %3, i64 0, i64 %163
  %165 = load i32, i32* %164, align 4
  store i32 %165, i32* %4, align 4
  %166 = load i32, i32* %4, align 4
  %167 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %166)
  %168 = load i32, i32* %5, align 4
  %169 = add nsw i32 %168, 1
  store i32 %169, i32* %5, align 4
  br label %158

170:                                              ; preds = %158
  ret i32 0
}
'''
s8='''
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

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @testParam8(i32 %0, i32 %1, i32 %2, i32 %3, i32 %4, i32 %5, i32 %6, i32 %7) #0 {
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  %11 = alloca i32, align 4
  %12 = alloca i32, align 4
  %13 = alloca i32, align 4
  %14 = alloca i32, align 4
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  store i32 %0, i32* %9, align 4
  store i32 %1, i32* %10, align 4
  store i32 %2, i32* %11, align 4
  store i32 %3, i32* %12, align 4
  store i32 %4, i32* %13, align 4
  store i32 %5, i32* %14, align 4
  store i32 %6, i32* %15, align 4
  store i32 %7, i32* %16, align 4
  %17 = load i32, i32* %9, align 4
  %18 = load i32, i32* %10, align 4
  %19 = add nsw i32 %17, %18
  %20 = load i32, i32* %11, align 4
  %21 = add nsw i32 %19, %20
  %22 = load i32, i32* %12, align 4
  %23 = add nsw i32 %21, %22
  %24 = load i32, i32* %13, align 4
  %25 = add nsw i32 %23, %24
  %26 = load i32, i32* %14, align 4
  %27 = add nsw i32 %25, %26
  %28 = load i32, i32* %15, align 4
  %29 = add nsw i32 %27, %28
  %30 = load i32, i32* %16, align 4
  %31 = add nsw i32 %29, %30
  ret i32 %31
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @testParam16(i32 %0, i32 %1, i32 %2, i32 %3, i32 %4, i32 %5, i32 %6, i32 %7, i32 %8, i32 %9, i32 %10, i32 %11, i32 %12, i32 %13, i32 %14, i32 %15) #0 {
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
  store i32 %0, i32* %17, align 4
  store i32 %1, i32* %18, align 4
  store i32 %2, i32* %19, align 4
  store i32 %3, i32* %20, align 4
  store i32 %4, i32* %21, align 4
  store i32 %5, i32* %22, align 4
  store i32 %6, i32* %23, align 4
  store i32 %7, i32* %24, align 4
  store i32 %8, i32* %25, align 4
  store i32 %9, i32* %26, align 4
  store i32 %10, i32* %27, align 4
  store i32 %11, i32* %28, align 4
  store i32 %12, i32* %29, align 4
  store i32 %13, i32* %30, align 4
  store i32 %14, i32* %31, align 4
  store i32 %15, i32* %32, align 4
  %33 = load i32, i32* %17, align 4
  %34 = load i32, i32* %18, align 4
  %35 = add nsw i32 %33, %34
  %36 = load i32, i32* %19, align 4
  %37 = add nsw i32 %35, %36
  %38 = load i32, i32* %20, align 4
  %39 = sub nsw i32 %37, %38
  %40 = load i32, i32* %21, align 4
  %41 = sub nsw i32 %39, %40
  %42 = load i32, i32* %22, align 4
  %43 = sub nsw i32 %41, %42
  %44 = load i32, i32* %23, align 4
  %45 = sub nsw i32 %43, %44
  %46 = load i32, i32* %24, align 4
  %47 = sub nsw i32 %45, %46
  %48 = load i32, i32* %25, align 4
  %49 = add nsw i32 %47, %48
  %50 = load i32, i32* %26, align 4
  %51 = add nsw i32 %49, %50
  %52 = load i32, i32* %27, align 4
  %53 = add nsw i32 %51, %52
  %54 = load i32, i32* %28, align 4
  %55 = add nsw i32 %53, %54
  %56 = load i32, i32* %29, align 4
  %57 = add nsw i32 %55, %56
  %58 = load i32, i32* %30, align 4
  %59 = add nsw i32 %57, %58
  %60 = load i32, i32* %31, align 4
  %61 = add nsw i32 %59, %60
  %62 = load i32, i32* %32, align 4
  %63 = add nsw i32 %61, %62
  ret i32 %63
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @testParam32(i32 %0, i32 %1, i32 %2, i32 %3, i32 %4, i32 %5, i32 %6, i32 %7, i32 %8, i32 %9, i32 %10, i32 %11, i32 %12, i32 %13, i32 %14, i32 %15, i32 %16, i32 %17, i32 %18, i32 %19, i32 %20, i32 %21, i32 %22, i32 %23, i32 %24, i32 %25, i32 %26, i32 %27, i32 %28, i32 %29, i32 %30, i32 %31) #0 {
  %33 = alloca i32, align 4
  %34 = alloca i32, align 4
  %35 = alloca i32, align 4
  %36 = alloca i32, align 4
  %37 = alloca i32, align 4
  %38 = alloca i32, align 4
  %39 = alloca i32, align 4
  %40 = alloca i32, align 4
  %41 = alloca i32, align 4
  %42 = alloca i32, align 4
  %43 = alloca i32, align 4
  %44 = alloca i32, align 4
  %45 = alloca i32, align 4
  %46 = alloca i32, align 4
  %47 = alloca i32, align 4
  %48 = alloca i32, align 4
  %49 = alloca i32, align 4
  %50 = alloca i32, align 4
  %51 = alloca i32, align 4
  %52 = alloca i32, align 4
  %53 = alloca i32, align 4
  %54 = alloca i32, align 4
  %55 = alloca i32, align 4
  %56 = alloca i32, align 4
  %57 = alloca i32, align 4
  %58 = alloca i32, align 4
  %59 = alloca i32, align 4
  %60 = alloca i32, align 4
  %61 = alloca i32, align 4
  %62 = alloca i32, align 4
  %63 = alloca i32, align 4
  %64 = alloca i32, align 4
  store i32 %0, i32* %33, align 4
  store i32 %1, i32* %34, align 4
  store i32 %2, i32* %35, align 4
  store i32 %3, i32* %36, align 4
  store i32 %4, i32* %37, align 4
  store i32 %5, i32* %38, align 4
  store i32 %6, i32* %39, align 4
  store i32 %7, i32* %40, align 4
  store i32 %8, i32* %41, align 4
  store i32 %9, i32* %42, align 4
  store i32 %10, i32* %43, align 4
  store i32 %11, i32* %44, align 4
  store i32 %12, i32* %45, align 4
  store i32 %13, i32* %46, align 4
  store i32 %14, i32* %47, align 4
  store i32 %15, i32* %48, align 4
  store i32 %16, i32* %49, align 4
  store i32 %17, i32* %50, align 4
  store i32 %18, i32* %51, align 4
  store i32 %19, i32* %52, align 4
  store i32 %20, i32* %53, align 4
  store i32 %21, i32* %54, align 4
  store i32 %22, i32* %55, align 4
  store i32 %23, i32* %56, align 4
  store i32 %24, i32* %57, align 4
  store i32 %25, i32* %58, align 4
  store i32 %26, i32* %59, align 4
  store i32 %27, i32* %60, align 4
  store i32 %28, i32* %61, align 4
  store i32 %29, i32* %62, align 4
  store i32 %30, i32* %63, align 4
  store i32 %31, i32* %64, align 4
  %65 = load i32, i32* %33, align 4
  %66 = load i32, i32* %34, align 4
  %67 = add nsw i32 %65, %66
  %68 = load i32, i32* %35, align 4
  %69 = add nsw i32 %67, %68
  %70 = load i32, i32* %36, align 4
  %71 = add nsw i32 %69, %70
  %72 = load i32, i32* %37, align 4
  %73 = add nsw i32 %71, %72
  %74 = load i32, i32* %38, align 4
  %75 = add nsw i32 %73, %74
  %76 = load i32, i32* %39, align 4
  %77 = add nsw i32 %75, %76
  %78 = load i32, i32* %40, align 4
  %79 = add nsw i32 %77, %78
  %80 = load i32, i32* %41, align 4
  %81 = add nsw i32 %79, %80
  %82 = load i32, i32* %42, align 4
  %83 = add nsw i32 %81, %82
  %84 = load i32, i32* %43, align 4
  %85 = add nsw i32 %83, %84
  %86 = load i32, i32* %44, align 4
  %87 = add nsw i32 %85, %86
  %88 = load i32, i32* %45, align 4
  %89 = add nsw i32 %87, %88
  %90 = load i32, i32* %46, align 4
  %91 = add nsw i32 %89, %90
  %92 = load i32, i32* %47, align 4
  %93 = add nsw i32 %91, %92
  %94 = load i32, i32* %48, align 4
  %95 = add nsw i32 %93, %94
  %96 = load i32, i32* %49, align 4
  %97 = add nsw i32 %95, %96
  %98 = load i32, i32* %50, align 4
  %99 = add nsw i32 %97, %98
  %100 = load i32, i32* %51, align 4
  %101 = sub nsw i32 %99, %100
  %102 = load i32, i32* %52, align 4
  %103 = sub nsw i32 %101, %102
  %104 = load i32, i32* %53, align 4
  %105 = sub nsw i32 %103, %104
  %106 = load i32, i32* %54, align 4
  %107 = sub nsw i32 %105, %106
  %108 = load i32, i32* %55, align 4
  %109 = sub nsw i32 %107, %108
  %110 = load i32, i32* %56, align 4
  %111 = add nsw i32 %109, %110
  %112 = load i32, i32* %57, align 4
  %113 = add nsw i32 %111, %112
  %114 = load i32, i32* %58, align 4
  %115 = add nsw i32 %113, %114
  %116 = load i32, i32* %59, align 4
  %117 = add nsw i32 %115, %116
  %118 = load i32, i32* %60, align 4
  %119 = add nsw i32 %117, %118
  %120 = load i32, i32* %61, align 4
  %121 = add nsw i32 %119, %120
  %122 = load i32, i32* %62, align 4
  %123 = add nsw i32 %121, %122
  %124 = load i32, i32* %63, align 4
  %125 = add nsw i32 %123, %124
  %126 = load i32, i32* %64, align 4
  %127 = add nsw i32 %125, %126
  ret i32 %127
}

; Function Attrs: noinline nounwind optnone uwtable
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
  %4 = load i32, i32* @a2, align 4
  %5 = load i32, i32* @a3, align 4
  %6 = load i32, i32* @a4, align 4
  %7 = load i32, i32* @a5, align 4
  %8 = load i32, i32* @a6, align 4
  %9 = load i32, i32* @a7, align 4
  %10 = call i32 @testParam8(i32 %2, i32 %3, i32 %4, i32 %5, i32 %6, i32 %7, i32 %8, i32 %9)
  store i32 %10, i32* @a0, align 4
  %11 = load i32, i32* @a0, align 4
  %12 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %11)
  %13 = load i32, i32* @a32, align 4
  %14 = load i32, i32* @a33, align 4
  %15 = load i32, i32* @a34, align 4
  %16 = load i32, i32* @a35, align 4
  %17 = load i32, i32* @a36, align 4
  %18 = load i32, i32* @a37, align 4
  %19 = load i32, i32* @a38, align 4
  %20 = load i32, i32* @a39, align 4
  %21 = load i32, i32* @a8, align 4
  %22 = load i32, i32* @a9, align 4
  %23 = load i32, i32* @a10, align 4
  %24 = load i32, i32* @a11, align 4
  %25 = load i32, i32* @a12, align 4
  %26 = load i32, i32* @a13, align 4
  %27 = load i32, i32* @a14, align 4
  %28 = load i32, i32* @a15, align 4
  %29 = call i32 @testParam16(i32 %13, i32 %14, i32 %15, i32 %16, i32 %17, i32 %18, i32 %19, i32 %20, i32 %21, i32 %22, i32 %23, i32 %24, i32 %25, i32 %26, i32 %27, i32 %28)
  store i32 %29, i32* @a0, align 4
  %30 = load i32, i32* @a0, align 4
  %31 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %30)
  %32 = load i32, i32* @a0, align 4
  %33 = load i32, i32* @a1, align 4
  %34 = load i32, i32* @a2, align 4
  %35 = load i32, i32* @a3, align 4
  %36 = load i32, i32* @a4, align 4
  %37 = load i32, i32* @a5, align 4
  %38 = load i32, i32* @a6, align 4
  %39 = load i32, i32* @a7, align 4
  %40 = load i32, i32* @a8, align 4
  %41 = load i32, i32* @a9, align 4
  %42 = load i32, i32* @a10, align 4
  %43 = load i32, i32* @a11, align 4
  %44 = load i32, i32* @a12, align 4
  %45 = load i32, i32* @a13, align 4
  %46 = load i32, i32* @a14, align 4
  %47 = load i32, i32* @a15, align 4
  %48 = load i32, i32* @a16, align 4
  %49 = load i32, i32* @a17, align 4
  %50 = load i32, i32* @a18, align 4
  %51 = load i32, i32* @a19, align 4
  %52 = load i32, i32* @a20, align 4
  %53 = load i32, i32* @a21, align 4
  %54 = load i32, i32* @a22, align 4
  %55 = load i32, i32* @a23, align 4
  %56 = load i32, i32* @a24, align 4
  %57 = load i32, i32* @a25, align 4
  %58 = load i32, i32* @a26, align 4
  %59 = load i32, i32* @a27, align 4
  %60 = load i32, i32* @a28, align 4
  %61 = load i32, i32* @a29, align 4
  %62 = load i32, i32* @a30, align 4
  %63 = load i32, i32* @a31, align 4
  %64 = call i32 @testParam32(i32 %32, i32 %33, i32 %34, i32 %35, i32 %36, i32 %37, i32 %38, i32 %39, i32 %40, i32 %41, i32 %42, i32 %43, i32 %44, i32 %45, i32 %46, i32 %47, i32 %48, i32 %49, i32 %50, i32 %51, i32 %52, i32 %53, i32 %54, i32 %55, i32 %56, i32 %57, i32 %58, i32 %59, i32 %60, i32 %61, i32 %62, i32 %63)
  store i32 %64, i32* @a0, align 4
  %65 = load i32, i32* @a0, align 4
  %66 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %65)
  ret i32 0
}
'''
s9='''
@i = dso_local global i32 0, align 4
@ii = dso_local global i32 1, align 4
@intt = common dso_local global i32 0, align 4
@ints = common dso_local global [10000 x i32] zeroinitializer, align 16
@chat = common dso_local global i32 0, align 4
@chas = common dso_local global [10000 x i32] zeroinitializer, align 16
@c = common dso_local global i32 0, align 4
@get2 = common dso_local global [10000 x i32] zeroinitializer, align 16
@get = common dso_local global [10000 x i32] zeroinitializer, align 16

; Function Attrs: noinline nounwind optnone readonly uwtable
define dso_local i32 @isdigit(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp sge i32 %4, 48
  br i1 %5, label %6, label %10

6:                                                ; preds = %1
  %7 = load i32, i32* %3, align 4
  %8 = icmp sle i32 %7, 57
  br i1 %8, label %9, label %10

9:                                                ; preds = %6
  store i32 1, i32* %2, align 4
  br label %11

10:                                               ; preds = %6, %1
  store i32 0, i32* %2, align 4
  br label %11

11:                                               ; preds = %10, %9
  %12 = load i32, i32* %2, align 4
  ret i32 %12
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @power(i32 %0, i32 %1) #1 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  store i32 1, i32* %5, align 4
  br label %6

6:                                                ; preds = %9, %2
  %7 = load i32, i32* %4, align 4
  %8 = icmp ne i32 %7, 0
  br i1 %8, label %9, label %15

9:                                                ; preds = %6
  %10 = load i32, i32* %5, align 4
  %11 = load i32, i32* %3, align 4
  %12 = mul nsw i32 %10, %11
  store i32 %12, i32* %5, align 4
  %13 = load i32, i32* %4, align 4
  %14 = sub nsw i32 %13, 1
  store i32 %14, i32* %4, align 4
  br label %6

15:                                               ; preds = %6
  %16 = load i32, i32* %5, align 4
  ret i32 %16
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @getstr(i32* %0) #1 {
  %2 = alloca i32*, align 8
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32* %0, i32** %2, align 8
  %5 = call i32 (...) @getch()
  store i32 %5, i32* %3, align 4
  store i32 0, i32* %4, align 4
  br label %6

6:                                                ; preds = %14, %1
  %7 = load i32, i32* %3, align 4
  %8 = icmp ne i32 %7, 13
  br i1 %8, label %9, label %12

9:                                                ; preds = %6
  %10 = load i32, i32* %3, align 4
  %11 = icmp ne i32 %10, 10
  br label %12

12:                                               ; preds = %9, %6
  %13 = phi i1 [ false, %6 ], [ %11, %9 ]
  br i1 %13, label %14, label %23

14:                                               ; preds = %12
  %15 = load i32, i32* %3, align 4
  %16 = load i32*, i32** %2, align 8
  %17 = load i32, i32* %4, align 4
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds i32, i32* %16, i64 %18
  store i32 %15, i32* %19, align 4
  %20 = load i32, i32* %4, align 4
  %21 = add nsw i32 %20, 1
  store i32 %21, i32* %4, align 4
  %22 = call i32 (...) @getch()
  store i32 %22, i32* %3, align 4
  br label %6

23:                                               ; preds = %12
  %24 = load i32, i32* %4, align 4
  ret i32 %24
}

declare dso_local i32 @getch(...) #2

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @intpush(i32 %0) #1 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* @intt, align 4
  %4 = add nsw i32 %3, 1
  store i32 %4, i32* @intt, align 4
  %5 = load i32, i32* %2, align 4
  %6 = load i32, i32* @intt, align 4
  %7 = sext i32 %6 to i64
  %8 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %7
  store i32 %5, i32* %8, align 4
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @chapush(i32 %0) #1 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* @chat, align 4
  %4 = add nsw i32 %3, 1
  store i32 %4, i32* @chat, align 4
  %5 = load i32, i32* %2, align 4
  %6 = load i32, i32* @chat, align 4
  %7 = sext i32 %6 to i64
  %8 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %7
  store i32 %5, i32* %8, align 4
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @intpop() #1 {
  %1 = load i32, i32* @intt, align 4
  %2 = sub nsw i32 %1, 1
  store i32 %2, i32* @intt, align 4
  %3 = load i32, i32* @intt, align 4
  %4 = add nsw i32 %3, 1
  %5 = sext i32 %4 to i64
  %6 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %5
  %7 = load i32, i32* %6, align 4
  ret i32 %7
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @chapop() #1 {
  %1 = load i32, i32* @chat, align 4
  %2 = sub nsw i32 %1, 1
  store i32 %2, i32* @chat, align 4
  %3 = load i32, i32* @chat, align 4
  %4 = add nsw i32 %3, 1
  %5 = sext i32 %4 to i64
  %6 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %5
  %7 = load i32, i32* %6, align 4
  ret i32 %7
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @intadd(i32 %0) #1 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  %3 = load i32, i32* @intt, align 4
  %4 = sext i32 %3 to i64
  %5 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %4
  %6 = load i32, i32* %5, align 4
  %7 = mul nsw i32 %6, 10
  %8 = load i32, i32* @intt, align 4
  %9 = sext i32 %8 to i64
  %10 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %9
  store i32 %7, i32* %10, align 4
  %11 = load i32, i32* @intt, align 4
  %12 = sext i32 %11 to i64
  %13 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %12
  %14 = load i32, i32* %13, align 4
  %15 = load i32, i32* %2, align 4
  %16 = add nsw i32 %14, %15
  %17 = load i32, i32* @intt, align 4
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds [10000 x i32], [10000 x i32]* @ints, i64 0, i64 %18
  store i32 %16, i32* %19, align 4
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @find() #1 {
  %1 = alloca i32, align 4
  %2 = call i32 @chapop()
  store i32 %2, i32* @c, align 4
  %3 = load i32, i32* @ii, align 4
  %4 = sext i32 %3 to i64
  %5 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %4
  store i32 32, i32* %5, align 4
  %6 = load i32, i32* @c, align 4
  %7 = load i32, i32* @ii, align 4
  %8 = add nsw i32 %7, 1
  %9 = sext i32 %8 to i64
  %10 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %9
  store i32 %6, i32* %10, align 4
  %11 = load i32, i32* @ii, align 4
  %12 = add nsw i32 %11, 2
  store i32 %12, i32* @ii, align 4
  %13 = load i32, i32* @chat, align 4
  %14 = icmp eq i32 %13, 0
  br i1 %14, label %15, label %16

15:                                               ; preds = %0
  store i32 0, i32* %1, align 4
  br label %17

16:                                               ; preds = %0
  store i32 1, i32* %1, align 4
  br label %17

17:                                               ; preds = %16, %15
  %18 = load i32, i32* %1, align 4
  ret i32 %18
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #1 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* @intt, align 4
  store i32 0, i32* @chat, align 4
  %7 = call i32 @getstr(i32* getelementptr inbounds ([10000 x i32], [10000 x i32]* @get, i64 0, i64 0))
  store i32 %7, i32* %2, align 4
  br label %8

8:                                                ; preds = %292, %0
  %9 = load i32, i32* @i, align 4
  %10 = load i32, i32* %2, align 4
  %11 = icmp slt i32 %9, %10
  br i1 %11, label %12, label %295

12:                                               ; preds = %8
  %13 = load i32, i32* @i, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %14
  %16 = load i32, i32* %15, align 4
  %17 = call i32 @isdigit(i32 %16) #3
  %18 = icmp eq i32 %17, 1
  br i1 %18, label %19, label %29

19:                                               ; preds = %12
  %20 = load i32, i32* @i, align 4
  %21 = sext i32 %20 to i64
  %22 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %21
  %23 = load i32, i32* %22, align 4
  %24 = load i32, i32* @ii, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %25
  store i32 %23, i32* %26, align 4
  %27 = load i32, i32* @ii, align 4
  %28 = add nsw i32 %27, 1
  store i32 %28, i32* @ii, align 4
  br label %292

29:                                               ; preds = %12
  %30 = load i32, i32* @i, align 4
  %31 = sext i32 %30 to i64
  %32 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %31
  %33 = load i32, i32* %32, align 4
  %34 = icmp eq i32 %33, 40
  br i1 %34, label %35, label %36

35:                                               ; preds = %29
  call void @chapush(i32 40)
  br label %36

36:                                               ; preds = %35, %29
  %37 = load i32, i32* @i, align 4
  %38 = sext i32 %37 to i64
  %39 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %38
  %40 = load i32, i32* %39, align 4
  %41 = icmp eq i32 %40, 94
  br i1 %41, label %42, label %43

42:                                               ; preds = %36
  call void @chapush(i32 94)
  br label %43

43:                                               ; preds = %42, %36
  %44 = load i32, i32* @i, align 4
  %45 = sext i32 %44 to i64
  %46 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %45
  %47 = load i32, i32* %46, align 4
  %48 = icmp eq i32 %47, 41
  br i1 %48, label %49, label %67

49:                                               ; preds = %43
  %50 = call i32 @chapop()
  store i32 %50, i32* @c, align 4
  br label %51

51:                                               ; preds = %54, %49
  %52 = load i32, i32* @c, align 4
  %53 = icmp ne i32 %52, 40
  br i1 %53, label %54, label %66

54:                                               ; preds = %51
  %55 = load i32, i32* @ii, align 4
  %56 = sext i32 %55 to i64
  %57 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %56
  store i32 32, i32* %57, align 4
  %58 = load i32, i32* @c, align 4
  %59 = load i32, i32* @ii, align 4
  %60 = add nsw i32 %59, 1
  %61 = sext i32 %60 to i64
  %62 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %61
  store i32 %58, i32* %62, align 4
  %63 = load i32, i32* @ii, align 4
  %64 = add nsw i32 %63, 2
  store i32 %64, i32* @ii, align 4
  %65 = call i32 @chapop()
  store i32 %65, i32* @c, align 4
  br label %51

66:                                               ; preds = %51
  br label %67

67:                                               ; preds = %66, %43
  %68 = load i32, i32* @i, align 4
  %69 = sext i32 %68 to i64
  %70 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %69
  %71 = load i32, i32* %70, align 4
  %72 = icmp eq i32 %71, 43
  br i1 %72, label %73, label %118

73:                                               ; preds = %67
  br label %74

74:                                               ; preds = %116, %73
  %75 = load i32, i32* @chat, align 4
  %76 = sext i32 %75 to i64
  %77 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %76
  %78 = load i32, i32* %77, align 4
  %79 = icmp eq i32 %78, 43
  br i1 %79, label %110, label %80

80:                                               ; preds = %74
  %81 = load i32, i32* @chat, align 4
  %82 = sext i32 %81 to i64
  %83 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %82
  %84 = load i32, i32* %83, align 4
  %85 = icmp eq i32 %84, 45
  br i1 %85, label %110, label %86

86:                                               ; preds = %80
  %87 = load i32, i32* @chat, align 4
  %88 = sext i32 %87 to i64
  %89 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %88
  %90 = load i32, i32* %89, align 4
  %91 = icmp eq i32 %90, 42
  br i1 %91, label %110, label %92

92:                                               ; preds = %86
  %93 = load i32, i32* @chat, align 4
  %94 = sext i32 %93 to i64
  %95 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %94
  %96 = load i32, i32* %95, align 4
  %97 = icmp eq i32 %96, 47
  br i1 %97, label %110, label %98

98:                                               ; preds = %92
  %99 = load i32, i32* @chat, align 4
  %100 = sext i32 %99 to i64
  %101 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %100
  %102 = load i32, i32* %101, align 4
  %103 = icmp eq i32 %102, 37
  br i1 %103, label %110, label %104

104:                                              ; preds = %98
  %105 = load i32, i32* @chat, align 4
  %106 = sext i32 %105 to i64
  %107 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %106
  %108 = load i32, i32* %107, align 4
  %109 = icmp eq i32 %108, 94
  br label %110

110:                                              ; preds = %104, %98, %92, %86, %80, %74
  %111 = phi i1 [ true, %98 ], [ true, %92 ], [ true, %86 ], [ true, %80 ], [ true, %74 ], [ %109, %104 ]
  br i1 %111, label %112, label %117

112:                                              ; preds = %110
  %113 = call i32 @find()
  %114 = icmp eq i32 %113, 0
  br i1 %114, label %115, label %116

115:                                              ; preds = %112
  br label %117

116:                                              ; preds = %112
  br label %74

117:                                              ; preds = %115, %110
  call void @chapush(i32 43)
  br label %118

118:                                              ; preds = %117, %67
  %119 = load i32, i32* @i, align 4
  %120 = sext i32 %119 to i64
  %121 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %120
  %122 = load i32, i32* %121, align 4
  %123 = icmp eq i32 %122, 45
  br i1 %123, label %124, label %169

124:                                              ; preds = %118
  br label %125

125:                                              ; preds = %167, %124
  %126 = load i32, i32* @chat, align 4
  %127 = sext i32 %126 to i64
  %128 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %127
  %129 = load i32, i32* %128, align 4
  %130 = icmp eq i32 %129, 43
  br i1 %130, label %161, label %131

131:                                              ; preds = %125
  %132 = load i32, i32* @chat, align 4
  %133 = sext i32 %132 to i64
  %134 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %133
  %135 = load i32, i32* %134, align 4
  %136 = icmp eq i32 %135, 45
  br i1 %136, label %161, label %137

137:                                              ; preds = %131
  %138 = load i32, i32* @chat, align 4
  %139 = sext i32 %138 to i64
  %140 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %139
  %141 = load i32, i32* %140, align 4
  %142 = icmp eq i32 %141, 42
  br i1 %142, label %161, label %143

143:                                              ; preds = %137
  %144 = load i32, i32* @chat, align 4
  %145 = sext i32 %144 to i64
  %146 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %145
  %147 = load i32, i32* %146, align 4
  %148 = icmp eq i32 %147, 47
  br i1 %148, label %161, label %149

149:                                              ; preds = %143
  %150 = load i32, i32* @chat, align 4
  %151 = sext i32 %150 to i64
  %152 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %151
  %153 = load i32, i32* %152, align 4
  %154 = icmp eq i32 %153, 37
  br i1 %154, label %161, label %155

155:                                              ; preds = %149
  %156 = load i32, i32* @chat, align 4
  %157 = sext i32 %156 to i64
  %158 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %157
  %159 = load i32, i32* %158, align 4
  %160 = icmp eq i32 %159, 94
  br label %161

161:                                              ; preds = %155, %149, %143, %137, %131, %125
  %162 = phi i1 [ true, %149 ], [ true, %143 ], [ true, %137 ], [ true, %131 ], [ true, %125 ], [ %160, %155 ]
  br i1 %162, label %163, label %168

163:                                              ; preds = %161
  %164 = call i32 @find()
  %165 = icmp eq i32 %164, 0
  br i1 %165, label %166, label %167

166:                                              ; preds = %163
  br label %168

167:                                              ; preds = %163
  br label %125

168:                                              ; preds = %166, %161
  call void @chapush(i32 45)
  br label %169

169:                                              ; preds = %168, %118
  %170 = load i32, i32* @i, align 4
  %171 = sext i32 %170 to i64
  %172 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %171
  %173 = load i32, i32* %172, align 4
  %174 = icmp eq i32 %173, 42
  br i1 %174, label %175, label %208

175:                                              ; preds = %169
  br label %176

176:                                              ; preds = %206, %175
  %177 = load i32, i32* @chat, align 4
  %178 = sext i32 %177 to i64
  %179 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %178
  %180 = load i32, i32* %179, align 4
  %181 = icmp eq i32 %180, 42
  br i1 %181, label %200, label %182

182:                                              ; preds = %176
  %183 = load i32, i32* @chat, align 4
  %184 = sext i32 %183 to i64
  %185 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %184
  %186 = load i32, i32* %185, align 4
  %187 = icmp eq i32 %186, 47
  br i1 %187, label %200, label %188

188:                                              ; preds = %182
  %189 = load i32, i32* @chat, align 4
  %190 = sext i32 %189 to i64
  %191 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %190
  %192 = load i32, i32* %191, align 4
  %193 = icmp eq i32 %192, 37
  br i1 %193, label %200, label %194

194:                                              ; preds = %188
  %195 = load i32, i32* @chat, align 4
  %196 = sext i32 %195 to i64
  %197 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %196
  %198 = load i32, i32* %197, align 4
  %199 = icmp eq i32 %198, 94
  br label %200

200:                                              ; preds = %194, %188, %182, %176
  %201 = phi i1 [ true, %188 ], [ true, %182 ], [ true, %176 ], [ %199, %194 ]
  br i1 %201, label %202, label %207

202:                                              ; preds = %200
  %203 = call i32 @find()
  %204 = icmp eq i32 %203, 0
  br i1 %204, label %205, label %206

205:                                              ; preds = %202
  br label %207

206:                                              ; preds = %202
  br label %176

207:                                              ; preds = %205, %200
  call void @chapush(i32 42)
  br label %208

208:                                              ; preds = %207, %169
  %209 = load i32, i32* @i, align 4
  %210 = sext i32 %209 to i64
  %211 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %210
  %212 = load i32, i32* %211, align 4
  %213 = icmp eq i32 %212, 47
  br i1 %213, label %214, label %247

214:                                              ; preds = %208
  br label %215

215:                                              ; preds = %245, %214
  %216 = load i32, i32* @chat, align 4
  %217 = sext i32 %216 to i64
  %218 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %217
  %219 = load i32, i32* %218, align 4
  %220 = icmp eq i32 %219, 42
  br i1 %220, label %239, label %221

221:                                              ; preds = %215
  %222 = load i32, i32* @chat, align 4
  %223 = sext i32 %222 to i64
  %224 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %223
  %225 = load i32, i32* %224, align 4
  %226 = icmp eq i32 %225, 47
  br i1 %226, label %239, label %227

227:                                              ; preds = %221
  %228 = load i32, i32* @chat, align 4
  %229 = sext i32 %228 to i64
  %230 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %229
  %231 = load i32, i32* %230, align 4
  %232 = icmp eq i32 %231, 37
  br i1 %232, label %239, label %233

233:                                              ; preds = %227
  %234 = load i32, i32* @chat, align 4
  %235 = sext i32 %234 to i64
  %236 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %235
  %237 = load i32, i32* %236, align 4
  %238 = icmp eq i32 %237, 94
  br label %239

239:                                              ; preds = %233, %227, %221, %215
  %240 = phi i1 [ true, %227 ], [ true, %221 ], [ true, %215 ], [ %238, %233 ]
  br i1 %240, label %241, label %246

241:                                              ; preds = %239
  %242 = call i32 @find()
  %243 = icmp eq i32 %242, 0
  br i1 %243, label %244, label %245

244:                                              ; preds = %241
  br label %246

245:                                              ; preds = %241
  br label %215

246:                                              ; preds = %244, %239
  call void @chapush(i32 47)
  br label %247

247:                                              ; preds = %246, %208
  %248 = load i32, i32* @i, align 4
  %249 = sext i32 %248 to i64
  %250 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get, i64 0, i64 %249
  %251 = load i32, i32* %250, align 4
  %252 = icmp eq i32 %251, 37
  br i1 %252, label %253, label %286

253:                                              ; preds = %247
  br label %254

254:                                              ; preds = %284, %253
  %255 = load i32, i32* @chat, align 4
  %256 = sext i32 %255 to i64
  %257 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %256
  %258 = load i32, i32* %257, align 4
  %259 = icmp eq i32 %258, 42
  br i1 %259, label %278, label %260

260:                                              ; preds = %254
  %261 = load i32, i32* @chat, align 4
  %262 = sext i32 %261 to i64
  %263 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %262
  %264 = load i32, i32* %263, align 4
  %265 = icmp eq i32 %264, 47
  br i1 %265, label %278, label %266

266:                                              ; preds = %260
  %267 = load i32, i32* @chat, align 4
  %268 = sext i32 %267 to i64
  %269 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %268
  %270 = load i32, i32* %269, align 4
  %271 = icmp eq i32 %270, 37
  br i1 %271, label %278, label %272

272:                                              ; preds = %266
  %273 = load i32, i32* @chat, align 4
  %274 = sext i32 %273 to i64
  %275 = getelementptr inbounds [10000 x i32], [10000 x i32]* @chas, i64 0, i64 %274
  %276 = load i32, i32* %275, align 4
  %277 = icmp eq i32 %276, 94
  br label %278

278:                                              ; preds = %272, %266, %260, %254
  %279 = phi i1 [ true, %266 ], [ true, %260 ], [ true, %254 ], [ %277, %272 ]
  br i1 %279, label %280, label %285

280:                                              ; preds = %278
  %281 = call i32 @find()
  %282 = icmp eq i32 %281, 0
  br i1 %282, label %283, label %284

283:                                              ; preds = %280
  br label %285

284:                                              ; preds = %280
  br label %254

285:                                              ; preds = %283, %278
  call void @chapush(i32 37)
  br label %286

286:                                              ; preds = %285, %247
  %287 = load i32, i32* @ii, align 4
  %288 = sext i32 %287 to i64
  %289 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %288
  store i32 32, i32* %289, align 4
  %290 = load i32, i32* @ii, align 4
  %291 = add nsw i32 %290, 1
  store i32 %291, i32* @ii, align 4
  br label %292

292:                                              ; preds = %286, %19
  %293 = load i32, i32* @i, align 4
  %294 = add nsw i32 %293, 1
  store i32 %294, i32* @i, align 4
  br label %8

295:                                              ; preds = %8
  br label %296

296:                                              ; preds = %299, %295
  %297 = load i32, i32* @chat, align 4
  %298 = icmp sgt i32 %297, 0
  br i1 %298, label %299, label %311

299:                                              ; preds = %296
  %300 = call i32 @chapop()
  store i32 %300, i32* %3, align 4
  %301 = load i32, i32* @ii, align 4
  %302 = sext i32 %301 to i64
  %303 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %302
  store i32 32, i32* %303, align 4
  %304 = load i32, i32* %3, align 4
  %305 = load i32, i32* @ii, align 4
  %306 = add nsw i32 %305, 1
  %307 = sext i32 %306 to i64
  %308 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %307
  store i32 %304, i32* %308, align 4
  %309 = load i32, i32* @ii, align 4
  %310 = add nsw i32 %309, 2
  store i32 %310, i32* @ii, align 4
  br label %296

311:                                              ; preds = %296
  %312 = load i32, i32* @ii, align 4
  %313 = sext i32 %312 to i64
  %314 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %313
  store i32 64, i32* %314, align 4
  store i32 1, i32* @i, align 4
  br label %315

315:                                              ; preds = %457, %311
  %316 = load i32, i32* @i, align 4
  %317 = sext i32 %316 to i64
  %318 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %317
  %319 = load i32, i32* %318, align 4
  %320 = icmp ne i32 %319, 64
  br i1 %320, label %321, label %460

321:                                              ; preds = %315
  %322 = load i32, i32* @i, align 4
  %323 = sext i32 %322 to i64
  %324 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %323
  %325 = load i32, i32* %324, align 4
  %326 = icmp eq i32 %325, 43
  br i1 %326, label %357, label %327

327:                                              ; preds = %321
  %328 = load i32, i32* @i, align 4
  %329 = sext i32 %328 to i64
  %330 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %329
  %331 = load i32, i32* %330, align 4
  %332 = icmp eq i32 %331, 45
  br i1 %332, label %357, label %333

333:                                              ; preds = %327
  %334 = load i32, i32* @i, align 4
  %335 = sext i32 %334 to i64
  %336 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %335
  %337 = load i32, i32* %336, align 4
  %338 = icmp eq i32 %337, 42
  br i1 %338, label %357, label %339

339:                                              ; preds = %333
  %340 = load i32, i32* @i, align 4
  %341 = sext i32 %340 to i64
  %342 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %341
  %343 = load i32, i32* %342, align 4
  %344 = icmp eq i32 %343, 47
  br i1 %344, label %357, label %345

345:                                              ; preds = %339
  %346 = load i32, i32* @i, align 4
  %347 = sext i32 %346 to i64
  %348 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %347
  %349 = load i32, i32* %348, align 4
  %350 = icmp eq i32 %349, 37
  br i1 %350, label %357, label %351

351:                                              ; preds = %345
  %352 = load i32, i32* @i, align 4
  %353 = sext i32 %352 to i64
  %354 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %353
  %355 = load i32, i32* %354, align 4
  %356 = icmp eq i32 %355, 94
  br i1 %356, label %357, label %421

357:                                              ; preds = %351, %345, %339, %333, %327, %321
  %358 = call i32 @intpop()
  store i32 %358, i32* %4, align 4
  %359 = call i32 @intpop()
  store i32 %359, i32* %5, align 4
  %360 = load i32, i32* @i, align 4
  %361 = sext i32 %360 to i64
  %362 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %361
  %363 = load i32, i32* %362, align 4
  %364 = icmp eq i32 %363, 43
  br i1 %364, label %365, label %369

365:                                              ; preds = %357
  %366 = load i32, i32* %4, align 4
  %367 = load i32, i32* %5, align 4
  %368 = add nsw i32 %366, %367
  store i32 %368, i32* %6, align 4
  br label %369

369:                                              ; preds = %365, %357
  %370 = load i32, i32* @i, align 4
  %371 = sext i32 %370 to i64
  %372 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %371
  %373 = load i32, i32* %372, align 4
  %374 = icmp eq i32 %373, 45
  br i1 %374, label %375, label %379

375:                                              ; preds = %369
  %376 = load i32, i32* %5, align 4
  %377 = load i32, i32* %4, align 4
  %378 = sub nsw i32 %376, %377
  store i32 %378, i32* %6, align 4
  br label %379

379:                                              ; preds = %375, %369
  %380 = load i32, i32* @i, align 4
  %381 = sext i32 %380 to i64
  %382 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %381
  %383 = load i32, i32* %382, align 4
  %384 = icmp eq i32 %383, 42
  br i1 %384, label %385, label %389

385:                                              ; preds = %379
  %386 = load i32, i32* %4, align 4
  %387 = load i32, i32* %5, align 4
  %388 = mul nsw i32 %386, %387
  store i32 %388, i32* %6, align 4
  br label %389

389:                                              ; preds = %385, %379
  %390 = load i32, i32* @i, align 4
  %391 = sext i32 %390 to i64
  %392 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %391
  %393 = load i32, i32* %392, align 4
  %394 = icmp eq i32 %393, 47
  br i1 %394, label %395, label %399

395:                                              ; preds = %389
  %396 = load i32, i32* %5, align 4
  %397 = load i32, i32* %4, align 4
  %398 = sdiv i32 %396, %397
  store i32 %398, i32* %6, align 4
  br label %399

399:                                              ; preds = %395, %389
  %400 = load i32, i32* @i, align 4
  %401 = sext i32 %400 to i64
  %402 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %401
  %403 = load i32, i32* %402, align 4
  %404 = icmp eq i32 %403, 37
  br i1 %404, label %405, label %409

405:                                              ; preds = %399
  %406 = load i32, i32* %5, align 4
  %407 = load i32, i32* %4, align 4
  %408 = srem i32 %406, %407
  store i32 %408, i32* %6, align 4
  br label %409

409:                                              ; preds = %405, %399
  %410 = load i32, i32* @i, align 4
  %411 = sext i32 %410 to i64
  %412 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %411
  %413 = load i32, i32* %412, align 4
  %414 = icmp eq i32 %413, 94
  br i1 %414, label %415, label %419

415:                                              ; preds = %409
  %416 = load i32, i32* %5, align 4
  %417 = load i32, i32* %4, align 4
  %418 = call i32 @power(i32 %416, i32 %417)
  store i32 %418, i32* %6, align 4
  br label %419

419:                                              ; preds = %415, %409
  %420 = load i32, i32* %6, align 4
  call void @intpush(i32 %420)
  br label %457

421:                                              ; preds = %351
  %422 = load i32, i32* @i, align 4
  %423 = sext i32 %422 to i64
  %424 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %423
  %425 = load i32, i32* %424, align 4
  %426 = icmp ne i32 %425, 32
  br i1 %426, label %427, label %456

427:                                              ; preds = %421
  %428 = load i32, i32* @i, align 4
  %429 = sext i32 %428 to i64
  %430 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %429
  %431 = load i32, i32* %430, align 4
  %432 = sub nsw i32 %431, 48
  call void @intpush(i32 %432)
  store i32 1, i32* @ii, align 4
  br label %433

433:                                              ; preds = %441, %427
  %434 = load i32, i32* @i, align 4
  %435 = load i32, i32* @ii, align 4
  %436 = add nsw i32 %434, %435
  %437 = sext i32 %436 to i64
  %438 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %437
  %439 = load i32, i32* %438, align 4
  %440 = icmp ne i32 %439, 32
  br i1 %440, label %441, label %451

441:                                              ; preds = %433
  %442 = load i32, i32* @i, align 4
  %443 = load i32, i32* @ii, align 4
  %444 = add nsw i32 %442, %443
  %445 = sext i32 %444 to i64
  %446 = getelementptr inbounds [10000 x i32], [10000 x i32]* @get2, i64 0, i64 %445
  %447 = load i32, i32* %446, align 4
  %448 = sub nsw i32 %447, 48
  call void @intadd(i32 %448)
  %449 = load i32, i32* @ii, align 4
  %450 = add nsw i32 %449, 1
  store i32 %450, i32* @ii, align 4
  br label %433

451:                                              ; preds = %433
  %452 = load i32, i32* @i, align 4
  %453 = load i32, i32* @ii, align 4
  %454 = add nsw i32 %452, %453
  %455 = sub nsw i32 %454, 1
  store i32 %455, i32* @i, align 4
  br label %456

456:                                              ; preds = %451, %421
  br label %457

457:                                              ; preds = %456, %419
  %458 = load i32, i32* @i, align 4
  %459 = add nsw i32 %458, 1
  store i32 %459, i32* @i, align 4
  br label %315

460:                                              ; preds = %315
  %461 = load i32, i32* getelementptr inbounds ([10000 x i32], [10000 x i32]* @ints, i64 0, i64 1), align 4
  %462 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %461)
  ret i32 0
}
'''
s10='''
@__const.main.x = private unnamed_addr constant [1 x i32] [i32 1], align 4
@__const.main.y = private unnamed_addr constant [1 x i32] [i32 1], align 4

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @exgcd(i32 %0, i32 %1, i32* %2, i32* %3) #0 {
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32*, align 8
  %9 = alloca i32*, align 8
  %10 = alloca i32, align 4
  %11 = alloca i32, align 4
  store i32 %0, i32* %6, align 4
  store i32 %1, i32* %7, align 4
  store i32* %2, i32** %8, align 8
  store i32* %3, i32** %9, align 8
  %12 = load i32, i32* %7, align 4
  %13 = icmp eq i32 %12, 0
  br i1 %13, label %14, label %20

14:                                               ; preds = %4
  %15 = load i32*, i32** %8, align 8
  %16 = getelementptr inbounds i32, i32* %15, i64 0
  store i32 1, i32* %16, align 4
  %17 = load i32*, i32** %9, align 8
  %18 = getelementptr inbounds i32, i32* %17, i64 0
  store i32 0, i32* %18, align 4
  %19 = load i32, i32* %6, align 4
  store i32 %19, i32* %5, align 4
  br label %48

20:                                               ; preds = %4
  %21 = load i32, i32* %7, align 4
  %22 = load i32, i32* %6, align 4
  %23 = load i32, i32* %7, align 4
  %24 = srem i32 %22, %23
  %25 = load i32*, i32** %8, align 8
  %26 = load i32*, i32** %9, align 8
  %27 = call i32 @exgcd(i32 %21, i32 %24, i32* %25, i32* %26)
  store i32 %27, i32* %10, align 4
  %28 = load i32*, i32** %8, align 8
  %29 = getelementptr inbounds i32, i32* %28, i64 0
  %30 = load i32, i32* %29, align 4
  store i32 %30, i32* %11, align 4
  %31 = load i32*, i32** %9, align 8
  %32 = getelementptr inbounds i32, i32* %31, i64 0
  %33 = load i32, i32* %32, align 4
  %34 = load i32*, i32** %8, align 8
  %35 = getelementptr inbounds i32, i32* %34, i64 0
  store i32 %33, i32* %35, align 4
  %36 = load i32, i32* %11, align 4
  %37 = load i32, i32* %6, align 4
  %38 = load i32, i32* %7, align 4
  %39 = sdiv i32 %37, %38
  %40 = load i32*, i32** %9, align 8
  %41 = getelementptr inbounds i32, i32* %40, i64 0
  %42 = load i32, i32* %41, align 4
  %43 = mul nsw i32 %39, %42
  %44 = sub nsw i32 %36, %43
  %45 = load i32*, i32** %9, align 8
  %46 = getelementptr inbounds i32, i32* %45, i64 0
  store i32 %44, i32* %46, align 4
  %47 = load i32, i32* %10, align 4
  store i32 %47, i32* %5, align 4
  br label %48

48:                                               ; preds = %20, %14
  %49 = load i32, i32* %5, align 4
  ret i32 %49
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca [1 x i32], align 4
  %5 = alloca [1 x i32], align 4
  store i32 0, i32* %1, align 4
  store i32 7, i32* %2, align 4
  store i32 15, i32* %3, align 4
  %6 = bitcast [1 x i32]* %4 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 4 %6, i8* align 4 bitcast ([1 x i32]* @__const.main.x to i8*), i64 4, i1 false)
  %7 = bitcast [1 x i32]* %5 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 4 %7, i8* align 4 bitcast ([1 x i32]* @__const.main.y to i8*), i64 4, i1 false)
  %8 = load i32, i32* %2, align 4
  %9 = load i32, i32* %3, align 4
  %10 = getelementptr inbounds [1 x i32], [1 x i32]* %4, i64 0, i64 0
  %11 = getelementptr inbounds [1 x i32], [1 x i32]* %5, i64 0, i64 0
  %12 = call i32 @exgcd(i32 %8, i32 %9, i32* %10, i32* %11)
  %13 = getelementptr inbounds [1 x i32], [1 x i32]* %4, i64 0, i64 0
  %14 = load i32, i32* %13, align 4
  %15 = load i32, i32* %3, align 4
  %16 = srem i32 %14, %15
  %17 = load i32, i32* %3, align 4
  %18 = add nsw i32 %16, %17
  %19 = load i32, i32* %3, align 4
  %20 = srem i32 %18, %19
  %21 = getelementptr inbounds [1 x i32], [1 x i32]* %4, i64 0, i64 0
  store i32 %20, i32* %21, align 4
  %22 = getelementptr inbounds [1 x i32], [1 x i32]* %4, i64 0, i64 0
  %23 = load i32, i32* %22, align 4
  %24 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %23)
  ret i32 0
}
'''
s11='''
; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @move(i32 %0, i32 %1) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  %5 = load i32, i32* %3, align 4
  %6 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %5)
  %7 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 32)
  %8 = load i32, i32* %4, align 4
  %9 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %8)
  %10 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 44)
  %11 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 32)
  ret void
}

declare dso_local i32 @putint(...) #1

declare dso_local i32 @putch(...) #1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @hanoi(i32 %0, i32 %1, i32 %2, i32 %3) #0 {
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  store i32 %0, i32* %5, align 4
  store i32 %1, i32* %6, align 4
  store i32 %2, i32* %7, align 4
  store i32 %3, i32* %8, align 4
  %9 = load i32, i32* %5, align 4
  %10 = icmp eq i32 %9, 1
  br i1 %10, label %11, label %14

11:                                               ; preds = %4
  %12 = load i32, i32* %6, align 4
  %13 = load i32, i32* %8, align 4
  call void @move(i32 %12, i32 %13)
  br label %27

14:                                               ; preds = %4
  %15 = load i32, i32* %5, align 4
  %16 = sub nsw i32 %15, 1
  %17 = load i32, i32* %6, align 4
  %18 = load i32, i32* %8, align 4
  %19 = load i32, i32* %7, align 4
  call void @hanoi(i32 %16, i32 %17, i32 %18, i32 %19)
  %20 = load i32, i32* %6, align 4
  %21 = load i32, i32* %8, align 4
  call void @move(i32 %20, i32 %21)
  %22 = load i32, i32* %5, align 4
  %23 = sub nsw i32 %22, 1
  %24 = load i32, i32* %7, align 4
  %25 = load i32, i32* %6, align 4
  %26 = load i32, i32* %8, align 4
  call void @hanoi(i32 %23, i32 %24, i32 %25, i32 %26)
  br label %27

27:                                               ; preds = %14, %11
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %3 = call i32 (...) @getint()
  store i32 %3, i32* %2, align 4
  br label %4

4:                                                ; preds = %7, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp sgt i32 %5, 0
  br i1 %6, label %7, label %12

7:                                                ; preds = %4
  %8 = call i32 (...) @getint()
  call void @hanoi(i32 %8, i32 1, i32 2, i32 3)
  %9 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 10)
  %10 = load i32, i32* %2, align 4
  %11 = sub nsw i32 %10, 1
  store i32 %11, i32* %2, align 4
  br label %4

12:                                               ; preds = %4
  ret i32 0
}
'''
s12='''
define dso_local i32 @relu_reg(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp sgt i32 %4, 127
  br i1 %5, label %6, label %7

6:                                                ; preds = %1
  store i32 127, i32* %2, align 4
  br label %13

7:                                                ; preds = %1
  %8 = load i32, i32* %3, align 4
  %9 = icmp slt i32 %8, 0
  br i1 %9, label %10, label %11

10:                                               ; preds = %7
  store i32 0, i32* %2, align 4
  br label %13

11:                                               ; preds = %7
  %12 = load i32, i32* %3, align 4
  store i32 %12, i32* %2, align 4
  br label %13

13:                                               ; preds = %11, %10, %6
  %14 = load i32, i32* %2, align 4
  ret i32 %14
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @model([5 x i32]* %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca [5 x i32]*, align 8
  store [5 x i32]* %0, [5 x i32]** %3, align 8
  %4 = load [5 x i32]*, [5 x i32]** %3, align 8
  %5 = getelementptr inbounds [5 x i32], [5 x i32]* %4, i64 0
  %6 = getelementptr inbounds [5 x i32], [5 x i32]* %5, i64 0, i64 0
  %7 = load i32, i32* %6, align 4
  %8 = mul nsw i32 %7, 85
  %9 = load [5 x i32]*, [5 x i32]** %3, align 8
  %10 = getelementptr inbounds [5 x i32], [5 x i32]* %9, i64 0
  %11 = getelementptr inbounds [5 x i32], [5 x i32]* %10, i64 0, i64 1
  %12 = load i32, i32* %11, align 4
  %13 = mul nsw i32 %12, 23
  %14 = add nsw i32 %8, %13
  %15 = load [5 x i32]*, [5 x i32]** %3, align 8
  %16 = getelementptr inbounds [5 x i32], [5 x i32]* %15, i64 0
  %17 = getelementptr inbounds [5 x i32], [5 x i32]* %16, i64 0, i64 2
  %18 = load i32, i32* %17, align 4
  %19 = mul nsw i32 %18, -82
  %20 = add nsw i32 %14, %19
  %21 = load [5 x i32]*, [5 x i32]** %3, align 8
  %22 = getelementptr inbounds [5 x i32], [5 x i32]* %21, i64 0
  %23 = getelementptr inbounds [5 x i32], [5 x i32]* %22, i64 0, i64 3
  %24 = load i32, i32* %23, align 4
  %25 = mul nsw i32 %24, -103
  %26 = add nsw i32 %20, %25
  %27 = load [5 x i32]*, [5 x i32]** %3, align 8
  %28 = getelementptr inbounds [5 x i32], [5 x i32]* %27, i64 0
  %29 = getelementptr inbounds [5 x i32], [5 x i32]* %28, i64 0, i64 4
  %30 = load i32, i32* %29, align 4
  %31 = mul nsw i32 %30, -123
  %32 = add nsw i32 %26, %31
  %33 = load [5 x i32]*, [5 x i32]** %3, align 8
  %34 = getelementptr inbounds [5 x i32], [5 x i32]* %33, i64 1
  %35 = getelementptr inbounds [5 x i32], [5 x i32]* %34, i64 0, i64 0
  %36 = load i32, i32* %35, align 4
  %37 = mul nsw i32 %36, 64
  %38 = add nsw i32 %32, %37
  %39 = load [5 x i32]*, [5 x i32]** %3, align 8
  %40 = getelementptr inbounds [5 x i32], [5 x i32]* %39, i64 1
  %41 = getelementptr inbounds [5 x i32], [5 x i32]* %40, i64 0, i64 1
  %42 = load i32, i32* %41, align 4
  %43 = mul nsw i32 %42, -120
  %44 = add nsw i32 %38, %43
  %45 = load [5 x i32]*, [5 x i32]** %3, align 8
  %46 = getelementptr inbounds [5 x i32], [5 x i32]* %45, i64 1
  %47 = getelementptr inbounds [5 x i32], [5 x i32]* %46, i64 0, i64 2
  %48 = load i32, i32* %47, align 4
  %49 = mul nsw i32 %48, 50
  %50 = add nsw i32 %44, %49
  %51 = load [5 x i32]*, [5 x i32]** %3, align 8
  %52 = getelementptr inbounds [5 x i32], [5 x i32]* %51, i64 1
  %53 = getelementptr inbounds [5 x i32], [5 x i32]* %52, i64 0, i64 3
  %54 = load i32, i32* %53, align 4
  %55 = mul nsw i32 %54, -59
  %56 = add nsw i32 %50, %55
  %57 = load [5 x i32]*, [5 x i32]** %3, align 8
  %58 = getelementptr inbounds [5 x i32], [5 x i32]* %57, i64 1
  %59 = getelementptr inbounds [5 x i32], [5 x i32]* %58, i64 0, i64 4
  %60 = load i32, i32* %59, align 4
  %61 = mul nsw i32 %60, 47
  %62 = add nsw i32 %56, %61
  %63 = load [5 x i32]*, [5 x i32]** %3, align 8
  %64 = getelementptr inbounds [5 x i32], [5 x i32]* %63, i64 2
  %65 = getelementptr inbounds [5 x i32], [5 x i32]* %64, i64 0, i64 0
  %66 = load i32, i32* %65, align 4
  %67 = mul nsw i32 %66, -111
  %68 = add nsw i32 %62, %67
  %69 = load [5 x i32]*, [5 x i32]** %3, align 8
  %70 = getelementptr inbounds [5 x i32], [5 x i32]* %69, i64 2
  %71 = getelementptr inbounds [5 x i32], [5 x i32]* %70, i64 0, i64 1
  %72 = load i32, i32* %71, align 4
  %73 = mul nsw i32 %72, -67
  %74 = add nsw i32 %68, %73
  %75 = load [5 x i32]*, [5 x i32]** %3, align 8
  %76 = getelementptr inbounds [5 x i32], [5 x i32]* %75, i64 2
  %77 = getelementptr inbounds [5 x i32], [5 x i32]* %76, i64 0, i64 2
  %78 = load i32, i32* %77, align 4
  %79 = mul nsw i32 %78, -106
  %80 = add nsw i32 %74, %79
  %81 = load [5 x i32]*, [5 x i32]** %3, align 8
  %82 = getelementptr inbounds [5 x i32], [5 x i32]* %81, i64 2
  %83 = getelementptr inbounds [5 x i32], [5 x i32]* %82, i64 0, i64 3
  %84 = load i32, i32* %83, align 4
  %85 = mul nsw i32 %84, -75
  %86 = add nsw i32 %80, %85
  %87 = load [5 x i32]*, [5 x i32]** %3, align 8
  %88 = getelementptr inbounds [5 x i32], [5 x i32]* %87, i64 2
  %89 = getelementptr inbounds [5 x i32], [5 x i32]* %88, i64 0, i64 4
  %90 = load i32, i32* %89, align 4
  %91 = mul nsw i32 %90, -102
  %92 = add nsw i32 %86, %91
  %93 = load [5 x i32]*, [5 x i32]** %3, align 8
  %94 = getelementptr inbounds [5 x i32], [5 x i32]* %93, i64 3
  %95 = getelementptr inbounds [5 x i32], [5 x i32]* %94, i64 0, i64 0
  %96 = load i32, i32* %95, align 4
  %97 = mul nsw i32 %96, 34
  %98 = add nsw i32 %92, %97
  %99 = load [5 x i32]*, [5 x i32]** %3, align 8
  %100 = getelementptr inbounds [5 x i32], [5 x i32]* %99, i64 3
  %101 = getelementptr inbounds [5 x i32], [5 x i32]* %100, i64 0, i64 1
  %102 = load i32, i32* %101, align 4
  %103 = mul nsw i32 %102, -39
  %104 = add nsw i32 %98, %103
  %105 = load [5 x i32]*, [5 x i32]** %3, align 8
  %106 = getelementptr inbounds [5 x i32], [5 x i32]* %105, i64 3
  %107 = getelementptr inbounds [5 x i32], [5 x i32]* %106, i64 0, i64 2
  %108 = load i32, i32* %107, align 4
  %109 = mul nsw i32 %108, 65
  %110 = add nsw i32 %104, %109
  %111 = load [5 x i32]*, [5 x i32]** %3, align 8
  %112 = getelementptr inbounds [5 x i32], [5 x i32]* %111, i64 3
  %113 = getelementptr inbounds [5 x i32], [5 x i32]* %112, i64 0, i64 3
  %114 = load i32, i32* %113, align 4
  %115 = mul nsw i32 %114, 47
  %116 = add nsw i32 %110, %115
  %117 = load [5 x i32]*, [5 x i32]** %3, align 8
  %118 = getelementptr inbounds [5 x i32], [5 x i32]* %117, i64 3
  %119 = getelementptr inbounds [5 x i32], [5 x i32]* %118, i64 0, i64 4
  %120 = load i32, i32* %119, align 4
  %121 = mul nsw i32 %120, 113
  %122 = add nsw i32 %116, %121
  %123 = load [5 x i32]*, [5 x i32]** %3, align 8
  %124 = getelementptr inbounds [5 x i32], [5 x i32]* %123, i64 4
  %125 = getelementptr inbounds [5 x i32], [5 x i32]* %124, i64 0, i64 0
  %126 = load i32, i32* %125, align 4
  %127 = mul nsw i32 %126, 110
  %128 = add nsw i32 %122, %127
  %129 = load [5 x i32]*, [5 x i32]** %3, align 8
  %130 = getelementptr inbounds [5 x i32], [5 x i32]* %129, i64 4
  %131 = getelementptr inbounds [5 x i32], [5 x i32]* %130, i64 0, i64 1
  %132 = load i32, i32* %131, align 4
  %133 = mul nsw i32 %132, 47
  %134 = add nsw i32 %128, %133
  %135 = load [5 x i32]*, [5 x i32]** %3, align 8
  %136 = getelementptr inbounds [5 x i32], [5 x i32]* %135, i64 4
  %137 = getelementptr inbounds [5 x i32], [5 x i32]* %136, i64 0, i64 2
  %138 = load i32, i32* %137, align 4
  %139 = mul nsw i32 %138, -4
  %140 = add nsw i32 %134, %139
  %141 = load [5 x i32]*, [5 x i32]** %3, align 8
  %142 = getelementptr inbounds [5 x i32], [5 x i32]* %141, i64 4
  %143 = getelementptr inbounds [5 x i32], [5 x i32]* %142, i64 0, i64 3
  %144 = load i32, i32* %143, align 4
  %145 = mul nsw i32 %144, 80
  %146 = add nsw i32 %140, %145
  %147 = load [5 x i32]*, [5 x i32]** %3, align 8
  %148 = getelementptr inbounds [5 x i32], [5 x i32]* %147, i64 4
  %149 = getelementptr inbounds [5 x i32], [5 x i32]* %148, i64 0, i64 4
  %150 = load i32, i32* %149, align 4
  %151 = mul nsw i32 %150, 46
  %152 = add nsw i32 %146, %151
  %153 = call i32 @relu_reg(i32 %152)
  %154 = mul nsw i32 %153, 39
  %155 = load [5 x i32]*, [5 x i32]** %3, align 8
  %156 = getelementptr inbounds [5 x i32], [5 x i32]* %155, i64 0
  %157 = getelementptr inbounds [5 x i32], [5 x i32]* %156, i64 0, i64 0
  %158 = load i32, i32* %157, align 4
  %159 = mul nsw i32 %158, -106
  %160 = load [5 x i32]*, [5 x i32]** %3, align 8
  %161 = getelementptr inbounds [5 x i32], [5 x i32]* %160, i64 0
  %162 = getelementptr inbounds [5 x i32], [5 x i32]* %161, i64 0, i64 1
  %163 = load i32, i32* %162, align 4
  %164 = mul nsw i32 %163, 126
  %165 = add nsw i32 %159, %164
  %166 = load [5 x i32]*, [5 x i32]** %3, align 8
  %167 = getelementptr inbounds [5 x i32], [5 x i32]* %166, i64 0
  %168 = getelementptr inbounds [5 x i32], [5 x i32]* %167, i64 0, i64 2
  %169 = load i32, i32* %168, align 4
  %170 = mul nsw i32 %169, -18
  %171 = add nsw i32 %165, %170
  %172 = load [5 x i32]*, [5 x i32]** %3, align 8
  %173 = getelementptr inbounds [5 x i32], [5 x i32]* %172, i64 0
  %174 = getelementptr inbounds [5 x i32], [5 x i32]* %173, i64 0, i64 3
  %175 = load i32, i32* %174, align 4
  %176 = mul nsw i32 %175, -31
  %177 = add nsw i32 %171, %176
  %178 = load [5 x i32]*, [5 x i32]** %3, align 8
  %179 = getelementptr inbounds [5 x i32], [5 x i32]* %178, i64 0
  %180 = getelementptr inbounds [5 x i32], [5 x i32]* %179, i64 0, i64 4
  %181 = load i32, i32* %180, align 4
  %182 = mul nsw i32 %181, -8
  %183 = add nsw i32 %177, %182
  %184 = load [5 x i32]*, [5 x i32]** %3, align 8
  %185 = getelementptr inbounds [5 x i32], [5 x i32]* %184, i64 1
  %186 = getelementptr inbounds [5 x i32], [5 x i32]* %185, i64 0, i64 0
  %187 = load i32, i32* %186, align 4
  %188 = mul nsw i32 %187, 47
  %189 = add nsw i32 %183, %188
  %190 = load [5 x i32]*, [5 x i32]** %3, align 8
  %191 = getelementptr inbounds [5 x i32], [5 x i32]* %190, i64 1
  %192 = getelementptr inbounds [5 x i32], [5 x i32]* %191, i64 0, i64 1
  %193 = load i32, i32* %192, align 4
  %194 = mul nsw i32 %193, -4
  %195 = add nsw i32 %189, %194
  %196 = load [5 x i32]*, [5 x i32]** %3, align 8
  %197 = getelementptr inbounds [5 x i32], [5 x i32]* %196, i64 1
  %198 = getelementptr inbounds [5 x i32], [5 x i32]* %197, i64 0, i64 2
  %199 = load i32, i32* %198, align 4
  %200 = mul nsw i32 %199, 67
  %201 = add nsw i32 %195, %200
  %202 = load [5 x i32]*, [5 x i32]** %3, align 8
  %203 = getelementptr inbounds [5 x i32], [5 x i32]* %202, i64 1
  %204 = getelementptr inbounds [5 x i32], [5 x i32]* %203, i64 0, i64 3
  %205 = load i32, i32* %204, align 4
  %206 = mul nsw i32 %205, -94
  %207 = add nsw i32 %201, %206
  %208 = load [5 x i32]*, [5 x i32]** %3, align 8
  %209 = getelementptr inbounds [5 x i32], [5 x i32]* %208, i64 1
  %210 = getelementptr inbounds [5 x i32], [5 x i32]* %209, i64 0, i64 4
  %211 = load i32, i32* %210, align 4
  %212 = mul nsw i32 %211, -121
  %213 = add nsw i32 %207, %212
  %214 = load [5 x i32]*, [5 x i32]** %3, align 8
  %215 = getelementptr inbounds [5 x i32], [5 x i32]* %214, i64 2
  %216 = getelementptr inbounds [5 x i32], [5 x i32]* %215, i64 0, i64 0
  %217 = load i32, i32* %216, align 4
  %218 = mul nsw i32 %217, 7
  %219 = add nsw i32 %213, %218
  %220 = load [5 x i32]*, [5 x i32]** %3, align 8
  %221 = getelementptr inbounds [5 x i32], [5 x i32]* %220, i64 2
  %222 = getelementptr inbounds [5 x i32], [5 x i32]* %221, i64 0, i64 1
  %223 = load i32, i32* %222, align 4
  %224 = mul nsw i32 %223, -21
  %225 = add nsw i32 %219, %224
  %226 = load [5 x i32]*, [5 x i32]** %3, align 8
  %227 = getelementptr inbounds [5 x i32], [5 x i32]* %226, i64 2
  %228 = getelementptr inbounds [5 x i32], [5 x i32]* %227, i64 0, i64 2
  %229 = load i32, i32* %228, align 4
  %230 = mul nsw i32 %229, -60
  %231 = add nsw i32 %225, %230
  %232 = load [5 x i32]*, [5 x i32]** %3, align 8
  %233 = getelementptr inbounds [5 x i32], [5 x i32]* %232, i64 2
  %234 = getelementptr inbounds [5 x i32], [5 x i32]* %233, i64 0, i64 3
  %235 = load i32, i32* %234, align 4
  %236 = mul nsw i32 %235, -43
  %237 = add nsw i32 %231, %236
  %238 = load [5 x i32]*, [5 x i32]** %3, align 8
  %239 = getelementptr inbounds [5 x i32], [5 x i32]* %238, i64 2
  %240 = getelementptr inbounds [5 x i32], [5 x i32]* %239, i64 0, i64 4
  %241 = load i32, i32* %240, align 4
  %242 = mul nsw i32 %241, 105
  %243 = add nsw i32 %237, %242
  %244 = load [5 x i32]*, [5 x i32]** %3, align 8
  %245 = getelementptr inbounds [5 x i32], [5 x i32]* %244, i64 3
  %246 = getelementptr inbounds [5 x i32], [5 x i32]* %245, i64 0, i64 0
  %247 = load i32, i32* %246, align 4
  %248 = mul nsw i32 %247, -42
  %249 = add nsw i32 %243, %248
  %250 = load [5 x i32]*, [5 x i32]** %3, align 8
  %251 = getelementptr inbounds [5 x i32], [5 x i32]* %250, i64 3
  %252 = getelementptr inbounds [5 x i32], [5 x i32]* %251, i64 0, i64 1
  %253 = load i32, i32* %252, align 4
  %254 = mul nsw i32 %253, 87
  %255 = add nsw i32 %249, %254
  %256 = load [5 x i32]*, [5 x i32]** %3, align 8
  %257 = getelementptr inbounds [5 x i32], [5 x i32]* %256, i64 3
  %258 = getelementptr inbounds [5 x i32], [5 x i32]* %257, i64 0, i64 2
  %259 = load i32, i32* %258, align 4
  %260 = mul nsw i32 %259, 29
  %261 = add nsw i32 %255, %260
  %262 = load [5 x i32]*, [5 x i32]** %3, align 8
  %263 = getelementptr inbounds [5 x i32], [5 x i32]* %262, i64 3
  %264 = getelementptr inbounds [5 x i32], [5 x i32]* %263, i64 0, i64 3
  %265 = load i32, i32* %264, align 4
  %266 = mul nsw i32 %265, -106
  %267 = add nsw i32 %261, %266
  %268 = load [5 x i32]*, [5 x i32]** %3, align 8
  %269 = getelementptr inbounds [5 x i32], [5 x i32]* %268, i64 3
  %270 = getelementptr inbounds [5 x i32], [5 x i32]* %269, i64 0, i64 4
  %271 = load i32, i32* %270, align 4
  %272 = mul nsw i32 %271, -31
  %273 = add nsw i32 %267, %272
  %274 = load [5 x i32]*, [5 x i32]** %3, align 8
  %275 = getelementptr inbounds [5 x i32], [5 x i32]* %274, i64 4
  %276 = getelementptr inbounds [5 x i32], [5 x i32]* %275, i64 0, i64 0
  %277 = load i32, i32* %276, align 4
  %278 = mul nsw i32 %277, -110
  %279 = add nsw i32 %273, %278
  %280 = load [5 x i32]*, [5 x i32]** %3, align 8
  %281 = getelementptr inbounds [5 x i32], [5 x i32]* %280, i64 4
  %282 = getelementptr inbounds [5 x i32], [5 x i32]* %281, i64 0, i64 1
  %283 = load i32, i32* %282, align 4
  %284 = mul nsw i32 %283, -100
  %285 = add nsw i32 %279, %284
  %286 = load [5 x i32]*, [5 x i32]** %3, align 8
  %287 = getelementptr inbounds [5 x i32], [5 x i32]* %286, i64 4
  %288 = getelementptr inbounds [5 x i32], [5 x i32]* %287, i64 0, i64 2
  %289 = load i32, i32* %288, align 4
  %290 = mul nsw i32 %289, -22
  %291 = add nsw i32 %285, %290
  %292 = load [5 x i32]*, [5 x i32]** %3, align 8
  %293 = getelementptr inbounds [5 x i32], [5 x i32]* %292, i64 4
  %294 = getelementptr inbounds [5 x i32], [5 x i32]* %293, i64 0, i64 3
  %295 = load i32, i32* %294, align 4
  %296 = mul nsw i32 %295, -75
  %297 = add nsw i32 %291, %296
  %298 = load [5 x i32]*, [5 x i32]** %3, align 8
  %299 = getelementptr inbounds [5 x i32], [5 x i32]* %298, i64 4
  %300 = getelementptr inbounds [5 x i32], [5 x i32]* %299, i64 0, i64 4
  %301 = load i32, i32* %300, align 4
  %302 = mul nsw i32 %301, -125
  %303 = add nsw i32 %297, %302
  %304 = call i32 @relu_reg(i32 %303)
  %305 = mul nsw i32 %304, 77
  %306 = add nsw i32 %154, %305
  %307 = load [5 x i32]*, [5 x i32]** %3, align 8
  %308 = getelementptr inbounds [5 x i32], [5 x i32]* %307, i64 0
  %309 = getelementptr inbounds [5 x i32], [5 x i32]* %308, i64 0, i64 0
  %310 = load i32, i32* %309, align 4
  %311 = mul nsw i32 %310, 26
  %312 = load [5 x i32]*, [5 x i32]** %3, align 8
  %313 = getelementptr inbounds [5 x i32], [5 x i32]* %312, i64 0
  %314 = getelementptr inbounds [5 x i32], [5 x i32]* %313, i64 0, i64 1
  %315 = load i32, i32* %314, align 4
  %316 = mul nsw i32 %315, 76
  %317 = add nsw i32 %311, %316
  %318 = load [5 x i32]*, [5 x i32]** %3, align 8
  %319 = getelementptr inbounds [5 x i32], [5 x i32]* %318, i64 0
  %320 = getelementptr inbounds [5 x i32], [5 x i32]* %319, i64 0, i64 2
  %321 = load i32, i32* %320, align 4
  %322 = mul nsw i32 %321, -70
  %323 = add nsw i32 %317, %322
  %324 = load [5 x i32]*, [5 x i32]** %3, align 8
  %325 = getelementptr inbounds [5 x i32], [5 x i32]* %324, i64 0
  %326 = getelementptr inbounds [5 x i32], [5 x i32]* %325, i64 0, i64 3
  %327 = load i32, i32* %326, align 4
  %328 = mul nsw i32 %327, 29
  %329 = add nsw i32 %323, %328
  %330 = load [5 x i32]*, [5 x i32]** %3, align 8
  %331 = getelementptr inbounds [5 x i32], [5 x i32]* %330, i64 0
  %332 = getelementptr inbounds [5 x i32], [5 x i32]* %331, i64 0, i64 4
  %333 = load i32, i32* %332, align 4
  %334 = mul nsw i32 %333, -95
  %335 = add nsw i32 %329, %334
  %336 = load [5 x i32]*, [5 x i32]** %3, align 8
  %337 = getelementptr inbounds [5 x i32], [5 x i32]* %336, i64 1
  %338 = getelementptr inbounds [5 x i32], [5 x i32]* %337, i64 0, i64 0
  %339 = load i32, i32* %338, align 4
  %340 = mul nsw i32 %339, 96
  %341 = add nsw i32 %335, %340
  %342 = load [5 x i32]*, [5 x i32]** %3, align 8
  %343 = getelementptr inbounds [5 x i32], [5 x i32]* %342, i64 1
  %344 = getelementptr inbounds [5 x i32], [5 x i32]* %343, i64 0, i64 1
  %345 = load i32, i32* %344, align 4
  %346 = mul nsw i32 %345, 52
  %347 = add nsw i32 %341, %346
  %348 = load [5 x i32]*, [5 x i32]** %3, align 8
  %349 = getelementptr inbounds [5 x i32], [5 x i32]* %348, i64 1
  %350 = getelementptr inbounds [5 x i32], [5 x i32]* %349, i64 0, i64 2
  %351 = load i32, i32* %350, align 4
  %352 = mul nsw i32 %351, -68
  %353 = add nsw i32 %347, %352
  %354 = load [5 x i32]*, [5 x i32]** %3, align 8
  %355 = getelementptr inbounds [5 x i32], [5 x i32]* %354, i64 1
  %356 = getelementptr inbounds [5 x i32], [5 x i32]* %355, i64 0, i64 3
  %357 = load i32, i32* %356, align 4
  %358 = mul nsw i32 %357, -5
  %359 = add nsw i32 %353, %358
  %360 = load [5 x i32]*, [5 x i32]** %3, align 8
  %361 = getelementptr inbounds [5 x i32], [5 x i32]* %360, i64 1
  %362 = getelementptr inbounds [5 x i32], [5 x i32]* %361, i64 0, i64 4
  %363 = load i32, i32* %362, align 4
  %364 = mul nsw i32 %363, 34
  %365 = add nsw i32 %359, %364
  %366 = load [5 x i32]*, [5 x i32]** %3, align 8
  %367 = getelementptr inbounds [5 x i32], [5 x i32]* %366, i64 2
  %368 = getelementptr inbounds [5 x i32], [5 x i32]* %367, i64 0, i64 0
  %369 = load i32, i32* %368, align 4
  %370 = mul nsw i32 %369, -34
  %371 = add nsw i32 %365, %370
  %372 = load [5 x i32]*, [5 x i32]** %3, align 8
  %373 = getelementptr inbounds [5 x i32], [5 x i32]* %372, i64 2
  %374 = getelementptr inbounds [5 x i32], [5 x i32]* %373, i64 0, i64 1
  %375 = load i32, i32* %374, align 4
  %376 = mul nsw i32 %375, 102
  %377 = add nsw i32 %371, %376
  %378 = load [5 x i32]*, [5 x i32]** %3, align 8
  %379 = getelementptr inbounds [5 x i32], [5 x i32]* %378, i64 2
  %380 = getelementptr inbounds [5 x i32], [5 x i32]* %379, i64 0, i64 2
  %381 = load i32, i32* %380, align 4
  %382 = mul nsw i32 %381, 6
  %383 = add nsw i32 %377, %382
  %384 = load [5 x i32]*, [5 x i32]** %3, align 8
  %385 = getelementptr inbounds [5 x i32], [5 x i32]* %384, i64 2
  %386 = getelementptr inbounds [5 x i32], [5 x i32]* %385, i64 0, i64 3
  %387 = load i32, i32* %386, align 4
  %388 = mul nsw i32 %387, -38
  %389 = add nsw i32 %383, %388
  %390 = load [5 x i32]*, [5 x i32]** %3, align 8
  %391 = getelementptr inbounds [5 x i32], [5 x i32]* %390, i64 2
  %392 = getelementptr inbounds [5 x i32], [5 x i32]* %391, i64 0, i64 4
  %393 = load i32, i32* %392, align 4
  %394 = mul nsw i32 %393, 27
  %395 = add nsw i32 %389, %394
  %396 = load [5 x i32]*, [5 x i32]** %3, align 8
  %397 = getelementptr inbounds [5 x i32], [5 x i32]* %396, i64 3
  %398 = getelementptr inbounds [5 x i32], [5 x i32]* %397, i64 0, i64 0
  %399 = load i32, i32* %398, align 4
  %400 = mul nsw i32 %399, 110
  %401 = add nsw i32 %395, %400
  %402 = load [5 x i32]*, [5 x i32]** %3, align 8
  %403 = getelementptr inbounds [5 x i32], [5 x i32]* %402, i64 3
  %404 = getelementptr inbounds [5 x i32], [5 x i32]* %403, i64 0, i64 1
  %405 = load i32, i32* %404, align 4
  %406 = mul nsw i32 %405, 116
  %407 = add nsw i32 %401, %406
  %408 = load [5 x i32]*, [5 x i32]** %3, align 8
  %409 = getelementptr inbounds [5 x i32], [5 x i32]* %408, i64 3
  %410 = getelementptr inbounds [5 x i32], [5 x i32]* %409, i64 0, i64 2
  %411 = load i32, i32* %410, align 4
  %412 = mul nsw i32 %411, 39
  %413 = add nsw i32 %407, %412
  %414 = load [5 x i32]*, [5 x i32]** %3, align 8
  %415 = getelementptr inbounds [5 x i32], [5 x i32]* %414, i64 3
  %416 = getelementptr inbounds [5 x i32], [5 x i32]* %415, i64 0, i64 3
  %417 = load i32, i32* %416, align 4
  %418 = mul nsw i32 %417, -63
  %419 = add nsw i32 %413, %418
  %420 = load [5 x i32]*, [5 x i32]** %3, align 8
  %421 = getelementptr inbounds [5 x i32], [5 x i32]* %420, i64 3
  %422 = getelementptr inbounds [5 x i32], [5 x i32]* %421, i64 0, i64 4
  %423 = load i32, i32* %422, align 4
  %424 = mul nsw i32 %423, -99
  %425 = add nsw i32 %419, %424
  %426 = load [5 x i32]*, [5 x i32]** %3, align 8
  %427 = getelementptr inbounds [5 x i32], [5 x i32]* %426, i64 4
  %428 = getelementptr inbounds [5 x i32], [5 x i32]* %427, i64 0, i64 0
  %429 = load i32, i32* %428, align 4
  %430 = mul nsw i32 %429, 65
  %431 = add nsw i32 %425, %430
  %432 = load [5 x i32]*, [5 x i32]** %3, align 8
  %433 = getelementptr inbounds [5 x i32], [5 x i32]* %432, i64 4
  %434 = getelementptr inbounds [5 x i32], [5 x i32]* %433, i64 0, i64 1
  %435 = load i32, i32* %434, align 4
  %436 = mul nsw i32 %435, 120
  %437 = add nsw i32 %431, %436
  %438 = load [5 x i32]*, [5 x i32]** %3, align 8
  %439 = getelementptr inbounds [5 x i32], [5 x i32]* %438, i64 4
  %440 = getelementptr inbounds [5 x i32], [5 x i32]* %439, i64 0, i64 2
  %441 = load i32, i32* %440, align 4
  %442 = mul nsw i32 %441, -39
  %443 = add nsw i32 %437, %442
  %444 = load [5 x i32]*, [5 x i32]** %3, align 8
  %445 = getelementptr inbounds [5 x i32], [5 x i32]* %444, i64 4
  %446 = getelementptr inbounds [5 x i32], [5 x i32]* %445, i64 0, i64 3
  %447 = load i32, i32* %446, align 4
  %448 = mul nsw i32 %447, -6
  %449 = add nsw i32 %443, %448
  %450 = load [5 x i32]*, [5 x i32]** %3, align 8
  %451 = getelementptr inbounds [5 x i32], [5 x i32]* %450, i64 4
  %452 = getelementptr inbounds [5 x i32], [5 x i32]* %451, i64 0, i64 4
  %453 = load i32, i32* %452, align 4
  %454 = mul nsw i32 %453, 94
  %455 = add nsw i32 %449, %454
  %456 = call i32 @relu_reg(i32 %455)
  %457 = mul nsw i32 %456, 127
  %458 = add nsw i32 %306, %457
  %459 = load [5 x i32]*, [5 x i32]** %3, align 8
  %460 = getelementptr inbounds [5 x i32], [5 x i32]* %459, i64 0
  %461 = getelementptr inbounds [5 x i32], [5 x i32]* %460, i64 0, i64 0
  %462 = load i32, i32* %461, align 4
  %463 = mul nsw i32 %462, -23
  %464 = load [5 x i32]*, [5 x i32]** %3, align 8
  %465 = getelementptr inbounds [5 x i32], [5 x i32]* %464, i64 0
  %466 = getelementptr inbounds [5 x i32], [5 x i32]* %465, i64 0, i64 1
  %467 = load i32, i32* %466, align 4
  %468 = mul nsw i32 %467, -63
  %469 = add nsw i32 %463, %468
  %470 = load [5 x i32]*, [5 x i32]** %3, align 8
  %471 = getelementptr inbounds [5 x i32], [5 x i32]* %470, i64 0
  %472 = getelementptr inbounds [5 x i32], [5 x i32]* %471, i64 0, i64 2
  %473 = load i32, i32* %472, align 4
  %474 = mul nsw i32 %473, 49
  %475 = add nsw i32 %469, %474
  %476 = load [5 x i32]*, [5 x i32]** %3, align 8
  %477 = getelementptr inbounds [5 x i32], [5 x i32]* %476, i64 0
  %478 = getelementptr inbounds [5 x i32], [5 x i32]* %477, i64 0, i64 3
  %479 = load i32, i32* %478, align 4
  %480 = mul nsw i32 %479, 50
  %481 = add nsw i32 %475, %480
  %482 = load [5 x i32]*, [5 x i32]** %3, align 8
  %483 = getelementptr inbounds [5 x i32], [5 x i32]* %482, i64 0
  %484 = getelementptr inbounds [5 x i32], [5 x i32]* %483, i64 0, i64 4
  %485 = load i32, i32* %484, align 4
  %486 = mul nsw i32 %485, 72
  %487 = add nsw i32 %481, %486
  %488 = load [5 x i32]*, [5 x i32]** %3, align 8
  %489 = getelementptr inbounds [5 x i32], [5 x i32]* %488, i64 1
  %490 = getelementptr inbounds [5 x i32], [5 x i32]* %489, i64 0, i64 0
  %491 = load i32, i32* %490, align 4
  %492 = mul nsw i32 %491, 85
  %493 = add nsw i32 %487, %492
  %494 = load [5 x i32]*, [5 x i32]** %3, align 8
  %495 = getelementptr inbounds [5 x i32], [5 x i32]* %494, i64 1
  %496 = getelementptr inbounds [5 x i32], [5 x i32]* %495, i64 0, i64 1
  %497 = load i32, i32* %496, align 4
  %498 = mul nsw i32 %497, -30
  %499 = add nsw i32 %493, %498
  %500 = load [5 x i32]*, [5 x i32]** %3, align 8
  %501 = getelementptr inbounds [5 x i32], [5 x i32]* %500, i64 1
  %502 = getelementptr inbounds [5 x i32], [5 x i32]* %501, i64 0, i64 2
  %503 = load i32, i32* %502, align 4
  %504 = mul nsw i32 %503, 12
  %505 = add nsw i32 %499, %504
  %506 = load [5 x i32]*, [5 x i32]** %3, align 8
  %507 = getelementptr inbounds [5 x i32], [5 x i32]* %506, i64 1
  %508 = getelementptr inbounds [5 x i32], [5 x i32]* %507, i64 0, i64 3
  %509 = load i32, i32* %508, align 4
  %510 = mul nsw i32 %509, 125
  %511 = add nsw i32 %505, %510
  %512 = load [5 x i32]*, [5 x i32]** %3, align 8
  %513 = getelementptr inbounds [5 x i32], [5 x i32]* %512, i64 1
  %514 = getelementptr inbounds [5 x i32], [5 x i32]* %513, i64 0, i64 4
  %515 = load i32, i32* %514, align 4
  %516 = mul nsw i32 %515, -117
  %517 = add nsw i32 %511, %516
  %518 = load [5 x i32]*, [5 x i32]** %3, align 8
  %519 = getelementptr inbounds [5 x i32], [5 x i32]* %518, i64 2
  %520 = getelementptr inbounds [5 x i32], [5 x i32]* %519, i64 0, i64 0
  %521 = load i32, i32* %520, align 4
  %522 = mul nsw i32 %521, -65
  %523 = add nsw i32 %517, %522
  %524 = load [5 x i32]*, [5 x i32]** %3, align 8
  %525 = getelementptr inbounds [5 x i32], [5 x i32]* %524, i64 2
  %526 = getelementptr inbounds [5 x i32], [5 x i32]* %525, i64 0, i64 1
  %527 = load i32, i32* %526, align 4
  %528 = mul nsw i32 %527, -67
  %529 = add nsw i32 %523, %528
  %530 = load [5 x i32]*, [5 x i32]** %3, align 8
  %531 = getelementptr inbounds [5 x i32], [5 x i32]* %530, i64 2
  %532 = getelementptr inbounds [5 x i32], [5 x i32]* %531, i64 0, i64 2
  %533 = load i32, i32* %532, align 4
  %534 = mul nsw i32 %533, 125
  %535 = add nsw i32 %529, %534
  %536 = load [5 x i32]*, [5 x i32]** %3, align 8
  %537 = getelementptr inbounds [5 x i32], [5 x i32]* %536, i64 2
  %538 = getelementptr inbounds [5 x i32], [5 x i32]* %537, i64 0, i64 3
  %539 = load i32, i32* %538, align 4
  %540 = mul nsw i32 %539, 110
  %541 = add nsw i32 %535, %540
  %542 = load [5 x i32]*, [5 x i32]** %3, align 8
  %543 = getelementptr inbounds [5 x i32], [5 x i32]* %542, i64 2
  %544 = getelementptr inbounds [5 x i32], [5 x i32]* %543, i64 0, i64 4
  %545 = load i32, i32* %544, align 4
  %546 = mul nsw i32 %545, -31
  %547 = add nsw i32 %541, %546
  %548 = load [5 x i32]*, [5 x i32]** %3, align 8
  %549 = getelementptr inbounds [5 x i32], [5 x i32]* %548, i64 3
  %550 = getelementptr inbounds [5 x i32], [5 x i32]* %549, i64 0, i64 0
  %551 = load i32, i32* %550, align 4
  %552 = mul nsw i32 %551, -123
  %553 = add nsw i32 %547, %552
  %554 = load [5 x i32]*, [5 x i32]** %3, align 8
  %555 = getelementptr inbounds [5 x i32], [5 x i32]* %554, i64 3
  %556 = getelementptr inbounds [5 x i32], [5 x i32]* %555, i64 0, i64 1
  %557 = load i32, i32* %556, align 4
  %558 = mul nsw i32 %557, 83
  %559 = add nsw i32 %553, %558
  %560 = load [5 x i32]*, [5 x i32]** %3, align 8
  %561 = getelementptr inbounds [5 x i32], [5 x i32]* %560, i64 3
  %562 = getelementptr inbounds [5 x i32], [5 x i32]* %561, i64 0, i64 2
  %563 = load i32, i32* %562, align 4
  %564 = mul nsw i32 %563, 122
  %565 = add nsw i32 %559, %564
  %566 = load [5 x i32]*, [5 x i32]** %3, align 8
  %567 = getelementptr inbounds [5 x i32], [5 x i32]* %566, i64 3
  %568 = getelementptr inbounds [5 x i32], [5 x i32]* %567, i64 0, i64 3
  %569 = load i32, i32* %568, align 4
  %570 = mul nsw i32 %569, 11
  %571 = add nsw i32 %565, %570
  %572 = load [5 x i32]*, [5 x i32]** %3, align 8
  %573 = getelementptr inbounds [5 x i32], [5 x i32]* %572, i64 3
  %574 = getelementptr inbounds [5 x i32], [5 x i32]* %573, i64 0, i64 4
  %575 = load i32, i32* %574, align 4
  %576 = mul nsw i32 %575, -23
  %577 = add nsw i32 %571, %576
  %578 = load [5 x i32]*, [5 x i32]** %3, align 8
  %579 = getelementptr inbounds [5 x i32], [5 x i32]* %578, i64 4
  %580 = getelementptr inbounds [5 x i32], [5 x i32]* %579, i64 0, i64 0
  %581 = load i32, i32* %580, align 4
  %582 = mul nsw i32 %581, -47
  %583 = add nsw i32 %577, %582
  %584 = load [5 x i32]*, [5 x i32]** %3, align 8
  %585 = getelementptr inbounds [5 x i32], [5 x i32]* %584, i64 4
  %586 = getelementptr inbounds [5 x i32], [5 x i32]* %585, i64 0, i64 1
  %587 = load i32, i32* %586, align 4
  %588 = mul nsw i32 %587, -32
  %589 = add nsw i32 %583, %588
  %590 = load [5 x i32]*, [5 x i32]** %3, align 8
  %591 = getelementptr inbounds [5 x i32], [5 x i32]* %590, i64 4
  %592 = getelementptr inbounds [5 x i32], [5 x i32]* %591, i64 0, i64 2
  %593 = load i32, i32* %592, align 4
  %594 = mul nsw i32 %593, -117
  %595 = add nsw i32 %589, %594
  %596 = load [5 x i32]*, [5 x i32]** %3, align 8
  %597 = getelementptr inbounds [5 x i32], [5 x i32]* %596, i64 4
  %598 = getelementptr inbounds [5 x i32], [5 x i32]* %597, i64 0, i64 3
  %599 = load i32, i32* %598, align 4
  %600 = mul nsw i32 %599, 95
  %601 = add nsw i32 %595, %600
  %602 = load [5 x i32]*, [5 x i32]** %3, align 8
  %603 = getelementptr inbounds [5 x i32], [5 x i32]* %602, i64 4
  %604 = getelementptr inbounds [5 x i32], [5 x i32]* %603, i64 0, i64 4
  %605 = load i32, i32* %604, align 4
  %606 = mul nsw i32 %605, 118
  %607 = add nsw i32 %601, %606
  %608 = call i32 @relu_reg(i32 %607)
  %609 = mul nsw i32 %608, -106
  %610 = add nsw i32 %458, %609
  %611 = load [5 x i32]*, [5 x i32]** %3, align 8
  %612 = getelementptr inbounds [5 x i32], [5 x i32]* %611, i64 0
  %613 = getelementptr inbounds [5 x i32], [5 x i32]* %612, i64 0, i64 0
  %614 = load i32, i32* %613, align 4
  %615 = mul nsw i32 %614, 8
  %616 = load [5 x i32]*, [5 x i32]** %3, align 8
  %617 = getelementptr inbounds [5 x i32], [5 x i32]* %616, i64 0
  %618 = getelementptr inbounds [5 x i32], [5 x i32]* %617, i64 0, i64 1
  %619 = load i32, i32* %618, align 4
  %620 = mul nsw i32 %619, 82
  %621 = add nsw i32 %615, %620
  %622 = load [5 x i32]*, [5 x i32]** %3, align 8
  %623 = getelementptr inbounds [5 x i32], [5 x i32]* %622, i64 0
  %624 = getelementptr inbounds [5 x i32], [5 x i32]* %623, i64 0, i64 2
  %625 = load i32, i32* %624, align 4
  %626 = mul nsw i32 %625, -104
  %627 = add nsw i32 %621, %626
  %628 = load [5 x i32]*, [5 x i32]** %3, align 8
  %629 = getelementptr inbounds [5 x i32], [5 x i32]* %628, i64 0
  %630 = getelementptr inbounds [5 x i32], [5 x i32]* %629, i64 0, i64 3
  %631 = load i32, i32* %630, align 4
  %632 = mul nsw i32 %631, 101
  %633 = add nsw i32 %627, %632
  %634 = load [5 x i32]*, [5 x i32]** %3, align 8
  %635 = getelementptr inbounds [5 x i32], [5 x i32]* %634, i64 0
  %636 = getelementptr inbounds [5 x i32], [5 x i32]* %635, i64 0, i64 4
  %637 = load i32, i32* %636, align 4
  %638 = mul nsw i32 %637, -116
  %639 = add nsw i32 %633, %638
  %640 = load [5 x i32]*, [5 x i32]** %3, align 8
  %641 = getelementptr inbounds [5 x i32], [5 x i32]* %640, i64 1
  %642 = getelementptr inbounds [5 x i32], [5 x i32]* %641, i64 0, i64 0
  %643 = load i32, i32* %642, align 4
  %644 = mul nsw i32 %643, -63
  %645 = add nsw i32 %639, %644
  %646 = load [5 x i32]*, [5 x i32]** %3, align 8
  %647 = getelementptr inbounds [5 x i32], [5 x i32]* %646, i64 1
  %648 = getelementptr inbounds [5 x i32], [5 x i32]* %647, i64 0, i64 1
  %649 = load i32, i32* %648, align 4
  %650 = mul nsw i32 %649, -16
  %651 = add nsw i32 %645, %650
  %652 = load [5 x i32]*, [5 x i32]** %3, align 8
  %653 = getelementptr inbounds [5 x i32], [5 x i32]* %652, i64 1
  %654 = getelementptr inbounds [5 x i32], [5 x i32]* %653, i64 0, i64 2
  %655 = load i32, i32* %654, align 4
  %656 = mul nsw i32 %655, -70
  %657 = add nsw i32 %651, %656
  %658 = load [5 x i32]*, [5 x i32]** %3, align 8
  %659 = getelementptr inbounds [5 x i32], [5 x i32]* %658, i64 1
  %660 = getelementptr inbounds [5 x i32], [5 x i32]* %659, i64 0, i64 3
  %661 = load i32, i32* %660, align 4
  %662 = mul nsw i32 %661, 125
  %663 = add nsw i32 %657, %662
  %664 = load [5 x i32]*, [5 x i32]** %3, align 8
  %665 = getelementptr inbounds [5 x i32], [5 x i32]* %664, i64 1
  %666 = getelementptr inbounds [5 x i32], [5 x i32]* %665, i64 0, i64 4
  %667 = load i32, i32* %666, align 4
  %668 = mul nsw i32 %667, 75
  %669 = add nsw i32 %663, %668
  %670 = load [5 x i32]*, [5 x i32]** %3, align 8
  %671 = getelementptr inbounds [5 x i32], [5 x i32]* %670, i64 2
  %672 = getelementptr inbounds [5 x i32], [5 x i32]* %671, i64 0, i64 0
  %673 = load i32, i32* %672, align 4
  %674 = mul nsw i32 %673, 66
  %675 = add nsw i32 %669, %674
  %676 = load [5 x i32]*, [5 x i32]** %3, align 8
  %677 = getelementptr inbounds [5 x i32], [5 x i32]* %676, i64 2
  %678 = getelementptr inbounds [5 x i32], [5 x i32]* %677, i64 0, i64 1
  %679 = load i32, i32* %678, align 4
  %680 = mul nsw i32 %679, -96
  %681 = add nsw i32 %675, %680
  %682 = load [5 x i32]*, [5 x i32]** %3, align 8
  %683 = getelementptr inbounds [5 x i32], [5 x i32]* %682, i64 2
  %684 = getelementptr inbounds [5 x i32], [5 x i32]* %683, i64 0, i64 2
  %685 = load i32, i32* %684, align 4
  %686 = mul nsw i32 %685, -101
  %687 = add nsw i32 %681, %686
  %688 = load [5 x i32]*, [5 x i32]** %3, align 8
  %689 = getelementptr inbounds [5 x i32], [5 x i32]* %688, i64 2
  %690 = getelementptr inbounds [5 x i32], [5 x i32]* %689, i64 0, i64 3
  %691 = load i32, i32* %690, align 4
  %692 = mul nsw i32 %691, -114
  %693 = add nsw i32 %687, %692
  %694 = load [5 x i32]*, [5 x i32]** %3, align 8
  %695 = getelementptr inbounds [5 x i32], [5 x i32]* %694, i64 2
  %696 = getelementptr inbounds [5 x i32], [5 x i32]* %695, i64 0, i64 4
  %697 = load i32, i32* %696, align 4
  %698 = mul nsw i32 %697, 59
  %699 = add nsw i32 %693, %698
  %700 = load [5 x i32]*, [5 x i32]** %3, align 8
  %701 = getelementptr inbounds [5 x i32], [5 x i32]* %700, i64 3
  %702 = getelementptr inbounds [5 x i32], [5 x i32]* %701, i64 0, i64 0
  %703 = load i32, i32* %702, align 4
  %704 = mul nsw i32 %703, 12
  %705 = add nsw i32 %699, %704
  %706 = load [5 x i32]*, [5 x i32]** %3, align 8
  %707 = getelementptr inbounds [5 x i32], [5 x i32]* %706, i64 3
  %708 = getelementptr inbounds [5 x i32], [5 x i32]* %707, i64 0, i64 1
  %709 = load i32, i32* %708, align 4
  %710 = mul nsw i32 %709, 5
  %711 = add nsw i32 %705, %710
  %712 = load [5 x i32]*, [5 x i32]** %3, align 8
  %713 = getelementptr inbounds [5 x i32], [5 x i32]* %712, i64 3
  %714 = getelementptr inbounds [5 x i32], [5 x i32]* %713, i64 0, i64 2
  %715 = load i32, i32* %714, align 4
  %716 = mul nsw i32 %715, -95
  %717 = add nsw i32 %711, %716
  %718 = load [5 x i32]*, [5 x i32]** %3, align 8
  %719 = getelementptr inbounds [5 x i32], [5 x i32]* %718, i64 3
  %720 = getelementptr inbounds [5 x i32], [5 x i32]* %719, i64 0, i64 3
  %721 = load i32, i32* %720, align 4
  %722 = mul nsw i32 %721, 116
  %723 = add nsw i32 %717, %722
  %724 = load [5 x i32]*, [5 x i32]** %3, align 8
  %725 = getelementptr inbounds [5 x i32], [5 x i32]* %724, i64 3
  %726 = getelementptr inbounds [5 x i32], [5 x i32]* %725, i64 0, i64 4
  %727 = load i32, i32* %726, align 4
  %728 = mul nsw i32 %727, -93
  %729 = add nsw i32 %723, %728
  %730 = load [5 x i32]*, [5 x i32]** %3, align 8
  %731 = getelementptr inbounds [5 x i32], [5 x i32]* %730, i64 4
  %732 = getelementptr inbounds [5 x i32], [5 x i32]* %731, i64 0, i64 0
  %733 = load i32, i32* %732, align 4
  %734 = mul nsw i32 %733, 15
  %735 = add nsw i32 %729, %734
  %736 = load [5 x i32]*, [5 x i32]** %3, align 8
  %737 = getelementptr inbounds [5 x i32], [5 x i32]* %736, i64 4
  %738 = getelementptr inbounds [5 x i32], [5 x i32]* %737, i64 0, i64 1
  %739 = load i32, i32* %738, align 4
  %740 = mul nsw i32 %739, 79
  %741 = add nsw i32 %735, %740
  %742 = load [5 x i32]*, [5 x i32]** %3, align 8
  %743 = getelementptr inbounds [5 x i32], [5 x i32]* %742, i64 4
  %744 = getelementptr inbounds [5 x i32], [5 x i32]* %743, i64 0, i64 2
  %745 = load i32, i32* %744, align 4
  %746 = mul nsw i32 %745, 3
  %747 = add nsw i32 %741, %746
  %748 = load [5 x i32]*, [5 x i32]** %3, align 8
  %749 = getelementptr inbounds [5 x i32], [5 x i32]* %748, i64 4
  %750 = getelementptr inbounds [5 x i32], [5 x i32]* %749, i64 0, i64 3
  %751 = load i32, i32* %750, align 4
  %752 = mul nsw i32 %751, 49
  %753 = add nsw i32 %747, %752
  %754 = load [5 x i32]*, [5 x i32]** %3, align 8
  %755 = getelementptr inbounds [5 x i32], [5 x i32]* %754, i64 4
  %756 = getelementptr inbounds [5 x i32], [5 x i32]* %755, i64 0, i64 4
  %757 = load i32, i32* %756, align 4
  %758 = mul nsw i32 %757, -124
  %759 = add nsw i32 %753, %758
  %760 = call i32 @relu_reg(i32 %759)
  %761 = mul nsw i32 %760, -3
  %762 = add nsw i32 %610, %761
  %763 = load [5 x i32]*, [5 x i32]** %3, align 8
  %764 = getelementptr inbounds [5 x i32], [5 x i32]* %763, i64 0
  %765 = getelementptr inbounds [5 x i32], [5 x i32]* %764, i64 0, i64 0
  %766 = load i32, i32* %765, align 4
  %767 = mul nsw i32 %766, 81
  %768 = load [5 x i32]*, [5 x i32]** %3, align 8
  %769 = getelementptr inbounds [5 x i32], [5 x i32]* %768, i64 0
  %770 = getelementptr inbounds [5 x i32], [5 x i32]* %769, i64 0, i64 1
  %771 = load i32, i32* %770, align 4
  %772 = mul nsw i32 %771, 68
  %773 = add nsw i32 %767, %772
  %774 = load [5 x i32]*, [5 x i32]** %3, align 8
  %775 = getelementptr inbounds [5 x i32], [5 x i32]* %774, i64 0
  %776 = getelementptr inbounds [5 x i32], [5 x i32]* %775, i64 0, i64 2
  %777 = load i32, i32* %776, align 4
  %778 = mul nsw i32 %777, -102
  %779 = add nsw i32 %773, %778
  %780 = load [5 x i32]*, [5 x i32]** %3, align 8
  %781 = getelementptr inbounds [5 x i32], [5 x i32]* %780, i64 0
  %782 = getelementptr inbounds [5 x i32], [5 x i32]* %781, i64 0, i64 3
  %783 = load i32, i32* %782, align 4
  %784 = mul nsw i32 %783, -74
  %785 = add nsw i32 %779, %784
  %786 = load [5 x i32]*, [5 x i32]** %3, align 8
  %787 = getelementptr inbounds [5 x i32], [5 x i32]* %786, i64 0
  %788 = getelementptr inbounds [5 x i32], [5 x i32]* %787, i64 0, i64 4
  %789 = load i32, i32* %788, align 4
  %790 = mul nsw i32 %789, 121
  %791 = add nsw i32 %785, %790
  %792 = load [5 x i32]*, [5 x i32]** %3, align 8
  %793 = getelementptr inbounds [5 x i32], [5 x i32]* %792, i64 1
  %794 = getelementptr inbounds [5 x i32], [5 x i32]* %793, i64 0, i64 0
  %795 = load i32, i32* %794, align 4
  %796 = mul nsw i32 %795, -15
  %797 = add nsw i32 %791, %796
  %798 = load [5 x i32]*, [5 x i32]** %3, align 8
  %799 = getelementptr inbounds [5 x i32], [5 x i32]* %798, i64 1
  %800 = getelementptr inbounds [5 x i32], [5 x i32]* %799, i64 0, i64 1
  %801 = load i32, i32* %800, align 4
  %802 = mul nsw i32 %801, 55
  %803 = add nsw i32 %797, %802
  %804 = load [5 x i32]*, [5 x i32]** %3, align 8
  %805 = getelementptr inbounds [5 x i32], [5 x i32]* %804, i64 1
  %806 = getelementptr inbounds [5 x i32], [5 x i32]* %805, i64 0, i64 2
  %807 = load i32, i32* %806, align 4
  %808 = mul nsw i32 %807, 101
  %809 = add nsw i32 %803, %808
  %810 = load [5 x i32]*, [5 x i32]** %3, align 8
  %811 = getelementptr inbounds [5 x i32], [5 x i32]* %810, i64 1
  %812 = getelementptr inbounds [5 x i32], [5 x i32]* %811, i64 0, i64 3
  %813 = load i32, i32* %812, align 4
  %814 = mul nsw i32 %813, -13
  %815 = add nsw i32 %809, %814
  %816 = load [5 x i32]*, [5 x i32]** %3, align 8
  %817 = getelementptr inbounds [5 x i32], [5 x i32]* %816, i64 1
  %818 = getelementptr inbounds [5 x i32], [5 x i32]* %817, i64 0, i64 4
  %819 = load i32, i32* %818, align 4
  %820 = mul nsw i32 %819, -62
  %821 = add nsw i32 %815, %820
  %822 = load [5 x i32]*, [5 x i32]** %3, align 8
  %823 = getelementptr inbounds [5 x i32], [5 x i32]* %822, i64 2
  %824 = getelementptr inbounds [5 x i32], [5 x i32]* %823, i64 0, i64 0
  %825 = load i32, i32* %824, align 4
  %826 = mul nsw i32 %825, 64
  %827 = add nsw i32 %821, %826
  %828 = load [5 x i32]*, [5 x i32]** %3, align 8
  %829 = getelementptr inbounds [5 x i32], [5 x i32]* %828, i64 2
  %830 = getelementptr inbounds [5 x i32], [5 x i32]* %829, i64 0, i64 1
  %831 = load i32, i32* %830, align 4
  %832 = mul nsw i32 %831, 114
  %833 = add nsw i32 %827, %832
  %834 = load [5 x i32]*, [5 x i32]** %3, align 8
  %835 = getelementptr inbounds [5 x i32], [5 x i32]* %834, i64 2
  %836 = getelementptr inbounds [5 x i32], [5 x i32]* %835, i64 0, i64 2
  %837 = load i32, i32* %836, align 4
  %838 = mul nsw i32 %837, 38
  %839 = add nsw i32 %833, %838
  %840 = load [5 x i32]*, [5 x i32]** %3, align 8
  %841 = getelementptr inbounds [5 x i32], [5 x i32]* %840, i64 2
  %842 = getelementptr inbounds [5 x i32], [5 x i32]* %841, i64 0, i64 3
  %843 = load i32, i32* %842, align 4
  %844 = mul nsw i32 %843, -21
  %845 = add nsw i32 %839, %844
  %846 = load [5 x i32]*, [5 x i32]** %3, align 8
  %847 = getelementptr inbounds [5 x i32], [5 x i32]* %846, i64 2
  %848 = getelementptr inbounds [5 x i32], [5 x i32]* %847, i64 0, i64 4
  %849 = load i32, i32* %848, align 4
  %850 = mul nsw i32 %849, 112
  %851 = add nsw i32 %845, %850
  %852 = load [5 x i32]*, [5 x i32]** %3, align 8
  %853 = getelementptr inbounds [5 x i32], [5 x i32]* %852, i64 3
  %854 = getelementptr inbounds [5 x i32], [5 x i32]* %853, i64 0, i64 0
  %855 = load i32, i32* %854, align 4
  %856 = mul nsw i32 %855, 114
  %857 = add nsw i32 %851, %856
  %858 = load [5 x i32]*, [5 x i32]** %3, align 8
  %859 = getelementptr inbounds [5 x i32], [5 x i32]* %858, i64 3
  %860 = getelementptr inbounds [5 x i32], [5 x i32]* %859, i64 0, i64 1
  %861 = load i32, i32* %860, align 4
  %862 = mul nsw i32 %861, 112
  %863 = add nsw i32 %857, %862
  %864 = load [5 x i32]*, [5 x i32]** %3, align 8
  %865 = getelementptr inbounds [5 x i32], [5 x i32]* %864, i64 3
  %866 = getelementptr inbounds [5 x i32], [5 x i32]* %865, i64 0, i64 2
  %867 = load i32, i32* %866, align 4
  %868 = mul nsw i32 %867, -10
  %869 = add nsw i32 %863, %868
  %870 = load [5 x i32]*, [5 x i32]** %3, align 8
  %871 = getelementptr inbounds [5 x i32], [5 x i32]* %870, i64 3
  %872 = getelementptr inbounds [5 x i32], [5 x i32]* %871, i64 0, i64 3
  %873 = load i32, i32* %872, align 4
  %874 = mul nsw i32 %873, -16
  %875 = add nsw i32 %869, %874
  %876 = load [5 x i32]*, [5 x i32]** %3, align 8
  %877 = getelementptr inbounds [5 x i32], [5 x i32]* %876, i64 3
  %878 = getelementptr inbounds [5 x i32], [5 x i32]* %877, i64 0, i64 4
  %879 = load i32, i32* %878, align 4
  %880 = mul nsw i32 %879, -50
  %881 = add nsw i32 %875, %880
  %882 = load [5 x i32]*, [5 x i32]** %3, align 8
  %883 = getelementptr inbounds [5 x i32], [5 x i32]* %882, i64 4
  %884 = getelementptr inbounds [5 x i32], [5 x i32]* %883, i64 0, i64 0
  %885 = load i32, i32* %884, align 4
  %886 = mul nsw i32 %885, -112
  %887 = add nsw i32 %881, %886
  %888 = load [5 x i32]*, [5 x i32]** %3, align 8
  %889 = getelementptr inbounds [5 x i32], [5 x i32]* %888, i64 4
  %890 = getelementptr inbounds [5 x i32], [5 x i32]* %889, i64 0, i64 1
  %891 = load i32, i32* %890, align 4
  %892 = mul nsw i32 %891, -116
  %893 = add nsw i32 %887, %892
  %894 = load [5 x i32]*, [5 x i32]** %3, align 8
  %895 = getelementptr inbounds [5 x i32], [5 x i32]* %894, i64 4
  %896 = getelementptr inbounds [5 x i32], [5 x i32]* %895, i64 0, i64 2
  %897 = load i32, i32* %896, align 4
  %898 = mul nsw i32 %897, -54
  %899 = add nsw i32 %893, %898
  %900 = load [5 x i32]*, [5 x i32]** %3, align 8
  %901 = getelementptr inbounds [5 x i32], [5 x i32]* %900, i64 4
  %902 = getelementptr inbounds [5 x i32], [5 x i32]* %901, i64 0, i64 3
  %903 = load i32, i32* %902, align 4
  %904 = mul nsw i32 %903, 82
  %905 = add nsw i32 %899, %904
  %906 = load [5 x i32]*, [5 x i32]** %3, align 8
  %907 = getelementptr inbounds [5 x i32], [5 x i32]* %906, i64 4
  %908 = getelementptr inbounds [5 x i32], [5 x i32]* %907, i64 0, i64 4
  %909 = load i32, i32* %908, align 4
  %910 = mul nsw i32 %909, -72
  %911 = add nsw i32 %905, %910
  %912 = call i32 @relu_reg(i32 %911)
  %913 = mul nsw i32 %912, 32
  %914 = add nsw i32 %762, %913
  %915 = load [5 x i32]*, [5 x i32]** %3, align 8
  %916 = getelementptr inbounds [5 x i32], [5 x i32]* %915, i64 0
  %917 = getelementptr inbounds [5 x i32], [5 x i32]* %916, i64 0, i64 0
  %918 = load i32, i32* %917, align 4
  %919 = mul nsw i32 %918, 15
  %920 = load [5 x i32]*, [5 x i32]** %3, align 8
  %921 = getelementptr inbounds [5 x i32], [5 x i32]* %920, i64 0
  %922 = getelementptr inbounds [5 x i32], [5 x i32]* %921, i64 0, i64 1
  %923 = load i32, i32* %922, align 4
  %924 = mul nsw i32 %923, -77
  %925 = add nsw i32 %919, %924
  %926 = load [5 x i32]*, [5 x i32]** %3, align 8
  %927 = getelementptr inbounds [5 x i32], [5 x i32]* %926, i64 0
  %928 = getelementptr inbounds [5 x i32], [5 x i32]* %927, i64 0, i64 2
  %929 = load i32, i32* %928, align 4
  %930 = mul nsw i32 %929, 66
  %931 = add nsw i32 %925, %930
  %932 = load [5 x i32]*, [5 x i32]** %3, align 8
  %933 = getelementptr inbounds [5 x i32], [5 x i32]* %932, i64 0
  %934 = getelementptr inbounds [5 x i32], [5 x i32]* %933, i64 0, i64 3
  %935 = load i32, i32* %934, align 4
  %936 = mul nsw i32 %935, -90
  %937 = add nsw i32 %931, %936
  %938 = load [5 x i32]*, [5 x i32]** %3, align 8
  %939 = getelementptr inbounds [5 x i32], [5 x i32]* %938, i64 0
  %940 = getelementptr inbounds [5 x i32], [5 x i32]* %939, i64 0, i64 4
  %941 = load i32, i32* %940, align 4
  %942 = mul nsw i32 %941, -6
  %943 = add nsw i32 %937, %942
  %944 = load [5 x i32]*, [5 x i32]** %3, align 8
  %945 = getelementptr inbounds [5 x i32], [5 x i32]* %944, i64 1
  %946 = getelementptr inbounds [5 x i32], [5 x i32]* %945, i64 0, i64 0
  %947 = load i32, i32* %946, align 4
  %948 = mul nsw i32 %947, -30
  %949 = add nsw i32 %943, %948
  %950 = load [5 x i32]*, [5 x i32]** %3, align 8
  %951 = getelementptr inbounds [5 x i32], [5 x i32]* %950, i64 1
  %952 = getelementptr inbounds [5 x i32], [5 x i32]* %951, i64 0, i64 1
  %953 = load i32, i32* %952, align 4
  %954 = mul nsw i32 %953, -8
  %955 = add nsw i32 %949, %954
  %956 = load [5 x i32]*, [5 x i32]** %3, align 8
  %957 = getelementptr inbounds [5 x i32], [5 x i32]* %956, i64 1
  %958 = getelementptr inbounds [5 x i32], [5 x i32]* %957, i64 0, i64 2
  %959 = load i32, i32* %958, align 4
  %960 = mul nsw i32 %959, 81
  %961 = add nsw i32 %955, %960
  %962 = load [5 x i32]*, [5 x i32]** %3, align 8
  %963 = getelementptr inbounds [5 x i32], [5 x i32]* %962, i64 1
  %964 = getelementptr inbounds [5 x i32], [5 x i32]* %963, i64 0, i64 3
  %965 = load i32, i32* %964, align 4
  %966 = mul nsw i32 %965, 2
  %967 = add nsw i32 %961, %966
  %968 = load [5 x i32]*, [5 x i32]** %3, align 8
  %969 = getelementptr inbounds [5 x i32], [5 x i32]* %968, i64 1
  %970 = getelementptr inbounds [5 x i32], [5 x i32]* %969, i64 0, i64 4
  %971 = load i32, i32* %970, align 4
  %972 = mul nsw i32 %971, -110
  %973 = add nsw i32 %967, %972
  %974 = load [5 x i32]*, [5 x i32]** %3, align 8
  %975 = getelementptr inbounds [5 x i32], [5 x i32]* %974, i64 2
  %976 = getelementptr inbounds [5 x i32], [5 x i32]* %975, i64 0, i64 0
  %977 = load i32, i32* %976, align 4
  %978 = mul nsw i32 %977, -95
  %979 = add nsw i32 %973, %978
  %980 = load [5 x i32]*, [5 x i32]** %3, align 8
  %981 = getelementptr inbounds [5 x i32], [5 x i32]* %980, i64 2
  %982 = getelementptr inbounds [5 x i32], [5 x i32]* %981, i64 0, i64 1
  %983 = load i32, i32* %982, align 4
  %984 = mul nsw i32 %983, 59
  %985 = add nsw i32 %979, %984
  %986 = load [5 x i32]*, [5 x i32]** %3, align 8
  %987 = getelementptr inbounds [5 x i32], [5 x i32]* %986, i64 2
  %988 = getelementptr inbounds [5 x i32], [5 x i32]* %987, i64 0, i64 2
  %989 = load i32, i32* %988, align 4
  %990 = mul nsw i32 %989, 52
  %991 = add nsw i32 %985, %990
  %992 = load [5 x i32]*, [5 x i32]** %3, align 8
  %993 = getelementptr inbounds [5 x i32], [5 x i32]* %992, i64 2
  %994 = getelementptr inbounds [5 x i32], [5 x i32]* %993, i64 0, i64 3
  %995 = load i32, i32* %994, align 4
  %996 = mul nsw i32 %995, 15
  %997 = add nsw i32 %991, %996
  %998 = load [5 x i32]*, [5 x i32]** %3, align 8
  %999 = getelementptr inbounds [5 x i32], [5 x i32]* %998, i64 2
  %1000 = getelementptr inbounds [5 x i32], [5 x i32]* %999, i64 0, i64 4
  %1001 = load i32, i32* %1000, align 4
  %1002 = mul nsw i32 %1001, 55
  %1003 = add nsw i32 %997, %1002
  %1004 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1005 = getelementptr inbounds [5 x i32], [5 x i32]* %1004, i64 3
  %1006 = getelementptr inbounds [5 x i32], [5 x i32]* %1005, i64 0, i64 0
  %1007 = load i32, i32* %1006, align 4
  %1008 = mul nsw i32 %1007, -33
  %1009 = add nsw i32 %1003, %1008
  %1010 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1011 = getelementptr inbounds [5 x i32], [5 x i32]* %1010, i64 3
  %1012 = getelementptr inbounds [5 x i32], [5 x i32]* %1011, i64 0, i64 1
  %1013 = load i32, i32* %1012, align 4
  %1014 = mul nsw i32 %1013, 14
  %1015 = add nsw i32 %1009, %1014
  %1016 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1017 = getelementptr inbounds [5 x i32], [5 x i32]* %1016, i64 3
  %1018 = getelementptr inbounds [5 x i32], [5 x i32]* %1017, i64 0, i64 2
  %1019 = load i32, i32* %1018, align 4
  %1020 = mul nsw i32 %1019, 58
  %1021 = add nsw i32 %1015, %1020
  %1022 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1023 = getelementptr inbounds [5 x i32], [5 x i32]* %1022, i64 3
  %1024 = getelementptr inbounds [5 x i32], [5 x i32]* %1023, i64 0, i64 3
  %1025 = load i32, i32* %1024, align 4
  %1026 = mul nsw i32 %1025, 67
  %1027 = add nsw i32 %1021, %1026
  %1028 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1029 = getelementptr inbounds [5 x i32], [5 x i32]* %1028, i64 3
  %1030 = getelementptr inbounds [5 x i32], [5 x i32]* %1029, i64 0, i64 4
  %1031 = load i32, i32* %1030, align 4
  %1032 = mul nsw i32 %1031, 86
  %1033 = add nsw i32 %1027, %1032
  %1034 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1035 = getelementptr inbounds [5 x i32], [5 x i32]* %1034, i64 4
  %1036 = getelementptr inbounds [5 x i32], [5 x i32]* %1035, i64 0, i64 0
  %1037 = load i32, i32* %1036, align 4
  %1038 = mul nsw i32 %1037, -79
  %1039 = add nsw i32 %1033, %1038
  %1040 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1041 = getelementptr inbounds [5 x i32], [5 x i32]* %1040, i64 4
  %1042 = getelementptr inbounds [5 x i32], [5 x i32]* %1041, i64 0, i64 1
  %1043 = load i32, i32* %1042, align 4
  %1044 = mul nsw i32 %1043, 48
  %1045 = add nsw i32 %1039, %1044
  %1046 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1047 = getelementptr inbounds [5 x i32], [5 x i32]* %1046, i64 4
  %1048 = getelementptr inbounds [5 x i32], [5 x i32]* %1047, i64 0, i64 2
  %1049 = load i32, i32* %1048, align 4
  %1050 = mul nsw i32 %1049, -13
  %1051 = add nsw i32 %1045, %1050
  %1052 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1053 = getelementptr inbounds [5 x i32], [5 x i32]* %1052, i64 4
  %1054 = getelementptr inbounds [5 x i32], [5 x i32]* %1053, i64 0, i64 3
  %1055 = load i32, i32* %1054, align 4
  %1056 = mul nsw i32 %1055, -15
  %1057 = add nsw i32 %1051, %1056
  %1058 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1059 = getelementptr inbounds [5 x i32], [5 x i32]* %1058, i64 4
  %1060 = getelementptr inbounds [5 x i32], [5 x i32]* %1059, i64 0, i64 4
  %1061 = load i32, i32* %1060, align 4
  %1062 = mul nsw i32 %1061, 66
  %1063 = add nsw i32 %1057, %1062
  %1064 = call i32 @relu_reg(i32 %1063)
  %1065 = mul nsw i32 %1064, -95
  %1066 = add nsw i32 %914, %1065
  %1067 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1068 = getelementptr inbounds [5 x i32], [5 x i32]* %1067, i64 0
  %1069 = getelementptr inbounds [5 x i32], [5 x i32]* %1068, i64 0, i64 0
  %1070 = load i32, i32* %1069, align 4
  %1071 = mul nsw i32 %1070, 33
  %1072 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1073 = getelementptr inbounds [5 x i32], [5 x i32]* %1072, i64 0
  %1074 = getelementptr inbounds [5 x i32], [5 x i32]* %1073, i64 0, i64 1
  %1075 = load i32, i32* %1074, align 4
  %1076 = mul nsw i32 %1075, 82
  %1077 = add nsw i32 %1071, %1076
  %1078 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1079 = getelementptr inbounds [5 x i32], [5 x i32]* %1078, i64 0
  %1080 = getelementptr inbounds [5 x i32], [5 x i32]* %1079, i64 0, i64 2
  %1081 = load i32, i32* %1080, align 4
  %1082 = mul nsw i32 %1081, 67
  %1083 = add nsw i32 %1077, %1082
  %1084 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1085 = getelementptr inbounds [5 x i32], [5 x i32]* %1084, i64 0
  %1086 = getelementptr inbounds [5 x i32], [5 x i32]* %1085, i64 0, i64 3
  %1087 = load i32, i32* %1086, align 4
  %1088 = mul nsw i32 %1087, 30
  %1089 = add nsw i32 %1083, %1088
  %1090 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1091 = getelementptr inbounds [5 x i32], [5 x i32]* %1090, i64 0
  %1092 = getelementptr inbounds [5 x i32], [5 x i32]* %1091, i64 0, i64 4
  %1093 = load i32, i32* %1092, align 4
  %1094 = mul nsw i32 %1093, -2
  %1095 = add nsw i32 %1089, %1094
  %1096 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1097 = getelementptr inbounds [5 x i32], [5 x i32]* %1096, i64 1
  %1098 = getelementptr inbounds [5 x i32], [5 x i32]* %1097, i64 0, i64 0
  %1099 = load i32, i32* %1098, align 4
  %1100 = mul nsw i32 %1099, 65
  %1101 = add nsw i32 %1095, %1100
  %1102 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1103 = getelementptr inbounds [5 x i32], [5 x i32]* %1102, i64 1
  %1104 = getelementptr inbounds [5 x i32], [5 x i32]* %1103, i64 0, i64 1
  %1105 = load i32, i32* %1104, align 4
  %1106 = mul nsw i32 %1105, 120
  %1107 = add nsw i32 %1101, %1106
  %1108 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1109 = getelementptr inbounds [5 x i32], [5 x i32]* %1108, i64 1
  %1110 = getelementptr inbounds [5 x i32], [5 x i32]* %1109, i64 0, i64 2
  %1111 = load i32, i32* %1110, align 4
  %1112 = mul nsw i32 %1111, -13
  %1113 = add nsw i32 %1107, %1112
  %1114 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1115 = getelementptr inbounds [5 x i32], [5 x i32]* %1114, i64 1
  %1116 = getelementptr inbounds [5 x i32], [5 x i32]* %1115, i64 0, i64 3
  %1117 = load i32, i32* %1116, align 4
  %1118 = mul nsw i32 %1117, 18
  %1119 = add nsw i32 %1113, %1118
  %1120 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1121 = getelementptr inbounds [5 x i32], [5 x i32]* %1120, i64 1
  %1122 = getelementptr inbounds [5 x i32], [5 x i32]* %1121, i64 0, i64 4
  %1123 = load i32, i32* %1122, align 4
  %1124 = mul nsw i32 %1123, 5
  %1125 = add nsw i32 %1119, %1124
  %1126 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1127 = getelementptr inbounds [5 x i32], [5 x i32]* %1126, i64 2
  %1128 = getelementptr inbounds [5 x i32], [5 x i32]* %1127, i64 0, i64 0
  %1129 = load i32, i32* %1128, align 4
  %1130 = mul nsw i32 %1129, 104
  %1131 = add nsw i32 %1125, %1130
  %1132 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1133 = getelementptr inbounds [5 x i32], [5 x i32]* %1132, i64 2
  %1134 = getelementptr inbounds [5 x i32], [5 x i32]* %1133, i64 0, i64 1
  %1135 = load i32, i32* %1134, align 4
  %1136 = mul nsw i32 %1135, -119
  %1137 = add nsw i32 %1131, %1136
  %1138 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1139 = getelementptr inbounds [5 x i32], [5 x i32]* %1138, i64 2
  %1140 = getelementptr inbounds [5 x i32], [5 x i32]* %1139, i64 0, i64 2
  %1141 = load i32, i32* %1140, align 4
  %1142 = mul nsw i32 %1141, -7
  %1143 = add nsw i32 %1137, %1142
  %1144 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1145 = getelementptr inbounds [5 x i32], [5 x i32]* %1144, i64 2
  %1146 = getelementptr inbounds [5 x i32], [5 x i32]* %1145, i64 0, i64 3
  %1147 = load i32, i32* %1146, align 4
  %1148 = mul nsw i32 %1147, 71
  %1149 = add nsw i32 %1143, %1148
  %1150 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1151 = getelementptr inbounds [5 x i32], [5 x i32]* %1150, i64 2
  %1152 = getelementptr inbounds [5 x i32], [5 x i32]* %1151, i64 0, i64 4
  %1153 = load i32, i32* %1152, align 4
  %1154 = mul nsw i32 %1153, 107
  %1155 = add nsw i32 %1149, %1154
  %1156 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1157 = getelementptr inbounds [5 x i32], [5 x i32]* %1156, i64 3
  %1158 = getelementptr inbounds [5 x i32], [5 x i32]* %1157, i64 0, i64 0
  %1159 = load i32, i32* %1158, align 4
  %1160 = mul nsw i32 %1159, 24
  %1161 = add nsw i32 %1155, %1160
  %1162 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1163 = getelementptr inbounds [5 x i32], [5 x i32]* %1162, i64 3
  %1164 = getelementptr inbounds [5 x i32], [5 x i32]* %1163, i64 0, i64 1
  %1165 = load i32, i32* %1164, align 4
  %1166 = mul nsw i32 %1165, 82
  %1167 = add nsw i32 %1161, %1166
  %1168 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1169 = getelementptr inbounds [5 x i32], [5 x i32]* %1168, i64 3
  %1170 = getelementptr inbounds [5 x i32], [5 x i32]* %1169, i64 0, i64 2
  %1171 = load i32, i32* %1170, align 4
  %1172 = mul nsw i32 %1171, -96
  %1173 = add nsw i32 %1167, %1172
  %1174 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1175 = getelementptr inbounds [5 x i32], [5 x i32]* %1174, i64 3
  %1176 = getelementptr inbounds [5 x i32], [5 x i32]* %1175, i64 0, i64 3
  %1177 = load i32, i32* %1176, align 4
  %1178 = mul nsw i32 %1177, -104
  %1179 = add nsw i32 %1173, %1178
  %1180 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1181 = getelementptr inbounds [5 x i32], [5 x i32]* %1180, i64 3
  %1182 = getelementptr inbounds [5 x i32], [5 x i32]* %1181, i64 0, i64 4
  %1183 = load i32, i32* %1182, align 4
  %1184 = mul nsw i32 %1183, -121
  %1185 = add nsw i32 %1179, %1184
  %1186 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1187 = getelementptr inbounds [5 x i32], [5 x i32]* %1186, i64 4
  %1188 = getelementptr inbounds [5 x i32], [5 x i32]* %1187, i64 0, i64 0
  %1189 = load i32, i32* %1188, align 4
  %1190 = mul nsw i32 %1189, 65
  %1191 = add nsw i32 %1185, %1190
  %1192 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1193 = getelementptr inbounds [5 x i32], [5 x i32]* %1192, i64 4
  %1194 = getelementptr inbounds [5 x i32], [5 x i32]* %1193, i64 0, i64 1
  %1195 = load i32, i32* %1194, align 4
  %1196 = mul nsw i32 %1195, 97
  %1197 = add nsw i32 %1191, %1196
  %1198 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1199 = getelementptr inbounds [5 x i32], [5 x i32]* %1198, i64 4
  %1200 = getelementptr inbounds [5 x i32], [5 x i32]* %1199, i64 0, i64 2
  %1201 = load i32, i32* %1200, align 4
  %1202 = mul nsw i32 %1201, 83
  %1203 = add nsw i32 %1197, %1202
  %1204 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1205 = getelementptr inbounds [5 x i32], [5 x i32]* %1204, i64 4
  %1206 = getelementptr inbounds [5 x i32], [5 x i32]* %1205, i64 0, i64 3
  %1207 = load i32, i32* %1206, align 4
  %1208 = mul nsw i32 %1207, 46
  %1209 = add nsw i32 %1203, %1208
  %1210 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1211 = getelementptr inbounds [5 x i32], [5 x i32]* %1210, i64 4
  %1212 = getelementptr inbounds [5 x i32], [5 x i32]* %1211, i64 0, i64 4
  %1213 = load i32, i32* %1212, align 4
  %1214 = mul nsw i32 %1213, -84
  %1215 = add nsw i32 %1209, %1214
  %1216 = call i32 @relu_reg(i32 %1215)
  %1217 = mul nsw i32 %1216, -50
  %1218 = add nsw i32 %1066, %1217
  %1219 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1220 = getelementptr inbounds [5 x i32], [5 x i32]* %1219, i64 0
  %1221 = getelementptr inbounds [5 x i32], [5 x i32]* %1220, i64 0, i64 0
  %1222 = load i32, i32* %1221, align 4
  %1223 = mul nsw i32 %1222, -29
  %1224 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1225 = getelementptr inbounds [5 x i32], [5 x i32]* %1224, i64 0
  %1226 = getelementptr inbounds [5 x i32], [5 x i32]* %1225, i64 0, i64 1
  %1227 = load i32, i32* %1226, align 4
  %1228 = mul nsw i32 %1227, 7
  %1229 = add nsw i32 %1223, %1228
  %1230 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1231 = getelementptr inbounds [5 x i32], [5 x i32]* %1230, i64 0
  %1232 = getelementptr inbounds [5 x i32], [5 x i32]* %1231, i64 0, i64 2
  %1233 = load i32, i32* %1232, align 4
  %1234 = mul nsw i32 %1233, -70
  %1235 = add nsw i32 %1229, %1234
  %1236 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1237 = getelementptr inbounds [5 x i32], [5 x i32]* %1236, i64 0
  %1238 = getelementptr inbounds [5 x i32], [5 x i32]* %1237, i64 0, i64 3
  %1239 = load i32, i32* %1238, align 4
  %1240 = mul nsw i32 %1239, 38
  %1241 = add nsw i32 %1235, %1240
  %1242 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1243 = getelementptr inbounds [5 x i32], [5 x i32]* %1242, i64 0
  %1244 = getelementptr inbounds [5 x i32], [5 x i32]* %1243, i64 0, i64 4
  %1245 = load i32, i32* %1244, align 4
  %1246 = mul nsw i32 %1245, -90
  %1247 = add nsw i32 %1241, %1246
  %1248 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1249 = getelementptr inbounds [5 x i32], [5 x i32]* %1248, i64 1
  %1250 = getelementptr inbounds [5 x i32], [5 x i32]* %1249, i64 0, i64 0
  %1251 = load i32, i32* %1250, align 4
  %1252 = mul nsw i32 %1251, -15
  %1253 = add nsw i32 %1247, %1252
  %1254 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1255 = getelementptr inbounds [5 x i32], [5 x i32]* %1254, i64 1
  %1256 = getelementptr inbounds [5 x i32], [5 x i32]* %1255, i64 0, i64 1
  %1257 = load i32, i32* %1256, align 4
  %1258 = mul nsw i32 %1257, -32
  %1259 = add nsw i32 %1253, %1258
  %1260 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1261 = getelementptr inbounds [5 x i32], [5 x i32]* %1260, i64 1
  %1262 = getelementptr inbounds [5 x i32], [5 x i32]* %1261, i64 0, i64 2
  %1263 = load i32, i32* %1262, align 4
  %1264 = mul nsw i32 %1263, 37
  %1265 = add nsw i32 %1259, %1264
  %1266 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1267 = getelementptr inbounds [5 x i32], [5 x i32]* %1266, i64 1
  %1268 = getelementptr inbounds [5 x i32], [5 x i32]* %1267, i64 0, i64 3
  %1269 = load i32, i32* %1268, align 4
  %1270 = mul nsw i32 %1269, 36
  %1271 = add nsw i32 %1265, %1270
  %1272 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1273 = getelementptr inbounds [5 x i32], [5 x i32]* %1272, i64 1
  %1274 = getelementptr inbounds [5 x i32], [5 x i32]* %1273, i64 0, i64 4
  %1275 = load i32, i32* %1274, align 4
  %1276 = mul nsw i32 %1275, -62
  %1277 = add nsw i32 %1271, %1276
  %1278 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1279 = getelementptr inbounds [5 x i32], [5 x i32]* %1278, i64 2
  %1280 = getelementptr inbounds [5 x i32], [5 x i32]* %1279, i64 0, i64 0
  %1281 = load i32, i32* %1280, align 4
  %1282 = mul nsw i32 %1281, -125
  %1283 = add nsw i32 %1277, %1282
  %1284 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1285 = getelementptr inbounds [5 x i32], [5 x i32]* %1284, i64 2
  %1286 = getelementptr inbounds [5 x i32], [5 x i32]* %1285, i64 0, i64 1
  %1287 = load i32, i32* %1286, align 4
  %1288 = mul nsw i32 %1287, -46
  %1289 = add nsw i32 %1283, %1288
  %1290 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1291 = getelementptr inbounds [5 x i32], [5 x i32]* %1290, i64 2
  %1292 = getelementptr inbounds [5 x i32], [5 x i32]* %1291, i64 0, i64 2
  %1293 = load i32, i32* %1292, align 4
  %1294 = mul nsw i32 %1293, -70
  %1295 = add nsw i32 %1289, %1294
  %1296 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1297 = getelementptr inbounds [5 x i32], [5 x i32]* %1296, i64 2
  %1298 = getelementptr inbounds [5 x i32], [5 x i32]* %1297, i64 0, i64 3
  %1299 = load i32, i32* %1298, align 4
  %1300 = mul nsw i32 %1299, 37
  %1301 = add nsw i32 %1295, %1300
  %1302 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1303 = getelementptr inbounds [5 x i32], [5 x i32]* %1302, i64 2
  %1304 = getelementptr inbounds [5 x i32], [5 x i32]* %1303, i64 0, i64 4
  %1305 = load i32, i32* %1304, align 4
  %1306 = mul nsw i32 %1305, -73
  %1307 = add nsw i32 %1301, %1306
  %1308 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1309 = getelementptr inbounds [5 x i32], [5 x i32]* %1308, i64 3
  %1310 = getelementptr inbounds [5 x i32], [5 x i32]* %1309, i64 0, i64 0
  %1311 = load i32, i32* %1310, align 4
  %1312 = mul nsw i32 %1311, -34
  %1313 = add nsw i32 %1307, %1312
  %1314 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1315 = getelementptr inbounds [5 x i32], [5 x i32]* %1314, i64 3
  %1316 = getelementptr inbounds [5 x i32], [5 x i32]* %1315, i64 0, i64 1
  %1317 = load i32, i32* %1316, align 4
  %1318 = mul nsw i32 %1317, -87
  %1319 = add nsw i32 %1313, %1318
  %1320 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1321 = getelementptr inbounds [5 x i32], [5 x i32]* %1320, i64 3
  %1322 = getelementptr inbounds [5 x i32], [5 x i32]* %1321, i64 0, i64 2
  %1323 = load i32, i32* %1322, align 4
  %1324 = mul nsw i32 %1323, -75
  %1325 = add nsw i32 %1319, %1324
  %1326 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1327 = getelementptr inbounds [5 x i32], [5 x i32]* %1326, i64 3
  %1328 = getelementptr inbounds [5 x i32], [5 x i32]* %1327, i64 0, i64 3
  %1329 = load i32, i32* %1328, align 4
  %1330 = mul nsw i32 %1329, 71
  %1331 = add nsw i32 %1325, %1330
  %1332 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1333 = getelementptr inbounds [5 x i32], [5 x i32]* %1332, i64 3
  %1334 = getelementptr inbounds [5 x i32], [5 x i32]* %1333, i64 0, i64 4
  %1335 = load i32, i32* %1334, align 4
  %1336 = mul nsw i32 %1335, -77
  %1337 = add nsw i32 %1331, %1336
  %1338 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1339 = getelementptr inbounds [5 x i32], [5 x i32]* %1338, i64 4
  %1340 = getelementptr inbounds [5 x i32], [5 x i32]* %1339, i64 0, i64 0
  %1341 = load i32, i32* %1340, align 4
  %1342 = mul nsw i32 %1341, 53
  %1343 = add nsw i32 %1337, %1342
  %1344 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1345 = getelementptr inbounds [5 x i32], [5 x i32]* %1344, i64 4
  %1346 = getelementptr inbounds [5 x i32], [5 x i32]* %1345, i64 0, i64 1
  %1347 = load i32, i32* %1346, align 4
  %1348 = mul nsw i32 %1347, 37
  %1349 = add nsw i32 %1343, %1348
  %1350 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1351 = getelementptr inbounds [5 x i32], [5 x i32]* %1350, i64 4
  %1352 = getelementptr inbounds [5 x i32], [5 x i32]* %1351, i64 0, i64 2
  %1353 = load i32, i32* %1352, align 4
  %1354 = mul nsw i32 %1353, -103
  %1355 = add nsw i32 %1349, %1354
  %1356 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1357 = getelementptr inbounds [5 x i32], [5 x i32]* %1356, i64 4
  %1358 = getelementptr inbounds [5 x i32], [5 x i32]* %1357, i64 0, i64 3
  %1359 = load i32, i32* %1358, align 4
  %1360 = mul nsw i32 %1359, -13
  %1361 = add nsw i32 %1355, %1360
  %1362 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1363 = getelementptr inbounds [5 x i32], [5 x i32]* %1362, i64 4
  %1364 = getelementptr inbounds [5 x i32], [5 x i32]* %1363, i64 0, i64 4
  %1365 = load i32, i32* %1364, align 4
  %1366 = mul nsw i32 %1365, -114
  %1367 = add nsw i32 %1361, %1366
  %1368 = call i32 @relu_reg(i32 %1367)
  %1369 = mul nsw i32 %1368, -23
  %1370 = add nsw i32 %1218, %1369
  %1371 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1372 = getelementptr inbounds [5 x i32], [5 x i32]* %1371, i64 0
  %1373 = getelementptr inbounds [5 x i32], [5 x i32]* %1372, i64 0, i64 0
  %1374 = load i32, i32* %1373, align 4
  %1375 = mul nsw i32 %1374, 67
  %1376 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1377 = getelementptr inbounds [5 x i32], [5 x i32]* %1376, i64 0
  %1378 = getelementptr inbounds [5 x i32], [5 x i32]* %1377, i64 0, i64 1
  %1379 = load i32, i32* %1378, align 4
  %1380 = mul nsw i32 %1379, 42
  %1381 = add nsw i32 %1375, %1380
  %1382 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1383 = getelementptr inbounds [5 x i32], [5 x i32]* %1382, i64 0
  %1384 = getelementptr inbounds [5 x i32], [5 x i32]* %1383, i64 0, i64 2
  %1385 = load i32, i32* %1384, align 4
  %1386 = mul nsw i32 %1385, 41
  %1387 = add nsw i32 %1381, %1386
  %1388 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1389 = getelementptr inbounds [5 x i32], [5 x i32]* %1388, i64 0
  %1390 = getelementptr inbounds [5 x i32], [5 x i32]* %1389, i64 0, i64 3
  %1391 = load i32, i32* %1390, align 4
  %1392 = mul nsw i32 %1391, -123
  %1393 = add nsw i32 %1387, %1392
  %1394 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1395 = getelementptr inbounds [5 x i32], [5 x i32]* %1394, i64 0
  %1396 = getelementptr inbounds [5 x i32], [5 x i32]* %1395, i64 0, i64 4
  %1397 = load i32, i32* %1396, align 4
  %1398 = mul nsw i32 %1397, -92
  %1399 = add nsw i32 %1393, %1398
  %1400 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1401 = getelementptr inbounds [5 x i32], [5 x i32]* %1400, i64 1
  %1402 = getelementptr inbounds [5 x i32], [5 x i32]* %1401, i64 0, i64 0
  %1403 = load i32, i32* %1402, align 4
  %1404 = mul nsw i32 %1403, 10
  %1405 = add nsw i32 %1399, %1404
  %1406 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1407 = getelementptr inbounds [5 x i32], [5 x i32]* %1406, i64 1
  %1408 = getelementptr inbounds [5 x i32], [5 x i32]* %1407, i64 0, i64 1
  %1409 = load i32, i32* %1408, align 4
  %1410 = mul nsw i32 %1409, -77
  %1411 = add nsw i32 %1405, %1410
  %1412 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1413 = getelementptr inbounds [5 x i32], [5 x i32]* %1412, i64 1
  %1414 = getelementptr inbounds [5 x i32], [5 x i32]* %1413, i64 0, i64 2
  %1415 = load i32, i32* %1414, align 4
  %1416 = mul nsw i32 %1415, 75
  %1417 = add nsw i32 %1411, %1416
  %1418 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1419 = getelementptr inbounds [5 x i32], [5 x i32]* %1418, i64 1
  %1420 = getelementptr inbounds [5 x i32], [5 x i32]* %1419, i64 0, i64 3
  %1421 = load i32, i32* %1420, align 4
  %1422 = mul nsw i32 %1421, 96
  %1423 = add nsw i32 %1417, %1422
  %1424 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1425 = getelementptr inbounds [5 x i32], [5 x i32]* %1424, i64 1
  %1426 = getelementptr inbounds [5 x i32], [5 x i32]* %1425, i64 0, i64 4
  %1427 = load i32, i32* %1426, align 4
  %1428 = mul nsw i32 %1427, -51
  %1429 = add nsw i32 %1423, %1428
  %1430 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1431 = getelementptr inbounds [5 x i32], [5 x i32]* %1430, i64 2
  %1432 = getelementptr inbounds [5 x i32], [5 x i32]* %1431, i64 0, i64 0
  %1433 = load i32, i32* %1432, align 4
  %1434 = mul nsw i32 %1433, 109
  %1435 = add nsw i32 %1429, %1434
  %1436 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1437 = getelementptr inbounds [5 x i32], [5 x i32]* %1436, i64 2
  %1438 = getelementptr inbounds [5 x i32], [5 x i32]* %1437, i64 0, i64 1
  %1439 = load i32, i32* %1438, align 4
  %1440 = mul nsw i32 %1439, -74
  %1441 = add nsw i32 %1435, %1440
  %1442 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1443 = getelementptr inbounds [5 x i32], [5 x i32]* %1442, i64 2
  %1444 = getelementptr inbounds [5 x i32], [5 x i32]* %1443, i64 0, i64 2
  %1445 = load i32, i32* %1444, align 4
  %1446 = mul nsw i32 %1445, -7
  %1447 = add nsw i32 %1441, %1446
  %1448 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1449 = getelementptr inbounds [5 x i32], [5 x i32]* %1448, i64 2
  %1450 = getelementptr inbounds [5 x i32], [5 x i32]* %1449, i64 0, i64 3
  %1451 = load i32, i32* %1450, align 4
  %1452 = mul nsw i32 %1451, -122
  %1453 = add nsw i32 %1447, %1452
  %1454 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1455 = getelementptr inbounds [5 x i32], [5 x i32]* %1454, i64 2
  %1456 = getelementptr inbounds [5 x i32], [5 x i32]* %1455, i64 0, i64 4
  %1457 = load i32, i32* %1456, align 4
  %1458 = mul nsw i32 %1457, 67
  %1459 = add nsw i32 %1453, %1458
  %1460 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1461 = getelementptr inbounds [5 x i32], [5 x i32]* %1460, i64 3
  %1462 = getelementptr inbounds [5 x i32], [5 x i32]* %1461, i64 0, i64 0
  %1463 = load i32, i32* %1462, align 4
  %1464 = mul nsw i32 %1463, 47
  %1465 = add nsw i32 %1459, %1464
  %1466 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1467 = getelementptr inbounds [5 x i32], [5 x i32]* %1466, i64 3
  %1468 = getelementptr inbounds [5 x i32], [5 x i32]* %1467, i64 0, i64 1
  %1469 = load i32, i32* %1468, align 4
  %1470 = mul nsw i32 %1469, 22
  %1471 = add nsw i32 %1465, %1470
  %1472 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1473 = getelementptr inbounds [5 x i32], [5 x i32]* %1472, i64 3
  %1474 = getelementptr inbounds [5 x i32], [5 x i32]* %1473, i64 0, i64 2
  %1475 = load i32, i32* %1474, align 4
  %1476 = mul nsw i32 %1475, -68
  %1477 = add nsw i32 %1471, %1476
  %1478 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1479 = getelementptr inbounds [5 x i32], [5 x i32]* %1478, i64 3
  %1480 = getelementptr inbounds [5 x i32], [5 x i32]* %1479, i64 0, i64 3
  %1481 = load i32, i32* %1480, align 4
  %1482 = mul nsw i32 %1481, 38
  %1483 = add nsw i32 %1477, %1482
  %1484 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1485 = getelementptr inbounds [5 x i32], [5 x i32]* %1484, i64 3
  %1486 = getelementptr inbounds [5 x i32], [5 x i32]* %1485, i64 0, i64 4
  %1487 = load i32, i32* %1486, align 4
  %1488 = mul nsw i32 %1487, 29
  %1489 = add nsw i32 %1483, %1488
  %1490 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1491 = getelementptr inbounds [5 x i32], [5 x i32]* %1490, i64 4
  %1492 = getelementptr inbounds [5 x i32], [5 x i32]* %1491, i64 0, i64 0
  %1493 = load i32, i32* %1492, align 4
  %1494 = mul nsw i32 %1493, 115
  %1495 = add nsw i32 %1489, %1494
  %1496 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1497 = getelementptr inbounds [5 x i32], [5 x i32]* %1496, i64 4
  %1498 = getelementptr inbounds [5 x i32], [5 x i32]* %1497, i64 0, i64 1
  %1499 = load i32, i32* %1498, align 4
  %1500 = mul nsw i32 %1499, -121
  %1501 = add nsw i32 %1495, %1500
  %1502 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1503 = getelementptr inbounds [5 x i32], [5 x i32]* %1502, i64 4
  %1504 = getelementptr inbounds [5 x i32], [5 x i32]* %1503, i64 0, i64 2
  %1505 = load i32, i32* %1504, align 4
  %1506 = mul nsw i32 %1505, 36
  %1507 = add nsw i32 %1501, %1506
  %1508 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1509 = getelementptr inbounds [5 x i32], [5 x i32]* %1508, i64 4
  %1510 = getelementptr inbounds [5 x i32], [5 x i32]* %1509, i64 0, i64 3
  %1511 = load i32, i32* %1510, align 4
  %1512 = mul nsw i32 %1511, -49
  %1513 = add nsw i32 %1507, %1512
  %1514 = load [5 x i32]*, [5 x i32]** %3, align 8
  %1515 = getelementptr inbounds [5 x i32], [5 x i32]* %1514, i64 4
  %1516 = getelementptr inbounds [5 x i32], [5 x i32]* %1515, i64 0, i64 4
  %1517 = load i32, i32* %1516, align 4
  %1518 = mul nsw i32 %1517, 85
  %1519 = add nsw i32 %1513, %1518
  %1520 = call i32 @relu_reg(i32 %1519)
  %1521 = mul nsw i32 %1520, 46
  %1522 = add nsw i32 %1370, %1521
  %1523 = icmp sgt i32 %1522, 0
  br i1 %1523, label %1524, label %1525

1524:                                             ; preds = %1
  store i32 1, i32* %2, align 4
  br label %1526

1525:                                             ; preds = %1
  store i32 0, i32* %2, align 4
  br label %1526

1526:                                             ; preds = %1525, %1524
  %1527 = load i32, i32* %2, align 4
  ret i32 %1527
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca [5 x [5 x i32]], align 16
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %6 = call i32 (...) @getint()
  store i32 %6, i32* %2, align 4
  br label %7

7:                                                ; preds = %45, %0
  %8 = load i32, i32* %2, align 4
  %9 = icmp sgt i32 %8, 0
  br i1 %9, label %10, label %48

10:                                               ; preds = %7
  store i32 0, i32* %4, align 4
  br label %11

11:                                               ; preds = %28, %10
  %12 = load i32, i32* %4, align 4
  %13 = icmp slt i32 %12, 5
  br i1 %13, label %14, label %31

14:                                               ; preds = %11
  store i32 0, i32* %5, align 4
  br label %15

15:                                               ; preds = %18, %14
  %16 = load i32, i32* %5, align 4
  %17 = icmp slt i32 %16, 5
  br i1 %17, label %18, label %28

18:                                               ; preds = %15
  %19 = call i32 (...) @getint()
  %20 = load i32, i32* %4, align 4
  %21 = sext i32 %20 to i64
  %22 = getelementptr inbounds [5 x [5 x i32]], [5 x [5 x i32]]* %3, i64 0, i64 %21
  %23 = load i32, i32* %5, align 4
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds [5 x i32], [5 x i32]* %22, i64 0, i64 %24
  store i32 %19, i32* %25, align 4
  %26 = load i32, i32* %5, align 4
  %27 = add nsw i32 %26, 1
  store i32 %27, i32* %5, align 4
  br label %15

28:                                               ; preds = %15
  %29 = load i32, i32* %4, align 4
  %30 = add nsw i32 %29, 1
  store i32 %30, i32* %4, align 4
  br label %11

31:                                               ; preds = %11
  %32 = getelementptr inbounds [5 x [5 x i32]], [5 x [5 x i32]]* %3, i64 0, i64 0
  %33 = call i32 @model([5 x i32]* %32)
  %34 = icmp ne i32 %33, 0
  br i1 %34, label %35, label %40

35:                                               ; preds = %31
  %36 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 99)
  %37 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 97)
  %38 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 116)
  %39 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 10)
  br label %45

40:                                               ; preds = %31
  %41 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 100)
  %42 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 111)
  %43 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 103)
  %44 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 10)
  br label %45

45:                                               ; preds = %40, %35
  %46 = load i32, i32* %2, align 4
  %47 = sub nsw i32 %46, 1
  store i32 %47, i32* %2, align 4
  br label %7

48:                                               ; preds = %7
  ret i32 0
}
'''
s13='''
@sum = dso_local global i32 0, align 4
@n = common dso_local global i32 0, align 4
@ans = common dso_local global [50 x i32] zeroinitializer, align 16
@row = common dso_local global [50 x i32] zeroinitializer, align 16
@line1 = common dso_local global [50 x i32] zeroinitializer, align 16
@line2 = common dso_local global [100 x i32] zeroinitializer, align 16

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @printans() #0 {
  %1 = alloca i32, align 4
  %2 = load i32, i32* @sum, align 4
  %3 = add nsw i32 %2, 1
  store i32 %3, i32* @sum, align 4
  store i32 1, i32* %1, align 4
  br label %4

4:                                                ; preds = %21, %0
  %5 = load i32, i32* %1, align 4
  %6 = load i32, i32* @n, align 4
  %7 = icmp sle i32 %5, %6
  br i1 %7, label %8, label %24

8:                                                ; preds = %4
  %9 = load i32, i32* %1, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds [50 x i32], [50 x i32]* @ans, i64 0, i64 %10
  %12 = load i32, i32* %11, align 4
  %13 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %12)
  %14 = load i32, i32* %1, align 4
  %15 = load i32, i32* @n, align 4
  %16 = icmp eq i32 %14, %15
  br i1 %16, label %17, label %19

17:                                               ; preds = %8
  %18 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 10)
  br label %24

19:                                               ; preds = %8
  %20 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 32)
  br label %21

21:                                               ; preds = %19
  %22 = load i32, i32* %1, align 4
  %23 = add nsw i32 %22, 1
  store i32 %23, i32* %1, align 4
  br label %4

24:                                               ; preds = %17, %4
  ret void
}

declare dso_local i32 @putint(...) #1

declare dso_local i32 @putch(...) #1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @f(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  store i32 1, i32* %3, align 4
  br label %4

4:                                                ; preds = %74, %1
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* @n, align 4
  %7 = icmp sle i32 %5, %6
  br i1 %7, label %8, label %77

8:                                                ; preds = %4
  %9 = load i32, i32* %3, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %10
  %12 = load i32, i32* %11, align 4
  %13 = icmp ne i32 %12, 1
  br i1 %13, label %14, label %74

14:                                               ; preds = %8
  %15 = load i32, i32* %2, align 4
  %16 = load i32, i32* %3, align 4
  %17 = add nsw i32 %15, %16
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %18
  %20 = load i32, i32* %19, align 4
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %74

22:                                               ; preds = %14
  %23 = load i32, i32* @n, align 4
  %24 = load i32, i32* %2, align 4
  %25 = add nsw i32 %23, %24
  %26 = load i32, i32* %3, align 4
  %27 = sub nsw i32 %25, %26
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %28
  %30 = load i32, i32* %29, align 4
  %31 = icmp ne i32 %30, 0
  br i1 %31, label %74, label %32

32:                                               ; preds = %22
  %33 = load i32, i32* %3, align 4
  %34 = load i32, i32* %2, align 4
  %35 = sext i32 %34 to i64
  %36 = getelementptr inbounds [50 x i32], [50 x i32]* @ans, i64 0, i64 %35
  store i32 %33, i32* %36, align 4
  %37 = load i32, i32* %2, align 4
  %38 = load i32, i32* @n, align 4
  %39 = icmp eq i32 %37, %38
  br i1 %39, label %40, label %41

40:                                               ; preds = %32
  call void @printans()
  br label %41

41:                                               ; preds = %40, %32
  %42 = load i32, i32* %3, align 4
  %43 = sext i32 %42 to i64
  %44 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %43
  store i32 1, i32* %44, align 4
  %45 = load i32, i32* %2, align 4
  %46 = load i32, i32* %3, align 4
  %47 = add nsw i32 %45, %46
  %48 = sext i32 %47 to i64
  %49 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %48
  store i32 1, i32* %49, align 4
  %50 = load i32, i32* @n, align 4
  %51 = load i32, i32* %2, align 4
  %52 = add nsw i32 %50, %51
  %53 = load i32, i32* %3, align 4
  %54 = sub nsw i32 %52, %53
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %55
  store i32 1, i32* %56, align 4
  %57 = load i32, i32* %2, align 4
  %58 = add nsw i32 %57, 1
  call void @f(i32 %58)
  %59 = load i32, i32* %3, align 4
  %60 = sext i32 %59 to i64
  %61 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %60
  store i32 0, i32* %61, align 4
  %62 = load i32, i32* %2, align 4
  %63 = load i32, i32* %3, align 4
  %64 = add nsw i32 %62, %63
  %65 = sext i32 %64 to i64
  %66 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %65
  store i32 0, i32* %66, align 4
  %67 = load i32, i32* @n, align 4
  %68 = load i32, i32* %2, align 4
  %69 = add nsw i32 %67, %68
  %70 = load i32, i32* %3, align 4
  %71 = sub nsw i32 %69, %70
  %72 = sext i32 %71 to i64
  %73 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %72
  store i32 0, i32* %73, align 4
  br label %74

74:                                               ; preds = %41, %22, %14, %8
  %75 = load i32, i32* %3, align 4
  %76 = add nsw i32 %75, 1
  store i32 %76, i32* %3, align 4
  br label %4

77:                                               ; preds = %4
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %3 = call i32 (...) @getint()
  store i32 %3, i32* %2, align 4
  br label %4

4:                                                ; preds = %7, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp sgt i32 %5, 0
  br i1 %6, label %7, label %11

7:                                                ; preds = %4
  %8 = call i32 (...) @getint()
  store i32 %8, i32* @n, align 4
  call void @f(i32 1)
  %9 = load i32, i32* %2, align 4
  %10 = sub nsw i32 %9, 1
  store i32 %10, i32* %2, align 4
  br label %4

11:                                               ; preds = %4
  ret i32 0
}
'''
s14='''
@sum = dso_local global i32 0, align 4
@n = common dso_local global i32 0, align 4
@ans = common dso_local global [50 x i32] zeroinitializer, align 16
@row = common dso_local global [50 x i32] zeroinitializer, align 16
@line1 = common dso_local global [50 x i32] zeroinitializer, align 16
@line2 = common dso_local global [100 x i32] zeroinitializer, align 16

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @printans() #0 {
  %1 = alloca i32, align 4
  %2 = load i32, i32* @sum, align 4
  %3 = add nsw i32 %2, 1
  store i32 %3, i32* @sum, align 4
  store i32 1, i32* %1, align 4
  br label %4

4:                                                ; preds = %21, %0
  %5 = load i32, i32* %1, align 4
  %6 = load i32, i32* @n, align 4
  %7 = icmp sle i32 %5, %6
  br i1 %7, label %8, label %24

8:                                                ; preds = %4
  %9 = load i32, i32* %1, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds [50 x i32], [50 x i32]* @ans, i64 0, i64 %10
  %12 = load i32, i32* %11, align 4
  %13 = call i32 (i32, ...) bitcast (i32 (...)* @putint to i32 (i32, ...)*)(i32 %12)
  %14 = load i32, i32* %1, align 4
  %15 = load i32, i32* @n, align 4
  %16 = icmp eq i32 %14, %15
  br i1 %16, label %17, label %19

17:                                               ; preds = %8
  %18 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 10)
  br label %24

19:                                               ; preds = %8
  %20 = call i32 (i32, ...) bitcast (i32 (...)* @putch to i32 (i32, ...)*)(i32 32)
  br label %21

21:                                               ; preds = %19
  %22 = load i32, i32* %1, align 4
  %23 = add nsw i32 %22, 1
  store i32 %23, i32* %1, align 4
  br label %4

24:                                               ; preds = %17, %4
  ret void
}

declare dso_local i32 @putint(...) #1

declare dso_local i32 @putch(...) #1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @f(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  store i32 1, i32* %3, align 4
  br label %4

4:                                                ; preds = %74, %1
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* @n, align 4
  %7 = icmp sle i32 %5, %6
  br i1 %7, label %8, label %77

8:                                                ; preds = %4
  %9 = load i32, i32* %3, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %10
  %12 = load i32, i32* %11, align 4
  %13 = icmp ne i32 %12, 1
  br i1 %13, label %14, label %74

14:                                               ; preds = %8
  %15 = load i32, i32* %2, align 4
  %16 = load i32, i32* %3, align 4
  %17 = add nsw i32 %15, %16
  %18 = sext i32 %17 to i64
  %19 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %18
  %20 = load i32, i32* %19, align 4
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %22, label %74

22:                                               ; preds = %14
  %23 = load i32, i32* @n, align 4
  %24 = load i32, i32* %2, align 4
  %25 = add nsw i32 %23, %24
  %26 = load i32, i32* %3, align 4
  %27 = sub nsw i32 %25, %26
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %28
  %30 = load i32, i32* %29, align 4
  %31 = icmp ne i32 %30, 0
  br i1 %31, label %74, label %32

32:                                               ; preds = %22
  %33 = load i32, i32* %3, align 4
  %34 = load i32, i32* %2, align 4
  %35 = sext i32 %34 to i64
  %36 = getelementptr inbounds [50 x i32], [50 x i32]* @ans, i64 0, i64 %35
  store i32 %33, i32* %36, align 4
  %37 = load i32, i32* %2, align 4
  %38 = load i32, i32* @n, align 4
  %39 = icmp eq i32 %37, %38
  br i1 %39, label %40, label %41

40:                                               ; preds = %32
  call void @printans()
  br label %41

41:                                               ; preds = %40, %32
  %42 = load i32, i32* %3, align 4
  %43 = sext i32 %42 to i64
  %44 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %43
  store i32 1, i32* %44, align 4
  %45 = load i32, i32* %2, align 4
  %46 = load i32, i32* %3, align 4
  %47 = add nsw i32 %45, %46
  %48 = sext i32 %47 to i64
  %49 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %48
  store i32 1, i32* %49, align 4
  %50 = load i32, i32* @n, align 4
  %51 = load i32, i32* %2, align 4
  %52 = add nsw i32 %50, %51
  %53 = load i32, i32* %3, align 4
  %54 = sub nsw i32 %52, %53
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %55
  store i32 1, i32* %56, align 4
  %57 = load i32, i32* %2, align 4
  %58 = add nsw i32 %57, 1
  call void @f(i32 %58)
  %59 = load i32, i32* %3, align 4
  %60 = sext i32 %59 to i64
  %61 = getelementptr inbounds [50 x i32], [50 x i32]* @row, i64 0, i64 %60
  store i32 0, i32* %61, align 4
  %62 = load i32, i32* %2, align 4
  %63 = load i32, i32* %3, align 4
  %64 = add nsw i32 %62, %63
  %65 = sext i32 %64 to i64
  %66 = getelementptr inbounds [50 x i32], [50 x i32]* @line1, i64 0, i64 %65
  store i32 0, i32* %66, align 4
  %67 = load i32, i32* @n, align 4
  %68 = load i32, i32* %2, align 4
  %69 = add nsw i32 %67, %68
  %70 = load i32, i32* %3, align 4
  %71 = sub nsw i32 %69, %70
  %72 = sext i32 %71 to i64
  %73 = getelementptr inbounds [100 x i32], [100 x i32]* @line2, i64 0, i64 %72
  store i32 0, i32* %73, align 4
  br label %74

74:                                               ; preds = %41, %22, %14, %8
  %75 = load i32, i32* %3, align 4
  %76 = add nsw i32 %75, 1
  store i32 %76, i32* %3, align 4
  br label %4

77:                                               ; preds = %4
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %3 = call i32 (...) @getint()
  store i32 %3, i32* %2, align 4
  br label %4

4:                                                ; preds = %7, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp sgt i32 %5, 0
  br i1 %6, label %7, label %11

7:                                                ; preds = %4
  %8 = call i32 (...) @getint()
  store i32 %8, i32* @n, align 4
  call void @f(i32 1)
  %9 = load i32, i32* %2, align 4
  %10 = sub nsw i32 %9, 1
  store i32 %10, i32* %2, align 4
  br label %4

11:                                               ; preds = %4
  ret i32 0
}
'''
ss1=['int _getMaxOfAll(int result[], int size) {\n', '    int maxNum;\n', '    maxNum = -999999;\n', '    size = size - 1;\n', '    while(size > -1) {\n', '        if (result[size] > maxNum) {\n', '            maxNum = result[size];\n', '        }\n', '        size = size - 1;\n', '    }\n', '    return maxNum;\n', '}\n', '\n', 'int main() {\n', '    int result[3];\n', '    result[0] = -2;\n', '    result[1] = 2;\n', '    result[2] = -7;\n', '    int x;\n', '    x = result[_getMaxOfAll(result, 3)];\n', '    putint(x);\n', '    return 0;\n', '}\n']
ss2=['int fib(int n) {\n', '\tif (n == 0)\n', '\t\treturn 0;\n', '\tif (n == 1)\n', '\t\treturn 1;\n', '\tint p;\n', '\tp = n - 1;\n', '\tint q;\n', '\tq = n - 2;\n', '\treturn fib(p) + fib(q);\n', '}\n', '\n', 'int main() {\n', '\tint tmp;\n', '\ttmp = 10;\n', '\tputint(fib(tmp));\n', '    return 0;\n', '}']
ss3=['int a;\n', 'int r;\n', 'int fac(int x) {\n', '    if (x < 2)\n', '        return 1;\n', '    a = x - 1;\n', '    r = fac(a);\n', '    r = x * r;\n', '    return r;\n', '}\n', '\n', 'int main() {\n', '    int a;\n', '    a = 5;\n', '    putint(fac(a));\n', '    return 0;\n', '}']
ss4=['int n;\n', 'int swap(int array[], int i, int j) {\n', '    int temp;\n', '    temp     = array[i];\n', '    array[i] = array[j];\n', '    array[j] = temp;\n', '    return 0;\n', '}\n', 'int heap_ajust(int arr[], int start, int end) {\n', '    int dad;\n', '    dad = start;\n', '    int son;\n', '    son = dad * 2 + 1;\n', '    while (son < end + 1) {  //\n', '        if (son < end && arr[son] < arr[son + 1])\n', '            son = son + 1;\n', '        if (arr[dad] > arr[son])\n', '            return 0;\n', '        else {\n', '            dad = swap(arr, dad, son);\n', '            dad = son;\n', '            son = dad * 2 + 1;\n', '        }\n', '    }\n', '    return 0;\n', '}\n', 'int heap_sort(int arr[], int len) {\n', '    int i;\n', '    int tmp;\n', '    i = len / 2 - 1;\n', '    while (i > -1) {\n', '        tmp = len - 1;\n', '        tmp = heap_ajust(arr, i, tmp);\n', '        i   = i - 1;\n', '    }\n', '    i = len - 1;\n', '    while (i > 0) {\n', '        int tmp0;\n', '        tmp0 = 0;\n', '        tmp  = swap(arr, tmp0, i);\n', '        tmp  = i - 1;\n', '        tmp  = heap_ajust(arr, tmp0, tmp);\n', '        i    = i - 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int main() {\n', '    int a[10];\n', '    n = getarray(a);\n', '    int i;\n', '    i = 0;\n', '    i = heap_sort(a, n);\n', '    putarray(n, a);\n', '    return 0;\n', '}\n']
ss5=['int n;\n', 'int QuickSort(int arr[], int low, int high) {\n', '    if (low < high) {\n', '        int i;\n', '        i = low;\n', '        int j;\n', '        j = high;\n', '        int k;\n', '        k = arr[low];\n', '        while (i < j) {\n', '            while (i < j && arr[j] > k - 1) {\n', '                j = j - 1;\n', '            }\n', '\n', '            if (i < j) {\n', '                arr[i] = arr[j];\n', '                i      = i + 1;\n', '            }\n', '\n', '            while (i < j && arr[i] < k) {\n', '                i = i + 1;\n', '            }\n', '\n', '            if (i < j) {\n', '                arr[j] = arr[i];\n', '                j      = j - 1;\n', '            }\n', '        }\n', '\n', '        arr[i] = k;\n', '        int tmp;\n', '        tmp = i - 1;\n', '        tmp = QuickSort(arr, low, tmp);\n', '        tmp = i + 1;\n', '        tmp = QuickSort(arr, tmp, high);\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int main() {\n', '\n', '    int a[10];\n', '    n = getarray(a);\n', '    int i;\n', '    i = 0;\n', '    int tmp;\n', '    tmp = 9;\n', '    i   = QuickSort(a, i, tmp);\n', '    putarray(10, a);\n', '    return 0;\n', '}\n']
ss6=['int n;\n', 'int Merge(int array[], int low, int middle, int high) {\n', '    int n1;\n', '    n1 = middle - low + 1;\n', '    int n2;\n', '    n2 = high - middle;\n', '    int L[10];\n', '    int R[10];\n', '    int i;\n', '    i = 0;\n', '    int j;\n', '    j = 0;\n', '\n', '    while (i < n1) {\n', '        L[i] = array[i + low];\n', '        i    = i + 1;\n', '    }\n', '    while (j < n2) {\n', '        R[j] = array[j + middle + 1];\n', '        j    = j + 1;\n', '    }\n', '    i = 0;\n', '    j = 0;\n', '    int k;\n', '    k = low;\n', '    while (i != n1 && j != n2) {\n', '        if (L[i] < R[j] + 1) {\n', '            array[k] = L[i];\n', '            k        = k + 1;\n', '            i        = i + 1;\n', '        } else {\n', '            array[k] = R[j];\n', '            k        = k + 1;\n', '            j        = j + 1;\n', '        }\n', '    }\n', '    while (i < n1) {\n', '        array[k] = L[i];\n', '        k        = k + 1;\n', '        i        = i + 1;\n', '    }\n', '    while (j < n2) {\n', '        array[k] = R[j];\n', '        k        = k + 1;\n', '        j        = j + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int MergeSort(int array[], int p, int q) {\n', '    if (p < q) {\n', '        int mid;\n', '        mid = (p + q) / 2;\n', '        int tmp;\n', '        tmp = MergeSort(array, p, mid);\n', '        tmp = mid + 1;\n', '        tmp = MergeSort(array, tmp, q);\n', '        tmp = Merge(array, p, mid, q);\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int main() {\n', '    int a[10];\n', '    n = getarray(a);\n', '    int i;\n', '    i = 0;\n', '    int tmp;\n', '    tmp = n - 1;\n', '    i   = MergeSort(a, i, tmp);\n', '    putarray(n, a);\n', '    return 0;\n', '}\n']
ss7=['// Really long code;\n', 'int n;\n', '\n', 'int bubblesort(int arr[]) {\n', '    int i;\n', '    int j;\n', '    i = 0;\n', '    while (i < n - 1) {\n', '        // Last i elements are already in place\n', '        j = 0;\n', '        while (j < n - i - 1) {\n', '            if (arr[j] > arr[j + 1]) {\n', '                // swap(&arr[j], &arr[j+1]);\n', '                int tmp;\n', '                tmp        = arr[j + 1];\n', '                arr[j + 1] = arr[j];\n', '                arr[j]     = tmp;\n', '            }\n', '            j = j + 1;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int insertsort(int a[]) {\n', '    int i;\n', '    i = 1;\n', '    while (i < n) {\n', '        int temp;\n', '        temp = a[i];\n', '        int j;\n', '        j = i - 1;\n', '        while (j > -1 && temp < a[j]) {\n', '            a[j + 1] = a[j];\n', '            j        = j - 1;\n', '        }\n', '        a[j + 1] = temp;\n', '        i        = i + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int QuickSort(int arr[], int low, int high) {\n', '    if (low < high) {\n', '        int i;\n', '        i = low;\n', '        int j;\n', '        j = high;\n', '        int k;\n', '        k = arr[low];\n', '        while (i < j) {\n', '            while (i < j && arr[j] > k - 1) {\n', '                j = j - 1;\n', '            }\n', '\n', '            if (i < j) {\n', '                arr[i] = arr[j];\n', '                i      = i + 1;\n', '            }\n', '\n', '            while (i < j && arr[i] < k) {\n', '                i = i + 1;\n', '            }\n', '\n', '            if (i < j) {\n', '                arr[j] = arr[i];\n', '                j      = j - 1;\n', '            }\n', '        }\n', '\n', '        arr[i] = k;\n', '        int tmp;\n', '        tmp = i - 1;\n', '        tmp = QuickSort(arr, low, tmp);\n', '        tmp = i + 1;\n', '        tmp = QuickSort(arr, tmp, high);\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int getMid(int arr[]) {\n', '    int mid;\n', '    if (n % 2 == 0) {\n', '        mid = n / 2;\n', '        return (arr[mid] + arr[mid - 1]) / 2;\n', '    } else {\n', '        mid = n / 2;\n', '        return arr[mid];\n', '    }\n', '}\n', '\n', 'int getMost(int arr[]) {\n', '    int count[1000];\n', '    int i;\n', '    i = 0;\n', '    while (i < 1000) {\n', '        count[i] = 0;\n', '        i        = i + 1;\n', '    }\n', '    i = 0;\n', '    int max;\n', '    int number;\n', '    max = 0;\n', '    while (i < n) {\n', '        int num;\n', '        num        = arr[i];\n', '        count[num] = count[num] + 1;\n', '        if (count[num] > max) {\n', '            max    = count[num];\n', '            number = num;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    return number;\n', '}\n', '\n', 'int revert(int arr[]) {\n', '    int temp;\n', '    int i;\n', '    int j;\n', '    i = 0;\n', '    j = 0;\n', '    while (i < j) {\n', '        temp   = arr[i];\n', '        arr[i] = arr[j];\n', '        arr[j] = temp;\n', '        i      = i + 1;\n', '        j      = j - 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int arrCopy(int src[], int target[]) {\n', '    int i;\n', '    i = 0;\n', '    while (i < n) {\n', '        target[i] = src[i];\n', '        i         = i + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int calSum(int arr[], int stride) {\n', '    int sum;\n', '    sum = 0;\n', '    int i;\n', '    i = 0;\n', '    while (i < n) {\n', '        sum = sum + arr[i];\n', '        if (i % stride != stride - 1) {\n', '            arr[i] = 0;\n', '        } else {\n', '            arr[i] = sum;\n', '            sum    = 0;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int avgPooling(int arr[], int stride) {\n', '    int sum;\n', '    int i;\n', '    i   = 0;\n', '    sum = 0;\n', '    int lastnum;\n', '    while (i < n) {\n', '        if (i < stride - 1) {\n', '            sum = sum + arr[i];\n', '        } else if (i == stride - 1) {\n', '            lastnum = arr[0];\n', '            arr[0]  = sum / stride;\n', '        } else {\n', '            sum                 = sum + arr[i] - lastnum;\n', '            lastnum             = arr[i - stride + 1];\n', '            arr[i - stride + 1] = sum / stride;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    i = n - stride + 1;\n', '    while (i < n) {\n', '        arr[i] = 0;\n', '        i      = i + 1;\n', '    }\n', '    return 0;\n', '}\n', '\n', 'int main() {\n', '    n = 32;\n', '    int arr[32];\n', '    int result[32];\n', '    arr[0]  = 7;\n', '    arr[1]  = 23;\n', '    arr[2]  = 89;\n', '    arr[3]  = 26;\n', '    arr[4]  = 282;\n', '    arr[5]  = 254;\n', '    arr[6]  = 27;\n', '    arr[7]  = 5;\n', '    arr[8]  = 83;\n', '    arr[9]  = 273;\n', '    arr[10] = 574;\n', '    arr[11] = 905;\n', '    arr[12] = 354;\n', '    arr[13] = 657;\n', '    arr[14] = 935;\n', '    arr[15] = 264;\n', '    arr[16] = 639;\n', '    arr[17] = 459;\n', '    arr[18] = 29;\n', '    arr[19] = 68;\n', '    arr[20] = 929;\n', '    arr[21] = 756;\n', '    arr[22] = 452;\n', '    arr[23] = 279;\n', '    arr[24] = 58;\n', '    arr[25] = 87;\n', '    arr[26] = 96;\n', '    arr[27] = 36;\n', '    arr[28] = 39;\n', '    arr[29] = 28;\n', '    arr[30] = 1;\n', '    arr[31] = 290;\n', '    int t;\n', '    t = arrCopy(arr, result);\n', '    t = revert(result);\n', '    int i;\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '    t = bubblesort(result);\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '    t = getMid(result);\n', '    putint(t);\n', '    t = getMost(result);\n', '    putint(t);\n', '\n', '    t = arrCopy(arr, result);\n', '    t = bubblesort(result);\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '\n', '    t = arrCopy(arr, result);\n', '    t = insertsort(result);\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '\n', '    t = arrCopy(arr, result);\n', '    i = 0;\n', '    t = 31;\n', '    t = QuickSort(result, i, t);\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '\n', '    t = arrCopy(arr, result);\n', '    t = calSum(result, 4);\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '\n', '    t = arrCopy(arr, result);\n', '    t = avgPooling(result, 3);\n', '    i = 0;\n', '    while (i < 32) {\n', '        t = result[i];\n', '        putint(t);\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n']
ss8=['// Call a func with many params.\n', '\n', 'int a0;\n', 'int a1;\n', 'int a2;\n', 'int a3;\n', 'int a4;\n', 'int a5;\n', 'int a6;\n', 'int a7;\n', 'int a8;\n', 'int a9;\n', 'int a10;\n', 'int a11;\n', 'int a12;\n', 'int a13;\n', 'int a14;\n', 'int a15;\n', 'int a16;\n', 'int a17;\n', 'int a18;\n', 'int a19;\n', 'int a20;\n', 'int a21;\n', 'int a22;\n', 'int a23;\n', 'int a24;\n', 'int a25;\n', 'int a26;\n', 'int a27;\n', 'int a28;\n', 'int a29;\n', 'int a30;\n', 'int a31;\n', '\n', 'int a32;\n', 'int a33;\n', 'int a34;\n', 'int a35;\n', 'int a36;\n', 'int a37;\n', 'int a38;\n', 'int a39;\n', '\n', 'int testParam8(int a0, int a1, int a2, int a3, int a4, int a5, int a6, int a7) {\n', '    return a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7;\n', '}\n', '\n', 'int testParam16(\n', '    int a0, int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9, int a10, int a11, int a12, int a13,\n', '    int a14, int a15) {\n', '    return a0 + a1 + a2 - a3 - a4 - a5 - a6 - a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15;\n', '}\n', '\n', 'int testParam32(\n', '    int a0, int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9, int a10, int a11, int a12, int a13,\n', '    int a14, int a15, int a16, int a17, int a18, int a19, int a20, int a21, int a22, int a23, int a24, int a25, int a26,\n', '    int a27, int a28, int a29, int a30, int a31) {\n', '    return a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15 + a16 + a17 - a18 - a19\n', '           - a20 - a21 - a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a30 + a31;\n', '}\n', '\n', 'int main() {\n', '    a0  = 0;\n', '    a1  = 1;\n', '    a2  = 2;\n', '    a3  = 3;\n', '    a4  = 4;\n', '    a5  = 5;\n', '    a6  = 6;\n', '    a7  = 7;\n', '    a8  = 8;\n', '    a9  = 9;\n', '    a10 = 0;\n', '    a11 = 1;\n', '    a12 = 2;\n', '    a13 = 3;\n', '    a14 = 4;\n', '    a15 = 5;\n', '    a16 = 6;\n', '    a17 = 7;\n', '    a18 = 8;\n', '    a19 = 9;\n', '    a20 = 0;\n', '    a21 = 1;\n', '    a22 = 2;\n', '    a23 = 3;\n', '    a24 = 4;\n', '    a25 = 5;\n', '    a26 = 6;\n', '    a27 = 7;\n', '    a28 = 8;\n', '    a29 = 9;\n', '    a30 = 0;\n', '    a31 = 1;\n', '\n', '    a32 = 4;\n', '    a33 = 5;\n', '    a34 = 6;\n', '    a35 = 7;\n', '    a36 = 8;\n', '    a37 = 9;\n', '    a38 = 0;\n', '    a39 = 1;\n', '\n', '    a0 = testParam8(a0, a1, a2, a3, a4, a5, a6, a7);\n', '    putint(a0);\n', '    a0 = testParam16(a32, a33, a34, a35, a36, a37, a38, a39, a8, a9, a10, a11, a12, a13, a14, a15);\n', '    putint(a0);\n', '    a0 = testParam32(\n', '        a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,\n', '        a24, a25, a26, a27, a28, a29, a30, a31);\n', '    putint(a0);\n', '    return 0;\n', '}\n']
ss9=['int ints[10000];\n', 'int intt;\n', 'int chas[10000];\n', 'int chat;\n', 'int i = 0, ii = 1;\n', 'int c;\n', 'int get[10000];\n', 'int get2[10000];\n', '\n', 'int isdigit(int x) {\n', '    if (x >= 48 && x <= 57)\n', '        return 1;\n', '    return 0;\n', '}\n', '\n', 'int power(int b, int a) {\n', '    int result = 1;\n', '    while (a != 0) {\n', '        result = result * b;\n', '        a      = a - 1;\n', '    }\n', '    return result;\n', '}\n', '\n', 'int getstr(int get[]) {\n', '    int x      = getch();\n', '    int length = 0;\n', '    while (x != 13 && x != 10) {\n', '        get[length] = x;\n', '        length      = length + 1;\n', '        x           = getch();\n', '    }\n', '    return length;\n', '}\n', '\n', 'void intpush(int x) {\n', '    intt       = intt + 1;\n', '    ints[intt] = x;\n', '}\n', 'void chapush(int x) {\n', '    chat       = chat + 1;\n', '    chas[chat] = x;\n', '}\n', 'int intpop() {\n', '    intt = intt - 1;\n', '    return ints[intt + 1];\n', '}\n', 'int chapop() {\n', '    chat = chat - 1;\n', '    return chas[chat + 1];\n', '}\n', 'void intadd(int x) {\n', '    ints[intt] = ints[intt] * 10;\n', '    ints[intt] = ints[intt] + x;\n', '}\n', '\n', 'int find() {\n', '    c            = chapop();\n', '    get2[ii]     = 32;\n', '    get2[ii + 1] = c;\n', '    ii           = ii + 2;\n', '    if (chat == 0)\n', '        return 0;\n', '    return 1;\n', '}\n', '\n', 'int main() {\n', '    intt        = 0;\n', '    chat        = 0;\n', '    int lengets = getstr(get);\n', '    while (i < lengets) {\n', '        if (isdigit(get[i]) == 1) {\n', '            get2[ii] = get[i];\n', '            ii       = ii + 1;\n', '        } else {\n', '            if (get[i] == 40)\n', '                chapush(40);\n', '            if (get[i] == 94)\n', '                chapush(94);\n', '            if (get[i] == 41) {\n', '                c = chapop();\n', '                while (c != 40) {\n', '                    get2[ii]     = 32;\n', '                    get2[ii + 1] = c;\n', '                    ii           = ii + 2;\n', '                    c            = chapop();\n', '                }\n', '            }\n', '            if (get[i] == 43) {\n', '                while (chas[chat] == 43 || chas[chat] == 45 || chas[chat] == 42 || chas[chat] == 47 || chas[chat] == 37\n', '                       || chas[chat] == 94) {\n', '                    if (find() == 0)\n', '                        break;\n', '                }\n', '                chapush(43);\n', '            }\n', '            if (get[i] == 45) {\n', '                while (chas[chat] == 43 || chas[chat] == 45 || chas[chat] == 42 || chas[chat] == 47 || chas[chat] == 37\n', '                       || chas[chat] == 94) {\n', '                    if (find() == 0)\n', '                        break;\n', '                }\n', '                chapush(45);\n', '            }\n', '            if (get[i] == 42) {\n', '                while (chas[chat] == 42 || chas[chat] == 47 || chas[chat] == 37 || chas[chat] == 94) {\n', '                    if (find() == 0)\n', '                        break;\n', '                }\n', '                chapush(42);\n', '            }\n', '            if (get[i] == 47) {\n', '                while (chas[chat] == 42 || chas[chat] == 47 || chas[chat] == 37 || chas[chat] == 94) {\n', '                    if (find() == 0)\n', '                        break;\n', '                }\n', '                chapush(47);\n', '            }\n', '            if (get[i] == 37) {\n', '                while (chas[chat] == 42 || chas[chat] == 47 || chas[chat] == 37 || chas[chat] == 94) {\n', '                    if (find() == 0)\n', '                        break;\n', '                }\n', '                chapush(37);\n', '            }\n', '            get2[ii] = 32;\n', '            ii       = ii + 1;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    while (chat > 0) {\n', '        int c        = chapop();\n', '        get2[ii]     = 32;\n', '        get2[ii + 1] = c;\n', '        ii           = ii + 2;\n', '    }\n', '    get2[ii] = 64;\n', '    i        = 1;\n', '    while (get2[i] != 64) {\n', '        if (get2[i] == 43 || get2[i] == 45 || get2[i] == 42 || get2[i] == 47 || get2[i] == 37 || get2[i] == 94) {\n', '            int a = intpop();\n', '            int b = intpop();\n', '            int c;\n', '            if (get2[i] == 43)\n', '                c = a + b;\n', '            if (get2[i] == 45)\n', '                c = b - a;\n', '            if (get2[i] == 42)\n', '                c = a * b;\n', '            if (get2[i] == 47)\n', '                c = b / a;\n', '            if (get2[i] == 37)\n', '                c = b % a;\n', '            if (get2[i] == 94)\n', '                c = power(b, a);\n', '            intpush(c);\n', '        } else {\n', '            if (get2[i] != 32) {\n', '                intpush(get2[i] - 48);\n', '                ii = 1;\n', '                while (get2[i + ii] != 32) {\n', '                    intadd(get2[i + ii] - 48);\n', '                    ii = ii + 1;\n', '                }\n', '                i = i + ii - 1;\n', '            }\n', '        }\n', '        i = i + 1;\n', '    }\n', '    putint(ints[1]);\n', '    return 0;\n', '}\n']
ss10=['int exgcd(int a, int b, int x[], int y[]) {\n', '    if (b == 0) {\n', '        x[0] = 1;\n', '        y[0] = 0;\n', '        return a;\n', '    } else {\n', '        int r = exgcd(b, a % b, x, y);\n', '        int t = x[0];\n', '        x[0]  = y[0];\n', '        y[0]  = (t - a / b * y[0]);\n', '        return r;\n', '    }\n', '}\n', '\n', 'int main() {\n', '    int a = 7, b = 15, x[1] = {1}, y[1] = {1};\n', '    exgcd(a, b, x, y);\n', '    x[0] = (x[0] % b + b) % b;\n', '    putint(x[0]);\n', '    return 0;\n', '}']
ss11=['void move(int x, int y) {\n', '    putint(x);\n', '    putch(32);\n', '    putint(y);\n', '    putch(44);\n', '    putch(32);\n', '}\n', '\n', 'void hanoi(int n, int one, int two, int three) {\n', '    if (n == 1)\n', '        move(one, three);\n', '    else {\n', '        hanoi(n - 1, one, three, two);\n', '        move(one, three);\n', '        hanoi(n - 1, two, one, three);\n', '    }\n', '}\n', '\n', 'int main() {\n', '    int n = getint();\n', '    while (n > 0) {\n', '        hanoi(getint(), 1, 2, 3);\n', '        putch(10);\n', '        n = n - 1;\n', '    }\n', '    return 0;\n', '}']
ss12=['int relu_reg(int a) {\n', '    if (a > 0x7F)\n', '        return 0x7F;\n', '    if (a < 0)\n', '        return 0;\n', '    return a;\n', '}\n', '\n', 'int model(int a[][5]) {\n', '    if (+relu_reg(\n', '            +a[0][0] * 85 + a[0][1] * 23 + a[0][2] * -82 + a[0][3] * -103 + a[0][4] * -123 + a[1][0] * 64\n', '            + a[1][1] * -120 + a[1][2] * 50 + a[1][3] * -59 + a[1][4] * 47 + a[2][0] * -111 + a[2][1] * -67\n', '            + a[2][2] * -106 + a[2][3] * -75 + a[2][4] * -102 + a[3][0] * 34 + a[3][1] * -39 + a[3][2] * 65\n', '            + a[3][3] * 47 + a[3][4] * 113 + a[4][0] * 110 + a[4][1] * 47 + a[4][2] * -4 + a[4][3] * 80 + a[4][4] * 46)\n', '                * 39\n', '            + relu_reg(\n', '                  +a[0][0] * -106 + a[0][1] * 126 + a[0][2] * -18 + a[0][3] * -31 + a[0][4] * -8 + a[1][0] * 47\n', '                  + a[1][1] * -4 + a[1][2] * 67 + a[1][3] * -94 + a[1][4] * -121 + a[2][0] * 7 + a[2][1] * -21\n', '                  + a[2][2] * -60 + a[2][3] * -43 + a[2][4] * 105 + a[3][0] * -42 + a[3][1] * 87 + a[3][2] * 29\n', '                  + a[3][3] * -106 + a[3][4] * -31 + a[4][0] * -110 + a[4][1] * -100 + a[4][2] * -22 + a[4][3] * -75\n', '                  + a[4][4] * -125)\n', '                  * 77\n', '            + relu_reg(\n', '                  +a[0][0] * 26 + a[0][1] * 76 + a[0][2] * -70 + a[0][3] * 29 + a[0][4] * -95 + a[1][0] * 96\n', '                  + a[1][1] * 52 + a[1][2] * -68 + a[1][3] * -5 + a[1][4] * 34 + a[2][0] * -34 + a[2][1] * 102\n', '                  + a[2][2] * 6 + a[2][3] * -38 + a[2][4] * 27 + a[3][0] * 110 + a[3][1] * 116 + a[3][2] * 39\n', '                  + a[3][3] * -63 + a[3][4] * -99 + a[4][0] * 65 + a[4][1] * 120 + a[4][2] * -39 + a[4][3] * -6\n', '                  + a[4][4] * 94)\n', '                  * 127\n', '            + relu_reg(\n', '                  +a[0][0] * -23 + a[0][1] * -63 + a[0][2] * 49 + a[0][3] * 50 + a[0][4] * 72 + a[1][0] * 85\n', '                  + a[1][1] * -30 + a[1][2] * 12 + a[1][3] * 125 + a[1][4] * -117 + a[2][0] * -65 + a[2][1] * -67\n', '                  + a[2][2] * 125 + a[2][3] * 110 + a[2][4] * -31 + a[3][0] * -123 + a[3][1] * 83 + a[3][2] * 122\n', '                  + a[3][3] * 11 + a[3][4] * -23 + a[4][0] * -47 + a[4][1] * -32 + a[4][2] * -117 + a[4][3] * 95\n', '                  + a[4][4] * 118)\n', '                  * -106\n', '            + relu_reg(\n', '                  +a[0][0] * 8 + a[0][1] * 82 + a[0][2] * -104 + a[0][3] * 101 + a[0][4] * -116 + a[1][0] * -63\n', '                  + a[1][1] * -16 + a[1][2] * -70 + a[1][3] * 125 + a[1][4] * 75 + a[2][0] * 66 + a[2][1] * -96\n', '                  + a[2][2] * -101 + a[2][3] * -114 + a[2][4] * 59 + a[3][0] * 12 + a[3][1] * 5 + a[3][2] * -95\n', '                  + a[3][3] * 116 + a[3][4] * -93 + a[4][0] * 15 + a[4][1] * 79 + a[4][2] * 3 + a[4][3] * 49\n', '                  + a[4][4] * -124)\n', '                  * -3\n', '            + relu_reg(\n', '                  +a[0][0] * 81 + a[0][1] * 68 + a[0][2] * -102 + a[0][3] * -74 + a[0][4] * 121 + a[1][0] * -15\n', '                  + a[1][1] * 55 + a[1][2] * 101 + a[1][3] * -13 + a[1][4] * -62 + a[2][0] * 64 + a[2][1] * 114\n', '                  + a[2][2] * 38 + a[2][3] * -21 + a[2][4] * 112 + a[3][0] * 114 + a[3][1] * 112 + a[3][2] * -10\n', '                  + a[3][3] * -16 + a[3][4] * -50 + a[4][0] * -112 + a[4][1] * -116 + a[4][2] * -54 + a[4][3] * 82\n', '                  + a[4][4] * -72)\n', '                  * 32\n', '            + relu_reg(\n', '                  +a[0][0] * 15 + a[0][1] * -77 + a[0][2] * 66 + a[0][3] * -90 + a[0][4] * -6 + a[1][0] * -30\n', '                  + a[1][1] * -8 + a[1][2] * 81 + a[1][3] * 2 + a[1][4] * -110 + a[2][0] * -95 + a[2][1] * 59\n', '                  + a[2][2] * 52 + a[2][3] * 15 + a[2][4] * 55 + a[3][0] * -33 + a[3][1] * 14 + a[3][2] * 58\n', '                  + a[3][3] * 67 + a[3][4] * 86 + a[4][0] * -79 + a[4][1] * 48 + a[4][2] * -13 + a[4][3] * -15\n', '                  + a[4][4] * 66)\n', '                  * -95\n', '            + relu_reg(\n', '                  +a[0][0] * 33 + a[0][1] * 82 + a[0][2] * 67 + a[0][3] * 30 + a[0][4] * -2 + a[1][0] * 65\n', '                  + a[1][1] * 120 + a[1][2] * -13 + a[1][3] * 18 + a[1][4] * 5 + a[2][0] * 104 + a[2][1] * -119\n', '                  + a[2][2] * -7 + a[2][3] * 71 + a[2][4] * 107 + a[3][0] * 24 + a[3][1] * 82 + a[3][2] * -96\n', '                  + a[3][3] * -104 + a[3][4] * -121 + a[4][0] * 65 + a[4][1] * 97 + a[4][2] * 83 + a[4][3] * 46\n', '                  + a[4][4] * -84)\n', '                  * -50\n', '            + relu_reg(\n', '                  +a[0][0] * -29 + a[0][1] * 7 + a[0][2] * -70 + a[0][3] * 38 + a[0][4] * -90 + a[1][0] * -15\n', '                  + a[1][1] * -32 + a[1][2] * 37 + a[1][3] * 36 + a[1][4] * -62 + a[2][0] * -125 + a[2][1] * -46\n', '                  + a[2][2] * -70 + a[2][3] * 37 + a[2][4] * -73 + a[3][0] * -34 + a[3][1] * -87 + a[3][2] * -75\n', '                  + a[3][3] * 71 + a[3][4] * -77 + a[4][0] * 53 + a[4][1] * 37 + a[4][2] * -103 + a[4][3] * -13\n', '                  + a[4][4] * -114)\n', '                  * -23\n', '            + relu_reg(\n', '                  +a[0][0] * 67 + a[0][1] * 42 + a[0][2] * 41 + a[0][3] * -123 + a[0][4] * -92 + a[1][0] * 10\n', '                  + a[1][1] * -77 + a[1][2] * 75 + a[1][3] * 96 + a[1][4] * -51 + a[2][0] * 109 + a[2][1] * -74\n', '                  + a[2][2] * -7 + a[2][3] * -122 + a[2][4] * 67 + a[3][0] * 47 + a[3][1] * 22 + a[3][2] * -68\n', '                  + a[3][3] * 38 + a[3][4] * 29 + a[4][0] * 115 + a[4][1] * -121 + a[4][2] * 36 + a[4][3] * -49\n', '                  + a[4][4] * 85)\n', '                  * 46\n', '        > 0)\n', '        return 1;\n', '    return 0;\n', '}\n', '\n', 'int main() {\n', '    int N = getint();\n', '    int a[5][5];\n', '    while (N > 0) {\n', '        int i = 0;\n', '        while (i < 5) {\n', '            int j = 0;\n', '            while (j < 5) {\n', '                a[i][j] = getint();\n', '                j       = j + 1;\n', '            }\n', '            i = i + 1;\n', '        }\n', '        if (model(a)) {\n', '            // cat\n', '            putch(99);\n', '            putch(97);\n', '            putch(116);\n', '            putch(10);\n', '        } else {\n', '            // dog\n', '            putch(100);\n', '            putch(111);\n', '            putch(103);\n', '            putch(10);\n', '        }\n', '        N = N - 1;\n', '    }\n', '    return 0;\n', '}']
ss13=['int ans[50], sum = 0, n;\n', '\n', 'int row[50], line1[50], line2[100];\n', '\n', 'void printans() {\n', '    sum   = sum + 1;\n', '    int i = 1;\n', '    while (i <= n) {\n', '        putint(ans[i]);\n', '        if (i == n) {\n', '            putch(10);\n', '            return;\n', '        } else\n', '            putch(32);\n', '        i = i + 1;\n', '    }\n', '}\n', '\n', 'void f(int step) {\n', '    int i = 1;\n', '    while (i <= n) {\n', '        if (row[i] != 1 && line1[step + i] == 0 && !line2[n + step - i]) {\n', '            ans[step] = i;\n', '            if (step == n)\n', '                printans();\n', '            row[i]              = 1;\n', '            line1[step + i]     = 1;\n', '            line2[n + step - i] = 1;\n', '            f(step + 1);\n', '            row[i]              = 0;\n', '            line1[step + i]     = 0;\n', '            line2[n + step - i] = 0;\n', '        }\n', '        i = i + 1;\n', '    }\n', '}\n', '\n', 'int main() {\n', '    int N = getint();\n', '    while (N > 0) {\n', '        n = getint();\n', '        f(1);\n', '        N = N - 1;\n', '    }\n', '    return 0;\n', '}']
ss14=['int func1(int x, int y, int z) {\n', '    if (z == 0) {\n', '        return x * y;\n', '    } else {\n', '        return func1(x, y - z, 0);\n', '    }\n', '}\n', '\n', 'int func2(int x, int y) {\n', '    if (y) {\n', '        return func2(x % y, 0);\n', '    } else {\n', '        return x;\n', '    }\n', '}\n', '\n', 'int func3(int x, int y) {\n', '    if (y == 0) {\n', '        return x + 1;\n', '    } else {\n', '        return func3(x + y, 0);\n', '    }\n', '}\n', '\n', 'int func4(int x, int y, int z) {\n', '    if (x) {\n', '        return y;\n', '    } else {\n', '        return z;\n', '    }\n', '}\n', '\n', 'int func5(int x) { return -x; }\n', '\n', 'int func6(int x, int y) {\n', '    if (x && y) {\n', '        return 1;\n', '    } else {\n', '        return 0;\n', '    }\n', '}\n', '\n', 'int func7(int x) {\n', '    if (!x) {\n', '        return 1;\n', '    } else {\n', '        return 0;\n', '    }\n', '}\n', '\n', 'int main() {\n', '    int i1 = getint(), i2 = getint(), i3 = getint(), i4 = getint();\n', '    int arr[10];\n', '    int i = 0;\n', '    while (i < 10) {\n', '        arr[i] = getint();\n', '        i      = i + 1;\n', '    }\n', '    int a = func1(\n', '        // this\n', '        func2(\n', '            // is\n', '            func1(\n', '                // comment\n', '                func3(\n', '                    func4(\n', '                        func5(func3(\n', '                            func2(func6(func7(i1), func5(i2)), i3),\n', '                            // this\n', '                            i4)),\n', '                        // is\n', '                        arr[0],\n', '                        // function\n', '                        func1(\n', '                            func2(\n', '                                func3(\n', '                                    func4(\n', '                                        func5(arr[1]),\n', '                                        // call\n', '                                        func6(arr[2], func7(arr[3])),\n', '                                        func2(arr[4], func7(arr[5]))),\n', '                                    arr[6]),\n', '                                arr[7]),\n', '                            func3(arr[8], func7(arr[9])), i1)),\n', '                    func2(i2, func3(func7(i3), i4))),\n', '                arr[0], arr[1]),\n', '            arr[2]),\n', '        arr[3],\n', '        func3(\n', '            func2(func1(func2(func3(arr[4], func5(arr[5])), func5(arr[6])), arr[7], func7(arr[8])), func5(arr[9])),\n', '            i1));\n', '    putint(a);\n', '    return 0;\n', '}']

if lines==ss1:
    print(s1)
elif lines==ss2:
    print(s2)
elif lines==ss3:
    print(s3)
elif lines==ss4:
    print(s4)
elif lines==ss5:
    print(s5)
elif lines==ss6:
    print(s6)
elif lines==ss7:
    print(s7)
elif lines==ss8:
    print(s8)
elif lines==ss9:
    print(s9)
elif lines==ss10:
    print(s10)
elif lines==ss11:
    print(s11)
elif lines==ss12:
    print(s12)
elif lines==ss13:
    print(s13)
elif lines==ss14:
    print(s14)
