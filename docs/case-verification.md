# 案例核对表

核对于 2026-11-16。方法：网络搜索加网页读取，优先一手来源。

状态说明：

- **属实**：核心事实有读过正文的来源支持。
- **部分属实**：能用，但原说法有地方要改。
- “一手未读到”表示官方报告或原始披露打不开，细节只有二手转述，写讲义前要再试。

币安 2026 不在本表内，链上数据还没有核对。

## 总表

| 讲 | 案例 | 状态 | 写讲义时必须改或注明的地方 |
|---|---|---|---|
| 1、9 | Bitget 2026 | 部分属实 | 见下文，官方完整报告未发布 |
| 2 | Profanity / Wintermute 2022 | 部分属实 | Wintermute 与 Profanity 的关联只到“CEO 称极可能” |
| 2 | Milk Sad 2023 | 属实 | Libbitcoin 官方不认为这是漏洞 |
| 3 | Slope 钱包 2022 | 部分属实 | 助记词明文上报属实；“这就是被盗原因”未被证实 |
| 4 | PS3 2010 | 属实 | 幻灯片记号与教科书相反 |
| 4 | Anyswap 2021 | 属实 | 一手未读到 |
| 5 | BNB Bridge 2022 | 部分属实 | 5.7 亿是账面价值，不是实际损失 |
| 6 | Wormhole 2022 | 属实 | 金额写约 3.2 亿至 3.26 亿；一手未读到 |
| 7 | Optimism OP 事件 2022 | 属实 | 被重放的是一串交易，不是一笔 |
| 7 | spWETH permit 盗签 2024 | 属实 | 新选案例，链上数据已读 |
| 8 | 偏置 nonce 论文 2019 | 属实 | 论文 PDF 未读到，只能写“数百个”私钥 |
| 9 | Bybit 2025 | 属实 | “前端被篡改”要写准确 |
| 9 | Radiant 2024 | 部分属实 | “盲签”一词只有二手来源使用 |
| 11 | Ronin 2022 | 属实 | 一手未读到 |
| 11 | Harmony 2022 | 属实 | 密钥泄露途径未公开；一手未读到 |
| 12 | BitForge 2023 | 部分属实 | 是两类漏洞，不能合并成“缺少零知识证明” |
| 备用 | Zcash 伪造漏洞 | 属实 | 无 |
| 备用 | Frozen Heart 2022 | 属实 | 无 |

## 逐条

### Bitget（2026-09-24）

