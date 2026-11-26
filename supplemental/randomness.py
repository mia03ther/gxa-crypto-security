"""第 2 讲补充：用 3 位整数演示取模偏差。"""

import secrets


def three_way_counts() -> tuple[list[int], list[int]]:
    """返回直接取模和拒绝采样下，三个结果各对应多少个输入。"""
    modulo = [0, 0, 0]
    accepted = [0, 0, 0]
    for value in range(8):
        bucket = value % 3
        modulo[bucket] += 1
        # 接受 0 到 5，留下可均分给三个结果的六个输入。
        if value < 6:
            accepted[bucket] += 1
    return modulo, accepted


def choose_bucket() -> int:
    """从 0、1、2 中等概率选出一个结果。"""
    return secrets.randbelow(3)
