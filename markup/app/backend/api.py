import sys

from markup.common.params import Param
from markup.config import webview

__all__ = [
    "Api",
]


class Api:
    def __init__(self):
        self.close_window_flag = False

    def init(self):
        return {"message": "Hello from Python {0}".format(sys.version)}

    def minimize_window(self):
        webview.windows[0].minimize()
        return {"message": "Window minimized"}

    def close_window(self):
        webview.active_window().destroy()
        self.close_window_flag = True
        sys.exit()

    def logTextChange(self):
        title = webview.active_window().title
        if Param.unsaved_mark not in title:
            unsaved_title = title.replace(Param.normal_mark, Param.unsaved_mark)
            webview.active_window().set_title(unsaved_title)
