"""Build navigable Markdown and a page-level coverage ledger; original PDFs read only."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT.parent
CH=sorted((ROOT/"chapters").glob("*.md"))
assert len(CH)==7
VIEWS=sorted((ROOT/"higher_views").glob("*.md"))

# inclusive PDF page ranges: chapter, instructional level, treatment.
M={
1:[
 (1,12,0,"课程组织","课程定位及材料范围记于凡例，不扩写人员与管理页"),
 (13,16,1,"基础理解","测量、预测、因果及金融计量的问题边界"),
 (17,19,1,"基础理解","截面、时间序列、面板；已检查图片"),
 (20,21,1,"基础理解","个股与市场、资产定价的问题；风险解释续第2、4章"),
 (22,24,1,"背景","替代数据示例为重复页，不扩展机器学习"),
 (25,25,1,"基础理解","资料来源与不虚构观测的原则"),
 (26,31,1,"核心方法","月末调整价格、起始月份与样本比较；无原始行情不伪造实证"),
 (32,32,0,"课程提纲","课程知识图；机器学习及未提供的完整PCA另记范围"),
],
2:[
 (1,1,0,"组织页","讲题记入材料表"),
 (2,5,1,"基础理解","融资、消费平滑、分散与资源配置；数学分散化续第2章"),
 (6,7,1,"基础理解","一级二级市场、资产类别与市场功能"),
 (8,9,1,"背景","交易所与指数、权重与比较口径；历史排名数字不作为现时事实"),
 (10,12,1,"基础理解","配置低效、委托代理与道德风险"),
 (13,14,1,"基础理解","金融资产、流动性与现金流贴现补注"),
 (15,18,1,"核心方法","收益口径、股息、复利、对数与组合期初权重"),
 (19,22,1,"基础理解","收益波动、国债收益率报价、指数及GDP；条件风险续第2章"),
 (23,23,1,"知识连接","风险、定价、效率与预测的问题链"),
 (24,28,1,"核心概念","EMH三形式、随机游走区别、成本及风险基准"),
],
3:[
 (1,2,0,"组织与动机","以收益风险推断三问重构第2、3章"),
 (3,6,2,"基础理解","随机变量、CDF/PDF与正态标准化"),
 (7,10,2,"核心概念","预期收益、方差、协方差、非线性反例"),
 (11,13,2,"核心方法","两资产方差逐步推导、有效组合、独立复算并绘图"),
 (14,15,2,"核心概念","Sharpe口径、年化条件与估计误差"),
 (16,19,2,"核心概念","偏度峰度、分位数、损失方向及VaR"),
 (20,21,2,"核心概念","条件均值风险、迭代期望；补全方差分解"),
 (22,25,3,"核心方法","i.i.d.、估计量、LLN/CLT与标准误"),
 (26,29,3,"核心方法","检验、p值与区间；60个月例子逐步复算"),
 (30,31,3,"核心方法","同月组合差值推断；无行情数据不伪造结果"),
 (32,32,3,"核心方法","金融依赖与HAC，完整推导均值长期方差"),
],
4:[
 (1,1,0,"组织页","讲题记入材料表"),
 (2,6,4,"核心概念","市场回归、超额收益、CAPM与αβ"),
 (7,9,4,"核心推导","OLS标量与矩阵、投影正交性"),
 (10,12,4,"输出解读","图片表格已检查，解释系数、样本与R²，记录舍入局限"),
 (13,18,4,"核心方法","无偏条件、系数不确定性、三种原假设与p值"),
 (19,19,4,"核心概念","拟合度分解及不能推出的结论"),
 (20,21,4,"核心方法","组合回归、平均跑赢与α分解；无原始数据不伪造"),
 (22,23,4,"核心方法","总体投影、因果边界与HAC"),
 (24,27,4,"诊断解读","残差、DW、JB、Omnibus与局限；截图已查"),
 (28,28,4,"知识连接","趋势与结构变化；详细处理在第6、7章"),
 (29,31,5,"核心方法","多因子、共线性与联合检验；补FWL及遗漏因子分解"),
 (32,33,5,"核心推导","六组排序、SMB/HML、组指标OLS和WLS"),
 (34,35,5,"核心方法","Fama–MacBeth按月截面、跨月推断与HAC"),
 (36,36,5,"核心推导","回归权重的组合解释，证明零净权重及实现边界"),
],
5:[
 (1,1,0,"组织页","讲题记入材料表"),
 (2,9,6,"核心动机","水平与收益的预测，R²和基准；第7章再解释单位根"),
 (10,14,6,"核心概念","两种平稳、白噪声、有限MA、随机游走；补遍历与初始化限定"),
 (15,15,6,"核心概念","总体和样本ACF及图形解释"),
 (16,18,6,"核心推导","AR(1)矩、AR(p)根条件、PACF"),
 (19,23,6,"图形解读","正负AR与AR(2)的样本路径、ACF/PACF；已检查"),
 (24,26,6,"核心方法","联合密度、条件及精确似然、MLE推断"),
 (27,29,6,"核心方法","一步多步预测、参数误差、RMSE与时间窗口"),
 (30,32,6,"核心推导","MA矩、滞后算子、可逆及MA(q)"),
 (33,34,6,"图形解读","MA的ACF/PACF模式；已检查"),
 (35,37,6,"核心方法","ARMA、判阶和月度收益图；补最简表示与ARMA(1,1)矩"),
 (38,44,7,"核心推导","单位根、随机游走、漂移与方差增长；图形已查"),
 (45,48,7,"核心方法","确定性趋势、差分及去趋势区别；图形已查"),
 (49,50,7,"核心方法","DF/ADF、非标准分布与课件输出；设置局限已记"),
 (51,53,7,"核心概念","I(1)回归、伪回归机制与图形"),
 (54,55,7,"复现实验","seed2026、240期、500次全部运行，保存代码CSV及图"),
 (56,57,7,"核心概念","协整、共同趋势与残差检验；p.57的0.080不能证明5%协整"),
 (58,60,7,"应用辨析","GLD/GDX候选价差、Z分数、头寸与事前执行；不虚构获利"),
],
}

pdfs=sorted(COURSE.glob("*.pdf"))
ledger=["# 逐页处理表：Lecture I—V",
        "\n页码均为PDF页序；覆盖表示知识已处理或已说明为何合并，不表示复算了缺少原始数据的行情。",
        "\n| 文件 | 页码 | 原页标题 | 正文位置 | 层次 | 处理记录 |",
        "|---|---:|---|---|---|---|"]
index=["# ECO6109 课件覆盖索引",
       "\n本次编撰 Lecture I—V，共188页。Lecture VI全部56页按读者要求暂缓。",
       "\n“核心”表示课程结构中的重要性，不是教师命题频率。逐页审查见[sources/逐页处理表.md](sources/逐页处理表.md)。",
       "\n| 课件 | PDF页码 | 主题与处理 | 去向 | 层次 | 状态 |",
       "|---|---|---|---|---|---|"]
manifest=[]
for k,f in enumerate(pdfs,1):
    pages=json.loads((ROOT/"sources"/(f.stem+".json")).read_text(encoding="utf-8"))
    manifest.append({"file":f.name,"pages":len(pages),"sha256":hashlib.sha256(f.read_bytes()).hexdigest(),
                     "status":"compiled" if k<=5 else "deferred_by_user"})
    if k==6:
        index.append(f"| [{f.name}](<../{f.name}>) | 1–56 | 机器学习 | 无 | 暂缓 | 仅留提取件，不编撰正文 |")
        continue
    for a,b,ch,level,note in M[k]:
        dest=f"[第{ch}章](chapters/{CH[ch-1].name})" if ch else "[凡例与总目](01_课程总目与知识体系.md)"
        index.append(f"| [{f.name}](<../{f.name}>) | {a}–{b} | {note} | {dest} | {level} | 已处理 |")
    seen=[]
    for p in pages:
        matches=[m for m in M[k] if m[0]<=p["page"]<=m[1]]
        assert len(matches)==1,(f.name,p["page"],matches)
        a,b,ch,level,note=matches[0]
        seen.append(p["page"])
        title=next((s.strip() for s in p["text"].splitlines() if s.strip()),"无提取文字").replace("|","/")
        dest=f"[第{ch}章](../chapters/{CH[ch-1].name})" if ch else "[凡例与总目](../01_课程总目与知识体系.md)"
        ledger.append(f"| {f.name} | {p['page']} | {title} | {dest} | {level} | {note} |")
    assert seen==list(range(1,len(pages)+1))
assert sum(m["pages"] for m in manifest if m["status"]=="compiled")==188
(ROOT/"02_课件覆盖索引.md").write_text("\n".join(index)+"\n",encoding="utf-8")
(ROOT/"sources"/"逐页处理表.md").write_text("\n".join(ledger)+"\n",encoding="utf-8")
(ROOT/"sources"/"原始材料校验清单.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")

book=["# ECO6109 金融市场计量详细注疏",
      "\n适合有数学与计量理论基础、未系统学习金融计量的读者。依据前五份课件重构为七章；最后一份机器学习暂缓。",
      "\n以问题动机、概念解释、逐步推导、算例、条件与辨析为主。完整来源与处理记录见同目录《课件覆盖索引》。",
      "\n## 目录"]
for j,f in enumerate(CH,1):
    title=f.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    book.append(f"- [{title}](#ch{j:02})")
book.append("\n高观点专题可在初读时跳过。")
for j,f in enumerate(VIEWS,1):
    title=f.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
    book.append(f"- [{title}](#view{j:02})")
for j,f in enumerate(CH+VIEWS):
    anchor=f"ch{j+1:02}" if j<len(CH) else f"view{j-len(CH)+1:02}"
    text=f.read_text(encoding="utf-8")
    text=re.sub(r"^(#{1,5}) ",r"#\1 ",text,flags=re.M)
    text=text.replace("](../images/","](images/").replace("](../exercises/","](exercises/")
    book.extend(["\n---\n",f'<a id="{anchor}"></a>\n',text])
(ROOT/"ECO6109_金融市场计量详细注疏_合订本.md").write_text("\n".join(book)+"\n",encoding="utf-8")

# Check only authored Markdown, excluding raw extraction copies.
paths=CH+VIEWS+list((ROOT/"exam").glob("*.md"))+[
    ROOT/"README.md",ROOT/"00_编纂凡例.md",ROOT/"01_课程总目与知识体系.md",
    ROOT/"02_课件覆盖索引.md",ROOT/"ECO6109_金融市场计量详细注疏_合订本.md",
    ROOT/"exercises"/"伪回归实验与结果.md",ROOT/"sources"/"逐页处理表.md"]
issues=[]
stats=[]
for f in paths:
    if not f.exists():
        issues.append(f"Missing file: {f}");continue
    text=f.read_text(encoding="utf-8")
    if len(re.findall(r"^\$\$\s*$",text,re.M))%2:
        issues.append(f"Unpaired display math: {f.name}")
    inline=re.sub(r"\$\$[\s\S]*?\$\$","",text)
    if len(re.findall(r"(?<!\\)\$",inline))%2:
        issues.append(f"Unpaired inline math: {f.name}")
    if "\ufffd" in text:issues.append(f"Replacement character: {f.name}")
    for target in re.findall(r"!?\[[^\]]*\]\((<[^>]+>|[^)\n]+)\)",text):
        target=target.strip("<>")
        if target.startswith(("https:","http:","#")):continue
        local=target.split("#")[0]
        if local and not (f.parent/local).exists():
            issues.append(f"Broken link: {f.name}: {target}")
    stats.append({"file":str(f.relative_to(ROOT)),"characters":len(text),
                  "display_formulas":len(re.findall(r"^\$\$\s*$",text,re.M))//2})
audit={"original_files":manifest,"compiled_pages":188,"deferred_pages":56,
       "chapters":7,"higher_view_topics":len(VIEWS),"exam_files":len(list((ROOT/"exam").glob("*.md"))),
       "chapter_characters":sum(len(f.read_text(encoding="utf-8")) for f in CH),
       "teaching_images":len(list((ROOT/"images").glob("*.png"))),
       "issues":issues,"files":stats}
(ROOT/"sources"/"编纂核查结果.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in audit.items() if k not in ["files","original_files"]},ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
