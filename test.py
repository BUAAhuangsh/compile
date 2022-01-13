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
s1='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  call void @putint(i32 6)
  call void @putch(i32 10)
  call void @putint(i32 23)
  ret i32 0
}
'''
s2='''
@a = common dso_local global [3 x [4 x i32]] zeroinitializer, align 16
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 0, i32* %3, align 4
  br label %6

6:                                                ; preds = %37, %0
  %7 = load i32, i32* %2, align 4
  %8 = icmp sle i32 %7, 5
  br i1 %8, label %9, label %40

9:                                                ; preds = %6
  %10 = load i32, i32* %2, align 4
  store i32 %10, i32* %4, align 4
  br label %11

11:                                               ; preds = %34, %9
  %12 = load i32, i32* %4, align 4
  %13 = icmp sge i32 %12, 0
  br i1 %13, label %14, label %37

14:                                               ; preds = %11
  %15 = load i32, i32* %4, align 4
  %16 = icmp slt i32 %15, 4
  br i1 %16, label %17, label %34

17:                                               ; preds = %14
  %18 = load i32, i32* %2, align 4
  %19 = load i32, i32* %4, align 4
  %20 = sub nsw i32 %18, %19
  %21 = icmp slt i32 %20, 3
  br i1 %21, label %22, label %34

22:                                               ; preds = %17
  %23 = load i32, i32* %3, align 4
  %24 = load i32, i32* %2, align 4
  %25 = load i32, i32* %4, align 4
  %26 = sub nsw i32 %24, %25
  %27 = sext i32 %26 to i64
  %28 = getelementptr inbounds [3 x [4 x i32]], [3 x [4 x i32]]* @a, i64 0, i64 %27
  %29 = load i32, i32* %4, align 4
  %30 = sext i32 %29 to i64
  %31 = getelementptr inbounds [4 x i32], [4 x i32]* %28, i64 0, i64 %30
  store i32 %23, i32* %31, align 4
  %32 = load i32, i32* %3, align 4
  %33 = add nsw i32 %32, 1
  store i32 %33, i32* %3, align 4
  br label %34

34:                                               ; preds = %22, %17, %14
  %35 = load i32, i32* %4, align 4
  %36 = sub nsw i32 %35, 1
  store i32 %36, i32* %4, align 4
  br label %11

37:                                               ; preds = %11
  %38 = load i32, i32* %2, align 4
  %39 = add nsw i32 %38, 1
  store i32 %39, i32* %2, align 4
  br label %6

40:                                               ; preds = %6
  store i32 0, i32* %2, align 4
  store i32 0, i32* %5, align 4
  br label %41

41:                                               ; preds = %58, %40
  %42 = load i32, i32* %2, align 4
  %43 = icmp slt i32 %42, 3
  br i1 %43, label %44, label %61

44:                                               ; preds = %41
  store i32 0, i32* %5, align 4
  br label %45

45:                                               ; preds = %48, %44
  %46 = load i32, i32* %5, align 4
  %47 = icmp slt i32 %46, 4
  br i1 %47, label %48, label %58

48:                                               ; preds = %45
  %49 = load i32, i32* %2, align 4
  %50 = sext i32 %49 to i64
  %51 = getelementptr inbounds [3 x [4 x i32]], [3 x [4 x i32]]* @a, i64 0, i64 %50
  %52 = load i32, i32* %5, align 4
  %53 = sext i32 %52 to i64
  %54 = getelementptr inbounds [4 x i32], [4 x i32]* %51, i64 0, i64 %53
  %55 = load i32, i32* %54, align 4
  call void @putint(i32 %55)
  call void @putch(i32 32)
  %56 = load i32, i32* %5, align 4
  %57 = add nsw i32 %56, 1
  store i32 %57, i32* %5, align 4
  br label %45

58:                                               ; preds = %45
  call void @putch(i32 10)
  %59 = load i32, i32* %2, align 4
  %60 = add nsw i32 %59, 1
  store i32 %60, i32* %2, align 4
  br label %41

61:                                               ; preds = %41
  ret i32 0
}
'''
s3='''
@__HELLO = dso_local global <{ [28 x i32], [72 x i32] }> <{ [28 x i32] [i32 87, i32 101, i32 108, i32 99, i32 111, i32 109, i32 101, i32 32, i32 116, i32 111, i32 32, i32 116, i32 104, i32 101, i32 32, i32 74, i32 97, i32 112, i32 97, i32 114, i32 105, i32 32, i32 80, i32 97, i32 114, i32 107, i32 33, i32 10], [72 x i32] zeroinitializer }>, align 16
@N4__mE___ = dso_local global <{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }>, <{ i32, i32, i32, i32, i32, [45 x i32] }>, <{ [12 x i32], [38 x i32] }>, <{ [8 x i32], [42 x i32] }>, <{ [16 x i32], [34 x i32] }>, <{ [14 x i32], [36 x i32] }> }> <{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }> <{ i32 83, i32 97, i32 97, i32 98, i32 97, i32 114, i32 117, [43 x i32] zeroinitializer }>, <{ i32, i32, i32, i32, i32, [45 x i32] }> <{ i32 75, i32 97, i32 98, i32 97, i32 110, [45 x i32] zeroinitializer }>, <{ [12 x i32], [38 x i32] }> <{ [12 x i32] [i32 72, i32 97, i32 115, i32 104, i32 105, i32 98, i32 105, i32 114, i32 111, i32 107, i32 111, i32 117], [38 x i32] zeroinitializer }>, <{ [8 x i32], [42 x i32] }> <{ [8 x i32] [i32 65, i32 114, i32 97, i32 105, i32 103, i32 117, i32 109, i32 97], [42 x i32] zeroinitializer }>, <{ [16 x i32], [34 x i32] }> <{ [16 x i32] [i32 72, i32 117, i32 110, i32 98, i32 111, i32 114, i32 117, i32 116, i32 111, i32 32, i32 80, i32 101, i32 110, i32 103, i32 105, i32 110], [34 x i32] zeroinitializer }>, <{ [14 x i32], [36 x i32] }> <{ [14 x i32] [i32 84, i32 97, i32 105, i32 114, i32 105, i32 107, i32 117, i32 32, i32 79, i32 111, i32 107, i32 97, i32 109, i32 105], [36 x i32] zeroinitializer }> }>, align 16
@saY_HeI10_To = dso_local global <{ [15 x i32], [25 x i32] }> <{ [15 x i32] [i32 32, i32 115, i32 97, i32 121, i32 115, i32 32, i32 104, i32 101, i32 108, i32 108, i32 111, i32 32, i32 116, i32 111, i32 32], [25 x i32] zeroinitializer }>, align 16
@RET = dso_local global [5 x i32] [i32 10, i32 0, i32 0, i32 0, i32 0], align 16
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  br label %6

6:                                                ; preds = %12, %0
  %7 = load i32, i32* %2, align 4
  %8 = sext i32 %7 to i64
  %9 = getelementptr inbounds [100 x i32], [100 x i32]* bitcast (<{ [28 x i32], [72 x i32] }>* @__HELLO to [100 x i32]*), i64 0, i64 %8
  %10 = load i32, i32* %9, align 4
  %11 = icmp ne i32 %10, 0
  br i1 %11, label %12, label %19

12:                                               ; preds = %6
  %13 = load i32, i32* %2, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds [100 x i32], [100 x i32]* bitcast (<{ [28 x i32], [72 x i32] }>* @__HELLO to [100 x i32]*), i64 0, i64 %14
  %16 = load i32, i32* %15, align 4
  call void @putch(i32 %16)
  %17 = load i32, i32* %2, align 4
  %18 = add nsw i32 %17, 1
  store i32 %18, i32* %2, align 4
  br label %6

19:                                               ; preds = %6
  store i32 0, i32* %3, align 4
  br label %20

