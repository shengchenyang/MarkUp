from markup.app.backend.action.main import MainMenu
from markup.config import wm


def create_menu() -> list:
    return [
        wm.Menu(
            "文件",
            [
                wm.MenuAction("新建", MainMenu.open_new_window),
                wm.MenuSeparator(),
                wm.MenuAction("打开...", MainMenu.open_file_dialog),
                wm.MenuSeparator(),
                wm.MenuAction("保存", MainMenu.save_file_dialog),
            ],
        ),
        wm.Menu(
            "编辑",
            [
                wm.MenuAction("撤消", MainMenu.undo),
                wm.MenuAction("恢复", MainMenu.redo),
                wm.MenuSeparator(),
                wm.MenuAction("剪切", MainMenu.cut),
                wm.MenuAction("复制", MainMenu.copy),
                wm.MenuAction("粘贴", MainMenu.paste),
                wm.MenuSeparator(),
                wm.MenuAction("彻底清空", MainMenu.clear),
            ],
        ),
        wm.Menu(
            "插入",
            [
                wm.MenuAction("一级标题", MainMenu.Level_one_head),
                wm.MenuAction("二级标题", MainMenu.Level_two_head),
                wm.MenuAction("三级标题", MainMenu.Level_three_head),
                wm.MenuAction("四级标题", MainMenu.Level_four_head),
                wm.MenuAction("五级标题", MainMenu.Level_five_head),
                wm.MenuAction("六级标题", MainMenu.Level_six_head),
                wm.MenuSeparator(),
                wm.MenuAction("图片", MainMenu.insert_img),
            ],
        ),
        wm.Menu(
            "页面",
            [
                wm.MenuAction("前进", MainMenu.backward_page),
                wm.MenuAction("后退", MainMenu.forward_page),
            ],
        ),
        wm.Menu(
            "帮助",
            [wm.MenuAction("关于", MainMenu.help_about)],
        ),
    ]
