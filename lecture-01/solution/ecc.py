"""第 1 讲参考答案。"""
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
    return pow(a, p - 2, p)


def add(A, B, p):
    """曲线 y² = x³ + 7 (mod p) 上的点加法 A + B。"""
    if A is None:
        return B
    if B is None:
        return A
    x1, y1 = A
    x2, y2 = B
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if A == B:
        k = 3 * x1 * x1 * inv(2 * y1, p) % p
    else:
        k = (y2 - y1) * inv(x2 - x1, p) % p
    x3 = (k * k - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return (x3, y3)


def mul(k, A, p):
    """标量乘法 k·A，用“倍加”法。"""
    R = None
    while k > 0:
        if k & 1:
            R = add(R, A, p)
        A = add(A, A, p)
        k >>= 1
    return R


def brute_force(Q, p=TOY_P, g=TOY_G):
    """在小曲线上从 1 开始试，找出 k 使 k·G = Q。"""
    R, k = g, 1
    while R != Q:
        R, k = add(R, g, p), k + 1
    return k


def address(priv):
    """进阶：私钥 → 以太坊地址（小写，带 0x）。"""
    x, y = mul(priv, G, P)
    h = keccak.new(digest_bits=256, data=x.to_bytes(32, "big") + y.to_bytes(32, "big")).digest()
    return "0x" + h[-20:].hex()
