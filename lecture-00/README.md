# 第 0 讲：开始之前

文字版，没有对应的动画讲解。读完这一页，你应该能做到三件事：

1. 在自己电脑上跑通第 1 讲的判分测试；
2. 确认自己的 Python 够用，不够的地方知道补什么；
3. 会做模运算，看懂第 1 讲里的“模 17”。

预计用时：环境 30 分钟，Python 自测 15 分钟，模运算 20 分钟。

---

## 一、这门课怎么学

每一讲分三步：

1. **学讲解**：在 B 站搜索“GXA 密码学训练营”。每讲从一起真实的安全事故讲起，倒推出背后的密码学原理。标有“进阶”的段落讲推导和攻击细节，第一遍可以跳过，不影响后面。
2. **读讲义**：本仓库 `lecture-NN/README.md`，写了这一讲的练习说明。
3. **做练习**：打开 `lecture-NN/exercise/`，把每个 `raise NotImplementedError` 换成你的代码，在本地跑判分测试，全部通过就算完成。

参考答案在 `lecture-NN/solution/`。先自己做，卡住了再看。

结课标准：12 道必做题完成 10 道，第 8 讲不强制。

---

## 二、搭环境

需要三样东西：Git（下载代码）、uv（管理 Python 和依赖）、一个代码编辑器。

### 1. 装 Git

- **Windows**：从 <https://git-scm.com/download/win> 下载安装，一路默认选项即可。
- **macOS**：打开“终端”，运行 `xcode-select --install`，按提示安装。如果提示已经安装，跳过这一步。

装好后，在终端（Windows 用 PowerShell）里运行：

```bash
git --version
```

能打印出版本号就行。

> 不想装 Git 也可以：在仓库主页点 **Code → Download ZIP**，解压后跳到第 3 步。但之后要往排行榜提交，还是需要 Git。

### 2. 装 uv

uv 是一个 Python 工具，能顺带装好合适版本的 Python，并按本仓库的 `pyproject.toml` 装依赖。你不需要提前装 Python。

- **Windows**（PowerShell）：

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- **macOS / Linux**（终端）：

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

装完**关掉终端再重新打开**，然后运行：

```bash
uv --version
```

能打印出版本号就行。安装方法以 uv 官方文档为准：<https://docs.astral.sh/uv/getting-started/installation/>。

### 3. 下载课程代码

```bash
git clone https://github.com/slucifersz/gxa-crypto-security.git
cd gxa-crypto-security
```

之后所有命令都在 `gxa-crypto-security` 这个文件夹里运行。

想上排行榜的话，先在 GitHub 上点 **Fork** 把仓库复制到自己账号下，再 clone 你自己的那份。

### 4. 装依赖

```bash
uv sync
```

这一步会在当前文件夹里建一个 `.venv`，装好 Python 3.11 以上的版本、`pycryptodome`（算哈希用）和 `pytest`（判分用）。

### 5. 跑一次判分，确认环境通了

```bash
uv run pytest lecture-01/tests
```

练习还没做，所以应该看到 6 个测试**全部失败**，最后一行类似：

```
FAILED lecture-01/tests/test_ecc.py::test_1_inv - NotImplementedError
...
============================== 6 failed in 0.61s ===============================
```

失败原因都是 `NotImplementedError`，说明环境没问题，只是函数还没写。看到这个结果，环境就搭好了。

再确认一下参考答案能通过（macOS / Linux）：

```bash
GXA_SOLUTION=1 uv run pytest lecture-01/tests
```

Windows PowerShell 的写法：

```powershell
$env:GXA_SOLUTION=1; uv run pytest lecture-01/tests; Remove-Item Env:GXA_SOLUTION
```

应该看到 `6 passed`。

### 6. 编辑器

用你习惯的就行。没有习惯的，推荐 VS Code，装上 Python 扩展。用 VS Code 打开 `gxa-crypto-security` 文件夹，右下角选择解释器时选 `.venv` 里的那个。

### 常见问题

| 现象 | 处理 |
|---|---|
| `uv` 或 `git` 提示“找不到命令” | 关掉终端重新打开；还不行就重启电脑，让新的 PATH 生效 |
| `uv sync` 下载很慢或超时 | 换国内 PyPI 镜像，见下方说明 |
| `uv sync` 下载 Python 失败 | 先从 <https://www.python.org/downloads/> 手动装 Python 3.11 或更新版本，再运行 `uv sync`，uv 会直接用它 |
| `git clone` 很慢或失败 | 改用 Download ZIP，或者换个网络环境 |
| 报 `ModuleNotFoundError: No module named 'Crypto'` | 没有通过 uv 运行。命令前面要加 `uv run` |
| Windows 上报“禁止运行脚本” | 用上面第 2 步带 `-ExecutionPolicy ByPass` 的那条命令安装 |

**换国内 PyPI 镜像**：在 `uv sync` 前设置环境变量，例如清华源：

```bash
# macOS / Linux
export UV_DEFAULT_INDEX=https://pypi.tuna.tsinghua.edu.cn/simple
```

