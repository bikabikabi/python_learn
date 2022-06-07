import Windows
from dataVisualization import getdata, draw_pie, draw_radar
from file import getheader, read, save

dic = {'姓名': '_name_', '年龄': '_age_', '性别': '_sex_', '联系方式': '_tel_', '班级': '_class_', '学号': '_number_'}
information = []
header = []
information_path = 'studentInformation/information.txt'
picture_path = {'sex': 'picture/sex.PNG', 'age': 'picture/age.PNG', 'score': 'picture/score.PNG'}


def getpath(key):
    return picture_path[key]


def start():
    global information
    global header
    information = read(information_path)
    header = getheader()
    draw_age_pie()
    draw_sex_pie()


def end():
    global information
    save(information_path, information)


def get_std(temp_std):
    number = temp_std['_list_'][0][0]
    for std in information:
        if std['学号'] == number:
            return std


def get_information():
    return information


def tolist(content):
    results = []
    for std in content:
        temp = []
        for i in std.items():
            temp.append(i[1])
        results.append(temp)
    return results


def add(std):
    global information
    global header
    temp = {}

    for i in header:
        temp[i] = std[dic[i]]
    information.append(temp)


def delete(temp_std):
    global information
    for std in information:
        if std['学号'] == temp_std['_number_']:
            information.remove(std)
            break


def find(temp_std):
    global information
    global header
    results = []
    for std in information:
        is_select = True
        for i in header:
            if i == '语文':
                break
            if temp_std[dic[i]] == '':
                continue
            if std[i] != str(temp_std[dic[i]]):
                is_select = False
                break

        if is_select:
            results.append(std)
    results = tolist(results)
    show(results)


def change(temp_std):
    global information
    for std in information:
        if std['学号'] == temp_std['_number_']:
            for i in header:
                temp = temp_std[dic[i]]
                if temp == '':
                    continue
                std[i] = str(temp)


def sort(content, values):
    tag = values['_tag_']
    sequence = False
    if values['_sequence_'] == '逆序':
        sequence = True
    index = None
    for i in range(len(header)):
        if header[i] == tag:
            index = i
            break
    content.sort(key=lambda x: x[index], reverse=sequence)


def show(content):
    show_window = Windows.create_show_window(content)
    while True:
        event_show, values_show = show_window.read()
        if event_show in [None, '_CANCEL_']:
            break
        if event_show == '_OK_':
            if not values_show['_list_']:
                Windows.pop_window()
                continue
            std = get_std(values_show)
            draw_score_radar(values_show)
            personal_window = Windows.create_personal_window(std)
            while True:
                event_personal, values_personal = personal_window.read()
                if event_personal in [None, "_CANCEL_"]:
                    break
            personal_window.close()
        if event_show == '_SORT_':
            sort(content, values_show)
            show_window['_list_'].update(content)
    show_window.close()


def draw_sex_pie():
    data, labels = getdata(information, "性别")
    draw_pie(data, labels, picture_path['sex'])


def draw_age_pie():
    data, labels = getdata(information, "年龄")
    draw_pie(data, labels, picture_path['age'])


def draw_score_radar(std):
    labels = getheader()[6:-1]
    data = list(map(eval, std['_list_'][0][6:-1]))
    draw_radar(labels, data, picture_path['score'])
