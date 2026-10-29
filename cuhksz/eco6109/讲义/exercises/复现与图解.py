"""Artificial teaching examples for Lecture I-V; no downloaded market data."""
from pathlib import Path
import json
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
FIG = ROOT / "images"
FIG.mkdir(exist_ok=True)
font = Path(r"C:\Windows\Fonts\msyh.ttc")
if font.exists():
    font_manager.fontManager.addfont(str(font))
    plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(font)).get_name()
plt.rcParams.update({"axes.unicode_minus": False, "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False})


def conventional_ols(x, y):
    """Ordinary iid t p-value, intentionally inapplicable to random-walk levels."""
    xc, yc = x-x.mean(), y-y.mean()
    slope = (xc @ yc) / (xc @ xc)
    intercept = y.mean()-slope*x.mean()
    residual = y-intercept-slope*x
    ssr = residual @ residual
    se = np.sqrt((ssr/(len(x)-2))/(xc@xc))
    t = slope/se
    return {"intercept": float(intercept), "slope": float(slope),
            "r2": float(1-ssr/(yc@yc)), "se": float(se), "t": float(t),
            "p": float(2*stats.t.sf(abs(t), len(x)-2))}, residual


# LV pp.54-55: seed once, retain all 500 replications.
rng = np.random.default_rng(2026)
records = []
first = None
for rep in range(500):
    u, v = rng.normal(0, .04, (2, 240))
    x, y = np.cumsum(u), np.cumsum(v)
    level, residual = conventional_ols(x, y)
    diff, _ = conventional_ols(u, v)
    records.append([rep+1, level["slope"], level["r2"], level["p"],
                    diff["slope"], diff["r2"], diff["p"]])
    if rep == 0:
        first = (x.copy(), y.copy(), residual.copy(), level, diff)
        data = np.column_stack([np.arange(241), np.r_[0, x], np.r_[0, y],
                                np.r_[np.nan, u], np.r_[np.nan, v]])
        np.savetxt(OUT/"spurious_first.csv", data, delimiter=",",
                   header="month,x_log_price,y_log_price,dx,dy", comments="")
results = np.asarray(records)
np.savetxt(OUT/"spurious_all_500.csv", results, delimiter=",",
           header="rep,level_slope,level_r2,level_p,diff_slope,diff_r2,diff_p", comments="")
counts = [int((results[:, j] < .05).sum()) for j in [3, 6]]
rates = [n/500 for n in counts]
summary = {
    "data_type": "artificial independent Gaussian random walks",
    "rng": "numpy.random.default_rng(2026), PCG64; draw u then v each replication",
    "T": 240, "replications": 500, "innovation_sd": .04,
    "level_rejections": counts[0], "difference_rejections": counts[1],
    "level_rejection_rate": rates[0], "difference_rejection_rate": rates[1],
    "first_level": first[3], "first_difference": first[4],
}
(OUT/"spurious_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

fig, ax = plt.subplots(2, 2, figsize=(11, 7), constrained_layout=True)
ax[0, 0].plot(first[0], label="X"); ax[0, 0].plot(first[1], label="Y")
ax[0, 0].set_title("两条独立随机游走：一次路径"); ax[0, 0].legend()
ax[0, 1].scatter(first[0], first[1], s=9, alpha=.6)
xx=np.array([min(first[0]), max(first[0])])
ax[0, 1].plot(xx, first[3]["intercept"]+first[3]["slope"]*xx, color="#bd3f32")
ax[0, 1].set_title(f'水平回归：R²={first[3]["r2"]:.3f}, 常规 p={first[3]["p"]:.3g}')
ax[1, 0].plot(first[2]); ax[1, 0].axhline(0, color="gray", linewidth=.8)
ax[1, 0].set_title("水平回归残差：拟合后仍有持续游走")
ax[1, 1].bar(["水平回归", "一阶差分回归"], rates, color=["#bd3f32", "#267a94"])
ax[1, 1].axhline(.05, linestyle="--", color="black", label="名义 5%")
ax[1, 1].set_ylim(0,1); ax[1, 1].legend()
ax[1, 1].set_title("全部 500 次实验的常规 5% 拒绝率")
fig.savefig(FIG/"03_伪回归实验.png", dpi=170); plt.close(fig)

w=np.linspace(0,1,501)
fig, ax=plt.subplots(figsize=(8,5), constrained_layout=True)
for corr,color in [(0,"#267a94"),(.2,"#bd3f32"),(.8,"#a58324")]:
    variance=w*w*.15**2+(1-w)**2*.25**2+2*w*(1-w)*corr*.15*.25
    ax.plot(np.sqrt(variance)*100,(w*.08+(1-w)*.12)*100,
            label=f"相关系数 {corr}",color=color)
    ax.scatter([np.sqrt(.25*.15**2+.25*.25**2+.5*corr*.15*.25)*100],[10],color=color)
ax.scatter([15,25],[8,12],color="black")
ax.annotate("A",(15,8),xytext=(5,5),textcoords="offset points")
ax.annotate("B",(25,12),xytext=(-15,-15),textcoords="offset points")
ax.set(xlabel="组合标准差（%）",ylabel="预期年收益（%）",
       title="同样两项资产，相关性改变组合风险\n圆点为 50/50 权重；曲线仅限不做空")
ax.legend();ax.grid(alpha=.2)
fig.savefig(FIG/"01_分散化与组合.png",dpi=170);plt.close(fig)

lags=np.arange(21)
fig, axes=plt.subplots(2,2,figsize=(10,6),constrained_layout=True)
for a,(name,acf) in zip(axes.flat,[
    ("AR(1)：φ=0.6",.6**lags),
    ("AR(1)：φ=-0.6",(-.6)**lags),
    ("MA(1)：θ=0.6",np.r_[1,.6/(1+.6**2),np.zeros(19)]),
    ("ARMA(1,1)：φ=0.6，θ=0.5",
     np.r_[1,(.6+.5)*(1+.6*.5)/(1+.5**2+2*.6*.5)*.6**np.arange(20)])]):
    a.stem(lags,acf,basefmt=" ");a.axhline(0,color="gray",lw=.7)
    a.set(title=name,xlabel="滞后阶 k",ylabel="总体 ACF",ylim=(-.75,1.1))
fig.suptitle("总体自相关：结构公式，不是一次样本估计",fontsize=14)
fig.savefig(FIG/"02_ARMA自相关.png",dpi=170);plt.close(fig)

rng2=np.random.default_rng(6109)
eps=rng2.normal(size=(150,200));rw=np.cumsum(eps,axis=1)
ar=np.empty_like(eps)
initial=rng2.normal(0,np.sqrt(1/(1-.6**2)),150)
for t in range(200):
    ar[:,t]=.6*(initial if t==0 else ar[:,t-1])+eps[:,t]
fig,axes=plt.subplots(1,3,figsize=(12,4),constrained_layout=True)
for a,series,title in [(axes[0],ar,"平稳初始化 AR(1)，φ=0.6"),(axes[1],rw,"固定初值随机游走")]:
    a.plot(np.arange(1,201),series[:35].T,alpha=.3,lw=.8)
    a.set(title=title,xlabel="时间",ylabel="水平")
axes[2].plot(np.arange(1,201),np.arange(1,201),label="随机游走：tσ²")
axes[2].axhline(1/(1-.6**2),color="#bd3f32",label="平稳 AR：σ²/(1-φ²)")
axes[2].set(title="相同创新方差，理论水平方差不同",xlabel="时间",ylabel="理论方差")
axes[2].legend()
fig.savefig(FIG/"04_平稳与单位根.png",dpi=170);plt.close(fig)

c=.2*.15*.25
wstar=(.25**2-c)/(.15**2+.25**2-2*c)
vstar=wstar*wstar*.15**2+(1-wstar)**2*.25**2+2*wstar*(1-wstar)*c
calculations={
    "three_state_mean": .2*(-.1)+.5*.04+.3*.12,
    "three_state_variance": .2*(-.1-.036)**2+.5*(.04-.036)**2+.3*(.12-.036)**2,
    "minimum_variance_weight_A":wstar,"minimum_variance_sd":float(np.sqrt(vstar)),
    "minimum_variance_mean":wstar*.08+(1-wstar)*.12,
    "mean_se_60":float(.04/np.sqrt(60)),
    "mean_t_60":float(.005/(.04/np.sqrt(60))),
    "mean_p_normal_60":float(2*stats.norm.sf(.005/(.04/np.sqrt(60)))),
}
(OUT/"worked_example_checks.json").write_text(json.dumps(calculations,indent=2),encoding="utf-8")

report=f"""# 伪回归实验：课件 LV pp.54–55 的完整复现

这里全部是**人工模拟数据**。没有使用或伪造市场行情。算法是 NumPy PCG64，
以 default_rng(2026) 初始化一次，每次先抽取 240 个 u 再抽取 240 个 v，
均为独立 N(0,0.04²)，将其分别累积；共 500 次，全部纳入结果。
初值 x₀=y₀=0；水平回归使用 t=1,…,240；差分回归也有 240 组创新，
因为 CSV 同时保存了 t=0 的初始点。

| 回归 | 5% 拒绝次数 | 全部实验数 | 拒绝率 |
|---|---:|---:|---:|
| 独立随机游走水平 | {counts[0]} | 500 | {rates[0]:.1%} |
| 独立的一阶差分 | {counts[1]} | 500 | {rates[1]:.1%} |

两者都刻意使用带截距 OLS 的常规 i.i.d. Student t 检验，
用于展示该检验对水平数据失准。拒绝率不是预测胜率、投资收益或协整概率。

第一次水平回归：斜率 {first[3]['slope']:.8f}，
R²={first[3]['r2']:.8f}，常规双侧 p={first[3]['p']:.8g}。
第一次差分回归：斜率 {first[4]['slope']:.8f}，
R²={first[4]['r2']:.8f}，双侧 p={first[4]['p']:.8g}。
首次结果可能偶然较强或较弱，不能以它代替全部模拟。

在真实拒绝概率为 5% 时，500 次模拟拒绝率的标准差约为
sqrt(0.05×0.95/500)=0.00975，即约 0.975 个百分点。
因此差分结果应与 5% 附近的模拟波动比较，不要求恰为 5%。
相同 seed 在不同随机数生成器、抽取顺序或回归样本定义下不保证产生相同路径。

![伪回归与差分的对照](../images/03_伪回归实验.png)

## 文件与手工核验

- spurious_first.csv：第一次实验，含初始点。
- spurious_all_500.csv：500 次实验逐次系数、R² 与 p 值。
- spurious_summary.json：配置与摘要。
- 复现与图解.py：完整代码；依赖 numpy、scipy、matplotlib。

Excel 中对 t=1,…,240 的 Y 列与 X 列使用 SLOPE(Y范围,X范围)，
应得到上述水平斜率。不能把初始点一并加进水平回归。
再由相邻水平作差核对 dx、dy；样本量应仍为 240。
不要对两条随机游走相同方向的“经济原因”作事后叙事。
"""
(OUT/"伪回归实验与结果.md").write_text(report,encoding="utf-8")
print(json.dumps({"summary":summary,"worked_examples":calculations},ensure_ascii=False,indent=2))
