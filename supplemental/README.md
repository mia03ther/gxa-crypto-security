# Fork 自学练习

这些练习按课程大纲补充，可在仓库根目录运行 `uv run python -m pytest supplemental/tests`。排行榜讲数以课程官方判分为准。

## 第 2 讲 · 随机数与熵

把 3 个随机位看作等概率的 0 到 7。先算出每个数对 3 取模后落在哪一组，再试只接受 0 到 5，抽到 6 或 7 就重抽。运行 [示例实现](randomness.py) 的 `three_way_counts()` 对照你的计数。

直接取模时，0 和 1 各有 3 个原始值，2 只有 2 个。拒绝采样让每组都有 2 个原始值。实际程序可以直接用 `secrets.randbelow(3)` 做有界采样。[Python secrets 文档](https://docs.python.org/3/library/secrets.html)

## 第 3 讲 · 密钥派生

在 [示例实现](key_derivation.py) 中，用固定的合成种子和盐跑两次 HKDF-SHA256。比较同一个用途重复派生的结果，再比较加密和认证两个用途的结果。试着让两个用途使用同一个标签并重跑测试。

同样的种子、盐和用途标签会得到同样的密钥。`info`（在 PyCryptodome 中叫 `context`）把输出绑定到指定用途。练习只使用合成字节，范围是 HKDF 用途分离。[RFC 5869](https://www.rfc-editor.org/rfc/rfc5869) · [PyCryptodome KDF 文档](https://www.pycryptodome.org/src/protocol/kdf)