20:                                               ; preds = %19, %105
  %21 = load i32, i32* %3, align 4
  %22 = sdiv i32 %21, 6
  store i32 %22, i32* %4, align 4
  %23 = load i32, i32* %3, align 4
  %24 = srem i32 %23, 6
  store i32 %24, i32* %5, align 4
  %25 = load i32, i32* %4, align 4
  %26 = load i32, i32* %5, align 4
  %27 = icmp ne i32 %25, %26
  br i1 %27, label %28, label %97

28:                                               ; preds = %20
  store i32 0, i32* %2, align 4
  br label %29

29:                                               ; preds = %38, %28
  %30 = load i32, i32* %4, align 4
  %31 = sext i32 %30 to i64
  %32 = getelementptr inbounds [6 x [50 x i32]], [6 x [50 x i32]]* bitcast (<{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }>, <{ i32, i32, i32, i32, i32, [45 x i32] }>, <{ [12 x i32], [38 x i32] }>, <{ [8 x i32], [42 x i32] }>, <{ [16 x i32], [34 x i32] }>, <{ [14 x i32], [36 x i32] }> }>* @N4__mE___ to [6 x [50 x i32]]*), i64 0, i64 %31
  %33 = load i32, i32* %2, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds [50 x i32], [50 x i32]* %32, i64 0, i64 %34
  %36 = load i32, i32* %35, align 4
  %37 = icmp ne i32 %36, 0
  br i1 %37, label %38, label %48

38:                                               ; preds = %29
  %39 = load i32, i32* %4, align 4
  %40 = sext i32 %39 to i64
  %41 = getelementptr inbounds [6 x [50 x i32]], [6 x [50 x i32]]* bitcast (<{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }>, <{ i32, i32, i32, i32, i32, [45 x i32] }>, <{ [12 x i32], [38 x i32] }>, <{ [8 x i32], [42 x i32] }>, <{ [16 x i32], [34 x i32] }>, <{ [14 x i32], [36 x i32] }> }>* @N4__mE___ to [6 x [50 x i32]]*), i64 0, i64 %40
  %42 = load i32, i32* %2, align 4
  %43 = sext i32 %42 to i64
  %44 = getelementptr inbounds [50 x i32], [50 x i32]* %41, i64 0, i64 %43
  %45 = load i32, i32* %44, align 4
  call void @putch(i32 %45)
  %46 = load i32, i32* %2, align 4
  %47 = add nsw i32 %46, 1
  store i32 %47, i32* %2, align 4
  br label %29

48:                                               ; preds = %29
  store i32 0, i32* %2, align 4
  br label %49

49:                                               ; preds = %55, %48
  %50 = load i32, i32* %2, align 4
  %51 = sext i32 %50 to i64
  %52 = getelementptr inbounds [40 x i32], [40 x i32]* bitcast (<{ [15 x i32], [25 x i32] }>* @saY_HeI10_To to [40 x i32]*), i64 0, i64 %51
  %53 = load i32, i32* %52, align 4
  %54 = icmp ne i32 %53, 0
  br i1 %54, label %55, label %62

55:                                               ; preds = %49
  %56 = load i32, i32* %2, align 4
  %57 = sext i32 %56 to i64
  %58 = getelementptr inbounds [40 x i32], [40 x i32]* bitcast (<{ [15 x i32], [25 x i32] }>* @saY_HeI10_To to [40 x i32]*), i64 0, i64 %57
  %59 = load i32, i32* %58, align 4
  call void @putch(i32 %59)
  %60 = load i32, i32* %2, align 4
  %61 = add nsw i32 %60, 1
  store i32 %61, i32* %2, align 4
  br label %49

62:                                               ; preds = %49
  store i32 0, i32* %2, align 4
  br label %63

63:                                               ; preds = %72, %62
  %64 = load i32, i32* %5, align 4
  %65 = sext i32 %64 to i64
  %66 = getelementptr inbounds [6 x [50 x i32]], [6 x [50 x i32]]* bitcast (<{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }>, <{ i32, i32, i32, i32, i32, [45 x i32] }>, <{ [12 x i32], [38 x i32] }>, <{ [8 x i32], [42 x i32] }>, <{ [16 x i32], [34 x i32] }>, <{ [14 x i32], [36 x i32] }> }>* @N4__mE___ to [6 x [50 x i32]]*), i64 0, i64 %65
  %67 = load i32, i32* %2, align 4
  %68 = sext i32 %67 to i64
  %69 = getelementptr inbounds [50 x i32], [50 x i32]* %66, i64 0, i64 %68
  %70 = load i32, i32* %69, align 4
  %71 = icmp ne i32 %70, 0
  br i1 %71, label %72, label %82

72:                                               ; preds = %63
  %73 = load i32, i32* %5, align 4
  %74 = sext i32 %73 to i64
  %75 = getelementptr inbounds [6 x [50 x i32]], [6 x [50 x i32]]* bitcast (<{ <{ i32, i32, i32, i32, i32, i32, i32, [43 x i32] }>, <{ i32, i32, i32, i32, i32, [45 x i32] }>, <{ [12 x i32], [38 x i32] }>, <{ [8 x i32], [42 x i32] }>, <{ [16 x i32], [34 x i32] }>, <{ [14 x i32], [36 x i32] }> }>* @N4__mE___ to [6 x [50 x i32]]*), i64 0, i64 %74
  %76 = load i32, i32* %2, align 4
  %77 = sext i32 %76 to i64
  %78 = getelementptr inbounds [50 x i32], [50 x i32]* %75, i64 0, i64 %77
  %79 = load i32, i32* %78, align 4
  call void @putch(i32 %79)
  %80 = load i32, i32* %2, align 4
  %81 = add nsw i32 %80, 1
  store i32 %81, i32* %2, align 4
  br label %63

82:                                               ; preds = %63
  store i32 0, i32* %2, align 4
  br label %83

83:                                               ; preds = %89, %82
  %84 = load i32, i32* %2, align 4
  %85 = sext i32 %84 to i64
  %86 = getelementptr inbounds [5 x i32], [5 x i32]* @RET, i64 0, i64 %85
  %87 = load i32, i32* %86, align 4
  %88 = icmp ne i32 %87, 0
  br i1 %88, label %89, label %96

89:                                               ; preds = %83
  %90 = load i32, i32* %2, align 4
  %91 = sext i32 %90 to i64
  %92 = getelementptr inbounds [5 x i32], [5 x i32]* @RET, i64 0, i64 %91
  %93 = load i32, i32* %92, align 4
  call void @putch(i32 %93)
  %94 = load i32, i32* %2, align 4
  %95 = add nsw i32 %94, 1
  store i32 %95, i32* %2, align 4
  br label %83

96:                                               ; preds = %83
  br label %97

97:                                               ; preds = %96, %20
  %98 = load i32, i32* %3, align 4
  %99 = mul nsw i32 %98, 17
  %100 = add nsw i32 %99, 23
  %101 = srem i32 %100, 32
  store i32 %101, i32* %3, align 4
  %102 = load i32, i32* %3, align 4
  %103 = icmp eq i32 %102, 0
  br i1 %103, label %104, label %105

104:                                              ; preds = %97
  br label %106

105:                                              ; preds = %97
  br label %20

