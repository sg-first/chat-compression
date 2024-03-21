f = open('D:/待富者俱乐部聊天记录2.txt', 'r', encoding='utf-8')
content = f.read()
content = content.split('\n')

def isName(line):
    s1 = line.find('20')
    s2 = line.find('-')
    s3 = line.find(':')
    return s1 == 0 and (s1 < s2 < s3)

def cutTime(line:str):
    slist = line.split(' ')
    print(slist)
    name = slist[2]
    if name == '':
        return '匿名'
    else:
        return slist[2]

bLastName = False
ret = ''
cache = ''

for i in content:
    if isName(i): # 名字（第一行）
        # 清缓存
        ret += cache
        cache = ''
        # 处理名字
        name = cutTime(i)
        cache = name + '：'
        bLastName = True
    elif cache != '' and bLastName:  # 正文
        if i != '':
            print(i)
            cache += i + '\n'
            bLastName = False
        else:  # 正文为空，过滤
            bLastName = False
            cache = ''
    else:  # 结尾空行
        ret += cache
        cache = ''

f = open('D:/待富者俱乐部聊天记录3.txt', 'w', encoding='utf-8')
f.write(ret)