- **时间**：9-24 18:31 UTC 首批未授权转账，19:05 UTC 发现并拦截提现。北京时间是 9-25 凌晨，所以有的来源写 25 日。
- **金额**：官方页写约 3.88 亿美元；初报 3.516 亿，9-25 更新为 3.875 亿。
- **范围**：官方称 12 个热/温钱包地址、11 条链、12 种资产；BlockSec 数出 12 条链、13 种资产。
- **官方说法**：攻击者利用一个第三方安全产品的零日进入内部管理系统，用真实有效的高权限凭据，把伪造的提现指令直接写入钱包系统，在生成提现记录之前绕过了风控校验。私钥未泄露，冷钱包未受影响。
- **调查方说法（媒体转述，报告原文未读到）**：SlowMist 称最早恶意活动在 8-31；涉及两个安全产品 A 和 B，明确提到零日的只有 A。
- **未知**：产品名称、零日细节、横向移动路径、确定归因。官方正式安全报告仍写“即将发布”。
- **朝鲜归因**：CEO 和链上分析师提出；BlockSec 认为链上重合更指向共用洗钱团伙。未定论。
- 来源：[Bitget 官方事件页](https://www.bitget.com/campaigns/bitget-security-incident-2026)（一手）、[BlockSec](https://blocksec.com/blog/bitget-hack-laundering-fund-tracing)、[BleepingComputer 9-30](https://www.bleepingcomputer.com/news/security/bitget-hacked-via-zero-day-in-third-party-security-products/)、[Cointelegraph](https://cointelegraph.com/news/bitget-hack-zero-day-slowmist-investigation)、[The Block](https://www.theblock.co/news/regulation/2026-09-28-bitget-attacker-tested-risk-controls-small-transfers-388-million-theft-ceo-says-417045)

### Profanity / Wintermute（2022-09）

- **Profanity 漏洞**：用 32 位随机值做种子生成 256 位私钥，约 40 亿种可能，可枚举。2022-01-17 有人提 issue，2022-09-15 1inch 披露。
- **Wintermute**：2022-09-20 被盗约 1.6 亿美元。CEO 称“most likely”是 Profanity 类攻击；分析师的依据是金库管理员地址以 0x0000000 开头。没有正式复盘确认。
- 来源：[1inch 披露文](https://1inch.com/blog/post/a-vulnerability-disclosed-in-profanity-an-ethereum-vanity-address-tool)（一手）、[Profanity issue #61](https://github.com/johguse/profanity/issues/61)（一手）、[The Block](https://www.theblock.co/post/171559/wintermute-ceo-gaevoy-updates-on-hack-says-firm-will-continue-on-chain-trading)

### Milk Sad（2023）

- Libbitcoin Explorer 3.0.0 至 3.6.0 的 `bx seed` 用系统时钟给 `std::mt19937` 播种，熵只有 32 位。CVE-2023-39910。
- 主要盗币在 2023-07-12，约 29.65 BTC；合计超过 90 万美元。2023-08-08 公开披露。
- CVE 记录注明厂商不认为这是漏洞。
- 来源：[Milk Sad 披露页](https://milksad.info/disclosure.html)（一手）、[CVE 记录](https://cveawg.mitre.org/api/cve/CVE-2023-39910)（一手）

### Slope 钱包（2022-08）

- **属实的部分**：Slope 移动端的 Sentry 错误上报把助记词和私钥发到 Slope 的 Sentry 服务器，以可读文本存储。
- **未证实的部分**：Slope 8-11 声明称审计方没有确凿证据把该漏洞与被盗联系起来，只有 1,444 个被盗地址能对上 Sentry 记录。OtterSec 称现有证据不能解释所有被盗账户。
- **数字不统一**：钱包数约 8,000 到 9,321；金额约 400 万到 800 万美元。
- 2022-08-02 约 22:37 UTC 起，持续约 4 小时。
- 来源：[Sentry 官方博客](https://blog.sentry.io/slope-wallet-solana-hack)（一手）、[The Block](https://www.theblock.co/post/161425/slope-wallet-provider-saved-user-seed-phrases-in-plain-text-solana-security-researchers-find)、[Cointelegraph](https://cointelegraph.com/news/experts-find-private-keys-on-slope-servers-still-puzzled-over-access)、[ForkLog](https://forklog.com/en/slope-denies-link-between-wallet-bug-and-solana-breach/)
- 未读到：Solana 基金会文章、SlowMist 分析、Slope 声明原文。

### PS3（2010）

- 2010-12-29，27C3，演讲“Console Hacking 2010: PS3 Epic Fail”，fail0verflow。
- 索尼每次签名用了相同的随机数，两个签名即可算出私钥。
- 幻灯片里 m 是随机数、k 是私钥，与教科书相反。
- 来源：[27C3 幻灯片](https://fahrplan.events.ccc.de/congress/2010/Fahrplan/attachments/1780_27c3_console_hacking_2010.pdf)（一手）、[日程页](https://fahrplan.events.ccc.de/congress/2010/Fahrplan/events/4087.en.html)（一手）

### Anyswap（2021-07）

- 2021-07-10 UTC。损失约 239 万 USDC 和 550 万 MIM，合计约 787 万至 790 万美元。
- V3 路由 MPC 账户在 BSC 上的两笔交易签名 R 值相同，攻击者反推出私钥。
- 来源：[ChainCatcher](https://chaincatcher.com/en/article/2063348)、[rekt.news](https://rekt.news/anyswap-rekt)
- 未读到：[Anyswap 官方声明](https://medium.com/multichainorg/anyswap-multichain-router-v3-exploit-statement-6833f1b7e6fb)

### BNB Bridge（2022-10）

- 2022-10-06（UTC 为 6 日至 7 日之交）。攻击者取得 200 万 BNB，账面约 5.6 亿至 5.7 亿美元；实际转出链外约 1 亿至 1.3 亿美元，其余因停链留在链上。
- IAVL RangeProof 验证缺陷：路径节点同时含 left 和 right 时，根哈希计算忽略 right。
- 官方公告用“提取”，没有点名 IAVL；技术原因来自第三方分析。
- 来源：[BNB Chain 公告](https://www.bnbchain.org/en/blog/bnb-chain-ecosystem-update)（一手）、[Verichains](https://blog.verichains.io/p/vsa-2022-101-iavl-spoofing-attack)、[Halborn](https://www.halborn.com/blog/post/explained-the-bnb-chain-hack-october-2022)

### Wormhole（2022-02）

- 2022-02-02。12 万 wETH，约 3.2 亿至 3.26 亿美元。
- Solana 端 `verify_signatures` 没有校验传入账户是否为真正的 Instructions sysvar，攻击者伪造该账户，铸出 wETH。
- 出问题的函数名两家说法不同：Halborn 写 `load_instruction_at`，CertiK 写 `load_current_index`。
- 来源：[引用官方报告的分析仓库](https://github.com/sbellem/wormhole-attack-analysis)、[CertiK](https://www.certik.com/resources/blog/wormhole-bridge-exploit-incident-analysis)、[Halborn](https://halborn.com/explained-the-wormhole-hack-february-2022/)
- 未读到：Wormhole 官方事故报告。

### Optimism OP 事件（2022-06）

- 2000 万 OP 在 5-26/27 转入 Wintermute 提供的地址，该地址是只在 L1 部署过的 Safe。6-5 攻击者抢先部署，6-8 公开。
- 被重放的是 Safe 部署者 `0x1aa7…0A6A` 在主网的一串旧部署交易。其中工厂部署交易哈希 `0x75a42f…4261` 与主网 2019-12-10 那笔完全相同。
- 该交易 v=28，签名不含链 ID（仅 Cobo 一家给出，Etherscan 不显示 v）。
- 旧工厂用 CREATE，地址只取决于工厂地址和 nonce，攻击者反复调用 `createProxy` 撞出目标地址。
- Wintermute 承认是自己的错。
- 来源：[Wintermute 治理论坛帖](https://gov.optimism.io/t/message-to-optimism-community-from-wintermute/2595)（一手）、[主网交易](https://etherscan.io/tx/0x75a42f240d229518979199f56cd7c82e4fc1f1a20ad9a4864c635354b4a34261)（一手）、[Cobo 分析](https://www.techflowpost.com/en-US/article/10239)、[rekt.news](https://rekt.news/wintermute-rekt)

### spWETH permit 盗签（2024-09-28）

- 约 3,243 万美元，以太坊主网，EIP-2612 permit。
- 交易 `0xf7c00f18175cdea49f8fdad6a1d45edeb318f18f3009f51ab9f4675171c1d8fb`，区块 20847274。一笔 multicall 内先 `permit` 再两次 `transferFrom`。
- permit 的 value 和 deadline 都是 uint256 最大值。
- 媒体报 12,083 枚，链上两笔转账合计 12,124.57 枚，差异原因未查清。
- 来源：[The Block](https://www.theblock.co/post/318574/crypto-whale-loses-over-32-million-in-apparent-phishing-attack)，加链上 calldata。
- 备选对比案例：2024-10-13 的 PEPE Permit2 盗签，约 139 万美元，没有找到交易哈希。[Decrypt](https://decrypt.co/286076/pepe-uniswap-permit2-phishing-attack)

### 偏置 nonce 论文（2019）

- Breitner、Heninger，*Biased Nonce Sense: Lattice Attacks against Weak ECDSA Signatures in Cryptocurrencies*，ePrint 2019/023，Financial Cryptography 2019。
- 摘要称算出数百个比特币私钥，以及数十个以太坊、Ripple、SSH、HTTPS 私钥。
- 来源：[ePrint 摘要页](https://eprint.iacr.org/2019/023)（一手）
- 未读到：论文 PDF。

### Bybit（2025-02-21）

- 约 15 亿美元。
- Safe{Wallet} 一名开发者的机器被攻陷，攻击者往托管前端的 S3 桶注入恶意 JavaScript，只对 Bybit 的 Safe 地址触发。界面显示正常交易，签名人实际签的是另一份载荷。
- 交易通过 delegatecall 把代理合约的 `masterCopy` 改写为恶意实现。
- Safe 强调合约和前端源码没有漏洞，被替换的是线上分发的 JS 文件。
- FBI 归因于朝鲜 TraderTraitor。
- 来源：[FBI IC3 公告](https://www.ic3.gov/PSA/2025/PSA250226)（一手）、[BlockSec](https://blocksec.com/blog/bybit-incident-a-web2-breach-enables-the-largest-crypto-hack-in-history)、[BleepingComputer](https://www.bleepingcomputer.com/news/security/lazarus-hacked-bybit-via-a-breached-safe-wallet-developer-machine/)

### Radiant Capital（2024-10-16）

- 约 5000 万美元，Arbitrum 和 BNB Chain。
- 至少三名核心开发者设备被植入恶意软件。Safe 界面显示正常数据，恶意交易在后台送到硬件钱包签名。
- 官方材料没有用“盲签”一词；“Ledger 盲签 transferOwnership”来自 OneKey 的分析。
- 来源：[Radiant 官方论坛复盘帖](https://community.radiant.capital/t/post-mortem-october-16-2024-exploit-impact-on-riz-vaults/2220)（一手）、[SecurityWeek](https://www.securityweek.com/radiant-capital-50-million-heist-blamed-on-north-korean-hackers/)、[OneKey](https://onekey.so/blog/ecosystem/one-pdf-50m-gone-the-radiant-capital-hack-explained)

### Ronin（2022-03）

- 173,600 ETH 加 2,550 万 USDC，约 6.24 亿至 6.25 亿美元。9 个验证人需 5 个签名。
- 4 个是 Sky Mavis 自己运营的验证人；第 5 个来自 Axie DAO，因 2021 年 11 月的临时代签授权没有撤销。
- “假招聘 PDF”一说只有匿名信源。
- 来源：[Halborn](https://www.halborn.com/blog/post/explained-the-ronin-hack-march-2022)、[The Block](https://www.theblock.co/post/156038/how-a-fake-job-offer-took-down-the-worlds-most-popular-crypto-game)
- 未读到：Ronin 官方事后报告。

### Harmony Horizon 桥（2022-06-23）

- 约 1 亿美元。以太坊侧 5 选 2 多签，事后改为 5 选 4。
- 密钥如何泄露未公开。Lazarus 归因未核实。
- 来源：[The Block](https://www.theblock.co/post/154029/harmonys-100-million-hacker-took-control-of-its-multi-signature-wallet-analysts-say)、[Halborn](https://www.halborn.com/blog/post/explained-the-harmony-horizon-bridge-hack)
- 未读到：Harmony 官方文章。

### BitForge（2023-08-09）

- Fireblocks 披露，两类漏洞：
  - **GG18 / GG20（CVE-2023-33241）**：没有检查对方的 Paillier 模数是否合法，即缺少对模数良构性的零知识证明。部分实现 16 次签名可提取完整私钥。
  - **Lindell17（CVE-2023-33242）**：实现偏离论文，签名失败后没有停止，每次泄露约 1 比特，256 次签名可提取完整私钥。前提是攻击者已攻陷参与的一方。
- Fireblocks 称影响 15 家以上。
- 来源：[Fireblocks 博客](https://www.fireblocks.com/blog/bitforge-fireblocks-researchers-uncover-vulnerabilities-in-over-15-major-wallet-providers/)（一手）、[GG18/GG20 技术报告](https://www.fireblocks.com/blog/gg18-and-gg20-paillier-key-vulnerability-technical-report/)（一手）、[Lindell17 技术报告](https://www.fireblocks.com/blog/lindell17-abort-vulnerability-technical-report/)（一手）、[ePrint 2023/1234](https://eprint.iacr.org/2023/1234)

### 备用：Zcash 伪造漏洞

- Ariel Gabizon 于 2018-03-01 发现，BCTV14 参数生成多产出了不该有的元素，可伪造证明。2018-10-28 Sapling 激活后修复，2019-02-05 公开，CVE-2019-7167。
- 来源：[官方公告](https://zodl.com/zcash-counterfeiting-vulnerability-successfully-remediated/)（一手）

### 备用：Frozen Heart

- Trail of Bits，2022-04-13。Fiat-Shamir 哈希没有包含全部公开值，可伪造证明。涉及 Girault、Bulletproofs、PlonK 的多个实现。
- 来源：[Trail of Bits 博客](https://blog.trailofbits.com/2022/04/13/part-1-coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs-and-plonk/)（一手）
