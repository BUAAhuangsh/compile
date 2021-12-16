import re,sys
reserved_words_dict={'int':'define',
                     'main':'dso_local i32 @main',
                     '(':'(',
                     ')':')',
                     'return':'ret',
                     '{':'{',
                     '}':'}',
                     ';':'',
                     '/':'/',
                     '*':'*'}
# 运算符表
y_list = {"+","-","*","/","<","<=",">",">=","=","==","!=","^",",","&","&&","|","||","%","~","<<",">>","!"}
# 分隔符表
f_list = {";","(",")","[","]","{","}", ".",":","\"","#","\'","\\","?"}
# 关键字表
k_list = {
    "auto", "break", "case", "char", "const", "continue","default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long","register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void","volatile", "while", "printf"
}
Cmp = ["<", ">", "==", "!=", "<=", ">="]
Type = {"int","float","char","double","void","long","unsigned","string"}
type_flag = ""
# 括号配对判断
kuo_cp = {'{':'}', '[':']', '(':')'}
# # 正则表达式判断是否为数字
# def if_num(int_word):
#     int_word = number_parsing(int_word)
#     if re.match("^([0-9]{1,}[.][0-9]*)$",int_word) or re.match("^([0-9]{1,})$",int_word) == None:
#         return False
#     else:
#         return True
#
# # 判断是否为为变量名
# def if_name(int_word):
#     if re.match("[a-zA-Z_][a-zA-Z0-9_]*",int_word) == None:
#         return False
#     else:
#         return True
#
# # 判断是否为终结符
# # def END_STATE(int_word):
# #     if
#
# # 判断变量名是否已存在
# def have_name(name_list,name):
#     for n in name_list:
#         if name == n['name']:
#             return True
#     return False
#
# # list的换行输出
# def printf(lists):
#     for l in lists:
#         print(l)
#
# # 分割并获取文本单词
# # 返回值为列表out_words
# # 列表元素{'word':ws, 'line':line_num}分别对应单词与所在行号
#
def get_word():
    global f_list
    out_words = []
    # 先逐行读取，并记录行号
    lines = []
    for line in sys.stdin:
        lines.append(line)
    line_num = 1
    # 判断是否含有注释块的标识
    pass_block = False
    for line in lines:
        words = list(line.split())
        for w in words:
            # 去除注释
            if '*/' in w:
                pass_block = False
                continue
            if '//' in w:
                break
            if '/*' in w:
                pass_block = True
                continue
            if pass_block:
                continue
            # 分析单词
            if w in Cmp:
                out_words.append({'word':w, 'line':line_num})
                continue
            ws = w
            for a in w:
                if a in f_list or a in y_list:
                    # index为分隔符的位置，将被分隔符或运算符隔开的单词提取
                    index = ws.find(a)
                    if index!=0:
                        # 存储单词与该单词的所在行号，方便报错定位
                        out_words.append({'word':ws[0:index], 'line':line_num})
                    ws = ws[index+1:]
                    out_words.append({'word':a, 'line':line_num})
            if ws!='':
                out_words.append({'word':ws, 'line':line_num})
        line_num += 1
    return out_words
#
# class word_list():
#     def __init__(self,in_words):
#         self.word_list = []  # 输出单词列表
#         self.separator_list = []  # 分隔符
#         self.operator_list = []  # 运算符
#         self.name_list = []  # 变量
#         self.key_word_table = []  # 关键字
#         self.string_list = []
#         self.flag = True  # 源代码是否正确标识
#
#         # get_word函数将源代码切割
#         self.creat_table(in_words)
#
#     # 创建各个表
#     def creat_table(self, in_words):
#         global type_flag
#         name_id = 0
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
#             # 其他字符处理
#             else:
#                 if if_num(w):
#                     w=number_parsing(w)
#                     self.word_list.append({'line': line, 'type': 'number', 'word': w})
#                 # 如果是变量名要判断是否已经存在
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
# def number_parsing(Num:str)->str:
#     if len(Num)>1 and (Num[0]=='0' and Num[1]=='x' or Num[0]=='0' and Num[1]=='X'):
#         return str(int(Num,16))
#     elif Num[0]=='0':
#         return str(int(Num,8))
#     elif re.match(Num[0],'[1-9]'):
#         return str(int(Num))
#     else:
#         return Num
# def main():
#     word=get_word()
#     list=word_list(word)
#     str=''
#     for i in range(len(list.word_list)):
#         if list.word_list[i]['type'] !='number':
#             str+=list.word_list[i]['word']
#     if str!='intmain(){return;}' or list.flag == False:
#         sys.exit(1)
#     line=1
#     for i in list.word_list:
#         if line!=i['line']:
#             line+=1
#             print()
#         if i['word'] in reserved_words_dict:
#             print(reserved_words_dict[i['word']],end=' ')
#         else:
#             print(i['word'],end=' ')

def main():
    lines=[]
    for line in sys.stdin:
        lines.append(line)
    for i in lines:
        print(i)

main()