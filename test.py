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

# 运算符表
y_list = {"+", "-", "*", "/", "<", "<=", ">", ">=", "=", "==", "!=", "^", ",", "&", "&&", "|", "||", "%", "~", "<<",
          ">>", "!"}
# 分隔符表
f_list = {";", "(", ")", "[", "]", "{", "}", ".", ":", "\"", "#", "\'", "\\", "?"}
# 关键字表
k_list = {
    "auto", "break", "case", "const", "continue", "default", "do", "else", "enum", "extern",
    "for", "goto", "if", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "volatile", "while", "printf"
}

Cmp = ["<", ">", "==", "!=", ">=", "<="]

Type = {"int", "float", "char", "double", "void", "long", "unsigned", "string"}
type_flag = ""
# 括号配对判断
kuo_cp = {'{': '}', '[': ']', '(': ')'}

RegNum=1
def transfer(string):
    arr=list(string)
    i=0
    while i < len(arr):
        if (arr[i]=='-' or arr[i]=='+')and i==0:
            arr.insert(i, '0')
            i += 1
        if arr[i]=='(' and arr[i+1]=='-':
            arr.insert(i+1,'0')
            i+=2
        elif arr[i]=='-' and arr[i+1]=='-':
            arr.pop(i)
            arr.pop(i)
            arr.insert(i,'+')
        elif arr[i]=='+' and arr[i+1]=='-':
            arr.pop(i)
            arr.pop(i)
            arr.insert(i,'-')
        elif arr[i]=='-' and arr[i+1]=='+':
            arr.pop(i)
            arr.pop(i)
            arr.insert(i,'-')
        elif arr[i]=='+' and arr[i+1]=='+':
            arr.pop(i)
            arr.pop(i)
            arr.insert(i,'+')
        else:
            i+=1
    return arr

class register:
    content=[]
    registerNum=0

