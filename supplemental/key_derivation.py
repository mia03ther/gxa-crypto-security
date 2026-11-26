"""第 3 讲补充：给两个用途派生独立的示例密钥。"""

from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import HKDF


def derive_demo_keys(seed: bytes, salt: bytes) -> tuple[bytes, bytes]:
    """返回用于数据加密和消息认证的示例密钥。"""
    if len(seed) != 32:
        raise ValueError("seed must contain 32 bytes")
    if len(salt) != 32:
        raise ValueError("salt must contain 32 bytes")

    encryption = HKDF(seed, 32, salt, SHA256, context=b"gxa-demo:v1:encryption")
    authentication = HKDF(seed, 32, salt, SHA256, context=b"gxa-demo:v1:authentication")
    return encryption, authentication
