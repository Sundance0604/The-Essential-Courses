# ECO6109 金融市场计量详细注疏

**适合有数学和计量理论基础、但没系统学过金融计量的读者。** 参照“GPT细写版”的教学方式，从金融问题开始，逐步解释概念、公式的来源、推导中的每一步和结果的经济含义。

本次完成前五份课件，共188页的重构编撰。最后一份机器学习按要求暂缓。

## 从哪里开始

想连续阅读，请打开[七章与高观点合订本](ECO6109_金融市场计量详细注疏_合订本.md)。想先了解学习顺序，请读[课程总目与知识体系](01_课程总目与知识体系.md)。具体写法、符号和来源约定见[编纂凡例](00_编纂凡例.md)。

## 分章阅读

1. [金融市场、收益与信息](chapters/01_金融市场收益与信息.md)：现金流、股息、复利、对数、基准与效率。
2. [风险、分散化与投资组合](chapters/02_风险分散化与投资组合.md)：方差推导、相关、最小方差、Sharpe、VaR 与条件风险。
3. [历史收益估计与统计推断](chapters/03_历史收益估计与统计推断.md)：标准误、检验、区间、配对比较与长期方差。
4. [市场回归、CAPM 与投资表现](chapters/04_市场回归CAPM与投资表现.md)：α/β 的金融解释、OLS、原课件输出与诊断。
5. [多因子、排序与截面回归](chapters/05_多因子排序与截面回归.md)：SMB/HML、分组投影、Fama–MacBeth 与回归组合权重。
6. [平稳过程、ARMA 与预测](chapters/06_平稳过程ARMA与预测.md)：稳定性、ACF/PACF、可逆、似然与多步预测。
7. [单位根、伪回归与协整](chapters/07_单位根伪回归与协整.md)：趋势处理、DF/ADF、共同趋势、误差修正与价差头寸。

## 深入与复习

高观点：[信息、条件期望与投影](higher_views/01_信息条件期望与投影.md)；[线性滤波、稳定性与共同趋势](higher_views/02_线性滤波稳定性与共同趋势.md)。

考试要略：[核心概念与公式](exam/核心概念与公式.md)、[重要定理与证明](exam/重要定理与证明.md)、[经典题型与解法](exam/经典题型与解法.md)、[易错概念辨析](exam/易错概念辨析.md)、[考前速览](exam/考前速览.md)。本地没有最新测验范围或历年试卷，因此没有虚构命题频率，也未将练习冒充真题。

## 来源与可核对结果

[课件覆盖索引](02_课件覆盖索引.md)按知识主题定位，[逐页处理表](sources/逐页处理表.md)逐页说明188页的去向，[编纂审查报告](03_编纂审查报告.md)记录技术核对与局限。

[伪回归实验报告](exercises/伪回归实验与结果.md)完整运行课件要求的500次人工模拟，附数据、图与复现方法。正文的四张图均为课件假设参数或人工模拟生成，不是真实行情实证图。

原始PDF保持不变。课件中只有截图、未提供原始数据的实证结果，已核对显示与解释，但没有声称独立复算。本次交付为Markdown。

> GitHub publication: this snapshot contains newly authored notes, generated teaching figures, and artificial simulation data only. Original lecture PDFs and verbatim text extractions remain local. Source page names identify local reference materials; rebuilding source coverage requires those PDFs. Lecture VI remains deferred.