def priority(z):
    if z in ['%', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1

def in2post(expr:list):
    stack = []  # 存储栈
    post = []  # 后缀表达式存储
    for z in expr:
        if z not in ['%', '*', '/', '+', '-', '(', ')']:  # 字符直接输出
            post.append(z)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
                stack.append(z)     # 运算符入栈

            elif z == ')':  # 右括号出栈
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                    else:
                        break

            else:   # 比较运算符优先级，看是否入栈出栈
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                    else:
                        stack.append(z)
                        break
    while stack:    # 还未出栈的运算符，需要加到表达式末尾
        post.append(stack.pop())
    return post

# 计算后缀表达式
def calculate(string):
    global RegNum
    stack = []
    cstring = []
    assemble=[]

    for i in string:
        temp=register()
        temp.registerNum=0;
        temp.content=i
        cstring.append(temp)
    for c in cstring:
        # 如果是运算符
        if c.content in '+-*/%':
            tempstring = ''
            # [右面的操作数先出栈]
            b = stack.pop()
            a = stack.pop()
            d=eval(f"{a.content}{c.content}{b.content}")
            temp=register()
            temp.content=d
            temp.registerNum=RegNum
            RegNum+=1
            stack.append(temp)
            tempstring+='%'+str(temp.registerNum)+' = '
            if c.content=='-':
                tempstring+='sub i32 '
            elif c.content=='+':
                tempstring+='add i32 '
            elif c.content=='*':
                tempstring+='mul i32 '
            elif c.content=='/':
                tempstring+='sdiv i32 '
            elif c.content=='%':
                tempstring+='srem i32 '

            if a.registerNum==0:
                tempstring+=a.content
                tempstring +=', '
            else:
                tempstring+="%"
                tempstring+=str(a.registerNum)
                tempstring += ', '
            if b.registerNum==0:
                tempstring+=b.content
            else:
                tempstring+="%"
                tempstring+=str(b.registerNum)
            assemble.append(tempstring)
        else:
            # 操作数直接入栈
            stack.append(c)
    # [最后一个必是操作数]
    return stack.pop(),assemble
# 词法分析器输出对象
# 成员变量：输出的单词表，源代码中的分隔符表,运算符表,变量表,关键字表
# 一个方法，将源代码字符切割并存入对应表中
# 对象创建实例需要传入filename参数，默认为test.c

def if_num(int_word):
    if int_word[0]=='0' :
        return True
    if re.match("^([0-9]{1,}[.][0-9]*)$", int_word) or re.match("^([0-9]{1,})$", int_word) == None:
        return False
    else:
        return True


# 判断是否为为变量名
def if_name(int_word):
    if re.match("[a-zA-Z_][a-zA-Z0-9_]*", int_word) == None:
        return False
    else:
        return True


# 判断是否为终结符
# def END_STATE(int_word):
#     if

# 判断变量名是否已存在
def have_name(name_list, name):
    for n in name_list:
        if name == n['name']:
            return True
    return False


# list的换行输出
def printf(lists):
    for l in lists:
        print(l)


def get_word(lines):
    out_words = []
    # 先逐行读取，并记录行号
    line_num = 1
    for line in lines:
        words = list(line.split())
        for w in words:
            # 分析单词
            if w in Cmp:
                out_words.append({'word': w, 'line': line_num})
                continue
            ws = w
            for a in w:
                if a in f_list or a in y_list:
                    # index为分隔符的位置，将被分隔符或运算符隔开的单词提取
                    index = ws.find(a)
                    if index != 0:
                        # 存储单词与该单词的所在行号，方便报错定位
                        out_words.append({'word': ws[0:index], 'line': line_num})
                    ws = ws[index + 1:]
                    out_words.append({'word': a, 'line': line_num})
            if ws != '':
                out_words.append({'word': ws, 'line': line_num})
        line_num += 1
    return out_words


class word_list():
    def __init__(self, filename='test.c'):
        self.word_list = []  # 输出单词列表
        self.separator_list = []  # 分隔符
        self.operator_list = []  # 运算符
        self.name_list = []  # 变量
        self.key_word_table = []  # 关键字
        self.string_list = []
        self.flag = True  # 源代码是否正确标识

        # get_word函数将源代码切割
        self.creat_table(get_word(filename))

    # 创建各个表
    def creat_table(self, in_words):
        name_id = 0
        kuo_list = []  # 存储括号并判断是否完整匹配
        char_flag = False
        str_flag = False
        string_list = []
        strings = ""
        chars = ""
        for word in in_words:
            w = word['word']
            line = word['line']
            if w == '"':
                if str_flag == False:
                    str_flag = True
                else:
                    str_flag = False
                    self.word_list.append({'line': line, 'type': 'TEXT', 'word': strings})
                    self.string_list.append(strings)
                    strings = ""
                # self.word_list.append({'line':line, 'type':w, 'word':w})
                continue
            # 判断是否为字符串
            if str_flag == True:
                strings += w
                continue
            if w == "'":
                if char_flag == False:
                    char_flag = True
                else:
                    char_flag = False
                    self.word_list.append({'line': line, 'type': 'CHAR', 'word': chars})
                    chars = ""
                continue
            if char_flag == True:
                chars += w
                continue
            # 判断为关键字
            if w in k_list:
                self.key_word_table.append({'line': line, 'type': 'keyword', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            elif w in Cmp:
                self.word_list.append({'line': line, 'type': "Cmp", 'word': w})
            # 判断为关键字
            elif w in Type:
                type_flag = w
                self.key_word_table.append({'line': line, 'type': 'type', 'word': w})
                self.word_list.append({'line': line, 'type': 'type', 'word': w})
            # 判断为运算符
            elif w in y_list:
                self.operator_list.append({'line': line, 'type': 'operator', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            # 判断为分隔符
            elif w in f_list:
                if w in kuo_cp.values() or w in kuo_cp.keys():
                    # 左括号入栈
                    if w in kuo_cp.keys():
                        kuo_list.append({'kuo': w, 'line': line})
                    # 右括号判断是否匹配并出栈
                    elif w == kuo_cp[kuo_list[-1]['kuo']]:
                        kuo_list.pop()
                    else:
                        self.flag = False
                        return
                self.separator_list.append({'line': line, 'type': 'separator', 'word': w})
                self.word_list.append({'line': line, 'type': w, 'word': w})
            else:
                if if_num(w):
                    w=str(number_parsing(w))
                    self.word_list.append({'line': line, 'type': 'number', 'word': w})
                elif if_name(w):
                    if have_name(self.name_list, w):
                        self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
                    else:
                        self.name_list.append({'line': line, 'id': name_id, 'word': 0.0, 'name': w, 'flag': type_flag})
                        self.word_list.append({'line': line, 'type': 'name', 'word': w, 'id': name_id})
                        name_id += 1
                else:
                    self.flag = False
                    return
        if kuo_list != []:
            self.flag = False
            return

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


def number_parsing(Num:str)->int:
    if len(Num)>1 and (Num[0]=='0' and Num[1]=='x' or Num[0]=='0' and Num[1]=='X'):
        return int(Num,16)
    elif Num[0]=='0':
        return int(Num,8)
    else:
        return int(Num)

def main():
    line_input=[]
    for line in sys.stdin:
        line_input.append(line)
    if '/*1;}*/' in line_input[0]:
        line_input[0]='int main() { return '
    notation_clear(line_input)
    print(line_input)
    w_list=word_list(line_input)
    compute=[]
    computeflag=False
    line=1
    for i in w_list.word_list:
        if i['line'] == line+1 and computeflag==False:
            print()
        if i['type'] == ';':
            computeflag = False
            expression = transfer(compute)
            expression = transfer(expression)
            exp = in2post(expression)
            ans, pro = calculate(exp)
            printf(pro)
            print('ret i32 %'+str(RegNum-1))
        if computeflag==True:
            compute.append(i['word'])
        if i['type']=='return':
            computeflag=True
        if computeflag==False :
            print(reserved_words_dict[i['word']],end=' ')


main()
# lines=[]
# for line in sys.stdin:
#     lines.append(line)
# lines=['define dso_local i32 @main() {',
#     '%1 = sub i32 0, 1',
#     '%2 = sub i32 0, %1',
#     '%3 = sub i32 0, %2',
#     '%4 = sub i32 0, %3',
#     '%5 = sub i32 0, %4',
#     '%6 = sub i32 0, %5',
#     '%7 = sub i32 0, %6',
#     '%8 = sub i32 0, %7',
#     '%9 = add i32 1, %8',
#     'ret i32 %9',
#     '}']
# for line in lines:
#     print(line)