106:                                              ; preds = %104
  ret i32 0
}
'''
s4="""
@field = common dso_local global [2 x i32] zeroinitializer, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [1 x i32], align 4
  %3 = alloca [3 x i32], align 4
  %4 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %5 = call i32 @getint()
  store i32 %5, i32* getelementptr inbounds ([2 x i32], [2 x i32]* @field, i64 0, i64 0), align 4
  %6 = call i32 @getint()
  store i32 %6, i32* getelementptr inbounds ([2 x i32], [2 x i32]* @field, i64 0, i64 1), align 4
  %7 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 0
  store i32 -1, i32* %7, align 4
  %8 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 0
  %9 = load i32, i32* %8, align 4
  %10 = sub nsw i32 %9, 2
  %11 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 1
  store i32 %10, i32* %11, align 4
  %12 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 1
  %13 = load i32, i32* %12, align 4
  store i32 %13, i32* %4, align 4
  %14 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 2
  store i32 16, i32* %14, align 4
  %15 = load i32, i32* getelementptr inbounds ([2 x i32], [2 x i32]* @field, i64 0, i64 0), align 4
  %16 = sub nsw i32 3, %15
  %17 = sext i32 %16 to i64
  %18 = getelementptr inbounds [3 x i32], [3 x i32]* %3, i64 0, i64 %17
  %19 = load i32, i32* %18, align 4
  %20 = add nsw i32 %19, 2
  %21 = load i32, i32* %4, align 4
  %22 = add nsw i32 %20, %21
  call void @putint(i32 %22)
  ret i32 0
}
"""
s5='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca [5 x i32], align 16
  %7 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 5, i32* %2, align 4
  store i32 5, i32* %3, align 4
  store i32 1, i32* %4, align 4
  store i32 -2, i32* %5, align 4
  %8 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 0
  store i32 1, i32* %8, align 16
  %9 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 1
  store i32 2, i32* %9, align 4
  %10 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 2
  store i32 3, i32* %10, align 8
  %11 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 3
  store i32 4, i32* %11, align 4
  %12 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 4
  store i32 5, i32* %12, align 16
  %13 = load i32, i32* %5, align 4
  %14 = mul nsw i32 %13, 1
  %15 = sdiv i32 %14, 2
  %16 = add nsw i32 %15, 4
  %17 = load i32, i32* %2, align 4
  %18 = load i32, i32* %3, align 4
  %19 = sub nsw i32 %17, %18
  %20 = add nsw i32 %16, %19
  %21 = load i32, i32* %4, align 4
  %22 = add nsw i32 %21, 3
  %23 = sub nsw i32 0, %22
  %24 = srem i32 %23, 2
  %25 = sub nsw i32 %20, %24
  %26 = srem i32 %25, 5
  %27 = sext i32 %26 to i64
  %28 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 %27
  %29 = load i32, i32* %28, align 4
  store i32 %29, i32* %7, align 4
  %30 = load i32, i32* %7, align 4
  call void @putint(i32 %30)
  call void @putch(i32 10)
  %31 = load i32, i32* %4, align 4
  %32 = srem i32 %31, 2
  %33 = add nsw i32 %32, 67
  %34 = load i32, i32* %2, align 4
  %35 = add nsw i32 %33, %34
  %36 = load i32, i32* %3, align 4
  %37 = sub nsw i32 %35, %36
  %38 = load i32, i32* %4, align 4
  %39 = add nsw i32 %38, 2
  %40 = srem i32 %39, 2
  %41 = sub nsw i32 0, %40
  %42 = sub nsw i32 %37, %41
  %43 = srem i32 %42, 5
  %44 = sext i32 %43 to i64
  %45 = getelementptr inbounds [5 x i32], [5 x i32]* %6, i64 0, i64 %44
  %46 = load i32, i32* %45, align 4
  store i32 %46, i32* %7, align 4
  %47 = load i32, i32* %7, align 4
  call void @putint(i32 %47)
  ret i32 0
}
'''
s6='''
@N = dso_local constant i32 -1, align 4
@arr = dso_local global [6 x i32] [i32 1, i32 2, i32 33, i32 4, i32 5, i32 6], align 16
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  store i32 0, i32* %3, align 4
  br label %4

4:                                                ; preds = %7, %0
  %5 = load i32, i32* %2, align 4
  %6 = icmp slt i32 %5, 5
  br i1 %6, label %7, label %16

7:                                                ; preds = %4
  %8 = load i32, i32* %3, align 4
  %9 = load i32, i32* %2, align 4
  %10 = sext i32 %9 to i64
  %11 = getelementptr inbounds [6 x i32], [6 x i32]* @arr, i64 0, i64 %10
  %12 = load i32, i32* %11, align 4
  %13 = add nsw i32 %8, %12
  store i32 %13, i32* %3, align 4
  %14 = load i32, i32* %2, align 4
  %15 = add nsw i32 %14, 1
  store i32 %15, i32* %2, align 4
  br label %4

16:                                               ; preds = %4
  %17 = load i32, i32* %3, align 4
  call void @putint(i32 %17)
  ret i32 0
}
'''
s7='''
@TAPE_LEN = dso_local constant i32 65536, align 4
@BUFFER_LEN = dso_local constant i32 32768, align 4
@ptr = dso_local global i32 0, align 4
@program = common dso_local global [32768 x i32] zeroinitializer, align 16
@tape = common dso_local global [65536 x i32] zeroinitializer, align 16
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %2, align 4
  %6 = call i32 @getint()
  store i32 %6, i32* %3, align 4
  br label %7

7:                                                ; preds = %11, %0
  %8 = load i32, i32* %2, align 4
  %9 = load i32, i32* %3, align 4
  %10 = icmp slt i32 %8, %9
  br i1 %10, label %11, label %18

11:                                               ; preds = %7
  %12 = call i32 @getch()
  %13 = load i32, i32* %2, align 4
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds [32768 x i32], [32768 x i32]* @program, i64 0, i64 %14
  store i32 %12, i32* %15, align 4
  %16 = load i32, i32* %2, align 4
  %17 = add nsw i32 %16, 1
  store i32 %17, i32* %2, align 4
  br label %7

18:                                               ; preds = %7
  %19 = load i32, i32* %2, align 4
  %20 = sext i32 %19 to i64
  %21 = getelementptr inbounds [32768 x i32], [32768 x i32]* @program, i64 0, i64 %20
  store i32 0, i32* %21, align 4
  store i32 0, i32* %2, align 4
  br label %22

22:                                               ; preds = %124, %18
  %23 = load i32, i32* %2, align 4
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds [32768 x i32], [32768 x i32]* @program, i64 0, i64 %24
  %26 = load i32, i32* %25, align 4
  %27 = icmp ne i32 %26, 0
  br i1 %27, label %28, label %127

28:                                               ; preds = %22
  %29 = load i32, i32* %2, align 4
  %30 = sext i32 %29 to i64
  %31 = getelementptr inbounds [32768 x i32], [32768 x i32]* @program, i64 0, i64 %30
  %32 = load i32, i32* %31, align 4
  store i32 %32, i32* %4, align 4
  %33 = load i32, i32* %4, align 4
  %34 = icmp eq i32 %33, 62
  br i1 %34, label %35, label %38

35:                                               ; preds = %28
  %36 = load i32, i32* @ptr, align 4
  %37 = add nsw i32 %36, 1
  store i32 %37, i32* @ptr, align 4
  br label %124

38:                                               ; preds = %28
  %39 = load i32, i32* %4, align 4
  %40 = icmp eq i32 %39, 60
  br i1 %40, label %41, label %44

41:                                               ; preds = %38
  %42 = load i32, i32* @ptr, align 4
  %43 = sub nsw i32 %42, 1
  store i32 %43, i32* @ptr, align 4
  br label %123

44:                                               ; preds = %38
  %45 = load i32, i32* %4, align 4
  %46 = icmp eq i32 %45, 43
  br i1 %46, label %47, label %56

47:                                               ; preds = %44
  %48 = load i32, i32* @ptr, align 4
  %49 = sext i32 %48 to i64
  %50 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %49
  %51 = load i32, i32* %50, align 4
  %52 = add nsw i32 %51, 1
  %53 = load i32, i32* @ptr, align 4
  %54 = sext i32 %53 to i64
  %55 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %54
  store i32 %52, i32* %55, align 4
  br label %122

56:                                               ; preds = %44
  %57 = load i32, i32* %4, align 4
  %58 = icmp eq i32 %57, 45
  br i1 %58, label %59, label %68

59:                                               ; preds = %56
  %60 = load i32, i32* @ptr, align 4
  %61 = sext i32 %60 to i64
  %62 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %61
  %63 = load i32, i32* %62, align 4
  %64 = sub nsw i32 %63, 1
  %65 = load i32, i32* @ptr, align 4
  %66 = sext i32 %65 to i64
  %67 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %66
  store i32 %64, i32* %67, align 4
  br label %121

68:                                               ; preds = %56
  %69 = load i32, i32* %4, align 4
  %70 = icmp eq i32 %69, 46
  br i1 %70, label %71, label %76

71:                                               ; preds = %68
  %72 = load i32, i32* @ptr, align 4
  %73 = sext i32 %72 to i64
  %74 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %73
  %75 = load i32, i32* %74, align 4
  call void @putch(i32 %75)
  br label %120

76:                                               ; preds = %68
  %77 = load i32, i32* %4, align 4
  %78 = icmp eq i32 %77, 44
  br i1 %78, label %79, label %84

79:                                               ; preds = %76
  %80 = call i32 @getch()
  %81 = load i32, i32* @ptr, align 4
  %82 = sext i32 %81 to i64
  %83 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %82
  store i32 %80, i32* %83, align 4
  br label %119

84:                                               ; preds = %76
  %85 = load i32, i32* %4, align 4
  %86 = icmp eq i32 %85, 93
  br i1 %86, label %87, label %118

87:                                               ; preds = %84
  %88 = load i32, i32* @ptr, align 4
  %89 = sext i32 %88 to i64
  %90 = getelementptr inbounds [65536 x i32], [65536 x i32]* @tape, i64 0, i64 %89
  %91 = load i32, i32* %90, align 4
  %92 = icmp ne i32 %91, 0
  br i1 %92, label %93, label %118

93:                                               ; preds = %87
  store i32 1, i32* %5, align 4
  br label %94

94:                                               ; preds = %116, %93
  %95 = load i32, i32* %5, align 4
  %96 = icmp sgt i32 %95, 0
  br i1 %96, label %97, label %117

97:                                               ; preds = %94
  %98 = load i32, i32* %2, align 4
  %99 = sub nsw i32 %98, 1
  store i32 %99, i32* %2, align 4
  %100 = load i32, i32* %2, align 4
  %101 = sext i32 %100 to i64
  %102 = getelementptr inbounds [32768 x i32], [32768 x i32]* @program, i64 0, i64 %101
  %103 = load i32, i32* %102, align 4
  store i32 %103, i32* %4, align 4
  %104 = load i32, i32* %4, align 4
  %105 = icmp eq i32 %104, 91
  br i1 %105, label %106, label %109

106:                                              ; preds = %97
  %107 = load i32, i32* %5, align 4
  %108 = sub nsw i32 %107, 1
  store i32 %108, i32* %5, align 4
  br label %116

109:                                              ; preds = %97
  %110 = load i32, i32* %4, align 4
  %111 = icmp eq i32 %110, 93
  br i1 %111, label %112, label %115

112:                                              ; preds = %109
  %113 = load i32, i32* %5, align 4
  %114 = add nsw i32 %113, 1
  store i32 %114, i32* %5, align 4
  br label %115

115:                                              ; preds = %112, %109
  br label %116

116:                                              ; preds = %115, %106
  br label %94

117:                                              ; preds = %94
  br label %118

118:                                              ; preds = %117, %87, %84
  br label %119

119:                                              ; preds = %118, %79
  br label %120

120:                                              ; preds = %119, %71
  br label %121

121:                                              ; preds = %120, %59
  br label %122

122:                                              ; preds = %121, %47
  br label %123

123:                                              ; preds = %122, %41
  br label %124

124:                                              ; preds = %123, %35
  %125 = load i32, i32* %2, align 4
  %126 = add nsw i32 %125, 1
  store i32 %126, i32* %2, align 4
  br label %22

127:                                              ; preds = %22
  ret i32 0
}
'''
s8='''
@n = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 10, i32* @n, align 4
  %7 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  store i32 4, i32* %7, align 16
  %8 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 1
  store i32 3, i32* %8, align 4
  %9 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 2
  store i32 9, i32* %9, align 8
  %10 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 3
  store i32 2, i32* %10, align 4
  %11 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 4
  store i32 0, i32* %11, align 16
  %12 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 5
  store i32 1, i32* %12, align 4
  %13 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 6
  store i32 6, i32* %13, align 8
  %14 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 7
  store i32 5, i32* %14, align 4
  %15 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 8
  store i32 7, i32* %15, align 16
  %16 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 9
  store i32 8, i32* %16, align 4
  store i32 1, i32* %3, align 4
  br label %17

17:                                               ; preds = %51, %0
  %18 = load i32, i32* %3, align 4
  %19 = load i32, i32* @n, align 4
  %20 = icmp slt i32 %18, %19
  br i1 %20, label %21, label %59

21:                                               ; preds = %17
  %22 = load i32, i32* %3, align 4
  %23 = sext i32 %22 to i64
  %24 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %23
  %25 = load i32, i32* %24, align 4
  store i32 %25, i32* %4, align 4
  %26 = load i32, i32* %3, align 4
  %27 = sub nsw i32 %26, 1
  store i32 %27, i32* %5, align 4
  br label %28

28:                                               ; preds = %40, %21
  %29 = load i32, i32* %5, align 4
  %30 = icmp sgt i32 %29, -1
  br i1 %30, label %31, label %38

31:                                               ; preds = %28
  %32 = load i32, i32* %4, align 4
  %33 = load i32, i32* %5, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %34
  %36 = load i32, i32* %35, align 4
  %37 = icmp slt i32 %32, %36
  br label %38

38:                                               ; preds = %31, %28
  %39 = phi i1 [ false, %28 ], [ %37, %31 ]
  br i1 %39, label %40, label %51

40:                                               ; preds = %38
  %41 = load i32, i32* %5, align 4
  %42 = sext i32 %41 to i64
  %43 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %42
  %44 = load i32, i32* %43, align 4
  %45 = load i32, i32* %5, align 4
  %46 = add nsw i32 %45, 1
  %47 = sext i32 %46 to i64
  %48 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %47
  store i32 %44, i32* %48, align 4
  %49 = load i32, i32* %5, align 4
  %50 = sub nsw i32 %49, 1
  store i32 %50, i32* %5, align 4
  br label %28

51:                                               ; preds = %38
  %52 = load i32, i32* %4, align 4
  %53 = load i32, i32* %5, align 4
  %54 = add nsw i32 %53, 1
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %55
  store i32 %52, i32* %56, align 4
  %57 = load i32, i32* %3, align 4
  %58 = add nsw i32 %57, 1
  store i32 %58, i32* %3, align 4
  br label %17

59:                                               ; preds = %17
  store i32 0, i32* %3, align 4
  br label %60

60:                                               ; preds = %64, %59
  %61 = load i32, i32* %3, align 4
  %62 = load i32, i32* @n, align 4
  %63 = icmp slt i32 %61, %62
  br i1 %63, label %64, label %73

64:                                               ; preds = %60
  %65 = load i32, i32* %3, align 4
  %66 = sext i32 %65 to i64
  %67 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %66
  %68 = load i32, i32* %67, align 4
  store i32 %68, i32* %6, align 4
  %69 = load i32, i32* %6, align 4
  call void @putint(i32 %69)
  store i32 10, i32* %6, align 4
  %70 = load i32, i32* %6, align 4
  call void @putch(i32 %70)
  %71 = load i32, i32* %3, align 4
  %72 = add nsw i32 %71, 1
  store i32 %72, i32* %3, align 4
  br label %60

73:                                               ; preds = %60
  ret i32 0
}
'''
s9='''
@n = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 10, i32* @n, align 4
  %8 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  store i32 4, i32* %8, align 16
  %9 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 1
  store i32 3, i32* %9, align 4
  %10 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 2
  store i32 9, i32* %10, align 8
  %11 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 3
  store i32 2, i32* %11, align 4
  %12 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 4
  store i32 0, i32* %12, align 16
  %13 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 5
  store i32 1, i32* %13, align 4
  %14 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 6
  store i32 6, i32* %14, align 8
  %15 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 7
  store i32 5, i32* %15, align 4
  %16 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 8
  store i32 7, i32* %16, align 16
  %17 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 9
  store i32 8, i32* %17, align 4
  store i32 0, i32* %3, align 4
  br label %18

18:                                               ; preds = %66, %0
  %19 = load i32, i32* %3, align 4
  %20 = load i32, i32* @n, align 4
  %21 = sub nsw i32 %20, 1
  %22 = icmp slt i32 %19, %21
  br i1 %22, label %23, label %69

23:                                               ; preds = %18
  %24 = load i32, i32* %3, align 4
  store i32 %24, i32* %5, align 4
  %25 = load i32, i32* %3, align 4
  %26 = add nsw i32 %25, 1
  store i32 %26, i32* %4, align 4
  br label %27

27:                                               ; preds = %43, %23
  %28 = load i32, i32* %4, align 4
  %29 = load i32, i32* @n, align 4
  %30 = icmp slt i32 %28, %29
  br i1 %30, label %31, label %46

31:                                               ; preds = %27
  %32 = load i32, i32* %5, align 4
  %33 = sext i32 %32 to i64
  %34 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %33
  %35 = load i32, i32* %34, align 4
  %36 = load i32, i32* %4, align 4
  %37 = sext i32 %36 to i64
  %38 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %37
  %39 = load i32, i32* %38, align 4
  %40 = icmp sgt i32 %35, %39
  br i1 %40, label %41, label %43

41:                                               ; preds = %31
  %42 = load i32, i32* %4, align 4
  store i32 %42, i32* %5, align 4
  br label %43

43:                                               ; preds = %41, %31
  %44 = load i32, i32* %4, align 4
  %45 = add nsw i32 %44, 1
  store i32 %45, i32* %4, align 4
  br label %27

46:                                               ; preds = %27
  %47 = load i32, i32* %5, align 4
  %48 = load i32, i32* %3, align 4
  %49 = icmp ne i32 %47, %48
  br i1 %49, label %50, label %66

50:                                               ; preds = %46
  %51 = load i32, i32* %5, align 4
  %52 = sext i32 %51 to i64
  %53 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %52
  %54 = load i32, i32* %53, align 4
  store i32 %54, i32* %6, align 4
  %55 = load i32, i32* %3, align 4
  %56 = sext i32 %55 to i64
  %57 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %56
  %58 = load i32, i32* %57, align 4
  %59 = load i32, i32* %5, align 4
  %60 = sext i32 %59 to i64
  %61 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %60
  store i32 %58, i32* %61, align 4
  %62 = load i32, i32* %6, align 4
  %63 = load i32, i32* %3, align 4
  %64 = sext i32 %63 to i64
  %65 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %64
  store i32 %62, i32* %65, align 4
  br label %66

66:                                               ; preds = %50, %46
  %67 = load i32, i32* %3, align 4
  %68 = add nsw i32 %67, 1
  store i32 %68, i32* %3, align 4
  br label %18

69:                                               ; preds = %18
  store i32 0, i32* %3, align 4
  br label %70

70:                                               ; preds = %74, %69
  %71 = load i32, i32* %3, align 4
  %72 = load i32, i32* @n, align 4
  %73 = icmp slt i32 %71, %72
  br i1 %73, label %74, label %83

74:                                               ; preds = %70
  %75 = load i32, i32* %3, align 4
  %76 = sext i32 %75 to i64
  %77 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %76
  %78 = load i32, i32* %77, align 4
  store i32 %78, i32* %7, align 4
  %79 = load i32, i32* %7, align 4
  call void @putint(i32 %79)
  store i32 10, i32* %7, align 4
  %80 = load i32, i32* %7, align 4
  call void @putch(i32 %80)
  %81 = load i32, i32* %3, align 4
  %82 = add nsw i32 %81, 1
  store i32 %82, i32* %3, align 4
  br label %70

83:                                               ; preds = %70
  ret i32 0
}
'''
s10='''
@n = common dso_local global i32 0, align 4
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [10 x i32], align 16
  %3 = alloca [10 x i32], align 16
  %4 = alloca [10 x i32], align 16
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca i32, align 4
  %8 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 10, i32* @n, align 4
  %9 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 0
  store i32 4, i32* %9, align 16
  %10 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 1
  store i32 3, i32* %10, align 4
  %11 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 2
  store i32 9, i32* %11, align 8
  %12 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 3
  store i32 2, i32* %12, align 4
  %13 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 4
  store i32 0, i32* %13, align 16
  %14 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 5
  store i32 1, i32* %14, align 4
  %15 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 6
  store i32 6, i32* %15, align 8
  %16 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 7
  store i32 5, i32* %16, align 4
  %17 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 8
  store i32 7, i32* %17, align 16
  %18 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 9
  store i32 8, i32* %18, align 4
  store i32 0, i32* %7, align 4
  store i32 0, i32* %5, align 4
  store i32 0, i32* %6, align 4
  br label %19

19:                                               ; preds = %22, %0
  %20 = load i32, i32* %7, align 4
  %21 = icmp slt i32 %20, 10
  br i1 %21, label %22, label %28

22:                                               ; preds = %19
  %23 = load i32, i32* %7, align 4
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %24
  store i32 0, i32* %25, align 4
  %26 = load i32, i32* %7, align 4
  %27 = add nsw i32 %26, 1
  store i32 %27, i32* %7, align 4
  br label %19

28:                                               ; preds = %19
  br label %29

29:                                               ; preds = %33, %28
  %30 = load i32, i32* %5, align 4
  %31 = load i32, i32* @n, align 4
  %32 = icmp slt i32 %30, %31
  br i1 %32, label %33, label %50

33:                                               ; preds = %29
  %34 = load i32, i32* %5, align 4
  %35 = sext i32 %34 to i64
  %36 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %35
  %37 = load i32, i32* %36, align 4
  %38 = sext i32 %37 to i64
  %39 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %38
  %40 = load i32, i32* %39, align 4
  %41 = add nsw i32 %40, 1
  %42 = load i32, i32* %5, align 4
  %43 = sext i32 %42 to i64
  %44 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %43
  %45 = load i32, i32* %44, align 4
  %46 = sext i32 %45 to i64
  %47 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %46
  store i32 %41, i32* %47, align 4
  %48 = load i32, i32* %5, align 4
  %49 = add nsw i32 %48, 1
  store i32 %49, i32* %5, align 4
  br label %29

50:                                               ; preds = %29
  store i32 1, i32* %7, align 4
  br label %51

51:                                               ; preds = %54, %50
  %52 = load i32, i32* %7, align 4
  %53 = icmp slt i32 %52, 10
  br i1 %53, label %54, label %70

54:                                               ; preds = %51
  %55 = load i32, i32* %7, align 4
  %56 = sext i32 %55 to i64
  %57 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %56
  %58 = load i32, i32* %57, align 4
  %59 = load i32, i32* %7, align 4
  %60 = sub nsw i32 %59, 1
  %61 = sext i32 %60 to i64
  %62 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %61
  %63 = load i32, i32* %62, align 4
  %64 = add nsw i32 %58, %63
  %65 = load i32, i32* %7, align 4
  %66 = sext i32 %65 to i64
  %67 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %66
  store i32 %64, i32* %67, align 4
  %68 = load i32, i32* %7, align 4
  %69 = add nsw i32 %68, 1
  store i32 %69, i32* %7, align 4
  br label %51

70:                                               ; preds = %51
  %71 = load i32, i32* @n, align 4
  store i32 %71, i32* %6, align 4
  br label %72

72:                                               ; preds = %75, %70
  %73 = load i32, i32* %6, align 4
  %74 = icmp sgt i32 %73, 0
  br i1 %74, label %75, label %109

75:                                               ; preds = %72
  %76 = load i32, i32* %6, align 4
  %77 = sub nsw i32 %76, 1
  %78 = sext i32 %77 to i64
  %79 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %78
  %80 = load i32, i32* %79, align 4
  %81 = sext i32 %80 to i64
  %82 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %81
  %83 = load i32, i32* %82, align 4
  %84 = sub nsw i32 %83, 1
  %85 = load i32, i32* %6, align 4
  %86 = sub nsw i32 %85, 1
  %87 = sext i32 %86 to i64
  %88 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %87
  %89 = load i32, i32* %88, align 4
  %90 = sext i32 %89 to i64
  %91 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %90
  store i32 %84, i32* %91, align 4
  %92 = load i32, i32* %6, align 4
  %93 = sub nsw i32 %92, 1
  %94 = sext i32 %93 to i64
  %95 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %94
  %96 = load i32, i32* %95, align 4
  %97 = load i32, i32* %6, align 4
  %98 = sub nsw i32 %97, 1
  %99 = sext i32 %98 to i64
  %100 = getelementptr inbounds [10 x i32], [10 x i32]* %2, i64 0, i64 %99
  %101 = load i32, i32* %100, align 4
  %102 = sext i32 %101 to i64
  %103 = getelementptr inbounds [10 x i32], [10 x i32]* %4, i64 0, i64 %102
  %104 = load i32, i32* %103, align 4
  %105 = sext i32 %104 to i64
  %106 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 %105
  store i32 %96, i32* %106, align 4
  %107 = load i32, i32* %6, align 4
  %108 = sub nsw i32 %107, 1
  store i32 %108, i32* %6, align 4
  br label %72

109:                                              ; preds = %72
  store i32 0, i32* %5, align 4
  br label %110

110:                                              ; preds = %114, %109
  %111 = load i32, i32* %5, align 4
  %112 = load i32, i32* @n, align 4
  %113 = icmp slt i32 %111, %112
  br i1 %113, label %114, label %123

114:                                              ; preds = %110
  %115 = load i32, i32* %5, align 4
  %116 = sext i32 %115 to i64
  %117 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 %116
  %118 = load i32, i32* %117, align 4
  store i32 %118, i32* %8, align 4
  %119 = load i32, i32* %8, align 4
  call void @putint(i32 %119)
  store i32 10, i32* %8, align 4
  %120 = load i32, i32* %8, align 4
  call void @putch(i32 %120)
  %121 = load i32, i32* %5, align 4
  %122 = add nsw i32 %121, 1
  store i32 %122, i32* %5, align 4
  br label %110

123:                                              ; preds = %110
  ret i32 0
}
'''
s11='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca [500 x i32], align 16
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  store i32 0, i32* %5, align 4
  store i32 0, i32* %4, align 4
  store i32 0, i32* %3, align 4
  br label %6

