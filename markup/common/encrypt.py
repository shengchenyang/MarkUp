import base64
import hashlib
from typing import Union

__all__ = ["EncryptOperation"]


class EncryptOperation:
    """普通加密方法"""

    @classmethod
    def md5(cls, encrypt_data: str) -> str:
        """md5 处理方法

        Args:
            encrypt_data: 需要 md5 处理的参数

        Returns:
            1): md5 处理后的参数
        """
        hl = hashlib.md5()
        hl.update(encrypt_data.encode(encoding="utf-8"))
        return hl.hexdigest()

    @classmethod
    def base64_encode(
        cls, encode_data: Union[bytes, str], url_safe: bool = False
    ) -> str:
        """base64 编码

        Args:
            encode_data: 需要 base64 编码的参数
            url_safe: 标准的 Base64 编码后可能出现字符 + 和 /，在 url 中就不能直接作为参数。是否要处理此情况

        Returns:
            1). base64 编码后的结果
        """
        if not isinstance(encode_data, bytes):
            encode_data = bytes(encode_data, encoding="utf-8")
        if url_safe:
            return str(base64.urlsafe_b64encode(encode_data), encoding="utf-8")
        return str(base64.b64encode(encode_data), encoding="utf-8")
