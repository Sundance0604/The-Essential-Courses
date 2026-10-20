# 高观点专题2：矩条件、GMM与弱识别

【学术拓展】本专题将课件OLS、IV、2SLS、稳健协方差和过度识别放入统一矩估计框架。完整矩阵证明属于理解用补注；L4a p.107明确IV一致性推导不要求考核。

## 一、统一对象：经验矩的根或最小距离

令$g_i(\beta)=z_i(y_i-x_i'\beta)$，$g_N(\beta)=N^{-1}\sum g_i(\beta)$，$S=E(zz')$、$G=E(zx')$。真参数满足$Eg_i(\beta_0)=0$。恰好识别且$G$可逆时，直接解$g_N=0$；过度识别时通常不能令所有样本矩同时为零，改为

$$
\hat\beta_W=\arg\min_b g_N(b)'W_Ng_N(b),
\quad W_N\to_p W\succ0.
$$

一阶条件给

$$
\hat\beta_W=(\hat G'W_N\hat G)^{-1}\hat G'W_N\left(\frac1N\sum z_iy_i\right).
$$

取$W_N=(Z'Z/N)^{-1}$就是2SLS；取$z=x$便退回OLS。权重决定如何比较不同单位、不同相关结构的矩偏离。

## 二、识别先于概率论

总体矩函数为$g(b)=E(zy)-Gb$。若$G$列满秩，则$g(b)=0$至多有一个解；若秩不足，非零$h$满足$Gh=0$，$b$与$b+h$产生完全相同的矩。增加样本不会创造缺失的方向。

这说明阶条件只能数方程，秩条件才检查方程是否独立。它也说明识别限制是可见分布和结构目标之间的桥，不能从样本矩求解成功反推经济假设正确。

## 三、线性GMM的一致性完整证明

定义$\hat G=Z'X/N$。线性结构给出精确式

$$
\hat\beta_W-\beta_0=(\hat G'W_N\hat G)^{-1}\hat G'W_Ng_N(\beta_0).
$$

LLN使$\hat G\to_pG$、$g_N(\beta_0)\to_p0$。因$W\succ0$、$G$列满秩，任意非零$a$有$a'G'WGa=(Ga)'W(Ga)>0$，故$G'WG$可逆。连续映射使整个乘积趋于0。

2SLS中$W=S^{-1}$，所以识别敏感度矩阵是$A=G'S^{-1}G$。这比“两个阶段都用OLS，所以一致”更严谨，因为第二阶段含样本估计出的解释变量，不能未经论证套普通外生模型。

## 四、渐近线性化与夹心结构

设$\Omega=E(u^2zz')$有限，i.i.d.和CLT给$\sqrt Ng_N(\beta_0)\Rightarrow N(0,\Omega)$。于是

$$
\sqrt N(\hat\beta_W-\beta_0)
=(G'WG)^{-1}G'W\frac1{\sqrt N}\sum z_iu_i+o_p(1),
$$

$$
V_W=(G'WG)^{-1}G'W\Omega WG(G'WG)^{-1}.
$$

$G$是矩对参数的负Jacobian，$\Omega$是矩噪声，逆Jacobian决定噪声放大。OLS与IV的稳健协方差并非软件特例，而是这一线性传递公式。

若$\Omega\succ0$，取$W=\Omega^{-1}$得$V_*=(G'\Omega^{-1}G)^{-1}$。可以直接证明其在该矩估计类中最优：任意一阶影响矩阵$A$满足$AG=I$，令$A_*=V_*G'\Omega^{-1}$，则

$$
A\Omega A'-A_*\Omega A_*'
=(A-A_*)\Omega(A-A_*)'\succeq0,
$$

因为交叉项$(A-A_*)\Omega A_*'=(A-A_*)GV_*=0$。这给出效率结论的数学根据与比较类。

若$E(u^2\mid z)=\sigma^2$，$\Omega=\sigma^2S$，最优权重与$S^{-1}$成比例，普通2SLS有效率；异方差下$\Omega$不再与$S$成比例，普通2SLS加稳健SE仍一致，却未必达到最优效率。

## 五、过度识别为何只剩L−K个自由度

以最优权重估计，$J=Ng_N(\hat\beta)'\hat\Omega^{-1}g_N(\hat\beta)$。将原始矩白化，令$B=\Omega^{-1/2}G$，则一阶上

$$
\sqrt N\Omega^{-1/2}g_N(\hat\beta)
=(I-P_B)\sqrt N\Omega^{-1/2}g_N(\beta_0)+o_p(1).
$$

原始白化矩趋于$L$维标准正态；估计参数吸收$\operatorname{col}(B)$中的$K$个方向，剩余投影维数$L-K$，平方长度便趋于$\chi^2_{L-K}$。若$L=K$，没有余空间可检查。

这也解释异方差下应使用正确白化：同方差Sargan的$NR^2$是特定噪声度量的结果，不能仅凭统计量长得像卡方就泛化。

## 六、弱识别：逆Jacobian的稳定性丢失

一元模型中$\hat\beta-\beta=\hat m_{zu}/\hat m_{zd}$。固定$m_{zd}\ne0$时，分母波动为$O_p(N^{-1/2})$，相对误差趋零，Taylor展开成立。

若$m_{zd,N}=a/\sqrt N$，假设适当三角阵CLT给

$$
\sqrt N\hat m_{zu}\Rightarrow U,\quad
\sqrt N\hat m_{zd}\Rightarrow a+V,
$$

那么$\hat\beta-\beta\Rightarrow U/(a+V)$，一般不趋零也非正态。随机分母可能接近零，常规t统计量无法由“加一个更稳健的SE”挽救。这里是为说明机制构造的弱识别序列，不声称所有弱IV分布都有同一精确形式。

无效IV令$Eg_i(\beta_0)\ne0$，弱IV令$G$的识别方向过弱；前者错在中心，后者错在敏感度。二者可同时发生，因此小外生性偏离在弱工具下尤其危险。

## 七、加权为何可能改变目标

原矩$E(zu)=0$不推出$E[w(z)zu]=0$。条件均值$E(u\mid z)=0$则使后一式对适当权重成立。课件加权2SLS采用这个更强条件，正是为保证变换后矩合法。

同理，仅将OLS定义为$E(xu)=0$的投影时，WLS可能估计另一个投影；若原条件均值模型正确，加权才在保持参数目标下有改进效率的空间。稳健SE与更换权重的根本区别在这里，而不只是“前者容易后者复杂”。