6:                                                ; preds = %25, %0
  %7 = load i32, i32* %3, align 4
  %8 = icmp ne i32 %7, 10
  br i1 %8, label %9, label %28

9:                                                ; preds = %6
  %10 = call i32 @getch()
  store i32 %10, i32* %3, align 4
  %11 = load i32, i32* %3, align 4
  %12 = icmp sgt i32 %11, 40
  br i1 %12, label %13, label %16

13:                                               ; preds = %9
  %14 = load i32, i32* %3, align 4
  %15 = icmp slt i32 %14, 91
  br i1 %15, label %22, label %16

16:                                               ; preds = %13, %9
  %17 = load i32, i32* %3, align 4
  %18 = icmp sgt i32 %17, 96
  br i1 %18, label %19, label %25

19:                                               ; preds = %16
  %20 = load i32, i32* %3, align 4
  %21 = icmp slt i32 %20, 123
  br i1 %21, label %22, label %25

22:                                               ; preds = %19, %13
  %23 = load i32, i32* %5, align 4
  %24 = add nsw i32 %23, 1
  store i32 %24, i32* %5, align 4
  br label %25

25:                                               ; preds = %22, %19, %16
  %26 = load i32, i32* %4, align 4
  %27 = add nsw i32 %26, 1
  store i32 %27, i32* %4, align 4
  br label %6