```powershell
# Windows PowerShell
$env:UV_DEFAULT_INDEX="https://pypi.tuna.tsinghua.edu.cn/simple"
```

**不想用 uv**：也可以用 Python 自带的 venv 和 pip，效果一样。需要你已经装好 Python 3.11 或更新版本：

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows：.venv\Scripts\activate
pip install pycryptodome pytest
python -m pytest lecture-01/tests
```

---

## 三、Python 要会到什么程度

练习只用 Python 的基础部分，不用任何框架。需要会：

- 变量、`if`、`for`、`while`
- 写函数：`def`、参数、`return`
- 元组：用 `(x, y)` 表示一个点，用 `x, y = P` 拆开
- `None`：本课用它表示“无穷远点”，判断写 `if P is None:`
- 整数运算：`+ - * // % **`
- 读懂报错信息里的文件名、行号和最后一行的错误类型

不需要会：类、装饰器、异步、第三方库的用法。

### 自测

不运行代码，先想一想下面每行会打印什么，再运行核对。全对或只错一两个，就够用了。

```python
print(17 // 5, 17 % 5)

def f(P):
    if P is None:
        return "O"
    x, y = P
    return x + y

print(f((3, 4)), f(None))

k, n = 13, 0
while k > 0:
    if k % 2 == 1:
        n += 1
    k //= 2
print(n)
```

答案：`3 2`、`7 O`、`3`。最后一段在数 13 的二进制里有几个 1（13 = 1101₂）。第 1 讲的“倍加法”就是这样一位一位处理 k 的。

如果错得比较多，建议先花几个小时过一遍任意一本 Python 入门书的前几章（变量、分支、循环、函数），再回来。

### 第 1 讲会用到的几个 Python 写法

```python
>>> 2**256                     # Python 的整数没有上限，256 位的数直接算
115792089237316195423570985008687907853269984665640564039457584007913129639936
>>> 0xFA                       # 0x 开头是十六进制
250
>>> hex(250)
'0xfa'
>>> int('11111010', 2)         # 二进制字符串转整数
250
>>> (250).to_bytes(1, 'big').hex()   # 整数转字节，再转十六进制字符串
'fa'
>>> pow(3, 16, 17)             # 3 的 16 次方再模 17，比 3**16 % 17 快得多
1
```

---

## 四、模运算入门

第 1 讲的所有计算都在“模 p”下进行。这一节先把它练熟。

### 1. 余数

`a mod p` 就是 a 除以 p 的余数，结果总在 0 到 p − 1 之间。Python 里写 `a % p`。

```
23 mod 17 = 6        因为 23 = 1×17 + 6
35 mod 17 = 1        因为 35 = 2×17 + 1
```

钟表就是“模 12”：10 点再过 5 小时是 3 点，因为 15 mod 12 = 3。

### 2. 负数取模

数学上，−7 mod 17 = 10，因为 −7 + 17 = 10。Python 的 `%` 也是这样算的：

```python
>>> -7 % 17
10
```

注意：C、Java、JavaScript 里 `-7 % 17` 得 −7，不是 10。用别的语言时要自己加上 p。

### 3. 加、减、乘

先正常算，最后取模。也可以每一步都取模，结果一样：

```
(14 + 9) mod 17 = 23 mod 17 = 6
(5 − 12) mod 17 = −7 mod 17 = 10
(6 × 7) mod 17 = 42 mod 17 = 8
```

数字很大时，每一步都取模可以让中间结果保持很小。

### 4. 除法：乘以逆元

模运算里没有小数，“除以 a”要换成“乘以 a 的逆元”。a 的逆元是满足下式的那个数 b：

```
a × b mod p = 1
```

例：5 × 7 = 35，35 mod 17 = 1，所以 5 在模 17 下的逆元是 7。于是“3 ÷ 5”在模 17 下等于 3 × 7 = 21，21 mod 17 = 4。

验算：4 × 5 = 20，20 mod 17 = 3。确实回到了 3。

p 是质数时，1 到 p − 1 的每个数都有逆元。怎样快速求逆元，是第 1 讲第一道练习 `inv` 要你写的内容，讲解里给了两种方法。

### 5. 练习

先手算，再用 Python 核对：

1. 100 mod 17
2. −1 mod 17
3. (13 × 13) mod 17
4. (15³ + 7) mod 17
5. 在 1 到 16 里试一试，找出 3 在模 17 下的逆元

答案：

1. 15
2. 16
3. 16
4. 16
5. 6（3 × 6 = 18，18 mod 17 = 1）

第 3 题和第 4 题的结果相等，说明点 (15, 13) 满足 y² ≡ x³ + 7 (mod 17)，也就是说它在第 1 讲那条小曲线上。它就是第 1 讲里的生成元 G。

---

## 五、准备好了

- [ ] `uv run pytest lecture-01/tests` 能跑，看到 6 个失败
- [ ] Python 自测基本答对
- [ ] 模运算练习全部答对

三项都打勾，就可以开始第 1 讲了。
