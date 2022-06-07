header = []


def getheader():
    global header
    return header


def read(path):
    f = open(path, 'rt', encoding='utf-8')
    information = [i.strip('\n').split(',') for i in f.readlines()]
    f.close()
    global header
    header = information[0]
    information = information[1:]
    information = [dict(zip(header, std)) for std in information]

    return information


def save(path, information):
    global header
    dealt = [','.join(header) + '\n']
    for std in information:
        temp = []
        for i in header:
            temp.append(std[i])
        temp = ','.join(temp) + '\n'
        dealt.append(temp)
    f = open(path, 'w', encoding='utf-8')
    f.writelines(dealt)
    f.close()
