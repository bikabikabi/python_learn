from Windows import create_change_window, create_find_window, create_delete_window, \
    create_add_window, create_main_window
from deal import add, delete, find, tolist, get_information, start, end, change, draw_sex_pie, draw_age_pie, show, \
    getpath


def init():
    start()
    main_window = create_main_window()  # 初始化并打开主窗口
    while True:
        event, values = main_window.read()

        if event == '_ADD_':  # 打开新增学生窗口
            main_window.hide()
            add_window = create_add_window()
            while True:
                event_add, values_add = add_window.read()
                if event_add in [None, '_CANCEL_']:
                    break
                if event_add == '_OK_':
                    add(values_add)
                    break
            add_window.close()
            main_window.reappear()
        if event == '_DELETE_':  # 打开删除学生窗口
            delete_window = create_delete_window()
            while True:
                event_delete, values_delete = delete_window.read()
                if event_delete in [None, '_CANCEL_']:
                    break
                if event_delete == '_OK_':
                    delete(values_delete)
                    break
            delete_window.close()

        if event == '_FIND_':  # 打开查找学生窗口
            find_window = create_find_window()
            while True:
                event_find, values_find = find_window.read()
                if event_find == '_OK_':
                    find(values_find)
                    break
                if event_find in [None, '_CANCEL_']:
                    break
            find_window.close()

        if event == '_CHANGE_':  # 打开更改信息窗口
            change_window = create_change_window()
            while True:
                event_change, values_change = change_window.read()
                if event_change == '_OK_':
                    change(values_change)
                    break
                if event_change in [None, '_CANCEL_']:
                    break
            change_window.close()

        if event == '_SHOW_':  # 打开查看窗口
            information = get_information()
            content = tolist(information)
            show(content)

        if event == '_SAVE_':
            end()

        if event == '_sex_':
            draw_sex_pie()
            main_window['_picture_'].update(getpath('sex'))

        if event == '_age_':
            draw_age_pie()
            main_window['_picture_'].update(getpath('age'))

        if event is None:
            break

    main_window.close()
    end()


init()