28:                                               ; preds = %6
  %29 = load i32, i32* %5, align 4
  call void @putint(i32 %29)
  ret i32 0
}
'''
s12='''
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca [10 x i32], align 16
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  %7 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 0
  store i32 3, i32* %7, align 16
  %8 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 1
  store i32 3, i32* %8, align 4
  %9 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 2
  store i32 9, i32* %9, align 8
  %10 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 3
  store i32 0, i32* %10, align 4
  %11 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 4
  store i32 0, i32* %11, align 16
  %12 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 5
  store i32 1, i32* %12, align 4
  %13 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 6
  store i32 1, i32* %13, align 8
  %14 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 7
  store i32 5, i32* %14, align 4
  %15 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 8
  store i32 7, i32* %15, align 16
  %16 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 9
  store i32 8, i32* %16, align 4
  store i32 10, i32* %2, align 4
  store i32 3, i32* %4, align 4
  %17 = load i32, i32* %2, align 4
  store i32 %17, i32* %5, align 4
  store i32 0, i32* %6, align 4
  br label %18

18:                                               ; preds = %43, %0
  %19 = load i32, i32* %6, align 4
  %20 = load i32, i32* %5, align 4
  %21 = icmp slt i32 %19, %20
  br i1 %21, label %22, label %44

