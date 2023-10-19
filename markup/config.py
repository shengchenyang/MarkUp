from pathlib import Path

import webview

from markup.common.params import FileInfo

__all__ = [
    "webview",
    "Config",
]


class Config:
    CONFIG_DIR = Path(__file__).parent
    ROOT_DIR = CONFIG_DIR.parent
    COMMON_DIR = CONFIG_DIR / "common"
    VIT_DIR = CONFIG_DIR / "VIT"

    FileInfo: FileInfo = None
