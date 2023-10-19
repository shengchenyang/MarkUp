from pathlib import Path

from markup.common.encrypt import EncryptOperation
from markup.common.params import FileInfo, Param
from markup.common.temp import JsAndHtmlGen
from markup.config import Config, webview


class MainMenu:
    @classmethod
    def change_active_window_content(cls):
        print("change_active_window_content")

    @classmethod
    def no_come(cls, window):
        window.create_confirmation_dialog("What's New", "还未开发，敬请期待。。。")

    @classmethod
    def click_me(cls):
        print("click_me")

    @classmethod
    def undo(cls, window):
        window.evaluate_js("document.execCommand('undo')", callback=None)

    @classmethod
    def redo(cls, window):
        window.evaluate_js("document.execCommand('redo')", callback=None)

    @classmethod
    def cut(cls, window):
        window.evaluate_js("document.execCommand('cut')", callback=None)

    @classmethod
    def copy(cls, window):
        js_code = "copySelectedTextToClipboard()"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def paste(cls, window):
        js_code = "pasteTextFromClipboard()"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def open_file_dialog(cls, window):
        file_types = ("Image Files (*.txt;*.md;*.doc)", "All files (*.*)")
        if file_tuple := window.create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types
        ):
            # todo: 添加多文件打开时的多窗口处理和原窗口保存提示功能
            for file in file_tuple:
                file_content = Path(file).read_text(encoding="utf-8")
                file_name = Path(file).name
                print("新文件：", file)
                content_encoded = EncryptOperation.base64_encode(file_content)
                js_code = f"const file_content=decodeBase64(`{content_encoded}`);$markdownElem.value = file_content;const event = new Event('change');$markdownElem.dispatchEvent(event);"
                window.evaluate_js(js_code, callback=None)
                # 窗口栏名设置为新的标题
                window.set_title(f"{file_name} - MarkUp")
                Config.file_info = FileInfo(path=file, notes="当前文件路径")

    @classmethod
    def save_file_dialog(cls, window):
        window_title = webview.active_window().title
        if Param.untitled_mark in window_title:
            result = window.create_file_dialog(
                webview.SAVE_DIALOG, directory="/", save_filename="test.md"
            )
            if result is not None:
                Config.file_info = FileInfo(path=result, notes="当前文件路径")
                file_name = f"{Path(result).name}{Param.normal_mark}"
                window.set_title(file_name)
                file_content = window.evaluate_js("$markdownElem.value;", callback=None)
                Path(result).write_text(file_content, encoding="utf-8")
        else:
            file_content = window.evaluate_js("$markdownElem.value;", callback=None)
            Path(Config.file_info["path"]).write_text(file_content, encoding="utf-8")
            saved_title = window_title.replace(Param.unsaved_mark, Param.normal_mark)
            window.set_title(saved_title)

    @classmethod
    def Level_one_head(cls, window):
        js_code = "insertTextAtCursor('# ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def Level_two_head(cls, window):
        js_code = "insertTextAtCursor('## ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def Level_three_head(cls, window):
        js_code = "insertTextAtCursor('### ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def Level_four_head(cls, window):
        js_code = "insertTextAtCursor('#### ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def Level_five_head(cls, window):
        js_code = "insertTextAtCursor('##### ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def Level_six_head(cls, window):
        js_code = "insertTextAtCursor('###### ')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def insert_img(cls, window):
        js_code = "insertTextAtCursor('![]()')"
        window.evaluate_js(js_code, callback=None)

    @classmethod
    def do_nothing(cls):
        print("do_nothing")

    @classmethod
    def clear(cls, window):
        if _ := webview.active_window():
            _clear_js_code = """handleClearClick();"""
            window.evaluate_js(_clear_js_code, callback=None)

    @classmethod
    def forward_page(cls, window):
        window.evaluate_js("history.back();")

    @classmethod
    def backward_page(cls, window):
        window.evaluate_js("history.forward();")

    @classmethod
    def help_about(cls, window):
        if _ := webview.active_window():
            _e = JsAndHtmlGen.gen_help_about()
            js_code = f"""document.getElementById("popup").innerHTML = '{_e}';"""
            window.evaluate_js(f"{js_code}window.showPopup();")
