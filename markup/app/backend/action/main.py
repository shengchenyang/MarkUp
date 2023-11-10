from pathlib import Path

from markup.app.backend.api import Api
from markup.common.encrypt import EncryptOperation
from markup.common.params import FileInfo, Param
from markup.common.temp import JsAndHtmlGen, ReadConf
from markup.config import Config, webview


class MainMenu:
    @staticmethod
    def open_new_window():
        api = Api()
        min_size = ReadConf.get_launcher_conf(Config.PROFILE_DIR / "app.ini")

        webview.create_window(
            "Untitled* - MarkUp",
            f"{Config.app_path}/app/frontend/main.html",
            width=min_size[0],
            height=min_size[1],
            min_size=(800, 600),
            js_api=api,
        )

    @staticmethod
    def no_come():
        if active_w := webview.active_window():
            active_w.create_confirmation_dialog("What's New", "还未开发，敬请期待。。。")

    @staticmethod
    def click_me():
        print("click_me")

    @staticmethod
    def undo():
        if active_w := webview.active_window():
            active_w.evaluate_js("document.execCommand('undo')", callback=None)

    @staticmethod
    def redo():
        if active_w := webview.active_window():
            active_w.evaluate_js("document.execCommand('redo')", callback=None)

    @staticmethod
    def cut():
        if active_w := webview.active_window():
            active_w.evaluate_js("document.execCommand('cut')", callback=None)

    @staticmethod
    def copy():
        if active_w := webview.active_window():
            js_code = "copySelectedTextToClipboard()"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def paste():
        if active_w := webview.active_window():
            js_code = "pasteTextFromClipboard()"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def open_file_dialog():
        if active_w := webview.active_window():
            file_types = ("Image Files (*.txt;*.md;*.doc)", "All files (*.*)")
            if file_tuple := active_w.create_file_dialog(
                webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types
            ):
                # todo: 添加多文件打开时的多窗口处理和原窗口保存提示功能
                for file in file_tuple:
                    file_content = Path(file).read_text(encoding="utf-8")
                    file_name = Path(file).name
                    content_encoded = EncryptOperation.base64_encode(file_content)
                    js_code = f"const file_content=decodeBase64(`{content_encoded}`);$markdownElem.value = file_content;const event = new Event('change');$markdownElem.dispatchEvent(event);"
                    active_w.evaluate_js(js_code, callback=None)
                    # 窗口栏名设置为新的标题
                    active_w.set_title(f"{file_name} - MarkUp")
                    Config.file_info = FileInfo(path=file, notes="当前文件路径")

    @staticmethod
    def save_file_dialog():
        if active_w := webview.active_window():
            window_title = webview.active_window().title
            if Param.untitled_mark in window_title:
                result = active_w.create_file_dialog(webview.SAVE_DIALOG, directory="/", save_filename="test.md")
                if result is not None:
                    Config.file_info = FileInfo(path=result, notes="当前文件路径")
                    file_name = f"{Path(result).name}{Param.normal_mark}"
                    active_w.set_title(file_name)
                    file_content = active_w.evaluate_js("$markdownElem.value;", callback=None)
                    Path(result).write_text(file_content, encoding="utf-8")
            else:
                file_content = active_w.evaluate_js("$markdownElem.value;", callback=None)
                Path(Config.file_info["path"]).write_text(file_content, encoding="utf-8")
                saved_title = window_title.replace(Param.unsaved_mark, Param.normal_mark)
                active_w.set_title(saved_title)

    @staticmethod
    def Level_one_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('# ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def Level_two_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('## ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def Level_three_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('### ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def Level_four_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('#### ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def Level_five_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('##### ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def Level_six_head():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('###### ')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def insert_img():
        if active_w := webview.active_window():
            js_code = "insertTextAtCursor('![]()')"
            active_w.evaluate_js(js_code, callback=None)

    @staticmethod
    def do_nothing():
        print("do_nothing")

    @staticmethod
    def clear():
        if active_w := webview.active_window():
            _clear_js_code = """handleClearClick();"""
            active_w.evaluate_js(_clear_js_code, callback=None)

    @staticmethod
    def forward_page():
        if active_w := webview.active_window():
            forward_code = "history.forward();" if Config.IS_WINDOWS else "history.back();"
            active_w.evaluate_js(forward_code)

    @staticmethod
    def backward_page():
        if active_w := webview.active_window():
            backward_code = "history.back();" if Config.IS_WINDOWS else "history.forward();"
            active_w.evaluate_js(backward_code)

    @staticmethod
    def help_about():
        if active_w := webview.active_window():
            _e = JsAndHtmlGen.gen_help_about()
            js_code = f"""document.getElementById("popup").innerHTML = '{_e}';"""
            active_w.evaluate_js(f"{js_code}window.showPopup();")
