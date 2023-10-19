from typing import Literal

from markup import __version__

PositionTypeStr = Literal["right", "left", "top", "bottom"]


class JsAndHtmlGen:
    @classmethod
    def gen_close_popup(cls, position: PositionTypeStr = "right"):
        return f"""<div style="text-align: {position};"><button onclick="hidePopup()">close</button></div>"""

    @classmethod
    def gen_help_about(cls):
        _close_popup = cls.gen_close_popup()
        _help = """<h2>关于 MarkUp</h2><p>Version: {}</p><p>Author: ayuge sheng</p><p>Copyright © 2023 - 2023 ayuge.</p>"""
        return f"{_help.format(__version__)}{_close_popup}"

    @classmethod
    def gen_no_come(cls):
        _close_popup = cls.gen_close_popup()
        normal = """<h2>还未开发，敬请期待。。。</h2>"""
        return _close_popup