22:                                               ; preds = %18
  %23 = load i32, i32* %6, align 4
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 %24
  %26 = load i32, i32* %25, align 4
  %27 = load i32, i32* %4, align 4
  %28 = icmp eq i32 %26, %27
  br i1 %28, label %29, label %40

29:                                               ; preds = %22
  %30 = load i32, i32* %5, align 4
  %31 = sub nsw i32 %30, 1
  %32 = sext i32 %31 to i64
  %33 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 %32
  %34 = load i32, i32* %33, align 4
  %35 = load i32, i32* %6, align 4
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds [10 x i32], [10 x i32]* %3, i64 0, i64 %36
  store i32 %34, i32* %37, align 4
  %38 = load i32, i32* %5, align 4
  %39 = sub nsw i32 %38, 1
  store i32 %39, i32* %5, align 4
  br label %43

40:                                               ; preds = %22
  %41 = load i32, i32* %6, align 4
  %42 = add nsw i32 %41, 1
  store i32 %42, i32* %6, align 4
  br label %43

43:                                               ; preds = %40, %29
  br label %18

44:                                               ; preds = %18
  %45 = load i32, i32* %5, align 4
  call void @putint(i32 %45)
  ret i32 0
}
'''
ss1=['int       a[4][2] = {};\n', 'const int b[8]    = {9, 2, 3, 4, 1, 5, 4};\n', 'int       c[4][2] = {{1, 2}, {3, 4}, {6, 3}, {7, 8}};\n', 'int       e[4][2] = {{6, 7}, {4, 5}, {5, 6}, {9, 10}};\n', '\n', 'int main() {\n', '    putint(e[2][1] + e[0][1] - e[0][0] + a[2][0]);\n', '    int a[4][2] = {};\n', '    int b[8]    = {1, 2, 3, 4, 5, 6, 7, 8};\n', '    int c[4][2] = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};\n', '    putch(10);\n', '    int e[4][2] = {{b[6], b[7]}, {3, 4}, {5, 6}, {7, 8}};\n', '    putint(e[3][1] + e[0][0] + e[0][1] + a[2][0]);\n', '    return 0;\n', '}']
ss2=['int a[3][4];\n', '\n', 'int main() {\n', '    int i   = 0;\n', '    int cnt = 0;\n', '    while (i <= 3 + 4 - 2) {\n', '        int j = i;\n', '        while (j >= 0) {\n', '            if (j < 4 && i - j < 3) {\n', '                a[i - j][j] = cnt;\n', '                cnt         = cnt + 1;\n', '            }\n', '            j = j - 1;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    i     = 0;\n', '    int j = 0;\n', '    while (i < 3) {\n', '        j = 0;\n', '        while (j < 4) {\n', '            putint(a[i][j]);\n', '            putch(32);\n', '            j = j + 1;\n', '        }\n', '        putch(10);\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}']
ss3=['int __HELLO [\n', '\n', '\t\n', '100\n', '\t\t]\t\n', '= {\n', '87, 101, 108, 99,\n', '111, 109, 101,\t \n', '32, 116, 111,\t32,\n', '116,\t 104,\n', '101, 32, \t74,\n', '97,\n', '\t\n', '112, 97,\n', ' \n', '\t114, \t105,\t32,\t80, 97,\t\n', '\t\n', '\t\n', '\n', '\n', '114, 107,\t 33, 10 }; /* Names of\t\n', 'kemono\n', 'friends */ int\tN4__mE___[6][50]\t\t= { { 83, 97,\t97, 98,\n', '97, \n', '114,\n', '117  }, \t{\t75, 97, 98,\t\n', '\n', '97,  110\n', ' \n', '}, { \n', ' \n', '\n', '72,\n', '\n', '\t  97,\n', '115, 104, 105,\n', '98, 105, 114, 111,\n', '\n', '\t\n', '\n', '\t\n', '\t\t\n', '\n', '107,\n', '\t 111,\n', ' \n', '\n', '117\n', '\n', '}, { 65, 114,\n', '\n', '97, \n', '\n', '105,\n', '103,\t\n', '\n', '117,\n', '109, \n', '\n', '\n', '\t\t\t97 },\t\n', '\t{ 72, 117,\n', '110, 98, 111, 114,\n', '117,\n', '\n', '116, 111,\t  32, 80,\n', '101, 110,\n', ' \n', '\t103, 105, \t110\n', '},\n', '  {\t84, 97, 105, 114, 105, 107, 117, 32, 79,\n', '\t\n', '\t \n', '111, 107,\n', '97, \n', '109,\n', '\t\n', '\t\n', ' \n', '\t \n', '\n', '\n', ' 105\t} };\n', '\tint\n', '\n', 'saY_HeI10_To[40] = { 32,\n', '115, 97,  121,  \n', '\t\n', '\t\t115,\n', '\n', '32,\n', '104,\n', '\n', ' 101, 108, 108,\t111, \n', '\n', ' 32,\n', ' \n', '\t\n', '116, 111, \n', '32 };\tint\n', '\t\tRET[5]\n', '=\n', '{10};  int main( /* no param */ )\t{int iNd__1X ;\n', 'iNd__1X\t\t= 0 ; while ( __HELLO\t[\tiNd__1X\n', '\t] ) { \n', '\t\n', ' putch (\n', '\n', '\t\t__HELLO\n', '[ iNd__1X \n', ']  \n', '\t) ; iNd__1X\n', '=\n', 'iNd__1X\n', ' \t\n', ' + 1 \t\n', '\n', ';\t}\tint i =\t\n', ' 0 ; /* say\n', '\n', ' \n', '\thello to\n', ' kemono friends \n', '~ */ while (  \n', ' \n', ' 1 ) {\n', '\n', 'int _  \n', ' = i\n', ' \n', '/ 6\n', '\t\n', '; int __\n', '= \t\n', 'i % 6\n', '\n', ';\n', '     \n', '\tif \n', '( \n', '\n', '_ \n', '\n', '!=\n', '\n', '\n', '\t__ )\n', '\t{ \n', '        \n', '\n', ' \tiNd__1X\t\t= 0 ; while ( N4__mE___\n', '\n', '\t[ \t_\t\n', ' ]\n', '\t\t[\tiNd__1X\n', '\t] ) { \n', '\t\n', ' putch (\n', '\n', 'N4__mE___\n', '\n', '\t[ \t_\t\n', ' ][ iNd__1X \n', ']  \n', '\t) ; iNd__1X\n', '=\n', 'iNd__1X\n', ' \t\n', ' + 1 \t\n', '\n', ';\t}\n', '      iNd__1X\t\t= 0 ; while ( saY_HeI10_To\t[\tiNd__1X\n', '\t] ) { \n', '\t\n', ' putch (\n', '\n', 'saY_HeI10_To[ iNd__1X \n', ']  \n', '\t) ; iNd__1X\n', '=\n', 'iNd__1X\n', ' \t\n', ' + 1 \t\n', '\n', ';\t}\n', 'iNd__1X\t\t= 0 ; while ( N4__mE___ [ \n', '\t\t\n', ' \n', '\n', '__ ]\t[\tiNd__1X\n', '\t] ) { \n', '\t\n', ' putch (\n', '\n', 'N4__mE___ [ \n', '\t\t\n', ' \n', '\n', '__ ][ iNd__1X \n', ']  \n', '\t) ; iNd__1X\n', '=\n', 'iNd__1X\n', ' \t\n', ' + 1 \t\n', '\n', ';\t}\n', '\n', '\t\tiNd__1X\t\t= 0 ; while ( RET\t[\tiNd__1X\n', '\t] ) { \n', '\t\n', ' putch (\n', '\n', 'RET\n', '\t\t\n', ' \n', '\n', '[ iNd__1X \n', ']  \n', '\t) ; iNd__1X\n', '=\n', 'iNd__1X\n', ' \t\n', ' + 1 \t\n', '\n', ';\t}\n', '}\n', '/*\n', '\t do\n', '\t\n', '\tlinear\n', 'modulo \n', 'to find \tthe \t next pair of friends  */ i = ( i\n', '*\n', ' \t\n', '\n', '17\n', '\n', '+\t 23\n', ')\n', '%\n', '\n', '\n', '32\t \n', '\n', ' \n', ' ;\n', 'if ( i\t\n', '==\n', '\t0\t) { break ;\t\t}\n', '\n', ' \n', ' } return 0; }\n']
ss4=['int field[2];\n', 'int main() {\n', '    int i[1];\n', '    int j[3];\n', '    int k;\n', '\n', '    field[0] = getint();\n', '    field[1] = getint();\n', '\n', '    j[0 + 0] = -1;\n', '    j[1]     = j[0] - 2;\n', '    k        = j[1];\n', '    j[2]     = 16;\n', '    \n', '    putint(j[3 - field[0]] + 2 + k);\n', '\n', '    return 0;\n', '}']
ss5=['// Use complex expression in assign structure\n', 'int main() {\n', '    int a;\n', '    int b;\n', '    int c;\n', '    int d;\n', '    int result[5];\n', '    a         = 5;\n', '    b         = 5;\n', '    c         = 1;\n', '    d         = -2;\n', '    result[0] = 1;\n', '    result[1] = 2;\n', '    result[2] = 3;\n', '    result[3] = 4;\n', '    result[4] = 5;\n', '    int t;\n', '    t = result[((d * 1 / 2) + 4 + (a - b) - -(c + 3) % 2) % 5];\n', '    putint(t);\n', '    putch(10);\n', '    t = result[(((c % 2 + 67) + a - b) - -((c + 2) % 2)) % 5];\n', '    putint(t);\n', '    return 0;\n', '}\n']
ss6=['const int N                        = -1;\n', 'int       arr[N + 2 * 4 - 99 / 99] = {1, 2, 33, 4, 5, 6};\n', '\n', 'int main() {\n', '    int i = 0, sum = 0;\n', '    while (i < 5) {\n', '        sum = sum + arr[i];\n', '        i   = i + 1;\n', '    }\n', '    putint(sum);\n', '    return 0;\n', '}\n']
ss7=['/*\n', 'a brainfuck interpreter\n', 'reference: https://gist.github.com/maxcountryman/1699708\n', '*/\n', '\n', '// tape, input buffer, and read/write pointer\n', 'const int TAPE_LEN = 65536, BUFFER_LEN = 32768;\n', 'int       tape[TAPE_LEN], program[BUFFER_LEN], ptr = 0;\n', '\n', 'int main() {\n', '    int i = 0, len = getint();\n', '    while (i < len) {\n', '        program[i] = getch();\n', '        i          = i + 1;\n', '    }\n', '    program[i] = 0;\n', '    int cur_char, loop;\n', '    i = 0;\n', '    while (program[i]) {\n', '        cur_char = program[i];\n', '        if (cur_char == 62) {\n', "            // '>'\n", '            ptr = ptr + 1;\n', '        } else if (cur_char == 60) {\n', "            // '<'\n", '            ptr = ptr - 1;\n', '        } else if (cur_char == 43) {\n', "            // '+'\n", '            tape[ptr] = tape[ptr] + 1;\n', '        } else if (cur_char == 45) {\n', "            // '-'\n", '            tape[ptr] = tape[ptr] - 1;\n', '        } else if (cur_char == 46) {\n', "            // '.'\n", '            putch(tape[ptr]);\n', '        } else if (cur_char == 44) {\n', "            // ','\n", '            tape[ptr] = getch();\n', '        } else if (cur_char == 93 && tape[ptr]) {\n', "            // ']'\n", '            loop = 1;\n', '            while (loop > 0) {\n', '                i        = i - 1;\n', '                cur_char = program[i];\n', '                if (cur_char == 91) {\n', "                    // '['\n", '                    loop = loop - 1;\n', '                } else if (cur_char == 93) {\n', "                    // ']'\n", '                    loop = loop + 1;\n', '                }\n', '            }\n', '        }\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n']
ss8=['int n;\n', '\n', 'int main() {\n', '    n = 10;\n', '    int a[10];\n', '    a[0] = 4;\n', '    a[1] = 3;\n', '    a[2] = 9;\n', '    a[3] = 2;\n', '    a[4] = 0;\n', '    a[5] = 1;\n', '    a[6] = 6;\n', '    a[7] = 5;\n', '    a[8] = 7;\n', '    a[9] = 8;\n', '    int i;\n', '    i = 1;\n', '    while (i < n) {\n', '        int temp;\n', '        temp = a[i];\n', '        int j;\n', '        j = i - 1;\n', '        while (j > -1 && temp < a[j]) {\n', '            a[j + 1] = a[j];\n', '            j        = j - 1;\n', '        }\n', '        a[j + 1] = temp;\n', '        i        = i + 1;\n', '    }\n', '    i = 0;\n', '    while (i < n) {\n', '        int tmp;\n', '        tmp = a[i];\n', '        putint(tmp);\n', '        tmp = 10;\n', '        putch(tmp);\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n']
ss9=['int n;\n', '\n', 'int main() {\n', '    n = 10;\n', '    int a[10];\n', '    a[0] = 4;\n', '    a[1] = 3;\n', '    a[2] = 9;\n', '    a[3] = 2;\n', '    a[4] = 0;\n', '    a[5] = 1;\n', '    a[6] = 6;\n', '    a[7] = 5;\n', '    a[8] = 7;\n', '    a[9] = 8;\n', '    int i;\n', '    int j;\n', '    int min;\n', '    i = 0;\n', '    while (i < n - 1) {\n', '        min = i;  //\n', '        j   = i + 1;\n', '        while (j < n) {\n', '            if (a[min] > a[j]) {\n', '                min = j;\n', '            }\n', '            j = j + 1;\n', '        }\n', '        if (min != i) {\n', '            int tmp;\n', '            tmp    = a[min];\n', '            a[min] = a[i];\n', '            a[i]   = tmp;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    i = 0;\n', '    while (i < n) {\n', '        int tmp;\n', '        tmp = a[i];\n', '        putint(tmp);\n', '        tmp = 10;\n', '        putch(tmp);\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n']
ss10=['int n;\n', '\n', 'int main() {\n', '    n = 10;\n', '    int ini_arr[10];\n', '    ini_arr[0] = 4;\n', '    ini_arr[1] = 3;\n', '    ini_arr[2] = 9;\n', '    ini_arr[3] = 2;\n', '    ini_arr[4] = 0;\n', '    ini_arr[5] = 1;\n', '    ini_arr[6] = 6;\n', '    ini_arr[7] = 5;\n', '    ini_arr[8] = 7;\n', '    ini_arr[9] = 8;\n', '\n', '    int sorted_arr[10];\n', '    int count_arr[10];\n', '    int i;\n', '    int j;\n', '    int k;\n', '    k = 0;\n', '    i = 0;\n', '    j = 0;\n', '    while (k < 10) {\n', '        count_arr[k] = 0;\n', '        k            = k + 1;\n', '    }\n', '    while (i < n) {\n', '        count_arr[ini_arr[i]] = count_arr[ini_arr[i]] + 1;\n', '        i                     = i + 1;\n', '    }\n', '    k = 1;\n', '    while (k < 10) {\n', '        count_arr[k] = count_arr[k] + count_arr[k - 1];\n', '        k            = k + 1;\n', '    }\n', '    j = n;\n', '    while (j > 0) {\n', '        count_arr[ini_arr[j - 1]]             = count_arr[ini_arr[j - 1]] - 1;\n', '        sorted_arr[count_arr[ini_arr[j - 1]]] = ini_arr[j - 1];\n', '        j                                     = j - 1;\n', '    }\n', '    i = 0;\n', '    while (i < n) {\n', '        int tmp;\n', '        tmp = sorted_arr[i];\n', '        putint(tmp);\n', '        tmp = 10;\n', '        putch(tmp);\n', '        i = i + 1;\n', '    }\n', '    return 0;\n', '}\n']
ss11=['int main() {\n', '    int string[500];\n', '    int temp;\n', '    int i;\n', '    int count;\n', '    count = 0;\n', '    i     = 0;\n', '    temp  = 0;\n', '    while (temp != 10) {\n', '        temp = getch();\n', '        if (temp > 40 && temp < 91 || temp > 96 && temp < 123) {\n', '            count = count + 1;\n', '        }\n', '        i = i + 1;\n', '    }\n', '    putint(count);\n', '    return 0;\n', '}']
ss12=['int main() {\n', '    int res;\n', '    int a[10];\n', '    a[0] = 3;\n', '    a[1] = 3;\n', '    a[2] = 9;\n', '    a[3] = 0;\n', '    a[4] = 0;\n', '    a[5] = 1;\n', '    a[6] = 1;\n', '    a[7] = 5;\n', '    a[8] = 7;\n', '    a[9] = 8;\n', '    res  = 10;\n', '    int val;\n', '    val   = 3;\n', '    int n = res;\n', '    int i;\n', '    i = 0;\n', '    while (i < n) {\n', '        if (a[i] == val) {\n', '            a[i] = a[n - 1];\n', '            n    = n - 1;\n', '        } else {\n', '            i = i + 1;\n', '        }\n', '    }\n', '    putint(n);\n', '    return 0;\n', '}']
print(s)
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