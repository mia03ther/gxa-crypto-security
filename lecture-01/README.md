# 第 1 讲：课程地图与椭圆曲线

- 事故：币安 2026、Bitget 2026
- 语言：Python

## 练习

打开 `exercise/ecc.py`，把每个 `raise NotImplementedError` 换成你的代码：

1. `inv`：模 p 下的逆元
2. `add`：曲线 y² = x³ + 7 上的点加法
3. `mul`：标量乘法 k·G
4. `brute_force`：在 mod 17 的小曲线上，从公钥倒推私钥
5. 用同一套 `add` 和 `mul` 算 secp256k1 上的 2G
6. 进阶：`address`，私钥 → 以太坊地址

第 4 题在 18 个点的曲线上一下就能试完；secp256k1 有约 2²⁵⁶ 个点，同样的方法试不完。这就是私钥安全的来源。

## 判分

```bash
uv run pytest lecture-01/tests
```

参考答案在 `solution/`，做完再看。用 `GXA_SOLUTION=1 uv run pytest lecture-01/tests` 可以检查参考答案。
