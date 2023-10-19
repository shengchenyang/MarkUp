import webview.menu as wm

from markup.app.backend.action.main import MainMenu
from markup.config import webview

if __name__ == "__main__":
    from markup.app.backend.api import Api

    api = Api()
    window = webview.create_window(
        "Untitled* - MarkUp",
        "app/frontend/main.html",
        min_size=(1024, 768),
        js_api=api,
    )

    menu_items = [
        wm.Menu(
            "文件",
            [
                wm.MenuAction(
                    "新建",
                    MainMenu.change_active_window_content,
                ),
                wm.MenuSeparator(),
                wm.MenuAction(
                    "打开...",
                    lambda: MainMenu.open_file_dialog(window),
                ),
                wm.MenuSeparator(),
                wm.MenuAction(
                    "保存",
                    lambda: MainMenu.save_file_dialog(window),
                ),
            ],
        ),
        wm.Menu(
            "编辑",
            [
                wm.MenuAction(
                    "撤消",
                    lambda: MainMenu.undo(window),
                ),
                wm.MenuAction(
                    "恢复",
                    lambda: MainMenu.redo(window),
                ),
                wm.MenuSeparator(),
                wm.MenuAction(
                    "剪切",
                    lambda: MainMenu.cut(window),
                ),
                wm.MenuAction(
                    "复制",
                    lambda: MainMenu.copy(window),
                ),
                wm.MenuAction(
                    "粘贴",
                    lambda: MainMenu.paste(window),
                ),
                wm.MenuSeparator(),
                wm.MenuAction(
                    "彻底清空",
                    lambda: MainMenu.clear(window),
                ),
            ],
        ),
        wm.Menu(
            "插入",
            [
                wm.MenuAction(
                    "一级标题",
                    lambda: MainMenu.Level_one_head(window),
                ),
                wm.MenuAction(
                    "二级标题",
                    lambda: MainMenu.Level_two_head(window),
                ),
                wm.MenuAction(
                    "三级标题",
                    lambda: MainMenu.Level_three_head(window),
                ),
                wm.MenuAction(
                    "四级标题",
                    lambda: MainMenu.Level_four_head(window),
                ),
                wm.MenuAction(
                    "五级标题",
                    lambda: MainMenu.Level_five_head(window),
                ),
                wm.MenuAction(
                    "六级标题",
                    lambda: MainMenu.Level_six_head(window),
                ),
                wm.MenuSeparator(),
                wm.MenuAction(
                    "图片",
                    lambda: MainMenu.insert_img(window),
                ),
            ],
        ),
        wm.Menu(
            "页面",
            [
                wm.MenuAction(
                    "前进",
                    lambda: MainMenu.backward_page(window),
                ),
                wm.MenuAction(
                    "后退",
                    lambda: MainMenu.forward_page(window),
                ),
            ],
        ),
        wm.Menu(
            "帮助",
            [
                # wm.MenuAction(
                #     "What's New",
                #     lambda: MainMenu.no_come(window),
                # ),
                # wm.MenuSeparator(),
                wm.MenuAction(
                    "关于",
                    lambda: MainMenu.help_about(window),
                ),
            ],
        ),
    ]

    webview.start(
        menu=menu_items,
        # debug=True,
        private_mode=True,
    )
