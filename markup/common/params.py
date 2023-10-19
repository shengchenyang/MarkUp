from typing import Any, Literal, NamedTuple, Optional, TypedDict, TypeVar, Union

__all__ = ["Param", "FileInfo"]


class Param:
    untitled_mark = "Untitled*"
    unsaved_mark = "• - MarkUp"
    normal_mark = " - MarkUp"


class FileInfo(TypedDict):
    path: str
    notes: str
