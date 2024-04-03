f = open('D:/chat/ARMA交流群1.txt', 'r', encoding='utf-8')
content = f.read()
content = content.replace('[表情]', '')
content = content.replace('[图片]', '')
content = content.split('\n')

def isName(line):
    bAccount = ('(' in line and ')' in line) or ('<' in line and '>' in line)
    return '20' in line and '-' in line and ':' in line and bAccount

def cutNumber(line:str):
    if '(' in line and ')' in line:
        i = line.find('(')
    else:
        i = line.find('<')
    return line[:i]

def cutAt(line:str):
    if len(line) > 0 and line[0] == '@':
        slist = line.split(' ')
        slist = slist[1:]
        return ' '.join(slist)
    else:
        return line

bLastName = False
ret = ''
cache = ''

for i in content:
    if isName(i): # 名字（第一行）
        # 清缓存
        ret += cache
        cache = ''
        # 处理名字
        i = cutNumber(i)
        print(i)
        cache = i + '\n'
        bLastName = True
    elif cache != '' and bLastName:  # 正文
        if i != '':
            i = cutAt(i)
            print(i)
            cache += i + '\n'
            bLastName = False
        else:  # 正文为空，过滤
            bLastName = False
            cache = ''
    else:  # 结尾空行
        ret += cache
        cache = ''

f = open('D:/chat/ARMA交流群2.txt', 'w', encoding='utf-8')
f.write(ret)