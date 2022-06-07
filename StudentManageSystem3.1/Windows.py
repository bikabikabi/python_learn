import PySimpleGUI as Ui

from deal import getpath
from file import getheader


def create_main_window():  # 主窗口布局
    ret_layout = [
        [Ui.B('年龄', size=(16, 5), key='_age_')],
        [Ui.B('性别', size=(16, 5), key='_sex_')]
    ]
    layout = [
        [Ui.T('学生管理系统', background_color='#E6E6FA', text_color='#191970')],
        [Ui.B('新增学生', size=(15, 3), key='_ADD_'), Ui.B('删除学生', size=(15, 3), key='_DELETE_'),
         Ui.B('查找学生', size=(15, 3), key='_FIND_'),
         Ui.B('更改学生信息', size=(15, 3), key='_CHANGE_'), Ui.B('查看全部学生', size=(15, 3), key='_SHOW_'),
         Ui.B('保存', size=(15, 3), key='_SAVE_')],
        [Ui.Column(ret_layout, background_color='#E6E6FA'), Ui.Im(getpath('age'), key='_picture_')]
    ]
    window = Ui.Window("学生管理系统", layout, font='宋体', button_color='#4169E1', background_color='#E6E6FA')

    return window


def create_add_window():  # 新增学生窗口布局
    layout = [
        [Ui.T('输入学生信息：')],
        [
            [Ui.T('学号', size=8), Ui.I(key='_number_')],
            [Ui.T('姓名', size=8), Ui.I(key='_name_')],
            [Ui.T('年龄', size=8), Ui.Combo([i for i in range(0, 100)], size=8, key='_age_')],
            [Ui.T('性别', size=8), Ui.Combo(['男', '女'], size=8, key='_sex_')],
            [Ui.T('联系方式', size=8), Ui.I(key='_tel_')],
            [Ui.T('班级', size=8), Ui.Combo([1, 2, 3], size=8, key='_class_')],
        ],
        [Ui.B('确定', size=25, key="_OK_"), Ui.B('取消', size=25, key="_CANCEL_")]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def create_delete_window():  # 删除学生窗口布局
    layout = [
        [Ui.T('输入要删除学生的学号：')],
        [Ui.I(key='_number_')],
        [Ui.B('确定', size=25, key="_OK_"), Ui.B('取消', size=25, key="_CANCEL_")]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def create_change_window():  # 更改信息窗口布局
    layout = [
        [Ui.T('学号', size=8), Ui.I(key='_number_')],
        [Ui.T('请输入更新的信息')],
        [Ui.T('姓名', size=8), Ui.I(key='_name_')],
        [Ui.T('年龄', size=8), Ui.Combo([i for i in range(0, 100)], size=10, key='_age_')],
        [Ui.T('性别', size=8), Ui.Combo(['男', '女'], size=10, key='_sex_')],
        [Ui.T('班级', size=8), Ui.Combo([1, 2, 3], size=10, key='_class_')],
        [Ui.T('联系方式', size=8), Ui.I(key='_tel_')],
        [Ui.B('确定', size=25, key="_OK_"), Ui.B('取消', size=25, key="_CANCEL_")]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def create_find_window():  # 查找学生窗口布局
    layout = [
        [Ui.T('请输入查找学生的信息')],
        [Ui.T('学号', size=8), Ui.I(key='_number_')],
        [Ui.T('姓名', size=8), Ui.I(key='_name_')],
        [Ui.T('年龄', size=8), Ui.Combo([i for i in range(0, 100)], size=10, key='_age_')],
        [Ui.T('性别', size=8), Ui.Combo(['男', '女'], size=10, key='_sex_')],
        [Ui.T('班级', size=8), Ui.Combo([1, 2, 3], size=10, key='_class_')],
        [Ui.T('联系方式', size=8), Ui.I(key='_tel_')],
        [Ui.B('确定', size=25, key="_OK_"), Ui.B('取消', size=25, key="_CANCEL_")]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def create_show_window(content):  # 查看学生窗口布局
    tag = getheader()
    layout = [
        [Ui.T('学生名单')],
        [Ui.B('排序', size=25, key='_SORT_'), Ui.Combo(tag[0:1] + tag[2:4] + tag[5:], size=25, key='_tag_'),
         Ui.Combo(['顺序', '逆序'], size=25, key='_sequence_', default_value='顺序')],
        [Ui.LBox(content, size=(100, 30), key="_list_")],
        [Ui.B('确定', size=25, key="_OK_"), Ui.B('取消', size=25, key="_CANCEL_")]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def create_personal_window(std):  # 个人信息窗口布局
    left_layout = [
        [Ui.T('个人信息')],
        [Ui.T('学号', size=8), Ui.T(std['学号'], key='_number_')],
        [Ui.T('姓名', size=8), Ui.T(std['姓名'], key='_name_')],
        [Ui.T('年龄', size=8), Ui.T(std['年龄'], key='_age_')],
        [Ui.T('性别', size=8), Ui.T(std['性别'], key='_sex_')],
        [Ui.T('班级', size=8), Ui.T(std['班级'], key='_class_')],
        [Ui.T('联系方式', size=8), Ui.T(std['联系方式'], key='_tel_')],
        [Ui.B('返回', size=25, key="_CANCEL_")]
    ]
    left_col = Ui.Column(left_layout)
    layout = [
        [left_col, Ui.Im('score.png')]
    ]
    window = Ui.Window("学生管理系统", layout)
    return window


def pop_window():
    Ui.popup_auto_close("close")
