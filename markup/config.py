import platform
from pathlib import Path
from typing import Literal

import webview
import webview.menu as wm

from markup.common.params import FileInfo

__all__ = [
    "webview",
    "Config",
    "wm",
]

SystemTypeStr = Literal["windows", "linux", "darwin"]


class Config:
    _sys: SystemTypeStr = platform.system().lower()
    app_path = Path(__file__).parent
    root_path = app_path.parent

    IS_WINDOWS = _sys == "windows"
    IS_LINUX = _sys == "linux"
    IS_MACOS = _sys == "darwin"

    COMMON_DIR = app_path / "common"
    VIT_DIR = app_path / "VIT"
    PROFILE_DIR = app_path / "profiles"

    FileInfo: FileInfo = None
