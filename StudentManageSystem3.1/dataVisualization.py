import math

import matplotlib
import matplotlib.pyplot as plt


def draw_radar(labels, data, path):
    matplotlib.rcParams['font.family'] = 'KaiTi'
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    data_length = len(data)
    angles = [2 * math.pi / data_length * i for i in range(data_length)]
    data.append(data[0])
    angles.append(angles[0])
    labels.append(labels[0])
    plt.figure()
    plt.polar(angles, data)
    plt.fill(angles, data, facecolor='b')
    angles = [i / math.pi * 180 for i in angles]
    plt.thetagrids(angles, labels)
    plt.savefig(path)


def draw_pie(data, labels, path):
    matplotlib.rcParams['font.family'] = 'KaiTi'
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rc('legend', fontsize=20)
    explode = [0] * len(data)
    for i in range(len(data)):
        for j in data:
            if data[i] > j:
                explode[i] += 0.03
    plt.figure(figsize=(13, 10), dpi=50)
    plt.pie(data, labels=labels, shadow=True, radius=1.1, explode=explode, textprops={'fontsize': 40, 'color': 'y'},
            autopct='%.1f%%')

    plt.savefig(path)


def getdata(information, tag):
    count = {}
    for std in information:
        count[std[tag]] = count.get(std[tag], 0) + 1
    data = []
    labels = []
    temp = list(count.items())
    temp.sort(key=lambda x: x[1])
    for i in temp:
        data.append(i[1])
        labels.append(i[0])
    return data, labels
