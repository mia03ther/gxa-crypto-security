"""第 1 讲练习：把每个 raise NotImplementedError 换成你的代码。

判分：pytest lecture-01/tests
"""
from Crypto.Hash import keccak

# 小曲线 y² = x³ + 7 (mod 17)，生成元 G = (15, 13)，一共 18 个点
TOY_P = 17
TOY_G = (15, 13)

# secp256k1：同样是 y² = x³ + 7，只是模数 p 大得多
P = 2**256 - 2**32 - 977
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)

# 无穷远点 O 用 None 表示


def inv(a, p):
    """a 在模 p 下的逆元。"""
    raise NotImplementedError


def add(A, B, p):
    """曲线 y² = x³ + 7 (mod p) 上的点加法 A + B。"""
    raise NotImplementedError


def mul(k, A, p):
    """标量乘法 k·A，用“倍加”法。"""
    raise NotImplementedError


def brute_force(Q, p=TOY_P, g=TOY_G):
    """在小曲线上从 1 开始试，找出 k 使 k·G = Q。"""
    raise NotImplementedError


def address(priv):
    """进阶：私钥 → 以太坊地址（小写，带 0x）。"""
    raise NotImplementedError
