# 原始材料文本提取：Lecture 3a.pdf

## PDF 第 1 页

ECO6102 / 2026–27 Term 1 (Fall)
Lecture 3a:
Linear Regression
Enjie (Jack) Ma
Lecture 3 · Monday 21 September 2026

## PDF 第 2 页

Key Dates and Exam Format
Finalized — as in the syllabus; problem sets are due by 23:59, no late work
• Problem Set 1: due Sunday 11 October 2026 (not Friday 9)
• Problem Set 2: due Friday 23 October 2026
• Midterm Exam (30%): Monday 26 October 2026, 09:00–11:00
• Problem Set 3: due Friday 11 December 2026
• Review: Monday 14 December 2026 (Week 15)
• Final Exam (40%): Monday 21 December 2026, 09:00–11:00
• Exam format: two hours each; closed book and in person; one
double-sided A4 cheat sheet is allowed
ECO6102 / L3 / 3a 1 / 57

## PDF 第 3 页

Participation (10%)
Course participation policy — completion and practice
• Credit is based on completion, not correctness.
• One missed quiz is allowed without penalty or documentation.
• Submit your name, UID and one short open-ended answer. The feedback
question is optional.
• Questions give you practice with the reasoning and question styles used
in exams.
• Complete the quiz in the classroom using WeChat; submit before the
lecture ends.
ECO6102 / L3 / 3a 2 / 57

## PDF 第 4 页

Roadmap
Wooldridge Chapter 4
• OLS recap
• 4.1 Overview of the Single-Equation Linear Model
• 4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 3 / 57

## PDF 第 5 页

Roadmap
Wooldridge Recap — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a OLS recap

## PDF 第 6 页

Ordinary least squares
Wooldridge 4.2.1, p. 57 — choose the line with the smallest sum of squared residuals
OBSERVED DA T A
Studenti: attendancex i (percentage points), standardized final scorey i.
• A candidate line predictsa+bx i; its residual isy i −a−bx i.
• Ordinary least squares (OLS)chooses the intercept and slope to
minimize
SSR(a,b)=
NX
i=1
(yi −a−bx i)2.
First-order conditions
ECO6102 / L3 / 3a OLS recap 4 / 57

## PDF 第 7 页

Ordinary least squares
Wooldridge 4.2.1, p. 57 — choose the line with the smallest sum of squared residuals
OBSERVED DA T A
Studenti: attendancex i (percentage points), standardized final scorey i.
• A candidate line predictsa+bx i; its residual isy i −a−bx i.
• Ordinary least squares (OLS)chooses the intercept and slope to
minimize
SSR(a,b)=
NX
i=1
(yi −a−bx i)2.
First-order conditions
ECO6102 / L3 / 3a OLS recap 4 / 57

## PDF 第 8 页

The OLS solution
Introductory Wooldridge, 6e, 2.2; Wooldridge 4.2.1 — intercept and slope for one
regressor
ˆβ1 =
P
i(xi − ¯x)(yi − ¯y)P
i(xi − ¯x)2 , ˆβ0 = ¯y− ˆβ1 ¯x.
• ¯xand ¯yare sample averages; the data must contain variation inx.
• The slope measures co-movement ofxandy, scaled by variation inx.
• The intercept makes the fitted line pass through( ¯x, ¯y).
Derivation Sample covariance and the limit
ECO6102 / L3 / 3a OLS recap 5 / 57

## PDF 第 9 页

The OLS solution
Introductory Wooldridge, 6e, 2.2; Wooldridge 4.2.1 — intercept and slope for one
regressor
ˆβ1 =
P
i(xi − ¯x)(yi − ¯y)P
i(xi − ¯x)2 , ˆβ0 = ¯y− ˆβ1 ¯x.
• ¯xand ¯yare sample averages; the data must contain variation inx.
• The slope measures co-movement ofxandy, scaled by variation inx.
• The intercept makes the fitted line pass through( ¯x, ¯y).
Derivation Sample covariance and the limit
ECO6102 / L3 / 3a OLS recap 5 / 57

## PDF 第 10 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 11 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 12 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 13 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 14 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 15 页

Candidate regression lines
Wooldridge 4.2.1 — the dots stay fixed; only the candidate line changes
50 75 100
−2
0
1
a=−0.16,b=0.0000
attendance (%)
standardized score
Horizontal
50 75 100
−2
0
1
a=−0.63,b=0.0081
attendance (%)
Relatively flat
50 75 100
−2
0
1
a=−2.38,b=0.0269
attendance (%)
OLS
ECO6102 / L3 / 3a OLS recap 6 / 57

## PDF 第 16 页

Comparing squared residuals
Wooldridge 4.2.1 — OLS wins this comparison by construction
Candidate LineSSR
Horizontal ˆy=−.1576 12.27
Relatively flat ˆy=−.6345+.00813x11.91
OLS ˆy=−2.3775+.02691x10.11
• The last line minimizes squared residuals for the 20 observations just
shown.
ECO6102 / L3 / 3a OLS recap 7 / 57

## PDF 第 17 页

Interpreting the OLS slope
Wooldridge 4.2.1 — read the change in predicted score
60 70 100
−.763
−.494
+10 pp
+.2691
attendance (%)
predicted score
• Same OLS line for the 20
students: slope.02691.
• Ten attendance percentage
points go with about.2691
standard deviations of score.
• This is a fitted association. A
causal interpretation needs
more assumptions.
ECO6102 / L3 / 3a OLS recap 8 / 57

## PDF 第 18 页

Population and sample regression functions
Wooldridge 4.1, (4.1)–(4.4) — a population relationship and a fitted sample line
• In a linear conditional-mean model, thepopulation regression function
(PRF)is
E(y|x)=β 0 +β 1x,y=β 0 +β 1x+u,E(u|x)=0.
• Thesample regression function (SRF)is the fitted line
ˆyi = ˆβ0 + ˆβ1xi, ˆui =y i − ˆyi.
• Theerroru i is measured from the population line; theresidual ˆui is
measured from the fitted line.
Back to slide 20
ECO6102 / L3 / 3a OLS recap 9 / 57

## PDF 第 19 页

Population and sample regression functions
Wooldridge 4.1, (4.1)–(4.4) — a population relationship and a fitted sample line
• In a linear conditional-mean model, thepopulation regression function
(PRF)is
E(y|x)=β 0 +β 1x,y=β 0 +β 1x+u,E(u|x)=0.
• Thesample regression function (SRF)is the fitted line
ˆyi = ˆβ0 + ˆβ1xi, ˆui =y i − ˆyi.
• Theerroru i is measured from the population line; theresidual ˆui is
measured from the fitted line.
Back to slide 20
ECO6102 / L3 / 3a OLS recap 9 / 57

## PDF 第 20 页

The population regression function
Wooldridge 2.2 and (4.4) —yis the conditional mean plus an individual deviationu
Solid line:Population regression function (PRF).
x1 x2 x3
E(y|x)uone person
x
y
Each curve is the distribution ofyamong people with thatx; its mean is the
dot on the line,E(y|x).
y=E(y|x)+u: the error is the gap to thepopulation
line; the residual, to thefittedline.
ECO6102 / L3 / 3a OLS recap 10 / 57

## PDF 第 21 页

The population regression function
Wooldridge 2.2 and (4.4) —yis the conditional mean plus an individual deviationu
Solid line:Population regression function (PRF).
x1 x2 x3
E(y|x)uone person
x
y
Each curve is the distribution ofyamong people with thatx; its mean is the
dot on the line,E(y|x).
y=E(y|x)+u: the error is the gap to thepopulation
line; the residual, to thefittedline.
ECO6102 / L3 / 3a OLS recap 10 / 57

## PDF 第 22 页

The population regression function
Wooldridge 2.2 and (4.4) —yis the conditional mean plus an individual deviationu
Solid line:Population regression function (PRF).
x1 x2 x3
E(y|x)uone person
x
y
Each curve is the distribution ofyamong people with thatx; its mean is the
dot on the line,E(y|x). y=E(y|x)+u: the error is the gap to thepopulation
line; the residual, to thefittedline.
ECO6102 / L3 / 3a OLS recap 10 / 57

## PDF 第 23 页

Parameter, estimator, and estimate
Wooldridge 3.5.1 and 4.2.1 — the target is fixed; the estimator changes with the sample
E(y|x)=β 0 +β 1x, ˆy= ˆβ0 + ˆβ1x.
• Parameter:β 1, a fixed but unknown feature of the population model.
• Estimator: ˆβ1, a rule applied to random data; before observing the sample,
its value is random.
• Estimate: the realized number from our data, such as.02691 for these 20
students.
ECO6102 / L3 / 3a OLS recap 11 / 57

## PDF 第 24 页

Parameter, estimator, and estimate
Wooldridge 3.5.1 and 4.2.1 — the target is fixed; the estimator changes with the sample
E(y|x)=β 0 +β 1x, ˆy= ˆβ0 + ˆβ1x.
• Parameter:β 1, a fixed but unknown feature of the population model.
• Estimator: ˆβ1, a rule applied to random data; before observing the sample,
its value is random.
• Estimate: the realized number from our data, such as.02691 for these 20
students.
ECO6102 / L3 / 3a OLS recap 11 / 57

## PDF 第 25 页

Sampling variation and a sampling
distribution
Wooldridge 3.5.1 — repeat the sampling rule and recompute the estimate
• Sampling variation: different random samples produce different
estimates, even when the population and estimation rule stay the same.
• Thesampling distributiondescribes those possible estimates and their
probabilities at a given sample size.
• Our demonstration treats the 680 ATTEND students as an empirical
population. Draw 20 students with replacement, fit OLS, and repeat.
Each point in the next histogram is a slope from a whole sample, not one
student’s score.
Back to slide 20
ECO6102 / L3 / 3a OLS recap 12 / 57

## PDF 第 26 页

Sampling variation and a sampling
distribution
Wooldridge 3.5.1 — repeat the sampling rule and recompute the estimate
• Sampling variation: different random samples produce different
estimates, even when the population and estimation rule stay the same.
• Thesampling distributiondescribes those possible estimates and their
probabilities at a given sample size.
• Our demonstration treats the 680 ATTEND students as an empirical
population. Draw 20 students with replacement, fit OLS, and repeat.
Each point in the next histogram is a slope from a whole sample, not one
student’s score.
Back to slide 20
ECO6102 / L3 / 3a OLS recap 12 / 57

## PDF 第 27 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 28 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 29 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 30 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 31 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 32 页

Three samples, three fitted lines
Wooldridge 4.2.1 — draw 20 students from the 680, refit, repeat: the data moved
680 students
draws of 20,
with replacement
50 100
−2
0
2
slope .0269
attendance (%)
score
draw 1
50 100
−2
0
2
slope .0603
attendance (%)
draw 2
50 100
−2
0
2
slope .0131
attendance (%)
draw 3
ECO6102 / L3 / 3a OLS recap 13 / 57

## PDF 第 33 页

Build the sampling distribution
Wooldridge 3.5.1 — one sample contributes one estimated slope
−0.04 0 0.04 0.08
0
1
2
3
estimated slope from one sample of 20
number of estimates
3 samples
Centre: where estimates tend to land. Spread: how much they vary.
ECO6102 / L3 / 3a OLS recap 14 / 57

## PDF 第 34 页

Build the sampling distribution
Wooldridge 3.5.1 — one sample contributes one estimated slope
−0.04 0 0.04 0.08
0
2
4
6
estimated slope from one sample of 20
number of estimates
20 samples
Centre: where estimates tend to land. Spread: how much they vary.
ECO6102 / L3 / 3a OLS recap 14 / 57

## PDF 第 35 页

Build the sampling distribution
Wooldridge 3.5.1 — one sample contributes one estimated slope
−0.04 0 0.04 0.08
0
5
10
15
20
estimated slope from one sample of 20
number of estimates
100 samples
Centre: where estimates tend to land. Spread: how much they vary.
ECO6102 / L3 / 3a OLS recap 14 / 57

## PDF 第 36 页

Build the sampling distribution
Wooldridge 3.5.1 — one sample contributes one estimated slope
−0.04 0 0.04 0.08
0
50
100
150
estimated slope from one sample of 20
number of estimates
1000 samples
Centre: where estimates tend to land. Spread: how much they vary.
ECO6102 / L3 / 3a OLS recap 14 / 57

## PDF 第 37 页

Bias compares an expectation with a target
Wooldridge 4.2.1, p. 58 — hold the sample size fixed
Bias( ˆβN)=E( ˆβN)−β;unbiased:E( ˆβN)=β.
• Imagine every possible sample of the same sizeN.
• Average the estimates across those samples, then compare that
expectation with the target.
ECO6102 / L3 / 3a OLS recap 15 / 57

## PDF 第 38 页

Bias compares an expectation with a target
Wooldridge 4.2.1, p. 58 — hold the sample size fixed
Bias( ˆβN)=E( ˆβN)−β;unbiased:E( ˆβN)=β.
• Imagine every possible sample of the same sizeN.
• Average the estimates across those samples, then compare that
expectation with the target.
ECO6102 / L3 / 3a OLS recap 15 / 57

## PDF 第 39 页

Bias at a fixed sample size
Wooldridge 4.2.1 and Problem 4.2 — distinguish the centre from the spread
Illustrative:y=3+2x+u,E(u|x)=0,N=20; ˜β1 = ˆβ1 +0.3.
1 2 3
β1 =2 E( ˜β1)=2.3
slope estimate from one sample of 20
samples
The expectation misses the target by 0.3: bias=.3.
Why OLS is unbiased here
ECO6102 / L3 / 3a OLS recap 16 / 57

## PDF 第 40 页

Bias at a fixed sample size
Wooldridge 4.2.1 and Problem 4.2 — distinguish the centre from the spread
Illustrative:y=3+2x+u,E(u|x)=0,N=20; ˜β1 = ˆβ1 +0.3.
1 2 3
β1 =2 E( ˜β1)=2.3
slope estimate from one sample of 20
samples
The expectation misses the target by 0.3: bias=.3.
Why OLS is unbiased here
ECO6102 / L3 / 3a OLS recap 16 / 57

## PDF 第 41 页

Bias at a fixed sample size
Wooldridge 4.2.1 and Problem 4.2 — distinguish the centre from the spread
Illustrative:y=3+2x+u,E(u|x)=0,N=20; ˜β1 = ˆβ1 +0.3.
1 2 3
β1 =2 E( ˜β1)=2.3
slope estimate from one sample of 20
samples
The expectation misses the target by 0.3: bias=.3. Why OLS is unbiased here
ECO6102 / L3 / 3a OLS recap 16 / 57

## PDF 第 42 页

Unbiasedness at a fixed sample size
Wooldridge 4.2.1 and Problem 4.2 — distinguish the centre from the spread
Illustrative:N=20,y=3+2x+u,E(u|x)=0.
1 2 3
β1 =2 E( ˆβ1)=2.0
slope estimate from one sample of 20
samples
The two lines coincide: unbiased. Individual estimates still vary.
Why OLS is unbiased here
ECO6102 / L3 / 3a OLS recap 17 / 57

## PDF 第 43 页

Unbiasedness at a fixed sample size
Wooldridge 4.2.1 and Problem 4.2 — distinguish the centre from the spread
Illustrative:N=20,y=3+2x+u,E(u|x)=0.
1 2 3
β1 =2 E( ˆβ1)=2.0
slope estimate from one sample of 20
samples
The two lines coincide: unbiased. Individual estimates still vary.
Why OLS is unbiased here
ECO6102 / L3 / 3a OLS recap 17 / 57

## PDF 第 44 页

What changes when the sample grows?
Wooldridge 3.5.1 — keep the population and estimation rule fixed
ˆβN
p
− →β⇐ ⇒P(| ˆβN −β|> ε)→0 for everyε >0.
SAMPLING EXPERIMENT
We drew 20 students repeatedly. Now repeat the same experiment with 100 and
then 500 students.
• Does collecting more data bring the estimate closer to our target?
ECO6102 / L3 / 3a OLS recap 18 / 57

## PDF 第 45 页

Larger samples concentrate near the target
Wooldridge 3.5.1 — can I get closer to the truth just by collecting larger data?
−0.05 0 0.05
0
200
400
600
samples
N=20: SD .0150
−0.05 0 0.05
0
200
400
600
N=100: SD .0057
−0.05 0 0.05
0
200
400
600
N=500: SD .0025
At the same tolerance, more estimates lie near the target asNgrows. The
normal approximation will explain the scale of the spread.
Back to slide 23
ECO6102 / L3 / 3a OLS recap 19 / 57

## PDF 第 46 页

Larger samples concentrate near the target
Wooldridge 3.5.1 — can I get closer to the truth just by collecting larger data?
−0.05 0 0.05
0
200
400
600
samples
N=20: SD .0150
−0.05 0 0.05
0
200
400
600
N=100: SD .0057
−0.05 0 0.05
0
200
400
600
N=500: SD .0025
At the same tolerance, more estimates lie near the target asNgrows. The
normal approximation will explain the scale of the spread.
Back to slide 23
ECO6102 / L3 / 3a OLS recap 19 / 57

## PDF 第 47 页

Larger samples concentrate near the target
Wooldridge 3.5.1 — can I get closer to the truth just by collecting larger data?
−0.05 0 0.05
0
200
400
600
samples
N=20: SD .0150
−0.05 0 0.05
0
200
400
600
N=100: SD .0057
−0.05 0 0.05
0
200
400
600
N=500: SD .0025
At the same tolerance, more estimates lie near the target asNgrows. The
normal approximation will explain the scale of the spread.
Back to slide 23
ECO6102 / L3 / 3a OLS recap 19 / 57

## PDF 第 48 页

OLS recap
Introductory Wooldridge, 6e, Chapters 2 and 5; Appendix C — three distinctions to
carry forward
• Fit and co-movement: OLS chooses the smallest squared loss. A fitted
slope measures association.
OLS solution: Chapter 2
• Population and sample: the target is fixed; another sample gives another
estimate.
PRF and SRF Sampling variation: Appendix C.1
• Unbiasedness and consistency: centered on the target at a fixedNversus
concentrating near it asNgrows.
Compare the properties: Appendix C.2–C.3
ECO6102 / L3 / 3a OLS recap 20 / 57

## PDF 第 49 页

OLS recap
Introductory Wooldridge, 6e, Chapters 2 and 5; Appendix C — three distinctions to
carry forward
• Fit and co-movement: OLS chooses the smallest squared loss. A fitted
slope measures association.
OLS solution: Chapter 2
• Population and sample: the target is fixed; another sample gives another
estimate.
PRF and SRF Sampling variation: Appendix C.1
• Unbiasedness and consistency: centered on the target at a fixedNversus
concentrating near it asNgrows.
Compare the properties: Appendix C.2–C.3
ECO6102 / L3 / 3a OLS recap 20 / 57

## PDF 第 50 页

OLS recap
Introductory Wooldridge, 6e, Chapters 2 and 5; Appendix C — three distinctions to
carry forward
• Fit and co-movement: OLS chooses the smallest squared loss. A fitted
slope measures association.
OLS solution: Chapter 2
• Population and sample: the target is fixed; another sample gives another
estimate.
PRF and SRF Sampling variation: Appendix C.1
• Unbiasedness and consistency: centered on the target at a fixedNversus
concentrating near it asNgrows.
Compare the properties: Appendix C.2–C.3
ECO6102 / L3 / 3a OLS recap 20 / 57

## PDF 第 51 页

Roadmap
Wooldridge 4.1 — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 4.1 Overview

## PDF 第 52 页

The population equation and its error
Wooldridge 4.1, equation (4.1) — start with the relationship of interest
y=β 0 +β 1x1 +· · ·+β pxp +u.(4.1)
• The coefficients are population parameters;ucontains unobserved
determinants.
• Linear in parameters: regressors can include squares, logarithms and
interactions.
ECO6102 / L3 / 3a 4.1 Overview 21 / 57

## PDF 第 53 页

The population equation and its error
Wooldridge 4.1, equation (4.1) — start with the relationship of interest
y=β 0 +β 1x1 +· · ·+β pxp +u.(4.1)
• The coefficients are population parameters;ucontains unobserved
determinants.
• Linear in parameters: regressors can include squares, logarithms and
interactions.
ECO6102 / L3 / 3a 4.1 Overview 21 / 57

## PDF 第 54 页

A structural relationship
Wooldridge 4.1, pp. 53–54 — the coefficient has an economic meaning
QUESTION
How would an additional year of schooling change a person’s wage, holding
other relevant determinants fixed?
• Astructural relationshiprepresent acausalrelationship.
• Here the target is the schooling effect at the same ability and experience,
not simply the wage gap between schooling groups –ceteris paribus
ECO6102 / L3 / 3a 4.1 Overview 22 / 57

## PDF 第 55 页

A structural relationship
Wooldridge 4.1, pp. 53–54 — the coefficient has an economic meaning
QUESTION
How would an additional year of schooling change a person’s wage, holding
other relevant determinants fixed?
• Astructural relationshiprepresent acausalrelationship.
• Here the target is the schooling effect at the same ability and experience,
not simply the wage gap between schooling groups –ceteris paribus
ECO6102 / L3 / 3a 4.1 Overview 22 / 57

## PDF 第 56 页

From the target to credible estimation
Wooldridge 4.1–4.2.1 — target, comparison and consistency
SCHOOLING EQUA TION
log(wage)=β 0 +β s schooling+β e experience+u.
1 Choose the target: schooling’s wage effect, holding relevant determinants
fixed.
2 Justify the comparison: differences in schooling must not systematically
carry differences in omitted wage determinants.
E(u|schooling,experience)=0.
3 Ask for consistency: with more observations, does our estimate
concentrate near that target?
But how can we make sure what we estimate from data is consistent?
Recall the consistency picture Formal definition of Consistency
ECO6102 / L3 / 3a 4.1 Overview 23 / 57

## PDF 第 57 页

From the target to credible estimation
Wooldridge 4.1–4.2.1 — target, comparison and consistency
SCHOOLING EQUA TION
log(wage)=β 0 +β s schooling+β e experience+u.
1 Choose the target: schooling’s wage effect, holding relevant determinants
fixed.
2 Justify the comparison: differences in schooling must not systematically
carry differences in omitted wage determinants.
E(u|schooling,experience)=0.
3 Ask for consistency: with more observations, does our estimate
concentrate near that target?
But how can we make sure what we estimate from data is consistent?
Recall the consistency picture Formal definition of Consistency
ECO6102 / L3 / 3a 4.1 Overview 23 / 57

## PDF 第 58 页

From the target to credible estimation
Wooldridge 4.1–4.2.1 — target, comparison and consistency
SCHOOLING EQUA TION
log(wage)=β 0 +β s schooling+β e experience+u.
1 Choose the target: schooling’s wage effect, holding relevant determinants
fixed.
2 Justify the comparison: differences in schooling must not systematically
carry differences in omitted wage determinants.
E(u|schooling,experience)=0.
3 Ask for consistency: with more observations, does our estimate
concentrate near that target?
But how can we make sure what we estimate from data is consistent?
Recall the consistency picture Formal definition of Consistency
ECO6102 / L3 / 3a 4.1 Overview 23 / 57

## PDF 第 59 页

From the target to credible estimation
Wooldridge 4.1–4.2.1 — target, comparison and consistency
SCHOOLING EQUA TION
log(wage)=β 0 +β s schooling+β e experience+u.
1 Choose the target: schooling’s wage effect, holding relevant determinants
fixed.
2 Justify the comparison: differences in schooling must not systematically
carry differences in omitted wage determinants.
E(u|schooling,experience)=0.
3 Ask for consistency: with more observations, does our estimate
concentrate near that target?
But how can we make sure what we estimate from data is consistent?
Recall the consistency picture Formal definition of Consistency
ECO6102 / L3 / 3a 4.1 Overview 23 / 57

## PDF 第 60 页

From the target to credible estimation
Wooldridge 4.1–4.2.1 — target, comparison and consistency
SCHOOLING EQUA TION
log(wage)=β 0 +β s schooling+β e experience+u.
1 Choose the target: schooling’s wage effect, holding relevant determinants
fixed.
2 Justify the comparison: differences in schooling must not systematically
carry differences in omitted wage determinants.
E(u|schooling,experience)=0.
3 Ask for consistency: with more observations, does our estimate
concentrate near that target?
But how can we make sure what we estimate from data is consistent?
Recall the consistency picture Formal definition of Consistency
ECO6102 / L3 / 3a 4.1 Overview 23 / 57

## PDF 第 61 页

Population restrictions for OLS
Wooldridge 4.1, equations (4.2)–(4.3) — the regressor must not move with the error
E(u)=0,Cov(x j,u)=0(j=1, . . . ,p).(4.2)
• These restrictions concern the population, not fitted sample residuals.
• Zero conditional mean,E(u|x 1, . . . ,xp)=0, is a sufficient condition.
• With random sampling, finite moments and full population rank, (4.2)
gives OLS consistency (Theorem 4.1).
Conditional mean versus zero covariance Why the intercept handles the mean
ECO6102 / L3 / 3a 4.1 Overview 24 / 57

## PDF 第 62 页

Population restrictions for OLS
Wooldridge 4.1, equations (4.2)–(4.3) — the regressor must not move with the error
E(u)=0,Cov(x j,u)=0(j=1, . . . ,p).(4.2)
• These restrictions concern the population, not fitted sample residuals.
• Zero conditional mean,E(u|x 1, . . . ,xp)=0, is a sufficient condition.
• With random sampling, finite moments and full population rank, (4.2)
gives OLS consistency (Theorem 4.1).
Conditional mean versus zero covariance Why the intercept handles the mean
ECO6102 / L3 / 3a 4.1 Overview 24 / 57

## PDF 第 63 页

Exogeneity vs. Endogeneity
Schooling example
• The errorucontains wage determinants absent from the equation, such as
unmeasured ability or motivation.
• A regressor isexogenouswhen it is uncorrelated withu; otherwise it is
endogenous.
• Zero conditional meanimplies exogeneity: within every
schooling-and-controls group, the omitted contribution to wages averages
to zero.
• Then a higher-schooling group does not also have a higher mean omitted
contribution to wages. This is an assumption, not a fact about schooling.
What could make schooling and omitted determinants move together?
Zero conditional mean versus zero covariance
ECO6102 / L3 / 3a 4.1 Overview 25 / 57

## PDF 第 64 页

Exogeneity vs. Endogeneity
Schooling example
• The errorucontains wage determinants absent from the equation, such as
unmeasured ability or motivation.
• A regressor isexogenouswhen it is uncorrelated withu; otherwise it is
endogenous.
• Zero conditional meanimplies exogeneity: within every
schooling-and-controls group, the omitted contribution to wages averages
to zero.
• Then a higher-schooling group does not also have a higher mean omitted
contribution to wages. This is an assumption, not a fact about schooling.
What could make schooling and omitted determinants move together?
Zero conditional mean versus zero covariance
ECO6102 / L3 / 3a 4.1 Overview 25 / 57

## PDF 第 65 页

Three sources of endogeneity
Wooldridge 4.1, pp. 54–55 — how a regressor can become connected to the error
1 Omitted variables: a missing determinant affects both the regressor and
the outcome.
2 Measurement error: using an imperfect measure can put its measurement
error into the regression error too.
3 Simultaneity: outcome conditions feed back into the regressor.
ECO6102 / L3 / 3a 4.1 Overview 26 / 57

## PDF 第 66 页

Three sources of endogeneity
Wooldridge 4.1, pp. 54–55 — how a regressor can become connected to the error
1 Omitted variables: a missing determinant affects both the regressor and
the outcome.
2 Measurement error: using an imperfect measure can put its measurement
error into the regression error too.
3 Simultaneity: outcome conditions feed back into the regressor.
ECO6102 / L3 / 3a 4.1 Overview 26 / 57

## PDF 第 67 页

Three sources of endogeneity
Wooldridge 4.1, pp. 54–55 — how a regressor can become connected to the error
1 Omitted variables: a missing determinant affects both the regressor and
the outcome.
2 Measurement error: using an imperfect measure can put its measurement
error into the regression error too.
3 Simultaneity: outcome conditions feed back into the regressor.
ECO6102 / L3 / 3a 4.1 Overview 26 / 57

## PDF 第 68 页

(1) Omitted variables
Wooldridge 4.1, pp. 54–55 — the omitted factor must affect both schooling and wages
• We want schooling’s effect on
wages, holding ability and
experience fixed.
• Higher ability may raise wages
and make further schooling more
attractive.
• The observed wage gap can
combine schooling’s effect with an
ability difference.
• This isself-selectioninto schooling
schooling log wage
abilityq
Conditional means and ability
ECO6102 / L3 / 3a 4.1 Overview 27 / 57

## PDF 第 69 页

(1) Omitted variables
Wooldridge 4.1, pp. 54–55 — the omitted factor must affect both schooling and wages
• We want schooling’s effect on
wages, holding ability and
experience fixed.
• Higher ability may raise wages
and make further schooling more
attractive.
• The observed wage gap can
combine schooling’s effect with an
ability difference.
• This isself-selectioninto schooling
schooling log wage
abilityq
Conditional means and ability
ECO6102 / L3 / 3a 4.1 Overview 27 / 57

## PDF 第 70 页

AI adoption, omitted variables, and
self-selection
Wooldridge 4.1 — a hypothetical AI-adoption comparison
Firms using AI are more productive. Does this show that AI raised
productivity, or can we not tell?
ECO6102 / L3 / 3a 4.1 Overview 28 / 57

## PDF 第 71 页

AI adoption, omitted variables, and
self-selection
Wooldridge 4.1 — a hypothetical AI-adoption comparison
AI adoption productivity
management quality
• Suppose better-managed firms are more likely to adopt and more
productive for other reasons.
• If omitted management entersu, adoption andumay be correlated. A
productivity gap alone does not isolate the tool’s effect.
ECO6102 / L3 / 3a 4.1 Overview 28 / 57

## PDF 第 72 页

(2) Measurement error
Wooldridge 4.1, p. 55; 4.4.2 — a reporting mistake enters both parts of the comparison
A person reports more schooling than they actually completed.
• Recorded schooling predicts wages using
years the person did not complete.
• Their actual wages reflect true schooling.
The unexplained part also contains the
reporting mistake.
reporting
mistake
recorded
schooling
unexplained
wages
CLASSICAL MEASUREMENT ERROR
Mean-zero reporting noise, uncorrelated with true schooling and the original
wage disturbance.
Substitution and attenuation
ECO6102 / L3 / 3a 4.1 Overview 29 / 57

## PDF 第 73 页

(2) Measurement error
Wooldridge 4.1, p. 55; 4.4.2 — a reporting mistake enters both parts of the comparison
A person reports more schooling than they actually completed.
• Recorded schooling predicts wages using
years the person did not complete.
• Their actual wages reflect true schooling.
The unexplained part also contains the
reporting mistake.
reporting
mistake
recorded
schooling
unexplained
wages
CLASSICAL MEASUREMENT ERROR
Mean-zero reporting noise, uncorrelated with true schooling and the original
wage disturbance.
Substitution and attenuation
ECO6102 / L3 / 3a 4.1 Overview 29 / 57

## PDF 第 74 页

(2) Measurement error
Wooldridge 4.1, p. 55; 4.4.2 — a reporting mistake enters both parts of the comparison
A person reports more schooling than they actually completed.
• Recorded schooling predicts wages using
years the person did not complete.
• Their actual wages reflect true schooling.
The unexplained part also contains the
reporting mistake.
reporting
mistake
recorded
schooling
unexplained
wages
CLASSICAL MEASUREMENT ERROR
Mean-zero reporting noise, uncorrelated with true schooling and the original
wage disturbance.
Substitution and attenuation
ECO6102 / L3 / 3a 4.1 Overview 29 / 57

## PDF 第 75 页

(3) Simultaneity
Wooldridge 4.1, p. 55 — the regressor responds to determinants of the outcome
Simultaneity: the regressor and outcome are jointly determined.
• We want to know how adding police
changes crime.
• Police deployment responds to crime,
which also depends on factors we
have not observed.
• Police levels may therefore track
unobserved crime determinants:
police is endogenous.
police
deployment
crime
effect response
Demand and supply example
ECO6102 / L3 / 3a 4.1 Overview 30 / 57

## PDF 第 76 页

(3) Simultaneity
Wooldridge 4.1, p. 55 — the regressor responds to determinants of the outcome
Simultaneity: the regressor and outcome are jointly determined.
• We want to know how adding police
changes crime.
• Police deployment responds to crime,
which also depends on factors we
have not observed.
• Police levels may therefore track
unobserved crime determinants:
police is endogenous.
police
deployment
crime
effect response
Demand and supply example
ECO6102 / L3 / 3a 4.1 Overview 30 / 57

## PDF 第 77 页

Three ways the comparison can go wrong
Wooldridge 4.1 — sources of endogeneity
• Omitted variables: schooling groups also differ in unobserved ability that
matters for wages.
• Measurement error: the recorded regressor and the regression error can
share the same measurement mistake.
• Simultaneity: police deployment responds to crime conditions that we
have not fully observed.
More observations alone cannot remove these connections. Proxies and
instruments need additional assumptions.
ECO6102 / L3 / 3a 4.1 Overview 31 / 57

## PDF 第 78 页

Three ways the comparison can go wrong
Wooldridge 4.1 — sources of endogeneity
• Omitted variables: schooling groups also differ in unobserved ability that
matters for wages.
• Measurement error: the recorded regressor and the regression error can
share the same measurement mistake.
• Simultaneity: police deployment responds to crime conditions that we
have not fully observed.
More observations alone cannot remove these connections. Proxies and
instruments need additional assumptions.
ECO6102 / L3 / 3a 4.1 Overview 31 / 57

## PDF 第 79 页

Three ways the comparison can go wrong
Wooldridge 4.1 — sources of endogeneity
• Omitted variables: schooling groups also differ in unobserved ability that
matters for wages.
• Measurement error: the recorded regressor and the regression error can
share the same measurement mistake.
• Simultaneity: police deployment responds to crime conditions that we
have not fully observed.
More observations alone cannot remove these connections. Proxies and
instruments need additional assumptions.
ECO6102 / L3 / 3a 4.1 Overview 31 / 57

## PDF 第 80 页

One equation, three sources of endogeneity
Wooldridge 4.1, p. 55 — alcohol consumption and worker productivity
QUESTION
How does alcohol consumption affect productivity, measured by wages?
1 Omitted variables: family background may affect both alcohol use and
wages.
2 Simultaneity: income, largely determined by wages, can affect alcohol
demand.
3 Measurement error: reported alcohol consumption may differ from actual
use.
The distinctions are not always sharp; more than one source can occur in the
same equation.
ECO6102 / L3 / 3a 4.1 Overview 32 / 57

## PDF 第 81 页

One equation, three sources of endogeneity
Wooldridge 4.1, p. 55 — alcohol consumption and worker productivity
QUESTION
How does alcohol consumption affect productivity, measured by wages?
1 Omitted variables: family background may affect both alcohol use and
wages.
2 Simultaneity: income, largely determined by wages, can affect alcohol
demand.
3 Measurement error: reported alcohol consumption may differ from actual
use.
The distinctions are not always sharp; more than one source can occur in the
same equation.
ECO6102 / L3 / 3a 4.1 Overview 32 / 57

## PDF 第 82 页

One equation, three sources of endogeneity
Wooldridge 4.1, p. 55 — alcohol consumption and worker productivity
QUESTION
How does alcohol consumption affect productivity, measured by wages?
1 Omitted variables: family background may affect both alcohol use and
wages.
2 Simultaneity: income, largely determined by wages, can affect alcohol
demand.
3 Measurement error: reported alcohol consumption may differ from actual
use.
The distinctions are not always sharp; more than one source can occur in the
same equation.
ECO6102 / L3 / 3a 4.1 Overview 32 / 57

## PDF 第 83 页

A sidenote: Structural vs. Reduced-form
Two perspectives of applied economics research
• Design-based (often called reduced-form): use a credible comparison to
estimate a policy or treatment effect, without estimating a full model of
behavior.
• Structural estimation: combine data with an economic model to estimate
behavioral parameters and study counterfactuals.
Both need identifying assumptions; the approaches can inform each other.
Policy-question example Formal reduced form Reading
ECO6102 / L3 / 3a 4.1 Overview 33 / 57

## PDF 第 84 页

A sidenote: Structural vs. Reduced-form
Two perspectives of applied economics research
• Design-based (often called reduced-form): use a credible comparison to
estimate a policy or treatment effect, without estimating a full model of
behavior.
• Structural estimation: combine data with an economic model to estimate
behavioral parameters and study counterfactuals.
Both need identifying assumptions; the approaches can inform each other.
Policy-question example Formal reduced form Reading
ECO6102 / L3 / 3a 4.1 Overview 33 / 57

## PDF 第 85 页

Roadmap
Wooldridge 4.2 — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 4.2 OLS properties

## PDF 第 86 页

The model in vector form
Wooldridge 4.2, (4.5) — a compact name for the same regression
y=xβ+u.(4.5)
• xcollects the constant and regressors;βcollects their coefficients.
• For attendance,x iβ=β 0 +β 1atndrtei.
• Ncounts observations;Kcounts coefficients, including the intercept. The
notation lets us handle several regressors together.
Rows and columns with real data
ECO6102 / L3 / 3a 4.2 OLS properties 34 / 57

## PDF 第 87 页

The model in vector form
Wooldridge 4.2, (4.5) — a compact name for the same regression
y=xβ+u.(4.5)
• xcollects the constant and regressors;βcollects their coefficients.
• For attendance,x iβ=β 0 +β 1atndrtei.
• Ncounts observations;Kcounts coefficients, including the intercept. The
notation lets us handle several regressors together.
Rows and columns with real data
ECO6102 / L3 / 3a 4.2 OLS properties 34 / 57

## PDF 第 88 页

Asymptotic properties
Wooldridge 4.2 introduction; Chapter 3 — let the sample grow under the same model
SAMPLING SETUP
A random sample(x i,y i),i=1, . . . ,N, from one population.
• Consistency: does the estimate concentrate near the target asNgrows?
• Asymptotic inference: what distribution and spread approximate its
sampling uncertainty?
Mathematical definition of consistency LLN and CLT
ECO6102 / L3 / 3a 4.2 OLS properties 35 / 57

## PDF 第 89 页

Asymptotic properties
Wooldridge 4.2 introduction; Chapter 3 — let the sample grow under the same model
SAMPLING SETUP
A random sample(x i,y i),i=1, . . . ,N, from one population.
• Consistency: does the estimate concentrate near the target asNgrows?
• Asymptotic inference: what distribution and spread approximate its
sampling uncertainty?
Mathematical definition of consistency LLN and CLT
ECO6102 / L3 / 3a 4.2 OLS properties 35 / 57

## PDF 第 90 页

Roadmap
Wooldridge 4.2.1 — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 4.2.1 Consistency

## PDF 第 91 页

Assumption OLS.1
Wooldridge 4.2.1, p. 56 — population errors must be unrelated to regressors
E(x′u)=0.
• The error has mean zero and is uncorrelated with every regressor in the
population.
• In the schooling example, omitted wage determinants must not
systematically move with schooling or the included controls.
Unpack OLS.1 Assumption versus fitted identity
ECO6102 / L3 / 3a 4.2.1 Consistency 36 / 57

## PDF 第 92 页

Assumption OLS.1
Wooldridge 4.2.1, p. 56 — population errors must be unrelated to regressors
E(x′u)=0.
• The error has mean zero and is uncorrelated with every regressor in the
population.
• In the schooling example, omitted wage determinants must not
systematically move with schooling or the included controls.
Unpack OLS.1 Assumption versus fitted identity
ECO6102 / L3 / 3a 4.2.1 Consistency 36 / 57

## PDF 第 93 页

Assumption OLS.2
Wooldridge 4.2.1, p. 57 — the data must separate the coefficients
rankE(x ′x)=K.
• No regressor can be an exact linear combination of the others in the
population.
• Example: including age in both years and months cannot identify two
separate effects; one column is twelve times the other.
• Correlated regressors are allowed. Perfect redundancy is the problem
here.
Rank condition and other examples
ECO6102 / L3 / 3a 4.2.1 Consistency 37 / 57

## PDF 第 94 页

Assumption OLS.2
Wooldridge 4.2.1, p. 57 — the data must separate the coefficients
rankE(x ′x)=K.
• No regressor can be an exact linear combination of the others in the
population.
• Example: including age in both years and months cannot identify two
separate effects; one column is twelve times the other.
• Correlated regressors are allowed. Perfect redundancy is the problem
here.
Rank condition and other examples
ECO6102 / L3 / 3a 4.2.1 Consistency 37 / 57

## PDF 第 95 页

Assumption OLS.2
Wooldridge 4.2.1, p. 57 — the data must separate the coefficients
rankE(x ′x)=K.
• No regressor can be an exact linear combination of the others in the
population.
• Example: including age in both years and months cannot identify two
separate effects; one column is twelve times the other.
• Correlated regressors are allowed. Perfect redundancy is the problem
here.
Rank condition and other examples
ECO6102 / L3 / 3a 4.2.1 Consistency 37 / 57

## PDF 第 96 页

Identification comes before estimation
Wooldridge 4.2.1, p. 57 — express the coefficient in observable population moments
• In this linear model with random sampling,identificationmeans thatβ
can be written in terms of population moments of observable variables.
• OLS.1 and OLS.2 give
β=[E(x ′x)]−1E(x′y).
• We observe(x,y); both expectations involve these observable variables.
Next, replace the population moments with their sample counterparts.
ECO6102 / L3 / 3a 4.2.1 Consistency 38 / 57

## PDF 第 97 页

Identification comes before estimation
Wooldridge 4.2.1, p. 57 — express the coefficient in observable population moments
• In this linear model with random sampling,identificationmeans thatβ
can be written in terms of population moments of observable variables.
• OLS.1 and OLS.2 give
β=[E(x ′x)]−1E(x′y).
• We observe(x,y); both expectations involve these observable variables.
Next, replace the population moments with their sample counterparts.
ECO6102 / L3 / 3a 4.2.1 Consistency 38 / 57

## PDF 第 98 页

The analogy principle
Wooldridge 4.2.1 — replace population averages with sample averages
Population
β=[E(x ′x)]−1E(x′y).
Sample
ˆβ=


1
N
X
i
x′
ixi


−1 

1
N
X
i
x′
iyi

 .
• We cannot see the whole population. We calculate averages and
co-movement from our sample instead.
• Theanalogy principlesolves the sample version of the population
problem. Here it gives the same OLS fit as least squares.
Population solution Sample solution Law of large numbers
ECO6102 / L3 / 3a 4.2.1 Consistency 39 / 57

## PDF 第 99 页

The analogy principle
Wooldridge 4.2.1 — replace population averages with sample averages
Population
β=[E(x ′x)]−1E(x′y).
Sample
ˆβ=


1
N
X
i
x′
ixi


−1 

1
N
X
i
x′
iyi

 .
• We cannot see the whole population. We calculate averages and
co-movement from our sample instead.
• Theanalogy principlesolves the sample version of the population
problem. Here it gives the same OLS fit as least squares.
Population solution Sample solution Law of large numbers
ECO6102 / L3 / 3a 4.2.1 Consistency 39 / 57

## PDF 第 100 页

The analogy principle
Wooldridge 4.2.1 — replace population averages with sample averages
Population
β=[E(x ′x)]−1E(x′y).
Sample
ˆβ=


1
N
X
i
x′
ixi


−1 

1
N
X
i
x′
iyi

 .
• We cannot see the whole population. We calculate averages and
co-movement from our sample instead.
• Theanalogy principlesolves the sample version of the population
problem. Here it gives the same OLS fit as least squares.
Population solution Sample solution Law of large numbers
ECO6102 / L3 / 3a 4.2.1 Consistency 39 / 57

## PDF 第 101 页

Consistency of OLS
Wooldridge 4.2.1, Theorem 4.1 — the chance of a large miss tends to zero
plimN→∞
ˆβ=β.
• Theorem 4.1: under OLS.1–OLS.2, OLS from a random sample following
y=xβ+uis consistent forβ.
• As the sample grows, the probability of a large estimation error tends to
zero.
• Consistencyis about growingN.Unbiasednessis about being centered
on the target at a fixedN; it is a different property.
The next picture holds the target fixed and lets the sample size grow.
Consistency proof Unbiasedness proof Definition of Consistency
Unbiasedness and consistency
ECO6102 / L3 / 3a 4.2.1 Consistency 40 / 57

## PDF 第 102 页

Consistency of OLS
Wooldridge 4.2.1, Theorem 4.1 — the chance of a large miss tends to zero
plimN→∞
ˆβ=β.
• Theorem 4.1: under OLS.1–OLS.2, OLS from a random sample following
y=xβ+uis consistent forβ.
• As the sample grows, the probability of a large estimation error tends to
zero.
• Consistencyis about growingN.Unbiasednessis about being centered
on the target at a fixedN; it is a different property.
The next picture holds the target fixed and lets the sample size grow.
Consistency proof Unbiasedness proof Definition of Consistency
Unbiasedness and consistency
ECO6102 / L3 / 3a 4.2.1 Consistency 40 / 57

## PDF 第 103 页

Consistency of OLS
Wooldridge 4.2.1, Theorem 4.1 — the chance of a large miss tends to zero
plimN→∞
ˆβ=β.
• Theorem 4.1: under OLS.1–OLS.2, OLS from a random sample following
y=xβ+uis consistent forβ.
• As the sample grows, the probability of a large estimation error tends to
zero.
• Consistencyis about growingN.Unbiasednessis about being centered
on the target at a fixedN; it is a different property.
The next picture holds the target fixed and lets the sample size grow.
Consistency proof Unbiasedness proof Definition of Consistency
Unbiasedness and consistency
ECO6102 / L3 / 3a 4.2.1 Consistency 40 / 57

## PDF 第 104 页

Consistency
Introductory Wooldridge 6e, 5-1, Figure 5.1 — schematic sampling distributions as the
sample grows
θ
possible estimates
density
N=2
N=8
N=32
More data makes a large miss less likely; it need not improve every realized
estimate.
The probability definition
ECO6102 / L3 / 3a 4.2.1 Consistency 41 / 57

## PDF 第 105 页

Consistency
Introductory Wooldridge 6e, 5-1, Figure 5.1 — schematic sampling distributions as the
sample grows
θ
possible estimates
density
N=2
N=8
N=32
More data makes a large miss less likely; it need not improve every realized
estimate.
The probability definition
ECO6102 / L3 / 3a 4.2.1 Consistency 41 / 57

## PDF 第 106 页

Consistency
Introductory Wooldridge 6e, 5-1, Figure 5.1 — schematic sampling distributions as the
sample grows
θ
possible estimates
density
N=2
N=8
N=32
More data makes a large miss less likely; it need not improve every realized
estimate.
The probability definition
ECO6102 / L3 / 3a 4.2.1 Consistency 41 / 57

## PDF 第 107 页

Roadmap
Wooldridge 4.2.2 — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 4.2.2 Inference

## PDF 第 108 页

Asymptotic normality
Wooldridge 4.2.2, p. 59 — the distribution needed for inference
• Consistency tells us that large misses become unlikely. Hypothesis testing
also requires the asymptotic distribution of the estimator.
• Under i.i.d. sampling, OLS.1–OLS.2 and finite second moments ofx ′u,
√
N( ˆβ−β)
d
− →N(0,A−1BA−1),
whereA=E(x ′x)andB=E(u 2x′x).
Derivation CLT intuition
ECO6102 / L3 / 3a 4.2.2 Inference 42 / 57

## PDF 第 109 页

Asymptotic normality
Wooldridge 4.2.2, p. 59 — the distribution needed for inference
• Consistency tells us that large misses become unlikely. Hypothesis testing
also requires the asymptotic distribution of the estimator.
• Under i.i.d. sampling, OLS.1–OLS.2 and finite second moments ofx ′u,
√
N( ˆβ−β)
d
− →N(0,A−1BA−1),
whereA=E(x ′x)andB=E(u 2x′x).
Derivation CLT intuition
ECO6102 / L3 / 3a 4.2.2 Inference 42 / 57

## PDF 第 110 页

Homoskedasticity and Theorem 4.2
Wooldridge 4.2.2, p. 59, (4.9) — simplify the asymptotic covariance
• Assumption OLS.3:
E(u2x′x)=σ 2E(x′x), σ 2 =E(u 2).
• Theorem 4.2: under OLS.1–OLS.3 and the maintained sampling and
moment conditions, √
N( ˆβ−β)
d
− →N

0, σ2[E(x′x)]−1

.(4.9)
OLS.3 givesB=σ 2A, soA −1BA−1 =σ 2A−1.
Read OLS.3 element by element Proof
ECO6102 / L3 / 3a 4.2.2 Inference 43 / 57

## PDF 第 111 页

Homoskedasticity and Theorem 4.2
Wooldridge 4.2.2, p. 59, (4.9) — simplify the asymptotic covariance
• Assumption OLS.3:
E(u2x′x)=σ 2E(x′x), σ 2 =E(u 2).
• Theorem 4.2: under OLS.1–OLS.3 and the maintained sampling and
moment conditions, √
N( ˆβ−β)
d
− →N

0, σ2[E(x′x)]−1

.(4.9)
OLS.3 givesB=σ 2A, soA −1BA−1 =σ 2A−1.
Read OLS.3 element by element Proof
ECO6102 / L3 / 3a 4.2.2 Inference 43 / 57

## PDF 第 112 页

A conditional-variance interpretation
Wooldridge 4.2.2, p. 59 — a familiar sufficient condition for OLS.3
x
ydensity
E(y|x)
homoskedastic: constant spread
x
ydensity
E(y|x)
heteroskedastic: spread grows
WhenE(u|x)=0,E(u 2 |x)=Var(u|x).
Constant variance=⇒OLS.3 (sufficient, not necessary).
Why LIE gives OLS.3
ECO6102 / L3 / 3a 4.2.2 Inference 44 / 57

## PDF 第 113 页

A conditional-variance interpretation
Wooldridge 4.2.2, p. 59 — a familiar sufficient condition for OLS.3
x
ydensity
E(y|x)
homoskedastic: constant spread
x
ydensity
E(y|x)
heteroskedastic: spread grows
WhenE(u|x)=0,E(u 2 |x)=Var(u|x).
Constant variance=⇒OLS.3 (sufficient, not necessary).
Why LIE gives OLS.3
ECO6102 / L3 / 3a 4.2.2 Inference 44 / 57

## PDF 第 114 页

Asymptotic variance under homoskedasticity
Wooldridge 4.2.2, p. 60 — from the limit to an estimated covariance
• Theorem 4.2 gives
Avar(ˆβ)= σ2
N [E(x′x)]−1.
• Estimate the unknown population quantities from the sample:
ˆσ2 =
P
i ˆu2
i
N−K , ˆA= X′X
N , ˆui =y i −x i ˆβ.
Kincludes the intercept. The factor 1/Nbelongs to the covariance of ˆβ.
ECO6102 / L3 / 3a 4.2.2 Inference 45 / 57

## PDF 第 115 页

Asymptotic variance under homoskedasticity
Wooldridge 4.2.2, p. 60 — from the limit to an estimated covariance
• Theorem 4.2 gives
Avar(ˆβ)= σ2
N [E(x′x)]−1.
• Estimate the unknown population quantities from the sample:
ˆσ2 =
P
i ˆu2
i
N−K , ˆA= X′X
N , ˆui =y i −x i ˆβ.
Kincludes the intercept. The factor 1/Nbelongs to the covariance of ˆβ.
ECO6102 / L3 / 3a 4.2.2 Inference 45 / 57

## PDF 第 116 页

From estimated covariance to standard errors
Wooldridge 4.2.2, (4.10); Definition 3.10, p. 44 — one standard error per coefficient
SAMPLE INPUTS
ˆσ2 =SSR/(N−K)and ˆA=X ′X/N.
[Avar(ˆβ)= ˆσ2
N
ˆA−1 = ˆσ2(X′X)−1.(4.10)
• Thestandard erroris the square root of the corresponding diagonal
element:
se( ˆβj)=
rh [Avar(ˆβ)
i
jj.
• It estimates the sampling spread of that coefficient estimator.
SE versus sampling SD Why the residual variance is consistent
ECO6102 / L3 / 3a 4.2.2 Inference 46 / 57

## PDF 第 117 页

From estimated covariance to standard errors
Wooldridge 4.2.2, (4.10); Definition 3.10, p. 44 — one standard error per coefficient
SAMPLE INPUTS
ˆσ2 =SSR/(N−K)and ˆA=X ′X/N.
[Avar(ˆβ)= ˆσ2
N
ˆA−1 = ˆσ2(X′X)−1.(4.10)
• Thestandard erroris the square root of the corresponding diagonal
element:
se( ˆβj)=
rh [Avar(ˆβ)
i
jj.
• It estimates the sampling spread of that coefficient estimator.
SE versus sampling SD Why the residual variance is consistent
ECO6102 / L3 / 3a 4.2.2 Inference 46 / 57

## PDF 第 118 页

Wooldridge 4.2.2
Statistical inference
ECO6102 / Lecture 3

## PDF 第 119 页

Why the OLS results make inference possible
Wooldridge 3.5.1, pp. 43–44; 4.2.2, pp. 59–60 — connect assumptions, distribution and
decisions
1 OLS.1–OLS.2 give consistency under random sampling.
2 Theorem 4.2 supplies a normal approximation; OLS.3 gives its usual
covariance.
3 A consistent covariance estimate supplies the scale:
ˆβj −β j
se( ˆβj)
d
− →N(0,1).
Why standardizing gives this limit
ECO6102 / L3 / 3a 4.2.2 Inference 47 / 57

## PDF 第 120 页

Why the OLS results make inference possible
Wooldridge 3.5.1, pp. 43–44; 4.2.2, pp. 59–60 — connect assumptions, distribution and
decisions
1 OLS.1–OLS.2 give consistency under random sampling.
2 Theorem 4.2 supplies a normal approximation; OLS.3 gives its usual
covariance.
3 A consistent covariance estimate supplies the scale:
ˆβj −β j
se( ˆβj)
d
− →N(0,1).
Why standardizing gives this limit
ECO6102 / L3 / 3a 4.2.2 Inference 47 / 57

## PDF 第 121 页

Testing one coefficient
Wooldridge 4.2.2, p. 60 — compare a statistic with its null reference
H0 :β j =β j,0 againstH 1 :β j ,β j,0.
t=
ˆβj −β j,0
se( ˆβj)
a
∼N(0,1)underH 0.
• A two-sided 5%test rejectsH 0 when|t|>1.96.
• Otherwise, fail to rejectH 0: insufficient evidence against the hypothesized
value.
Possible testing errors P-values
ECO6102 / L3 / 3a 4.2.2 Inference 48 / 57

## PDF 第 122 页

Testing one coefficient
Wooldridge 4.2.2, p. 60 — compare a statistic with its null reference
H0 :β j =β j,0 againstH 1 :β j ,β j,0.
t=
ˆβj −β j,0
se( ˆβj)
a
∼N(0,1)underH 0.
• A two-sided 5%test rejectsH 0 when|t|>1.96.
• Otherwise, fail to rejectH 0: insufficient evidence against the hypothesized
value.
Possible testing errors P-values
ECO6102 / L3 / 3a 4.2.2 Inference 48 / 57

## PDF 第 123 页

Statistical inference
Wooldridge 4.2.2; Example 4.1 data — read an estimate together with its uncertainty
MROZ: 428 working, married women.
log(wagei)=β 0 +β 1educi +β 2experi +β 3exper2
i
+β 4agei +β 5kidslt6i +β 6kidsge6i +u i.
kidslt6: children under six;kidsge6: children aged six or older.
Coefficient Estimate Usual SE
Children under six (β5)−.06071.08876
• Estimate: fitted log-wage association, holding the other regressors fixed.
• SE: estimated sampling spread of this coefficient.
Full model and inference example
ECO6102 / L3 / 3a 4.2.2 Inference 49 / 57

## PDF 第 124 页

Statistical inference
Wooldridge 4.2.2; Example 4.1 data — read an estimate together with its uncertainty
MROZ: 428 working, married women.
log(wagei)=β 0 +β 1educi +β 2experi +β 3exper2
i
+β 4agei +β 5kidslt6i +β 6kidsge6i +u i.
kidslt6: children under six;kidsge6: children aged six or older.
Coefficient Estimate Usual SE
Children under six (β5)−.06071.08876
• Estimate: fitted log-wage association, holding the other regressors fixed.
• SE: estimated sampling spread of this coefficient.
Full model and inference example
ECO6102 / L3 / 3a 4.2.2 Inference 49 / 57

## PDF 第 125 页

Hypothesis testing
Wooldridge 4.2.2 — is the estimate unusual if the coefficient is zero?
Null:H 0 :β 5 =0; alternative:H 1 :β 5 ,0.
• Distance from zero in SEs:
t= −.06071
.08876 ≈ −.684.
• Null reference: standard normal,
approximately.
• At 5%, reject if|t|>1.96. Here: fail to
reject—too little evidence against
zero.
−1.96 0 1.96
observed−.684
test statistic underH 0
Testing, p-values and possible errors
ECO6102 / L3 / 3a 4.2.2 Inference 50 / 57

## PDF 第 126 页

Hypothesis testing
Wooldridge 4.2.2 — is the estimate unusual if the coefficient is zero?
Null:H 0 :β 5 =0; alternative:H 1 :β 5 ,0.
• Distance from zero in SEs:
t= −.06071
.08876 ≈ −.684.
• Null reference: standard normal,
approximately.
• At 5%, reject if|t|>1.96. Here: fail to
reject—too little evidence against
zero.
−1.96 0 1.96
observed−.684
test statistic underH 0
Testing, p-values and possible errors
ECO6102 / L3 / 3a 4.2.2 Inference 50 / 57

## PDF 第 127 页

Confidence intervals from the same normal
reference
Wooldridge 3.5.1, p. 44; 4.2.2, p. 60 — use the estimate and its standard error
A large-sample 95%confidence interval forβ j ish ˆβj −1.96se( ˆβj), ˆβj +1.96se( ˆβj)
i
.
• The normal reference gives approximately 95%coverage across repeated
samples.
• The interval changes across samples; the population coefficient is fixed.
• Using the same SE, a value is outside this interval exactly when its
two-sided 5%test rejects it.
Calculation and interpretation
ECO6102 / L3 / 3a 4.2.2 Inference 51 / 57

## PDF 第 128 页

Confidence intervals from the same normal
reference
Wooldridge 3.5.1, p. 44; 4.2.2, p. 60 — use the estimate and its standard error
A large-sample 95%confidence interval forβ j ish ˆβj −1.96se( ˆβj), ˆβj +1.96se( ˆβj)
i
.
• The normal reference gives approximately 95%coverage across repeated
samples.
• The interval changes across samples; the population coefficient is fixed.
• Using the same SE, a value is outside this interval exactly when its
two-sided 5%test rejects it.
Calculation and interpretation
ECO6102 / L3 / 3a 4.2.2 Inference 51 / 57

## PDF 第 129 页

Confidence intervals
Wooldridge 3.5.1 and 4.2.2 — show the uncertainty as a range
ˆβ5 ±1.96se( ˆβ5)=−.06071±1.96(.08876)≈[−.235, .113].
−.235 .113
0estimate
children under six coefficient (log-wage units)
• The interval includes zero and either sign: the estimate is imprecise.
• Across repeated samples, this procedure covers the fixed coefficient
approximately 95%of the time.
Interval calculation and interpretation
ECO6102 / L3 / 3a 4.2.2 Inference 52 / 57

## PDF 第 130 页

Confidence intervals
Wooldridge 3.5.1 and 4.2.2 — show the uncertainty as a range
ˆβ5 ±1.96se( ˆβ5)=−.06071±1.96(.08876)≈[−.235, .113].
−.235 .113
0estimate
children under six coefficient (log-wage units)
• The interval includes zero and either sign: the estimate is imprecise.
• Across repeated samples, this procedure covers the fixed coefficient
approximately 95%of the time.
Interval calculation and interpretation
ECO6102 / L3 / 3a 4.2.2 Inference 52 / 57

## PDF 第 131 页

From OLS properties to inference
Wooldridge 4.2.1–4.2.3 — each result has a different job
Maintain OLS.1–OLS.2 and the sampling/moment conditions.
LLN
Consistency
Large misses unlikely.
CLT
Normal
approximation
Sampling shape.
Sample + formula
Standard error
Estimated
sampling SD.
Difference / SE: normal reference
Test a value; form a confidence interval.
More data cannot
fix endogeneity.
Usual SEs need OLS.3; robust SEs allow its failure.
MROZ:t≈ −.684; no rejection at 5%; zero lies in the 95%CI.
ECO6102 / L3 / 3a 4.2.2 Inference 53 / 57

## PDF 第 132 页

From OLS properties to inference
Wooldridge 4.2.1–4.2.3 — each result has a different job
Maintain OLS.1–OLS.2 and the sampling/moment conditions.
LLN
Consistency
Large misses unlikely.
CLT
Normal
approximation
Sampling shape.
Sample + formula
Standard error
Estimated
sampling SD.
Difference / SE: normal reference
Test a value; form a confidence interval.
More data cannot
fix endogeneity.
Usual SEs need OLS.3; robust SEs allow its failure.
MROZ:t≈ −.684; no rejection at 5%; zero lies in the 95%CI.
ECO6102 / L3 / 3a 4.2.2 Inference 53 / 57

## PDF 第 133 页

From OLS properties to inference
Wooldridge 4.2.1–4.2.3 — each result has a different job
Maintain OLS.1–OLS.2 and the sampling/moment conditions.
LLN
Consistency
Large misses unlikely.
CLT
Normal
approximation
Sampling shape.
Sample + formula
Standard error
Estimated
sampling SD.
Difference / SE: normal reference
Test a value; form a confidence interval.
More data cannot
fix endogeneity.
Usual SEs need OLS.3; robust SEs allow its failure.
MROZ:t≈ −.684; no rejection at 5%; zero lies in the 95%CI.
ECO6102 / L3 / 3a 4.2.2 Inference 53 / 57

## PDF 第 134 页

Roadmap
Wooldridge 4.2.3 — current location in blue
OLS recap
4.1 Overview of the Single-Equation Linear Model
4.2 Asymptotic Properties of Ordinary Least Squares
4.2.1 Consistency
4.2.2 Asymptotic Inference Using Ordinary Least Squares
4.2.3 Heteroskedasticity-Robust Inference
ECO6102 / L3 / 3a 4.2.3 Robust inference

## PDF 第 135 页

Heteroskedasticity-robust standard errors
Wooldridge 4.2.3, pp. 61–62 — retain OLS and estimate its covariance
Without OLS.3, retain the general covariance and estimateB:
Avar(ˆβ)= A−1BA−1
N , ˆB= 1
N
X
i
ˆu2
i x′
ixi.
bΣHC0 =(X ′X)−1
X
i
ˆu2
i x′
ixi

(X′X)−1.(4.11)
• Robust SEs are
q
[bΣ]jj; OLS coefficients are unchanged.
• Stata:regress y x1 x2, vce(robust)uses bΣHC1 = N
N−K
bΣHC0.
MROZ comparison Covariance derivation
ECO6102 / L3 / 3a 4.2.3 Robust inference 54 / 57

## PDF 第 136 页

Heteroskedasticity-robust standard errors
Wooldridge 4.2.3, pp. 61–62 — retain OLS and estimate its covariance
Without OLS.3, retain the general covariance and estimateB:
Avar(ˆβ)= A−1BA−1
N , ˆB= 1
N
X
i
ˆu2
i x′
ixi.
bΣHC0 =(X ′X)−1
X
i
ˆu2
i x′
ixi

(X′X)−1.(4.11)
• Robust SEs are
q
[bΣ]jj; OLS coefficients are unchanged.
• Stata:regress y x1 x2, vce(robust)uses bΣHC1 = N
N−K
bΣHC0.
MROZ comparison Covariance derivation
ECO6102 / L3 / 3a 4.2.3 Robust inference 54 / 57

## PDF 第 137 页

Wrap-up (3a)
ECO6102 / Lecture 3

## PDF 第 138 页

Key takeaways
Wooldridge 4.2.1–4.2.3 — estimate, target and uncertainty
• Consistency: Theorem 4.1 says OLS concentrates near its target under
OLS.1–OLS.2 and the sampling/moment conditions.
• Normal approximation: Theorem 4.2 adds OLS.3 for the usual SEs.
Normal disturbances are unnecessary; the CLT concerns estimates across
samples.
• Inference: combine the estimate with a justified SE for a test or interval.
Robust SEs handle changing error spreads, not endogeneity.
The econometric workflow
ECO6102 / L3 / 3a Wrap-up 55 / 57

## PDF 第 139 页

Key takeaways
Wooldridge 4.2.1–4.2.3 — estimate, target and uncertainty
• Consistency: Theorem 4.1 says OLS concentrates near its target under
OLS.1–OLS.2 and the sampling/moment conditions.
• Normal approximation: Theorem 4.2 adds OLS.3 for the usual SEs.
Normal disturbances are unnecessary; the CLT concerns estimates across
samples.
• Inference: combine the estimate with a justified SE for a test or interval.
Robust SEs handle changing error spreads, not endogeneity.
The econometric workflow
ECO6102 / L3 / 3a Wrap-up 55 / 57

## PDF 第 140 页

Key takeaways
Wooldridge 4.2.1–4.2.3 — estimate, target and uncertainty
• Consistency: Theorem 4.1 says OLS concentrates near its target under
OLS.1–OLS.2 and the sampling/moment conditions.
• Normal approximation: Theorem 4.2 adds OLS.3 for the usual SEs.
Normal disturbances are unnecessary; the CLT concerns estimates across
samples.
• Inference: combine the estimate with a justified SE for a test or interval.
Robust SEs handle changing error spreads, not endogeneity.
The econometric workflow
ECO6102 / L3 / 3a Wrap-up 55 / 57

## PDF 第 141 页

Next lecture
Wooldridge 4.3–4.4 — when important determinants are missing or mismeasured
• 3b: more inference, omitted variables and proxies (4.3), then measurement
error (4.4).
• Read Sections 4.3–4.4. Detailed inference calculations from today remain
in this deck’s appendix.
• Problem Set 1 is due Sunday 11 October 2026 (new date).
Appendix contents
ECO6102 / L3 / 3a Wrap-up 56 / 57

## PDF 第 142 页

Appendix
ECO6102 / Lecture 3
Main lecture: slide 56

## PDF 第 143 页

Appendix contents
Reference material in textbook order; use the return button after a detour
A Probability tools and sampling illustrations App. 1
B Population restrictions and economic models App. 16
C OLS calculations and estimator properties App. 39
D Inference calculations and proofs App. 67
E Robust covariance and weighting App. 86
F Optional LM tests App. 95
Back to slide 56
ECO6102 / L3 / 3a

## PDF 第 144 页

Appendix roadmap
APPENDIX A · Wooldridge 3.2–3.5.2 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a Chapter 3 tools

## PDF 第 145 页

Consistency
Introductory Wooldridge 6e, C-3a, equation (C.7) — make a large miss unlikely
WN: estimator fromNobservations;θ: fixed target;ϵ >0: fixed tolerance.
Pr

|WN −θ|> ϵ

− →0 for everyϵ >0 asN− → ∞.(C.7)
θ−ϵ θ θ+ϵ
within the tolerance
large miss large miss
Equivalently,W N
p
− →θ: the chance of a large miss tends to zero.
Back to slide 23 Back to slide 35 Back to slide 40 Back to slide 41
Back to contents
ECO6102 / L3 / 3a Chapter 3 tools App. 1 / 97

## PDF 第 146 页

Unbiasedness and consistency
Introductory Wooldridge 6e, C-2d and C-3a — using more observations matters
ILLUSTRA TIVE POPULA TION
Independent drawsY i ∼Bernoulli(.5):E(Y i)=.5,Var(Y i)=.25.
Estimator Mean Variance
First observationY 1 .5.25
Average ¯YN .5.25/N
• Both are unbiased. Only the average becomes more precise asNgrows.
• Y1 is always 0 or 1: it remains .5 away from the target, even if we collect
more data.
Back to slide 20 Main lecture: slide 40
ECO6102 / L3 / 3a Chapter 3 tools App. 2 / 97

## PDF 第 147 页

The law of large numbers
Introductory Wooldridge 6e, C-3a, equation (C.8) — averages approach population
means
Independent, identically distributed observations; finite meanµ.
¯YN = 1
N
NX
i=1
Yi
p
− →µ.(C.8)
• An average from a large sample is likely to be close to its population
mean.
• An average of 0/1 observations approaches.5 in our example.
• OLS uses such averages. Their limits give consistency under the model’s
assumptions.
Back to slide 35 Back to slide 39 Main lecture: slide 40
ECO6102 / L3 / 3a Chapter 3 tools App. 3 / 97

## PDF 第 148 页

The central limit theorem
Introductory Wooldridge 6e, C-3b — a reference shape for sampling uncertainty
Independent, identically distributed observations; meanµand variance
0< σ 2 <∞.
¯YN −µ
σ/
√
N
d
− →N(0,1).
• Center at the target; divide by the sampling SD.
• The resulting sampling distribution approaches the standard normal
curve.
• A consistent sample SD can replace the unknownσ.
Back to slide 42
ECO6102 / L3 / 3a Chapter 3 tools App. 4 / 97

## PDF 第 149 页

Why normal disturbances can be implausible
Introductory Wooldridge 6e, 5-2, Figure 5.2 — schematic participation-rate support
Participation rate: the percentage of eligible employees in a firm’s pension
plan.
0% 50% 100%
possible participation rates
• Participation cannot be below 0%or above 100%.
• A nondegenerate normal distribution has no such bounds.
• A coefficient estimate can still be approximately normal across samples.
Back to App. 6 Main lecture: slide 42
ECO6102 / L3 / 3a Chapter 3 tools App. 5 / 97

## PDF 第 150 页

Two different distributions
Wooldridge 3.5.1; 4.2.2 — outcomes and estimates vary differently
• Outcome variation: among
people with the same schooling,
wages differ.
• We holdxfixed and vary the
person.Heteroskedasticity: the
conditional disturbance variance
changes withx.
• Sampling variation: across
possible datasets, estimated
schooling slopes differ.
• We hold the population and
sampling rule fixed and vary the
dataset. An SE describes
uncertainty about a coefficient
estimate.
A bounded-outcome example
Main lecture: slide 44
ECO6102 / L3 / 3a Chapter 3 tools App. 6 / 97

## PDF 第 151 页

Convergence in probability
Wooldridge 3.2, Definitions 3.3–3.4, Lemmas 3.2 and 3.4 — plim,o p,O p, Slutsky
• xN
p
− →a(plimxN =a): for everyϵ >0,Pr(|x N −a|> ϵ)→0. Same thing
element by element for vectors and matrices.
• xN =o p(1): converges in probability to zero.x N =O p(1)(bounded in
probability): for everyϵthere isb ϵ withPr(|x N| ≥b ϵ)< ϵfor all largeN. A
plim to any constant impliesO p(1).
• Algebra (Lemma 3.2):o p(1)+o p(1)=o p(1),O p(1)+O p(1)=O p(1),
Op(1)·O p(1)=O p(1),o p(1)·O p(1)=o p(1). The last is what makes theo p(1)
in (4.8) harmless.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 7 / 97

## PDF 第 152 页

Slutsky’s theorem
Wooldridge 3.2, Lemma 3.4, Cor. 3.1 — plims pass through continuous functions
• Slutsky(Lemma 3.4): ifgis continuous atcandx N
p
− →c, theng(xN)
p
− →g(c):
plimg(x N)=g(plimx N). Expectations do not have this property, which is
why finite-sample analysis is hard.
• Corollary 3.1: ifZ N
p
− →AwithAinvertible, thenZ −1
N exists with probability
approaching one andZ −1
N
p
− →A−1.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 8 / 97

## PDF 第 153 页

Convergence in distribution; WLLN and CLT
Wooldridge 3.3–3.4, Definitions 3.6–3.7, Lemmas 3.6–3.7, Theorems 3.1–3.2
• xN
d
− →x: the c.d.f. ofxN converges to the (continuous) c.d.f. ofxat every
point. For vectors:c ′xN
d
− →c′xfor every unit vectorc(Cram ´er–Wold).
xN
a
∼N(µ,V)meansx N
d
− →N(µ,V).
• Continuous mapping(Lemma 3.6):x N
d
− →xandgcontinuous imply
g(xN)
d
− →g(x). Corollary 3.2: ifzN
d
− →N(0,V)with nonsingularV, then
A′zN
d
− →N(0,A′V A)andz ′
NV−1zN
d
− →χ2
K.
• Asymptotic equivalence(Lemma 3.7): ifz N
d
− →zandxN −z N
p
− →0, then
xN
d
− →z.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 9 / 97

## PDF 第 154 页

The two limit theorems
Wooldridge 3.4, Theorems 3.1–3.2 — for random samples
• WLLN(Theorem 3.1):{w i}i.i.d. with finite means:N −1 P
i wi
p
− →E(wi).
• CLT(Theorem 3.2, Lindeberg–L ´evy):{w i}i.i.d. with mean zero and finite
second moments:N −1/2 P
i wi
d
− →N(0,B),B=E(w iw′
i). Both survive
independent, non-identically distributed draws under weak conditions.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 10 / 97

## PDF 第 155 页

Estimators, standard errors, delta method
Wooldridge 3.5.1–3.5.2, Definitions 3.8–3.10, Lemma 3.9, Problem 3.7
• Consistent: ˆθN
p
− →θfor every value ofθ(3.2).
√
N-asymptotically
normal:
√
N( ˆθN −θ)
d
− →N(0,V)(3.3);Vis the asymptotic variance of√
N( ˆθN −θ)andAvar( ˆθN)=V/N(3.5). It implies ˆθN −θ=O p(N−1/2):√
N-consistent.
• Asymptotic standard error(Definition 3.10):se( ˆθNj)=( ˆvNjj/N)1/2 with
ˆVN
p
− →V— the number every regression table reports.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 11 / 97

## PDF 第 156 页

The delta method, with Problem 3.7
Wooldridge 3.5.2, Lemma 3.9 and (3.10)
• Delta method(Lemma 3.9): forc(·)continuously differentiable with
JacobianC(θ),
√
N[c( ˆθN)−c(θ)]
a
∼N(0,CVC ′)(3.8), so
[Avar[c(ˆθN)]= ˆCN[ [Avar(ˆθN)] ˆC′
N (3.10), where ˆCN =C( ˆθN).
• Problem 3.7: ˆθ=4,se=2, andγ=logθ. Then ˆγ=log4=1.386,
se( ˆγ)=se( ˆθ)/ ˆθ=.5. Testingθ=1 givest=(4−1)/2=1.5; testing the
equivalentγ=0 givest=1.386/.5=2.77. Asymptotically equivalent tests
can disagree in a given sample.
Main lecture: slide 56
ECO6102 / L3 / 3a Chapter 3 tools App. 12 / 97

## PDF 第 157 页

Six words before Chapter 4
Wooldridge 3.5.1, 4.2.1 — six words defined once; each returns where it is used
Unbiased
right on average at thisN: the pile is centred onβ(4.2.1)
Consistent
asNgrows, the chance of being far fromβvanishes (Thm 4.1)
Estimator
a rule mapping a sample into a coefficient estimate
Analogy
principle
population averages→sample averages (method of moments;
4.2.1)
Asymptotic
“asN→ ∞”, used as an approximation at ourN(Thm 4.2)
Inference
from one sample to the population, with uncertainty attached
(4.2.2–4.2.3)
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 13 / 97

## PDF 第 158 页

Six words before Chapter 4
Wooldridge 3.5.1, 4.2.1 — six words defined once; each returns where it is used
Unbiased
right on average at thisN: the pile is centred onβ(4.2.1)
Consistent
asNgrows, the chance of being far fromβvanishes (Thm 4.1)
Estimator
a rule mapping a sample into a coefficient estimate
Analogy
principle
population averages→sample averages (method of moments;
4.2.1)
Asymptotic
“asN→ ∞”, used as an approximation at ourN(Thm 4.2)
Inference
from one sample to the population, with uncertainty attached
(4.2.2–4.2.3)
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 13 / 97

## PDF 第 159 页

Six words before Chapter 4
Wooldridge 3.5.1, 4.2.1 — six words defined once; each returns where it is used
Unbiased
right on average at thisN: the pile is centred onβ(4.2.1)
Consistent
asNgrows, the chance of being far fromβvanishes (Thm 4.1)
Estimator
a rule mapping a sample into a coefficient estimate
Analogy
principle
population averages→sample averages (method of moments;
4.2.1)
Asymptotic
“asN→ ∞”, used as an approximation at ourN(Thm 4.2)
Inference
from one sample to the population, with uncertainty attached
(4.2.2–4.2.3)
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 13 / 97

## PDF 第 160 页

Six words before Chapter 4
Wooldridge 3.5.1, 4.2.1 — six words defined once; each returns where it is used
Unbiased
right on average at thisN: the pile is centred onβ(4.2.1)
Consistent
asNgrows, the chance of being far fromβvanishes (Thm 4.1)
Estimator
a rule mapping a sample into a coefficient estimate
Analogy
principle
population averages→sample averages (method of moments;
4.2.1)
Asymptotic
“asN→ ∞”, used as an approximation at ourN(Thm 4.2)
Inference
from one sample to the population, with uncertainty attached
(4.2.2–4.2.3)
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 13 / 97

## PDF 第 161 页

What Lectures 1 and 2 already gave us
Recall — L1: obstacles to causality and random draws; L2: composite slopes
• L1, obstacles: omitted variables,
measurement error, simultaneity,
self-selection — all can makeumove with
the regressors: endogeneity.
• L1, random draws:(y i,x i)are drawn
together; regressors are random, not fixed.
• L2, composite slopes: with ability missing,
the observed schooling slope is
α1 =β 1 +β 3δ1: target plus ability’s link to
schooling.
population
random draw
(yi,x i),i=1, . . . ,N
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 14 / 97

## PDF 第 162 页

What Lectures 1 and 2 already gave us
Recall — L1: obstacles to causality and random draws; L2: composite slopes
• L1, obstacles: omitted variables,
measurement error, simultaneity,
self-selection — all can makeumove with
the regressors: endogeneity.
• L1, random draws:(y i,x i)are drawn
together; regressors are random, not fixed.
• L2, composite slopes: with ability missing,
the observed schooling slope is
α1 =β 1 +β 3δ1: target plus ability’s link to
schooling.
population
random draw
(yi,x i),i=1, . . . ,N
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 14 / 97

## PDF 第 163 页

What Lectures 1 and 2 already gave us
Recall — L1: obstacles to causality and random draws; L2: composite slopes
• L1, obstacles: omitted variables,
measurement error, simultaneity,
self-selection — all can makeumove with
the regressors: endogeneity.
• L1, random draws:(y i,x i)are drawn
together; regressors are random, not fixed.
• L2, composite slopes: with ability missing,
the observed schooling slope is
α1 =β 1 +β 3δ1: target plus ability’s link to
schooling.
population
random draw
(yi,x i),i=1, . . . ,N
Main lecture: slide 9
ECO6102 / L3 / 3a Chapter 3 tools App. 14 / 97

## PDF 第 164 页

A world we built: unbiased and consistent
Wooldridge p. 58 —y=3+2x+u: centred on 2 at everyN; spreads .298, .091, .029
1.5 2 2.5
0
200
400
samples
N=50: mean 1.999, SD .298
1.5 2 2.5
0
200
400
N=500: mean 2.001, SD .091
1.5 2 2.5
0
200
400
N=5,000: mean 1.999, SD .029
Knownβ 1 =2: centered at eachN, and narrowing. Asymptotic SD: 6/
√
9N=
.283, .089, .028.
Main lecture: slide 17
ECO6102 / L3 / 3a Chapter 3 tools App. 15 / 97

## PDF 第 165 页

Appendix roadmap
APPENDIX B · Wooldridge 4.1 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a The population model and economic interpretation

## PDF 第 166 页

Holding ability fixed versus averaging it out
Wooldridge 4.1 — two conditional means answer different questions
SCHOOLING AND WAGES
y=β 0 +β 1s+β 2e+γq+v,E(v|s,e,q)=0;sschooling,eexperience,qability.
• Hold ability fixed:
E(y|s,e,q)=β 0 +β 1s+β 2e+γq.
• Average over ability at each(s,e):
E(y|s,e)=β 0 +β 1s+β 2e+γE(q|s,e).
• If ability composition changes with schooling, the observed mean
difference includes that change.
Back to slide 27 Back to contents
ECO6102 / L3 / 3a The population model and economic interpretation App. 16 / 97

## PDF 第 167 页

Holding ability fixed versus averaging it out
Wooldridge 4.1 — two conditional means answer different questions
SCHOOLING AND WAGES
y=β 0 +β 1s+β 2e+γq+v,E(v|s,e,q)=0;sschooling,eexperience,qability.
• Hold ability fixed:
E(y|s,e,q)=β 0 +β 1s+β 2e+γq.
• Average over ability at each(s,e):
E(y|s,e)=β 0 +β 1s+β 2e+γE(q|s,e).
• If ability composition changes with schooling, the observed mean
difference includes that change.
Back to slide 27 Back to contents
ECO6102 / L3 / 3a The population model and economic interpretation App. 16 / 97

## PDF 第 168 页

Put the omitted variable into the error
Wooldridge 4.1, p. 55 — substitution reveals the covariance that matters
FULL WAGE EQUA TION
y=β 0 +β 1educ+β 2exper+γq+v, withE(v|educ,exper,q)=0.
• Without ability in the data, write the same equation as
y=β 0 +β 1educ+β 2exper+u,u=γq+v.
• Therefore
Cov(educ,u)=γCov(educ,q).
• The problem arises when ability matters for wages and co-moves with
schooling.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 17 / 97

## PDF 第 169 页

Put the omitted variable into the error
Wooldridge 4.1, p. 55 — substitution reveals the covariance that matters
FULL WAGE EQUA TION
y=β 0 +β 1educ+β 2exper+γq+v, withE(v|educ,exper,q)=0.
• Without ability in the data, write the same equation as
y=β 0 +β 1educ+β 2exper+u,u=γq+v.
• Therefore
Cov(educ,u)=γCov(educ,q).
• The problem arises when ability matters for wages and co-moves with
schooling.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 17 / 97

## PDF 第 170 页

Measurement error in symbols
Wooldridge 4.4.2 — the same reporting mistake enters the regressor and the error
TRUE AND RECORDED SCHOOLING
y=β 0 +β 1x∗ +v,x=x ∗ +e;Cov(x ∗,v)=0.
• Classical error:E(e)=0,Cov(e,x ∗)=Cov(e,v)=0.
• Substitute recorded schooling:
y=β 0 +β 1x+u,u=v−β 1e,Cov(x,u)=−β 1 Var(e).
Why the simple-regression slope is attenuated
Back to slide 29
ECO6102 / L3 / 3a The population model and economic interpretation App. 18 / 97

## PDF 第 171 页

Measurement error in symbols
Wooldridge 4.4.2 — the same reporting mistake enters the regressor and the error
TRUE AND RECORDED SCHOOLING
y=β 0 +β 1x∗ +v,x=x ∗ +e;Cov(x ∗,v)=0.
• Classical error:E(e)=0,Cov(e,x ∗)=Cov(e,v)=0.
• Substitute recorded schooling:
y=β 0 +β 1x+u,u=v−β 1e,Cov(x,u)=−β 1 Var(e).
Why the simple-regression slope is attenuated
Back to slide 29
ECO6102 / L3 / 3a The population model and economic interpretation App. 18 / 97

## PDF 第 172 页

When measurement error attenuates the slope
Wooldridge 4.4.2 — a result for classical error in a simple regression
SAME MODEL
y=β 0 +β 1x∗ +v,x=x ∗ +e,Cov(x ∗,v)=0.
• MaintainE(e)=0 andCov(e,x ∗)=Cov(e,v)=0, i.i.d. sampling, finite
second moments andVar(x ∗)>0.
plim ˆβ1 =β 1
Var(x∗)
Var(x∗)+Var(e) .
• Noise dilutes the signal; more data does not remove the attenuation.
• This is not a universal rule for measurement error in other settings.
Back to App. 18 Main lecture: slide 29
ECO6102 / L3 / 3a The population model and economic interpretation App. 19 / 97

## PDF 第 173 页

When measurement error attenuates the slope
Wooldridge 4.4.2 — a result for classical error in a simple regression
SAME MODEL
y=β 0 +β 1x∗ +v,x=x ∗ +e,Cov(x ∗,v)=0.
• MaintainE(e)=0 andCov(e,x ∗)=Cov(e,v)=0, i.i.d. sampling, finite
second moments andVar(x ∗)>0.
plim ˆβ1 =β 1
Var(x∗)
Var(x∗)+Var(e) .
• Noise dilutes the signal; more data does not remove the attenuation.
• This is not a universal rule for measurement error in other settings.
Back to App. 18 Main lecture: slide 29
ECO6102 / L3 / 3a The population model and economic interpretation App. 19 / 97

## PDF 第 174 页

Demand, supply, and equilibrium
Wooldridge 4.1 — two behavioral relationships jointly determine an observed outcome
0 6 12
0
3
6
demand supply
E0
quantityQ
priceP
• Demand(blue): buyers’
response to price, holding
demand shifters fixed.
• Supply(orange): sellers’
response, holding supply
shifters fixed.
• Equilibrium: both choices are
compatible atP=3,Q=6.
Back to slide 30
ECO6102 / L3 / 3a The population model and economic interpretation App. 20 / 97

## PDF 第 175 页

Which curve moved?
Wooldridge 4.1 — different outside shifts trace different relationships
0 6 8 12
0
3
4
6
quantityQ
priceP
Demand rises
0 6 8 12
0
2
3
6
quantityQ
Supply rises
• Demand shift:(P,Q)=(3,6)→(4,8); price and quantity rise together.
• Supply shift:(P,Q)=(3,6)→(2,8); price falls while quantity rises.
Main lecture: slide 30
ECO6102 / L3 / 3a The population model and economic interpretation App. 21 / 97

## PDF 第 176 页

What a reduced form solves for
Wooldridge 4.1 and 9.2.1 — express equilibrium outcomes in terms of outside
determinants
Areduced formexpresses each jointly determined outcome using only
outside determinants.
Behavioral equations− →equilibrium− →reduced forms.
• In this market,PandQbecome functions of the demand and supply
shifters,dands.
• A regression ofQon jointly determinedPis not automatically a reduced
form or a demand curve.
Solve the illustrative market
Back to slide 33 Main lecture: slide 30
ECO6102 / L3 / 3a The population model and economic interpretation App. 22 / 97

## PDF 第 177 页

What a reduced form solves for
Wooldridge 4.1 and 9.2.1 — express equilibrium outcomes in terms of outside
determinants
Areduced formexpresses each jointly determined outcome using only
outside determinants.
Behavioral equations− →equilibrium− →reduced forms.
• In this market,PandQbecome functions of the demand and supply
shifters,dands.
• A regression ofQon jointly determinedPis not automatically a reduced
form or a demand curve.
Solve the illustrative market
Back to slide 33 Main lecture: slide 30
ECO6102 / L3 / 3a The population model and economic interpretation App. 22 / 97

## PDF 第 178 页

Why this course does OLS again
Wooldridge 4.1, p. 53 — fixed regressors to random draws; same formula, new
questions
• Some traditional treatments take regressors as fixed. Here(x,y)is a
random draw: both vary across samples. ECO3121 also used random
sampling.
• OLS.1–OLS.3 restrict the joint population distribution of(x,u);
conditioning onX(appendix C) is notXbeing fixed by design.
• Statistical questions after identification: whether estimates concentrate
near the target (Thm 4.1), how wide and what shape (Thm 4.2), what one
sample says about the width (se).
Main lecture: slide 9
ECO6102 / L3 / 3a The population model and economic interpretation App. 23 / 97

## PDF 第 179 页

Why this course does OLS again
Wooldridge 4.1, p. 53 — fixed regressors to random draws; same formula, new
questions
• Some traditional treatments take regressors as fixed. Here(x,y)is a
random draw: both vary across samples. ECO3121 also used random
sampling.
• OLS.1–OLS.3 restrict the joint population distribution of(x,u);
conditioning onX(appendix C) is notXbeing fixed by design.
• Statistical questions after identification: whether estimates concentrate
near the target (Thm 4.1), how wide and what shape (Thm 4.2), what one
sample says about the width (se).
Main lecture: slide 9
ECO6102 / L3 / 3a The population model and economic interpretation App. 23 / 97

## PDF 第 180 页

Why this course does OLS again
Wooldridge 4.1, p. 53 — fixed regressors to random draws; same formula, new
questions
• Some traditional treatments take regressors as fixed. Here(x,y)is a
random draw: both vary across samples. ECO3121 also used random
sampling.
• OLS.1–OLS.3 restrict the joint population distribution of(x,u);
conditioning onX(appendix C) is notXbeing fixed by design.
• Statistical questions after identification: whether estimates concentrate
near the target (Thm 4.1), how wide and what shape (Thm 4.2), what one
sample says about the width (se).
Main lecture: slide 9
ECO6102 / L3 / 3a The population model and economic interpretation App. 23 / 97

## PDF 第 181 页

Why the zero mean is free
Wooldridge 4.1, p. 54 — with an intercept,E(u)=0 is a normalisation, no more
• SupposeE(u)=µ,0 in (4.1). Setβ ′
0 =β 0 +µandu ′ =u−µ: the same
equation holds withE(u ′)=0 — same slopes, samey, a relabelled
intercept.
• Nothing else changes:Cov(x j,u ′)=Cov(x j,u−µ)=Cov(x j,u). Subtracting
a constant moves no covariance, so the content of (4.2) is untouched.
• A normalisation, not exogeneity: the intercept absorbs the average of
what we left out; nothing about whether it moves withx.
• Without an intercept, mean zero is no longer a free normalization. Zero
covariance alone need not makeE(x ju)=Cov(x j,u)+µE(x j)zero.
Back to slide 24 Back to App. 27 Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 24 / 97

## PDF 第 182 页

Why the zero mean is free
Wooldridge 4.1, p. 54 — with an intercept,E(u)=0 is a normalisation, no more
• SupposeE(u)=µ,0 in (4.1). Setβ ′
0 =β 0 +µandu ′ =u−µ: the same
equation holds withE(u ′)=0 — same slopes, samey, a relabelled
intercept.
• Nothing else changes:Cov(x j,u ′)=Cov(x j,u−µ)=Cov(x j,u). Subtracting
a constant moves no covariance, so the content of (4.2) is untouched.
• A normalisation, not exogeneity: the intercept absorbs the average of
what we left out; nothing about whether it moves withx.
• Without an intercept, mean zero is no longer a free normalization. Zero
covariance alone need not makeE(x ju)=Cov(x j,u)+µE(x j)zero.
Back to slide 24 Back to App. 27 Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 24 / 97

## PDF 第 183 页

Why the zero mean is free
Wooldridge 4.1, p. 54 — with an intercept,E(u)=0 is a normalisation, no more
• SupposeE(u)=µ,0 in (4.1). Setβ ′
0 =β 0 +µandu ′ =u−µ: the same
equation holds withE(u ′)=0 — same slopes, samey, a relabelled
intercept.
• Nothing else changes:Cov(x j,u ′)=Cov(x j,u−µ)=Cov(x j,u). Subtracting
a constant moves no covariance, so the content of (4.2) is untouched.
• A normalisation, not exogeneity: the intercept absorbs the average of
what we left out; nothing about whether it moves withx.
• Without an intercept, mean zero is no longer a free normalization. Zero
covariance alone need not makeE(x ju)=Cov(x j,u)+µE(x j)zero.
Back to slide 24 Back to App. 27 Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 24 / 97

## PDF 第 184 页

The conditional mean restriction
Wooldridge 4.1, (4.3)–(4.4) —E(u|x)=0 is sufficient, not necessary, for (4.2)
• A sufficient condition for (4.2) is the zero conditional meanE(u|x)=0
(4.3): thenxβis the population regression functionE(y|x), (4.4).
• It is not necessary: (4.2) alone makesxβthe best linear predictor, which
can miss the group means (next frame).
• (4.3) says more than (4.2): after including the population line, no
additional function of the explanatory variables helps to explainy(p. 54);
(4.2) rules out only a linear one.
Back to slide 24 Back to slide 25
ECO6102 / L3 / 3a The population model and economic interpretation App. 25 / 97

## PDF 第 185 页

The conditional mean restriction
Wooldridge 4.1, (4.3)–(4.4) —E(u|x)=0 is sufficient, not necessary, for (4.2)
• A sufficient condition for (4.2) is the zero conditional meanE(u|x)=0
(4.3): thenxβis the population regression functionE(y|x), (4.4).
• It is not necessary: (4.2) alone makesxβthe best linear predictor, which
can miss the group means (next frame).
• (4.3) says more than (4.2): after including the population line, no
additional function of the explanatory variables helps to explainy(p. 54);
(4.2) rules out only a linear one.
Back to slide 24 Back to slide 25
ECO6102 / L3 / 3a The population model and economic interpretation App. 25 / 97

## PDF 第 186 页

The conditional mean restriction
Wooldridge 4.1, (4.3)–(4.4) —E(u|x)=0 is sufficient, not necessary, for (4.2)
• A sufficient condition for (4.2) is the zero conditional meanE(u|x)=0
(4.3): thenxβis the population regression functionE(y|x), (4.4).
• It is not necessary: (4.2) alone makesxβthe best linear predictor, which
can miss the group means (next frame).
• (4.3) says more than (4.2): after including the population line, no
additional function of the explanatory variables helps to explainy(p. 54);
(4.2) rules out only a linear one.
Back to slide 24 Back to slide 25
ECO6102 / L3 / 3a The population model and economic interpretation App. 25 / 97

## PDF 第 187 页

Zero overall is not zero within groups
Wooldridge 4.1 and 2.3 — (4.2) can hold while (4.3) fails: the line misses the means
8 12 16
4
6
8
10
12
group means
schooling (years)
mean hourly wage (US$)
• Three schooling groups,
probability 1/3 each; group
means 4,8,10.
• Best line:−5/3+.75x. Its
errorvhasE(v)=0 and
E(xv)=0: (4.2) holds.
• ButE(v|x=12)=2/3,0:
(4.3) fails.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 26 / 97

## PDF 第 188 页

Zero overall is not zero within groups
Wooldridge 4.1 and 2.3 — (4.2) can hold while (4.3) fails: the line misses the means
8 12 16
4
6
8
10
12
group means
−1/3 +2/3 −1/3
schooling (years)
mean hourly wage (US$)
• Three schooling groups,
probability 1/3 each; group
means 4,8,10.
• Best line:−5/3+.75x. Its
errorvhasE(v)=0 and
E(xv)=0: (4.2) holds.
• ButE(v|x=12)=2/3,0:
(4.3) fails.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 26 / 97

## PDF 第 189 页

The two conditions in words
Wooldridge 4.1, (4.2) and p. 54 — what each condition rules out; linear in parameters
(4.2)
E(u)=0 andCov(x j,u)=0 for everyj
• E(u)=0: the intercept absorbs the average of what we left out — a
normalisation, free with an intercept.
• Cov(xj,u)=0: what we left out does not move linearly with what we put
in — the content; it is what self-selection breaks.
• Linear in parameters, not in variables:log(income),age 2 orcollege·ageas
regressors are fine (the book’s savings example, p. 54).
Appendix B: why the zero mean is free
Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 27 / 97

## PDF 第 190 页

The two conditions in words
Wooldridge 4.1, (4.2) and p. 54 — what each condition rules out; linear in parameters
(4.2)
E(u)=0 andCov(x j,u)=0 for everyj
• E(u)=0: the intercept absorbs the average of what we left out — a
normalisation, free with an intercept.
• Cov(xj,u)=0: what we left out does not move linearly with what we put
in — the content; it is what self-selection breaks.
• Linear in parameters, not in variables:log(income),age 2 orcollege·ageas
regressors are fine (the book’s savings example, p. 54).
Appendix B: why the zero mean is free
Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 27 / 97

## PDF 第 191 页

The two conditions in words
Wooldridge 4.1, (4.2) and p. 54 — what each condition rules out; linear in parameters
(4.2)
E(u)=0 andCov(x j,u)=0 for everyj
• E(u)=0: the intercept absorbs the average of what we left out — a
normalisation, free with an intercept.
• Cov(xj,u)=0: what we left out does not move linearly with what we put
in — the content; it is what self-selection breaks.
• Linear in parameters, not in variables:log(income),age 2 orcollege·ageas
regressors are fine (the book’s savings example, p. 54).
Appendix B: why the zero mean is free
Main lecture: slide 21
ECO6102 / L3 / 3a The population model and economic interpretation App. 27 / 97

## PDF 第 192 页

Three strengths of unrelatedness
Wooldridge pp. 54 and 58 — withE(u)=0, independence is strongest
(4.2):E(x ′u)=0
(4.3):E(u|x)=0
independent,
E(u)=0
• Independence+E(u)=0 (inner): fixes the
conditional distribution; implies (4.3) and
constant variance.
• (4.3)(middle): fixes the mean, not the
variance; gives (4.4).
• (4.2)(outer): fixes only the covariances;
gives the linear projection.
Estimator conclusions retain sampling, rank and moment conditions: (4.3)
supports unbiasedness; (4.2) supports consistency.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 28 / 97

## PDF 第 193 页

Three strengths of unrelatedness
Wooldridge pp. 54 and 58 — withE(u)=0, independence is strongest
(4.2):E(x ′u)=0
(4.3):E(u|x)=0
independent,
E(u)=0
• Independence+E(u)=0 (inner): fixes the
conditional distribution; implies (4.3) and
constant variance.
• (4.3)(middle): fixes the mean, not the
variance; gives (4.4).
• (4.2)(outer): fixes only the covariances;
gives the linear projection.
Estimator conclusions retain sampling, rank and moment conditions: (4.3)
supports unbiasedness; (4.2) supports consistency.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 28 / 97

## PDF 第 194 页

Three strengths of unrelatedness
Wooldridge pp. 54 and 58 — withE(u)=0, independence is strongest
(4.2):E(x ′u)=0
(4.3):E(u|x)=0
independent,
E(u)=0
• Independence+E(u)=0 (inner): fixes the
conditional distribution; implies (4.3) and
constant variance.
• (4.3)(middle): fixes the mean, not the
variance; gives (4.4).
• (4.2)(outer): fixes only the covariances;
gives the linear projection.
Estimator conclusions retain sampling, rank and moment conditions: (4.3)
supports unbiasedness; (4.2) supports consistency.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 28 / 97

## PDF 第 195 页

Three strengths of unrelatedness
Wooldridge pp. 54 and 58 — withE(u)=0, independence is strongest
(4.2):E(x ′u)=0
(4.3):E(u|x)=0
independent,
E(u)=0
• Independence+E(u)=0 (inner): fixes the
conditional distribution; implies (4.3) and
constant variance.
• (4.3)(middle): fixes the mean, not the
variance; gives (4.4).
• (4.2)(outer): fixes only the covariances;
gives the linear projection.
Estimator conclusions retain sampling, rank and moment conditions: (4.3)
supports unbiasedness; (4.2) supports consistency.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 28 / 97

## PDF 第 196 页

OLS.1 unpacked
Wooldridge 4.2.1 — zero conditional mean gives (4.2), not the other way
• Element by element, withx=(1,x 1, . . . ,xp):E(x ′u)=0givesE(u)=0 and
E(xju)=Cov(x j,u)=0,j=1, . . . ,p.
• (4.3)⇒(4.2)by iterated expectations:E(u)=E[E(u|x)]=0,
E(xju)=E[x jE(u|x)]=0; indeedE[h(x)u]=0 for any integrable product
h(x)u.
• Not the other way:x∈ {−1,0,1}with probabilities 1
4 , 1
2 , 1
4 andu=x 2 − 1
2:
E(u)= 1
2 − 1
2 =0,Cov(x,u)=E(x 3)=0, so (4.2) holds — but
E(u|x)= + 1
2,− 1
2,+ 1
2 atx=−1,0,1: (4.3) fails.
Back to slide 36
ECO6102 / L3 / 3a The population model and economic interpretation App. 29 / 97

## PDF 第 197 页

OLS.1 unpacked
Wooldridge 4.2.1 — zero conditional mean gives (4.2), not the other way
• Element by element, withx=(1,x 1, . . . ,xp):E(x ′u)=0givesE(u)=0 and
E(xju)=Cov(x j,u)=0,j=1, . . . ,p.
• (4.3)⇒(4.2)by iterated expectations:E(u)=E[E(u|x)]=0,
E(xju)=E[x jE(u|x)]=0; indeedE[h(x)u]=0 for any integrable product
h(x)u.
• Not the other way:x∈ {−1,0,1}with probabilities 1
4 , 1
2 , 1
4 andu=x 2 − 1
2:
E(u)= 1
2 − 1
2 =0,Cov(x,u)=E(x 3)=0, so (4.2) holds — but
E(u|x)= + 1
2,− 1
2,+ 1
2 atx=−1,0,1: (4.3) fails.
Back to slide 36
ECO6102 / L3 / 3a The population model and economic interpretation App. 29 / 97

## PDF 第 198 页

OLS.1 unpacked
Wooldridge 4.2.1 — zero conditional mean gives (4.2), not the other way
• Element by element, withx=(1,x 1, . . . ,xp):E(x ′u)=0givesE(u)=0 and
E(xju)=Cov(x j,u)=0,j=1, . . . ,p.
• (4.3)⇒(4.2)by iterated expectations:E(u)=E[E(u|x)]=0,
E(xju)=E[x jE(u|x)]=0; indeedE[h(x)u]=0 for any integrable product
h(x)u.
• Not the other way:x∈ {−1,0,1}with probabilities 1
4 , 1
2 , 1
4 andu=x 2 − 1
2:
E(u)= 1
2 − 1
2 =0,Cov(x,u)=E(x 3)=0, so (4.2) holds — but
E(u|x)= + 1
2,− 1
2,+ 1
2 atx=−1,0,1: (4.3) fails.
Back to slide 36
ECO6102 / L3 / 3a The population model and economic interpretation App. 29 / 97

## PDF 第 199 页

What zero covariance looks like
Wooldridge 4.1, (4.2)–(4.3) —uagainst schooling in three illustrative populations
8 12 16
−1
0
1
schooling
u
(4.3) holds
8 12 16
−1
0
1
schooling
(4.2) holds, (4.3) fails
8 12 16
−1
0
1
schooling
endogenous: (4.2) fails
Dashed: the best line through(x,u).
Left: every group mean ofuis zero.
Middle: errors−1/3,2/3,−1/3: flat line, nonzero group means. Right: the
line tilts; OLS missesβ.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 30 / 97

## PDF 第 200 页

What zero covariance looks like
Wooldridge 4.1, (4.2)–(4.3) —uagainst schooling in three illustrative populations
8 12 16
−1
0
1
schooling
u
(4.3) holds
8 12 16
−1
0
1
schooling
(4.2) holds, (4.3) fails
8 12 16
−1
0
1
schooling
endogenous: (4.2) fails
Dashed: the best line through(x,u). Left: every group mean ofuis zero.
Middle: errors−1/3,2/3,−1/3: flat line, nonzero group means.
Right: the
line tilts; OLS missesβ.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 30 / 97

## PDF 第 201 页

What zero covariance looks like
Wooldridge 4.1, (4.2)–(4.3) —uagainst schooling in three illustrative populations
8 12 16
−1
0
1
schooling
u
(4.3) holds
8 12 16
−1
0
1
schooling
(4.2) holds, (4.3) fails
8 12 16
−1
0
1
schooling
endogenous: (4.2) fails
Dashed: the best line through(x,u). Left: every group mean ofuis zero.
Middle: errors−1/3,2/3,−1/3: flat line, nonzero group means. Right: the
line tilts; OLS missesβ.
Main lecture: slide 24
ECO6102 / L3 / 3a The population model and economic interpretation App. 30 / 97

## PDF 第 202 页

Two meanings of endogenous
Wooldridge 4.1 and 9.2.1 — distinguish equilibrium determination from regressor–error
correlation
• In an economic system, price isendogenousbecause equilibrium
determines it jointly with quantity.
• In a regression equation, price isendogenousif it is correlated with that
equation’s disturbance.
• An unobserved demand shock that moves equilibrium price creates this
problem in the demand equation.
• If only a supply shifter varies and it is independent of the demand
disturbance, joint determination alone does not establish demand-error
correlation.
Main lecture: slide 30
ECO6102 / L3 / 3a The population model and economic interpretation App. 31 / 97

## PDF 第 203 页

Self-selection in the wild
Wooldridge 4.1 — hypothetical applications requested by Jack
• Job choice and later pay.If ambition raises both selection into a
tech/finance job and later pay, the raw gap can overstate the job effect.
• AI tools and outcomes.Better management may raise both adoption and
productivity. Learning difficulties may raise AI-tutor use and lower
scores. Direction depends on both links.
• Training and earnings.A lay-off may lower earnings and trigger
enrolment. A before/after gain may partly reflect recovery from that dip.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 32 / 97

## PDF 第 204 页

Self-selection in the wild
Wooldridge 4.1 — hypothetical applications requested by Jack
• Job choice and later pay.If ambition raises both selection into a
tech/finance job and later pay, the raw gap can overstate the job effect.
• AI tools and outcomes.Better management may raise both adoption and
productivity. Learning difficulties may raise AI-tutor use and lower
scores. Direction depends on both links.
• Training and earnings.A lay-off may lower earnings and trigger
enrolment. A before/after gain may partly reflect recovery from that dip.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 32 / 97

## PDF 第 205 页

Self-selection in the wild
Wooldridge 4.1 — hypothetical applications requested by Jack
• Job choice and later pay.If ambition raises both selection into a
tech/finance job and later pay, the raw gap can overstate the job effect.
• AI tools and outcomes.Better management may raise both adoption and
productivity. Learning difficulties may raise AI-tutor use and lower
scores. Direction depends on both links.
• Training and earnings.A lay-off may lower earnings and trigger
enrolment. A before/after gain may partly reflect recovery from that dip.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 32 / 97

## PDF 第 206 页

How an omitted variable becomes part of the
error
Wooldridge 4.1, p. 54 — the conditional mean changes when ability is omitted
FULL EQUA TION
y=β 0 +β 1educ+β 2exper+γq+v, withE(v|educ,exper,q)=0.
• Absorb unobserved ability:u=γq+v. The observed equation is
y=β 0 +β 1educ+β 2exper+u.
• Iterated expectations gives
E(u|educ,exper)=γE(q|educ,exper).
• Centeringqmakes its overall mean zero; it does not make its mean zero
within every schooling/experience group.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 33 / 97

## PDF 第 207 页

How an omitted variable becomes part of the
error
Wooldridge 4.1, p. 54 — the conditional mean changes when ability is omitted
FULL EQUA TION
y=β 0 +β 1educ+β 2exper+γq+v, withE(v|educ,exper,q)=0.
• Absorb unobserved ability:u=γq+v. The observed equation is
y=β 0 +β 1educ+β 2exper+u.
• Iterated expectations gives
E(u|educ,exper)=γE(q|educ,exper).
• Centeringqmakes its overall mean zero; it does not make its mean zero
within every schooling/experience group.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 33 / 97

## PDF 第 208 页

How an omitted variable becomes part of the
error
Wooldridge 4.1, p. 54 — the conditional mean changes when ability is omitted
FULL EQUA TION
y=β 0 +β 1educ+β 2exper+γq+v, withE(v|educ,exper,q)=0.
• Absorb unobserved ability:u=γq+v. The observed equation is
y=β 0 +β 1educ+β 2exper+u.
• Iterated expectations gives
E(u|educ,exper)=γE(q|educ,exper).
• Centeringqmakes its overall mean zero; it does not make its mean zero
within every schooling/experience group.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 33 / 97

## PDF 第 209 页

Self-selection: who picks more schooling?
Wooldridge 4.1, p. 55 — the two schooling groups differ in ability before any wage
12 years 16 years16 years, by lottery
ability (unobservedq) schooling wage
β1
abilityq
lottery
• Wage gap=return to four more years+ability gap between those who
chose them (illustrative).
• Random assignment to completed schooling equalizes the population
ability distributions and cuts the confounding arrow.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 34 / 97

## PDF 第 210 页

Self-selection: who picks more schooling?
Wooldridge 4.1, p. 55 — the two schooling groups differ in ability before any wage
12 years 16 years16 years, by lottery
ability (unobservedq) schooling wage
β1
abilityq
lottery
• Wage gap=return to four more years+ability gap between those who
chose them (illustrative).
• Random assignment to completed schooling equalizes the population
ability distributions and cuts the confounding arrow.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 34 / 97

## PDF 第 211 页

Self-selection: who picks more schooling?
Wooldridge 4.1, p. 55 — the two schooling groups differ in ability before any wage
12 years 16 years16 years, by lottery
ability (unobservedq) schooling wage
β1
abilityq
lottery
• Wage gap=return to four more years+ability gap between those who
chose them (illustrative).
• Random assignment to completed schooling equalizes the population
ability distributions and cuts the confounding arrow.
Main lecture: slide 27
ECO6102 / L3 / 3a The population model and economic interpretation App. 34 / 97

## PDF 第 212 页

Several sources can overlap
Wooldridge 4.1, p. 55 — alcohol and earnings illustrate overlapping concerns
ONE REGRESSION
Suppose we relate earnings to reported alcohol consumption.
• Omitted factors: family background or preferences may affect both
drinking and earnings.
• Measurement: reported consumption can differ from true consumption.
• Simultaneity: earnings can affect drinking choices as well as the reverse.
Naming a concern starts the argument; we still need to show how it enters
the relevant error.
Main lecture: slide 31
ECO6102 / L3 / 3a The population model and economic interpretation App. 35 / 97

## PDF 第 213 页

Solve the market and recover its slopes
Wooldridge 4.1 and 9.2.1 — solve the system; recover slopes from shifters
ILLUSTRA TIVE EQUA TIONS
Qd =12−2P+d,Q s =2P+s; equilibrium requiresQ d =Q s.
Equating the two gives 12−2P+d=2P+s, hence
P=3+ d−s
4 ,Q=6+ d+s
2 .
Demand from a supply shift
∂Q/∂s
∂P/∂s = 1/2
−1/4 =−2.
Supply from a demand shift
∂Q/∂d
∂P/∂d = 1/2
1/4 =2.
Recovery requires relevant, excluded and exogenous shifters (Lecture 6).
Back to App. 22 Main lecture: slide 33
ECO6102 / L3 / 3a The population model and economic interpretation App. 36 / 97

## PDF 第 214 页

Match the method to the policy question
Wooldridge 4.1; Nevo–Whinston (2010) — what can this evidence support?
ONE MARKET , TWO QUESTIONS
A shipping-cost subsidy has been introduced in some markets.
• Effect of the rollout: how did prices change because of this policy? We
need a credible comparison for what would otherwise have happened.
• A different policy: what would a larger subsidy do in another market?
An economic model can describe adjustment, but its behavioral and
transfer assumptions matter.
• Evidence from a credible rollout can also help identify or assess an
economic model.
Back to slide 33
ECO6102 / L3 / 3a The population model and economic interpretation App. 37 / 97

## PDF 第 215 页

Match the method to the policy question
Wooldridge 4.1; Nevo–Whinston (2010) — what can this evidence support?
ONE MARKET , TWO QUESTIONS
A shipping-cost subsidy has been introduced in some markets.
• Effect of the rollout: how did prices change because of this policy? We
need a credible comparison for what would otherwise have happened.
• A different policy: what would a larger subsidy do in another market?
An economic model can describe adjustment, but its behavioral and
transfer assumptions matter.
• Evidence from a credible rollout can also help identify or assess an
economic model.
Back to slide 33
ECO6102 / L3 / 3a The population model and economic interpretation App. 37 / 97

## PDF 第 216 页

Structural and reduced-form research:
readings
Optional perspectives on the research approaches introduced beside Wooldridge 4.1
• Angrist and Pischke (2010): The Credibility Revolution
Why credible research design matters.
• Nevo and Whinston (2010): Taking the Dogma out of Econometrics
Structural models, credible inference and counterfactuals.
• Abadie and Cattaneo (2018): Econometric Methods for Program
Evaluation
Begin at p. 466, footnote 1: different uses of “reduced form”.
Back to slide 33
ECO6102 / L3 / 3a The population model and economic interpretation App. 38 / 97

## PDF 第 217 页

Appendix roadmap
APPENDIX C · Wooldridge 4.2.1–4.2.2 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a OLS calculations and estimator properties

## PDF 第 218 页

The vector form with real observations
Wooldridge 4.2, illustration of (4.6) — rows are students; columns are regressors
A TTENDANCE EQUA TION
stndfnli =β 0 +β 1atndrtei +u i.
• One row isx i =(1,atndrte i), sox iβ=β 0 +β 1atndrtei.
• Three observed rows illustrate the matrix layout:
X=


1 100.0
1 93.8
1 84.4

 ,Y=


2.57
.68
.05

 ,β=
 
β0
β1
!
.
• HereK=2: the constant and attendance. Estimation uses all observations
in the chosen sample.
Back to slide 34 Back to contents
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 39 / 97

## PDF 第 219 页

The vector form with real observations
Wooldridge 4.2, illustration of (4.6) — rows are students; columns are regressors
A TTENDANCE EQUA TION
stndfnli =β 0 +β 1atndrtei +u i.
• One row isx i =(1,atndrte i), sox iβ=β 0 +β 1atndrtei.
• Three observed rows illustrate the matrix layout:
X=


1 100.0
1 93.8
1 84.4

 ,Y=


2.57
.68
.05

 ,β=
 
β0
β1
!
.
• HereK=2: the constant and attendance. Estimation uses all observations
in the chosen sample.
Back to slide 34 Back to contents
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 39 / 97

## PDF 第 220 页

The identified population coefficient
Wooldridge 4.2.1, p. 57 — orthogonality plus rank gives one solution
TWO ASSUMPTIONS
OLS.1:E(x ′u)=0; OLS.2:E(x ′x)has full rankK.
• Multiplyingy=xβ+ubyx ′ and taking expectations gives
E(x′y)=E(x ′x)β.
• OLS.2 allows us to solve:
β=[E(x ′x)]−1E(x′y).
This is a population result. Its interpretation depends on the equation and
orthogonality assumptions we justified.
Back to slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 40 / 97

## PDF 第 221 页

The identified population coefficient
Wooldridge 4.2.1, p. 57 — orthogonality plus rank gives one solution
TWO ASSUMPTIONS
OLS.1:E(x ′u)=0; OLS.2:E(x ′x)has full rankK.
• Multiplyingy=xβ+ubyx ′ and taking expectations gives
E(x′y)=E(x ′x)β.
• OLS.2 allows us to solve:
β=[E(x ′x)]−1E(x′y).
This is a population result. Its interpretation depends on the equation and
orthogonality assumptions we justified.
Back to slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 40 / 97

## PDF 第 222 页

The OLS estimator
Wooldridge 4.2.1, p. 57 — the sample analogue of the identifiedβ
• Replacing the population expectations with sample averages gives the
ordinary least squares (OLS) estimator
ˆβ=


1
N
NX
i=1
x′
ixi


−1 

1
N
NX
i=1
x′
iyi

 =(X ′X)−1X′Y.
• It minimises P
i(yi −x ib)2, which is where the name comes from; the
moment equations are its first-order conditions.
• ˆβis random: its value depends on the sample, which is random. How can
we tell whether it is a good estimator ofβ?
Back to slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 41 / 97

## PDF 第 223 页

The OLS estimator
Wooldridge 4.2.1, p. 57 — the sample analogue of the identifiedβ
• Replacing the population expectations with sample averages gives the
ordinary least squares (OLS) estimator
ˆβ=


1
N
NX
i=1
x′
ixi


−1 

1
N
NX
i=1
x′
iyi

 =(X ′X)−1X′Y.
• It minimises P
i(yi −x ib)2, which is where the name comes from; the
moment equations are its first-order conditions.
• ˆβis random: its value depends on the sample, which is random. How can
we tell whether it is a good estimator ofβ?
Back to slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 41 / 97

## PDF 第 224 页

Why the OLS slope is consistent
Wooldridge 4.2.1, Theorem 4.1 — a sample covariance divided by a sample variance
Consistency:plim ˆβj =β j.
SCALAR MODEL
yi =β 0 +β 1xi +u i; i.i.d. sampling, finite second moments,E(u)=0,Cov(x,u)=0,
andVar(x)>0.
ˆβ1 −β 1 = N−1 P
i(xi − ¯x)(ui − ¯u)
N−1 P
i(xi − ¯x)2
p
− →Cov(x,u)
Var(x) =0.
• LLN: sample moments approach population moments.
• Orthogonality: zero numerator. Rank: positive denominator.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 42 / 97

## PDF 第 225 页

Why the OLS slope is consistent
Wooldridge 4.2.1, Theorem 4.1 — a sample covariance divided by a sample variance
Consistency:plim ˆβj =β j.
SCALAR MODEL
yi =β 0 +β 1xi +u i; i.i.d. sampling, finite second moments,E(u)=0,Cov(x,u)=0,
andVar(x)>0.
ˆβ1 −β 1 = N−1 P
i(xi − ¯x)(ui − ¯u)
N−1 P
i(xi − ¯x)2
p
− →Cov(x,u)
Var(x) =0.
• LLN: sample moments approach population moments.
• Orthogonality: zero numerator. Rank: positive denominator.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 42 / 97

## PDF 第 226 页

The slope as a covariance ratio
Wooldridge 4.2.1 — a sample identity becomes a population limit
Simple regression with an intercept:y i =β 0 +β 1xi +u i.
Sab =N −1 P
i(ai − ¯a)(bi − ¯b); the fitted sample hasS xx >0.
Fitted slope
ˆβ1 =S xy/Sxx
= Target
β1
+ Sample contribution
Sxu/Sxx
I.i.d. sampling, finite second moments, andVar(x)>0: LLN gives
plim ˆβ1 =β 1 + Cov(x,u)
Var(x) .
IfCov(x,u)=0, the limit isβ 1; sampleS xu need not be zero.
Back to slide 5
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 43 / 97

## PDF 第 227 页

The slope as a covariance ratio
Wooldridge 4.2.1 — a sample identity becomes a population limit
Simple regression with an intercept:y i =β 0 +β 1xi +u i.
Sab =N −1 P
i(ai − ¯a)(bi − ¯b); the fitted sample hasS xx >0.
Fitted slope
ˆβ1 =S xy/Sxx
= Target
β1
+ Sample contribution
Sxu/Sxx
I.i.d. sampling, finite second moments, andVar(x)>0: LLN gives
plim ˆβ1 =β 1 + Cov(x,u)
Var(x) .
IfCov(x,u)=0, the limit isβ 1; sampleS xu need not be zero.
Back to slide 5
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 43 / 97

## PDF 第 228 页

When is OLS also unbiased?
Wooldridge 4.2.1, p. 58 and Problem 4.2 — condition on the observed regressor matrix
Unbiasedness:E( ˆβ)=βat a fixedN.
• Addzero conditional meanto random sampling:E(u i |x i)=0 gives
E(u|X)=0.
• With full sample rank, the regression weights are fixed after conditioning
onX:
E( ˆβ|X)=β+(X ′X)−1X′E(u|X)=β.
• If the expectation exists, thelaw of iterated expectationsgives
E( ˆβ)=E{E( ˆβ|X)}=E(β)=β.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 44 / 97

## PDF 第 229 页

When is OLS also unbiased?
Wooldridge 4.2.1, p. 58 and Problem 4.2 — condition on the observed regressor matrix
Unbiasedness:E( ˆβ)=βat a fixedN.
• Addzero conditional meanto random sampling:E(u i |x i)=0 gives
E(u|X)=0.
• With full sample rank, the regression weights are fixed after conditioning
onX:
E( ˆβ|X)=β+(X ′X)−1X′E(u|X)=β.
• If the expectation exists, thelaw of iterated expectationsgives
E( ˆβ)=E{E( ˆβ|X)}=E(β)=β.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 44 / 97

## PDF 第 230 页

OLS first-order conditions
Wooldridge 4.2.1, p. 57 — minimise the squared residuals; the sample moment
equations
• One regressor: choose(b 0,b 1)to minimise P
i(yi −b 0 −b 1xi)2. The two
derivatives set to zero:X
i
(yi − ˆβ0 − ˆβ1xi)=0,
X
i
xi(yi − ˆβ0 − ˆβ1xi)=0:
that is P
i ˆui =0 and P
i xi ˆui =0.
• Solving: ˆβ0 = ¯y− ˆβ1 ¯xand ˆβ1 = P
i(xi − ¯x)(yi − ¯y)/P
i(xi − ¯x)2; these also solve
the sample moment equations.
• Kregressors: minimise(Y−Xb) ′(Y−Xb); the conditionX ′(Y−X ˆβ)=0
gives ˆβ=(X ′X)−1X′Y: one orthogonality per column ofX.
Back to slide 4 Back to slide 5 Back to slide 20 Main lecture: slide 6
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 45 / 97

## PDF 第 231 页

OLS first-order conditions
Wooldridge 4.2.1, p. 57 — minimise the squared residuals; the sample moment
equations
• One regressor: choose(b 0,b 1)to minimise P
i(yi −b 0 −b 1xi)2. The two
derivatives set to zero:X
i
(yi − ˆβ0 − ˆβ1xi)=0,
X
i
xi(yi − ˆβ0 − ˆβ1xi)=0:
that is P
i ˆui =0 and P
i xi ˆui =0.
• Solving: ˆβ0 = ¯y− ˆβ1 ¯xand ˆβ1 = P
i(xi − ¯x)(yi − ¯y)/P
i(xi − ¯x)2; these also solve
the sample moment equations.
• Kregressors: minimise(Y−Xb) ′(Y−Xb); the conditionX ′(Y−X ˆβ)=0
gives ˆβ=(X ′X)−1X′Y: one orthogonality per column ofX.
Back to slide 4 Back to slide 5 Back to slide 20 Main lecture: slide 6
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 45 / 97

## PDF 第 232 页

OLS first-order conditions
Wooldridge 4.2.1, p. 57 — minimise the squared residuals; the sample moment
equations
• One regressor: choose(b 0,b 1)to minimise P
i(yi −b 0 −b 1xi)2. The two
derivatives set to zero:X
i
(yi − ˆβ0 − ˆβ1xi)=0,
X
i
xi(yi − ˆβ0 − ˆβ1xi)=0:
that is P
i ˆui =0 and P
i xi ˆui =0.
• Solving: ˆβ0 = ¯y− ˆβ1 ¯xand ˆβ1 = P
i(xi − ¯x)(yi − ¯y)/P
i(xi − ¯x)2; these also solve
the sample moment equations.
• Kregressors: minimise(Y−Xb) ′(Y−Xb); the conditionX ′(Y−X ˆβ)=0
gives ˆβ=(X ′X)−1X′Y: one orthogonality per column ofX.
Back to slide 4 Back to slide 5 Back to slide 20 Main lecture: slide 6
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 45 / 97

## PDF 第 233 页

Read the coefficient in its units
Wooldridge 4.2.1 — the ATTEND fitted line, interpreted
[stndfnl=−.6345+.00813atndrte.
• Attendance is measured in percentage points; the final score is
standardized.
• Ten more attendance percentage points go with about.00813×10=.0813
standard deviations of score.
• This is a descriptive association. Motivation or prior preparation could
affect both attendance and scores.
Population slope formula
Main lecture: slide 8
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 46 / 97

## PDF 第 234 页

Identification with one regressor
Wooldridge 4.2.1 — the scalar projection formula
POPULA TION MODEL
y=β 0 +β 1x+u,E(u)=0,Cov(x,u)=0,Var(x)>0.
β1 = Cov(x,y)
Var(x) , β 0 =E(y)−β 1E(x).
• The slope scales population co-movement by the variation inx.
• In the ATTEND empirical pool, the projection is−.6345+.00813atndrte.
• This pool projection is the known target of the resampling demonstration,
not a known causal effect.
Back to App. 46 Main lecture: slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 47 / 97

## PDF 第 235 页

Think first: we do not have the population
Wooldridge 4.2.1 — from a formula in population moments to a formula in data
IDENTIFIED
β=[E(x ′x)]−1E(x′y)
• We observe an i.i.d. random sample{(x i,y i) :i=1, . . . ,N}, not the
population.
Main lecture: slide 38
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 48 / 97

## PDF 第 236 页

Method of moments with one regressor
Wooldridge 4.2.1 — replace each population moment by its sample counterpart
POPULA TION RESTRICTIONS
u=y−β 0 −β 1x;E(u)=0 andE(xu)=0.
• Replace expectations by averages and solveX
i
(yi − ˆβ0 − ˆβ1xi)=0,
X
i
xi(yi − ˆβ0 − ˆβ1xi)=0.
• The solution is the familiar OLS formula:
ˆβ1 =
P
i(xi − ¯x)(yi − ¯y)P
i(xi − ¯x)2 , ˆβ0 = ¯y− ˆβ1 ¯x.
Main lecture: slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 49 / 97

## PDF 第 237 页

Why the moment equations identify the
coefficients
Wooldridge 4.2.1 — observable population moments and a unique solution
MODEL AND MOMENTS
y=xβ+u,E(x ′u)=0,A=E(x ′x)nonsingular.
• Multiply byx ′ and take expectations:
E(x′y)=E(x ′x)β+E(x ′u)=Aβ.
• Henceβ=A −1E(x′y), a function of population moments of observables.
• Ifβandβ ∗ both solve the equations,A(β−β ∗)=0implies equality.
Without rank, uniqueness can fail.
Main lecture: slide 38
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 50 / 97

## PDF 第 238 页

Why the moment equations identify the
coefficients
Wooldridge 4.2.1 — observable population moments and a unique solution
MODEL AND MOMENTS
y=xβ+u,E(x ′u)=0,A=E(x ′x)nonsingular.
• Multiply byx ′ and take expectations:
E(x′y)=E(x ′x)β+E(x ′u)=Aβ.
• Henceβ=A −1E(x′y), a function of population moments of observables.
• Ifβandβ ∗ both solve the equations,A(β−β ∗)=0implies equality.
Without rank, uniqueness can fail.
Main lecture: slide 38
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 50 / 97

## PDF 第 239 页

Why the moment equations identify the
coefficients
Wooldridge 4.2.1 — observable population moments and a unique solution
MODEL AND MOMENTS
y=xβ+u,E(x ′u)=0,A=E(x ′x)nonsingular.
• Multiply byx ′ and take expectations:
E(x′y)=E(x ′x)β+E(x ′u)=Aβ.
• Henceβ=A −1E(x′y), a function of population moments of observables.
• Ifβandβ ∗ both solve the equations,A(β−β ∗)=0implies equality.
Without rank, uniqueness can fail.
Main lecture: slide 38
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 50 / 97

## PDF 第 240 页

Assumption versus sample identity
Wooldridge 4.1–4.2.1 — no hats in the population; hats and subscripts in the sample
Population(fixed, unknown)Sample(computed, random)
Parameters β0, . . . , βp ˆβ0, . . . , ˆβp
Line E(y|x)=xβ(under (4.3)) fitted ˆyi =x i ˆβ
Deviation erroru=y−xβresidual ˆui =y i − ˆyi
Orthogonality E(u)=0,E(x ju)=0: assumed P
i ˆui =0, P
i xij ˆui =0: always true
The last row: the sample identities hold by construction for any data, so they can
never test the population assumption.
Back to slide 36
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 51 / 97

## PDF 第 241 页

Assumption versus sample identity
Wooldridge 4.1–4.2.1 — no hats in the population; hats and subscripts in the sample
Population(fixed, unknown)Sample(computed, random)
Parameters β0, . . . , βp ˆβ0, . . . , ˆβp
Line E(y|x)=xβ(under (4.3)) fitted ˆyi =x i ˆβ
Deviation erroru=y−xβresidual ˆui =y i − ˆyi
Orthogonality E(u)=0,E(x ju)=0: assumed P
i ˆui =0, P
i xij ˆui =0: always true
The last row: the sample identities hold by construction for any data, so they can
never test the population assumption.
Back to slide 36
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 51 / 97

## PDF 第 242 页

Assumption versus sample identity
Wooldridge 4.1–4.2.1 — no hats in the population; hats and subscripts in the sample
Population(fixed, unknown)Sample(computed, random)
Parameters β0, . . . , βp ˆβ0, . . . , ˆβp
Line E(y|x)=xβ(under (4.3)) fitted ˆyi =x i ˆβ
Deviation erroru=y−xβresidual ˆui =y i − ˆyi
Orthogonality E(u)=0,E(x ju)=0: assumed P
i ˆui =0, P
i xij ˆui =0: always true
The last row: the sample identities hold by construction for any data, so they can
never test the population assumption.
Back to slide 36
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 51 / 97

## PDF 第 243 页

Assumption versus sample identity
Wooldridge 4.1–4.2.1 — no hats in the population; hats and subscripts in the sample
Population(fixed, unknown)Sample(computed, random)
Parameters β0, . . . , βp ˆβ0, . . . , ˆβp
Line E(y|x)=xβ(under (4.3)) fitted ˆyi =x i ˆβ
Deviation erroru=y−xβresidual ˆui =y i − ˆyi
Orthogonality E(u)=0,E(x ju)=0: assumed P
i ˆui =0, P
i xij ˆui =0: always true
The last row: the sample identities hold by construction for any data, so they can
never test the population assumption.
Back to slide 36
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 51 / 97

## PDF 第 244 页

When OLS.2 fails
Wooldridge pp. 57 and 60 — exact linear dependence; why the constant matters
• The book’s examples(p. 57): every category dummy plus the constant;
log(age)withlog(age 2)=2log(age): improper specification (drop one).
• Exact versus high: only anexactrelation fails OLS.2; correlation at .95
does not by itself violate OLS.2.
• Why the constant matters: withx=(1,z),zthe nonconstant regressors,
E(x′x)=
 
1E(z)
E(z)′ E(z′z)
!
,E(z ′z)−E(z) ′E(z)=Var(z),
sorankE(x ′x)=K⇔Var(z)nonsingular (p. 57); the variance of the fullx
is always singular.
Back to slide 37
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 52 / 97

## PDF 第 245 页

When OLS.2 fails
Wooldridge pp. 57 and 60 — exact linear dependence; why the constant matters
• The book’s examples(p. 57): every category dummy plus the constant;
log(age)withlog(age 2)=2log(age): improper specification (drop one).
• Exact versus high: only anexactrelation fails OLS.2; correlation at .95
does not by itself violate OLS.2.
• Why the constant matters: withx=(1,z),zthe nonconstant regressors,
E(x′x)=
 
1E(z)
E(z)′ E(z′z)
!
,E(z ′z)−E(z) ′E(z)=Var(z),
sorankE(x ′x)=K⇔Var(z)nonsingular (p. 57); the variance of the fullx
is always singular.
Back to slide 37
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 52 / 97

## PDF 第 246 页

When OLS.2 fails
Wooldridge pp. 57 and 60 — exact linear dependence; why the constant matters
• The book’s examples(p. 57): every category dummy plus the constant;
log(age)withlog(age 2)=2log(age): improper specification (drop one).
• Exact versus high: only anexactrelation fails OLS.2; correlation at .95
does not by itself violate OLS.2.
• Why the constant matters: withx=(1,z),zthe nonconstant regressors,
E(x′x)=
 
1E(z)
E(z)′ E(z′z)
!
,E(z ′z)−E(z) ′E(z)=Var(z),
sorankE(x ′x)=K⇔Var(z)nonsingular (p. 57); the variance of the fullx
is always singular.
Back to slide 37
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 52 / 97

## PDF 第 247 页

OLS equals the target plus sampling error
Wooldridge 4.2.1, p. 57 — the identity both theorems of this chapter use
ˆβ=β+


1
N
NX
i=1
x′
ixi


−1 

1
N
NX
i=1
x′
iui


|                           {z                           }
sample average ofx ′
i ui, rescaled
• Substitutey i =x iβ+u i into the OLS formula and simplify.
• The rightmost bracket is a sample average of the population object whose
mean OLS.1 sets to zero. Its probability limit is the key to consistency.
Main lecture: slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 53 / 97

## PDF 第 248 页

OLS equals the target plus sampling error
Wooldridge 4.2.1, p. 57 — the identity both theorems of this chapter use
ˆβ=β+


1
N
NX
i=1
x′
ixi


−1 

1
N
NX
i=1
x′
iui


|                           {z                           }
sample average ofx ′
i ui, rescaled
• Substitutey i =x iβ+u i into the OLS formula and simplify.
• The rightmost bracket is a sample average of the population object whose
mean OLS.1 sets to zero. Its probability limit is the key to consistency.
Main lecture: slide 39
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 53 / 97

## PDF 第 249 页

Why: the plim passes through
Wooldridge 3.2, 3.4, p. 58 — proof of Theorem 4.1: two sample averages, two limits
OLS IDENTITY
ˆβ=β+
h 1
N
P
i x′
ixi
i−1h 1
N
P
i x′
iui
i
• Law of large numbers(Theorem 3.1): i.i.d. sample averages converge to
population means: 1
N
P
i x′
ixi
p
− →E(x′x), 1
N
P
i x′
iui
p
− →E(x′u)=0(OLS.1).
• Slutsky(Lemma 3.4): plims pass through continuous functions; inversion
is continuous under OLS.2. So the product→[E(x ′x)]−10=0.
• For everyϵ >0, consistency meansPr(∥ ˆβ−β∥> ϵ)→0. Henceplim ˆβ=β:
OLS consistently estimates the linear projection ofyonx, whateveryis,
and the conditional mean when that is linear.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 54 / 97

## PDF 第 250 页

Why: the plim passes through
Wooldridge 3.2, 3.4, p. 58 — proof of Theorem 4.1: two sample averages, two limits
OLS IDENTITY
ˆβ=β+
h 1
N
P
i x′
ixi
i−1h 1
N
P
i x′
iui
i
• Law of large numbers(Theorem 3.1): i.i.d. sample averages converge to
population means: 1
N
P
i x′
ixi
p
− →E(x′x), 1
N
P
i x′
iui
p
− →E(x′u)=0(OLS.1).
• Slutsky(Lemma 3.4): plims pass through continuous functions; inversion
is continuous under OLS.2. So the product→[E(x ′x)]−10=0.
• For everyϵ >0, consistency meansPr(∥ ˆβ−β∥> ϵ)→0. Henceplim ˆβ=β:
OLS consistently estimates the linear projection ofyonx, whateveryis,
and the conditional mean when that is linear.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 54 / 97

## PDF 第 251 页

Why: the plim passes through
Wooldridge 3.2, 3.4, p. 58 — proof of Theorem 4.1: two sample averages, two limits
OLS IDENTITY
ˆβ=β+
h 1
N
P
i x′
ixi
i−1h 1
N
P
i x′
iui
i
• Law of large numbers(Theorem 3.1): i.i.d. sample averages converge to
population means: 1
N
P
i x′
ixi
p
− →E(x′x), 1
N
P
i x′
iui
p
− →E(x′u)=0(OLS.1).
• Slutsky(Lemma 3.4): plims pass through continuous functions; inversion
is continuous under OLS.2. So the product→[E(x ′x)]−10=0.
• For everyϵ >0, consistency meansPr(∥ ˆβ−β∥> ϵ)→0. Henceplim ˆβ=β:
OLS consistently estimates the linear projection ofyonx, whateveryis,
and the conditional mean when that is linear.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 54 / 97

## PDF 第 252 页

What Theorem 4.1 does not say
Wooldridge 4.2.1, p. 58 — not causality, not unbiasedness, not accuracy at yourN
• It does not sayβis the parameter you want. If the regressor you care
about is endogenous, OLS.1 fails for the structuralβand OLS converges
to something else (3b).
• It does not sayE( ˆβ)=βat any finiteN. Under OLS.1–OLS.2 alone the
estimator is not necessarily unbiased.
• It does not say how close you are withN=20. The histogram atN=20
had samples with a negative slope.
• It does not assumeuindependent ofx: neither constant conditional
variance nor the weaker OLS.3 restriction is needed for consistency.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 55 / 97

## PDF 第 253 页

What Theorem 4.1 does not say
Wooldridge 4.2.1, p. 58 — not causality, not unbiasedness, not accuracy at yourN
• It does not sayβis the parameter you want. If the regressor you care
about is endogenous, OLS.1 fails for the structuralβand OLS converges
to something else (3b).
• It does not sayE( ˆβ)=βat any finiteN. Under OLS.1–OLS.2 alone the
estimator is not necessarily unbiased.
• It does not say how close you are withN=20. The histogram atN=20
had samples with a negative slope.
• It does not assumeuindependent ofx: neither constant conditional
variance nor the weaker OLS.3 restriction is needed for consistency.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 55 / 97

## PDF 第 254 页

What Theorem 4.1 does not say
Wooldridge 4.2.1, p. 58 — not causality, not unbiasedness, not accuracy at yourN
• It does not sayβis the parameter you want. If the regressor you care
about is endogenous, OLS.1 fails for the structuralβand OLS converges
to something else (3b).
• It does not sayE( ˆβ)=βat any finiteN. Under OLS.1–OLS.2 alone the
estimator is not necessarily unbiased.
• It does not say how close you are withN=20. The histogram atN=20
had samples with a negative slope.
• It does not assumeuindependent ofx: neither constant conditional
variance nor the weaker OLS.3 restriction is needed for consistency.
Main lecture: slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 55 / 97

## PDF 第 255 页

Unbiasedness and consistency
Wooldridge 3.5.1; 4.2.1 — centering and concentration answer different questions
OLS with an intercept: maintain the linear model and i.i.d. sampling.
Unbiasedness Consistency
MeaningE( ˆβ1)=β 1
at a fixedN
P(| ˆβ1 −β 1|> ϵ)→0
for everyϵ >0 asN→ ∞
Condition 4:E(u|x)=0 4 ′ :E(u)=0 andCov(x,u)=0
Also
require
Full sample rank;
E( ˆβ1)exists.
Population rank;
finite second moments.
These are sufficient OLS routes. With an intercept, 4′ is OLS.1; 4⇒4 ′.
Neither property alone supplies a normal ortreference distribution.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 56 / 97

## PDF 第 256 页

Unbiasedness and consistency
Wooldridge 3.5.1; 4.2.1 — centering and concentration answer different questions
OLS with an intercept: maintain the linear model and i.i.d. sampling.
Unbiasedness Consistency
MeaningE( ˆβ1)=β 1
at a fixedN
P(| ˆβ1 −β 1|> ϵ)→0
for everyϵ >0 asN→ ∞
Condition 4:E(u|x)=0 4 ′ :E(u)=0 andCov(x,u)=0
Also
require
Full sample rank;
E( ˆβ1)exists.
Population rank;
finite second moments.
These are sufficient OLS routes. With an intercept, 4′ is OLS.1; 4⇒4 ′.
Neither property alone supplies a normal ortreference distribution.
Back to slide 40
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 56 / 97

## PDF 第 257 页

Unbiasedness under zero conditional mean
Wooldridge p. 58, Problem 4.2 — the introductory finite-sample result, in matrix form
• From the OLS error identity, ˆβ=β+(X ′X)−1X′u. Under random sampling,
E(ui |X)=E(u i |x i), soE(u|x)=0 givesE(u|X)=0and
E( ˆβ|X)=β+(X ′X)−1X′E(u|X)=βwheneverX ′Xis nonsingular.
If the expectation exists,E( ˆβ)=βby iterated expectations (L2). Adding
Var(u|x)=σ 2 givesVar( ˆβ|X)=σ 2(X′X)−1.
Back to slide 16 Back to slide 17
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 57 / 97

## PDF 第 258 页

Unbiasedness with one regressor
Wooldridge p. 58, Problem 4.2 — the same result with one regressor
MODEL
yi =β 0 +β 1xi +u i,E(u i |X)=0
• One regressor(the undergraduate proof): withw i =(x i − ¯x)/P
j(xj − ¯x)2,
ˆβ1 =β 1 +
X
i
wiui,E( ˆβ1 |X)=β 1 +
X
i
wiE(ui |X)=β 1.
Main lecture: slide 17
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 58 / 97

## PDF 第 259 页

Why zero correlation is not enough
Wooldridge Problem 4.3 — and why OLS.3 is written withE(u 2x′x)
• Why the zero-correlation version does not deliver this(Problem 4.3):
with onlyE(x ′u)=0,E(u|X)need not be zero, so the conditional mean of
ˆβneed not equalβ; andVar(u|x)=σ 2 then no longer implies
E(u2 |x)=σ 2, sinceE(u 2 |x)=σ 2 +[E(u|x)] 2.
Main lecture: slide 17
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 59 / 97

## PDF 第 260 页

SLR assumptions versus OLS.1–3
Wooldridge 4.1–4.2.2 — random sampling stays; population moments replace SLR.4–5
• SLR.1–3: one regressor is a special case; random sampling stays. OLS.2
requires population rank, not just variation in this sample.
• SLR.4:E(u|x)=0 implies OLS.1,E(x ′u)=0. The converse need not hold.
• SLR.4–5: zero conditional mean and constant conditional variance imply
OLS.3,
E(u2x′x)=σ 2E(x′x).
Main lecture: slide 43
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 60 / 97

## PDF 第 261 页

SLR assumptions versus OLS.1–3
Wooldridge 4.1–4.2.2 — random sampling stays; population moments replace SLR.4–5
• SLR.1–3: one regressor is a special case; random sampling stays. OLS.2
requires population rank, not just variation in this sample.
• SLR.4:E(u|x)=0 implies OLS.1,E(x ′u)=0. The converse need not hold.
• SLR.4–5: zero conditional mean and constant conditional variance imply
OLS.3,
E(u2x′x)=σ 2E(x′x).
Main lecture: slide 43
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 60 / 97

## PDF 第 262 页

SLR assumptions versus OLS.1–3
Wooldridge 4.1–4.2.2 — random sampling stays; population moments replace SLR.4–5
• SLR.1–3: one regressor is a special case; random sampling stays. OLS.2
requires population rank, not just variation in this sample.
• SLR.4:E(u|x)=0 implies OLS.1,E(x ′u)=0. The converse need not hold.
• SLR.4–5: zero conditional mean and constant conditional variance imply
OLS.3,
E(u2x′x)=σ 2E(x′x).
Main lecture: slide 43
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 60 / 97

## PDF 第 263 页

Where the root-N equation comes from
Wooldridge 4.2.2, p. 59 — rescale the exact OLS identity
POPULA TION MOMENTS
A=E(x ′x)is nonsingular;B=E(u 2x′x), (4.7), is finite.
√
N( ˆβ−β)=
h
1
N
P
i x′
ixi
i−1h
1√
N
P
i x′
iui
i
.
• Exact identity: multiply the OLS error identity by
√
N.
• Under i.i.d. sampling and OLS.1,Var(N −1/2 P
i x′
iui)=B: the spread stays
finite.
• The inverse isA −1 +o p(1); the sum isO p(1). Their remainder iso p(1)
(Lemma 3.2).
Back to slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 61 / 97

## PDF 第 264 页

Where the root-N equation comes from
Wooldridge 4.2.2, p. 59 — rescale the exact OLS identity
POPULA TION MOMENTS
A=E(x ′x)is nonsingular;B=E(u 2x′x), (4.7), is finite.
√
N( ˆβ−β)=
h
1
N
P
i x′
ixi
i−1h
1√
N
P
i x′
iui
i
.
• Exact identity: multiply the OLS error identity by
√
N.
• Under i.i.d. sampling and OLS.1,Var(N −1/2 P
i x′
iui)=B: the spread stays
finite.
• The inverse isA −1 +o p(1); the sum isO p(1). Their remainder iso p(1)
(Lemma 3.2).
Back to slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 61 / 97

## PDF 第 265 页

Where the root-N equation comes from
Wooldridge 4.2.2, p. 59 — rescale the exact OLS identity
POPULA TION MOMENTS
A=E(x ′x)is nonsingular;B=E(u 2x′x), (4.7), is finite.
√
N( ˆβ−β)=
h
1
N
P
i x′
ixi
i−1h
1√
N
P
i x′
iui
i
.
• Exact identity: multiply the OLS error identity by
√
N.
• Under i.i.d. sampling and OLS.1,Var(N −1/2 P
i x′
iui)=B: the spread stays
finite.
• The inverse isA −1 +o p(1); the sum isO p(1). Their remainder iso p(1)
(Lemma 3.2).
Back to slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 61 / 97

## PDF 第 266 页

Proof of Theorem 4.2
Wooldridge 4.2.2, p. 59 — CLT, Slutsky, then the OLS.3 simplification
POPULA TION MOMENTS
A=E(x ′x)nonsingular;B=E(u 2x′x)finite.
• CLT: i.i.d. sampling and OLS.1 giveN −1/2 P
i x′
iui
d
− →N(0,B).
• Slutsky: the inverse sample moment converges toA −1, hence
√
N( ˆβ−β)
d
− →N(0,V),V=A −1BA−1.
• OLS.3:B=σ 2A, soV=σ 2A−1. Otherwise retain the sandwich.
• Vis the limiting variance of the rescaled estimator;V/Napproximates
Var(ˆβ).
Back to slide 43 Main lecture: slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 62 / 97

## PDF 第 267 页

Proof of Theorem 4.2
Wooldridge 4.2.2, p. 59 — CLT, Slutsky, then the OLS.3 simplification
POPULA TION MOMENTS
A=E(x ′x)nonsingular;B=E(u 2x′x)finite.
• CLT: i.i.d. sampling and OLS.1 giveN −1/2 P
i x′
iui
d
− →N(0,B).
• Slutsky: the inverse sample moment converges toA −1, hence
√
N( ˆβ−β)
d
− →N(0,V),V=A −1BA−1.
• OLS.3:B=σ 2A, soV=σ 2A−1. Otherwise retain the sandwich.
• Vis the limiting variance of the rescaled estimator;V/Napproximates
Var(ˆβ).
Back to slide 43 Main lecture: slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 62 / 97

## PDF 第 268 页

Proof of Theorem 4.2
Wooldridge 4.2.2, p. 59 — CLT, Slutsky, then the OLS.3 simplification
POPULA TION MOMENTS
A=E(x ′x)nonsingular;B=E(u 2x′x)finite.
• CLT: i.i.d. sampling and OLS.1 giveN −1/2 P
i x′
iui
d
− →N(0,B).
• Slutsky: the inverse sample moment converges toA −1, hence
√
N( ˆβ−β)
d
− →N(0,V),V=A −1BA−1.
• OLS.3:B=σ 2A, soV=σ 2A−1. Otherwise retain the sandwich.
• Vis the limiting variance of the rescaled estimator;V/Napproximates
Var(ˆβ).
Back to slide 43 Main lecture: slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 62 / 97

## PDF 第 269 页

Proof of Theorem 4.2
Wooldridge 4.2.2, p. 59 — CLT, Slutsky, then the OLS.3 simplification
POPULA TION MOMENTS
A=E(x ′x)nonsingular;B=E(u 2x′x)finite.
• CLT: i.i.d. sampling and OLS.1 giveN −1/2 P
i x′
iui
d
− →N(0,B).
• Slutsky: the inverse sample moment converges toA −1, hence
√
N( ˆβ−β)
d
− →N(0,V),V=A −1BA−1.
• OLS.3:B=σ 2A, soV=σ 2A−1. Otherwise retain the sandwich.
• Vis the limiting variance of the rescaled estimator;V/Napproximates
Var(ˆβ).
Back to slide 43 Main lecture: slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 62 / 97

## PDF 第 270 页

The bell appears
Wooldridge 3.5.1, Def. 3.9 —
√
N( ˆβ1 −β 1)atN=20,100,500: the spread settles
−0.1 0 0.1 0.2
0
50
100
150
samples
N=20: SD .067
−0.1 0 0.1 0.2
0
50
100
150
N=100: SD .057
−0.1 0 0.1 0.2
0
50
100
150
N=500: SD .057
After scaling by
√
N, the SD settles near .0552.
Main lecture: slide 42
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 63 / 97

## PDF 第 271 页

Standard errors
Wooldridge 4.2.3, (4.11); Definition 3.10 — an SE estimates sampling SD
A standard error estimates sampling spread.
0 0.005 0.01 0.015 0.02
0
100
200
SD .0025
OLS slope from a sample of 500
samples
• Astandard error (SE)
estimates how much the
coefficient estimate varies
across samples.
• One draw of 500: ˆβ1 =.0080,
robustse=.0025.
• The 1,000-draw pile has SD
.0025: the SE estimates its
width.
Back to slide 46
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 64 / 97

## PDF 第 272 页

Standard errors
Wooldridge 4.2.3, (4.11); Definition 3.10 — an SE estimates sampling SD
A standard error estimates sampling spread.
0 0.005 0.01 0.015 0.02
0
100
200
SD .0025
OLS slope from a sample of 500
samples
• Astandard error (SE)
estimates how much the
coefficient estimate varies
across samples.
• One draw of 500: ˆβ1 =.0080,
robustse=.0025.
• The 1,000-draw pile has SD
.0025: the SE estimates its
width.
Back to slide 46
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 64 / 97

## PDF 第 273 页

OLS.3 element by element
Wooldridge 4.2.2, p. 59 — withK=2, three scalar statements aboutu 2
• Withx=(1,x):E(u 2x′x)=
 
E(u2)E(u 2x)
E(u2x)E(u 2x2)
!
andσ 2E(x′x)=σ 2
 
1E(x)
E(x)E(x 2)
!
.
• (1,1)definesσ 2 =E(u 2);(1,2)saysCov(u 2,x)=0;(2,2)saysCov(u 2,x 2)=0;
in general(j,k)saysCov(u 2,x jxk)=0.
• LIE: a sufficient condition: ifE(u 2 |x)=σ 2, then
E(u2xjxk)=E[x jxkE(u2 |x)]=σ 2E(xjxk)for every(j,k); it fixes a whole
conditional moment, OLS.3 onlyK(K+1)/2 covariances.
• Second moment versus variance:Var(u|x)=E(u 2 |x)−[E(u|x)] 2; under
(4.3) they coincide, soE(u 2 |x)=σ 2 readsVar(u|x)=σ 2.
Back to slide 43 Back to slide 44
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 65 / 97

## PDF 第 274 页

OLS.3 element by element
Wooldridge 4.2.2, p. 59 — withK=2, three scalar statements aboutu 2
• Withx=(1,x):E(u 2x′x)=
 
E(u2)E(u 2x)
E(u2x)E(u 2x2)
!
andσ 2E(x′x)=σ 2
 
1E(x)
E(x)E(x 2)
!
.
• (1,1)definesσ 2 =E(u 2);(1,2)saysCov(u 2,x)=0;(2,2)saysCov(u 2,x 2)=0;
in general(j,k)saysCov(u 2,x jxk)=0.
• LIE: a sufficient condition: ifE(u 2 |x)=σ 2, then
E(u2xjxk)=E[x jxkE(u2 |x)]=σ 2E(xjxk)for every(j,k); it fixes a whole
conditional moment, OLS.3 onlyK(K+1)/2 covariances.
• Second moment versus variance:Var(u|x)=E(u 2 |x)−[E(u|x)] 2; under
(4.3) they coincide, soE(u 2 |x)=σ 2 readsVar(u|x)=σ 2.
Back to slide 43 Back to slide 44
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 65 / 97

## PDF 第 275 页

OLS.3 element by element
Wooldridge 4.2.2, p. 59 — withK=2, three scalar statements aboutu 2
• Withx=(1,x):E(u 2x′x)=
 
E(u2)E(u 2x)
E(u2x)E(u 2x2)
!
andσ 2E(x′x)=σ 2
 
1E(x)
E(x)E(x 2)
!
.
• (1,1)definesσ 2 =E(u 2);(1,2)saysCov(u 2,x)=0;(2,2)saysCov(u 2,x 2)=0;
in general(j,k)saysCov(u 2,x jxk)=0.
• LIE: a sufficient condition: ifE(u 2 |x)=σ 2, then
E(u2xjxk)=E[x jxkE(u2 |x)]=σ 2E(xjxk)for every(j,k); it fixes a whole
conditional moment, OLS.3 onlyK(K+1)/2 covariances.
• Second moment versus variance:Var(u|x)=E(u 2 |x)−[E(u|x)] 2; under
(4.3) they coincide, soE(u 2 |x)=σ 2 readsVar(u|x)=σ 2.
Back to slide 43 Back to slide 44
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 65 / 97

## PDF 第 276 页

OLS.3 element by element
Wooldridge 4.2.2, p. 59 — withK=2, three scalar statements aboutu 2
• Withx=(1,x):E(u 2x′x)=
 
E(u2)E(u 2x)
E(u2x)E(u 2x2)
!
andσ 2E(x′x)=σ 2
 
1E(x)
E(x)E(x 2)
!
.
• (1,1)definesσ 2 =E(u 2);(1,2)saysCov(u 2,x)=0;(2,2)saysCov(u 2,x 2)=0;
in general(j,k)saysCov(u 2,x jxk)=0.
• LIE: a sufficient condition: ifE(u 2 |x)=σ 2, then
E(u2xjxk)=E[x jxkE(u2 |x)]=σ 2E(xjxk)for every(j,k); it fixes a whole
conditional moment, OLS.3 onlyK(K+1)/2 covariances.
• Second moment versus variance:Var(u|x)=E(u 2 |x)−[E(u|x)] 2; under
(4.3) they coincide, soE(u 2 |x)=σ 2 readsVar(u|x)=σ 2.
Back to slide 43 Back to slide 44
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 65 / 97

## PDF 第 277 页

Connect the econometric objects
Wooldridge 4.1–4.2.2 — from the economic question to a qualified conclusion
1 Target: define the coefficient and the question it answers.
2 Model and assumptions: explain orthogonality, rank, and sampling.
3 Estimate: compute ˆβfrom the observed data.
4 Sampling properties: distinguish unbiasedness, consistency, and normal
approximation.
5 Uncertainty and interpretation: estimate SEs, conduct inference, and state
what the result supports.
3b develops omitted variables, proxies and measurement error.
Back to slide 55
ECO6102 / L3 / 3a OLS calculations and estimator properties App. 66 / 97

## PDF 第 278 页

Appendix roadmap
APPENDIX D · Wooldridge 4.2.2 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a Inference: calculations and proofs

## PDF 第 279 页

One wage regression for the inference
calculations
Wooldridge Example 4.1 — 428 married women in the working sample
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2
+β 4age+β 5kidslt6+β 6kidsge6+u.
• kidslt6: children under six;kidsge6: children aged six or older.
• Estimate wage associations and their uncertainty.
• Working-sample associations alone do not establish causal effects.
Back to slide 49 Back to contents
ECO6102 / L3 / 3a Inference: calculations and proofs App. 67 / 97

## PDF 第 280 页

One wage regression for the inference
calculations
Wooldridge Example 4.1 — 428 married women in the working sample
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2
+β 4age+β 5kidslt6+β 6kidsge6+u.
• kidslt6: children under six;kidsge6: children aged six or older.
• Estimate wage associations and their uncertainty.
• Working-sample associations alone do not establish causal effects.
Back to slide 49 Back to contents
ECO6102 / L3 / 3a Inference: calculations and proofs App. 67 / 97

## PDF 第 281 页

Read an estimate beside its standard error
Wooldridge 4.2.2; Example 4.1 data — usual standard errors
SAME MODEL
Log wage on education, experience, experience squared, age and both child
counts.
Regressor Estimate Usual SE
Education .1078 .0144
Experience .0398 .0134
Children under six -.0607 .0888
• A negative point estimate can still be imprecise: compare−.0607 with its
SE,.0888.
Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 68 / 97

## PDF 第 282 页

Read an estimate beside its standard error
Wooldridge 4.2.2; Example 4.1 data — usual standard errors
SAME MODEL
Log wage on education, experience, experience squared, age and both child
counts.
Regressor Estimate Usual SE
Education .1078 .0144
Experience .0398 .0134
Children under six -.0607 .0888
• A negative point estimate can still be imprecise: compare−.0607 with its
SE,.0888.
Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 68 / 97

## PDF 第 283 页

State the question as a hypothesis
Wooldridge 4.2.2 — a two-sided test of one coefficient
QUESTION
After controlling for the other regressors, is the coefficient on young children zero?
H0 :β 5 =0 againstH 1 :β 5 ,0.
• Sampling variation can produce a nonzero estimate even ifH 0 is true.
• Compare the estimate with the variation we expectunder the null.
Back to slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 69 / 97

## PDF 第 284 页

State the question as a hypothesis
Wooldridge 4.2.2 — a two-sided test of one coefficient
QUESTION
After controlling for the other regressors, is the coefficient on young children zero?
H0 :β 5 =0 againstH 1 :β 5 ,0.
• Sampling variation can produce a nonzero estimate even ifH 0 is true.
• Compare the estimate with the variation we expectunder the null.
Back to slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 69 / 97

## PDF 第 285 页

Measure the distance in standard errors
Wooldridge 4.2.2 — the t statistic has a large-sample normal reference
t=
ˆβj −β j,0
se( ˆβj)
a
∼N(0,1)underH 0.
• Children under six:
t=−.06071/.08876≈ −.684.
• At 5%, reject a two-sided null
when|t|>1.96.
• Here: fail to rejectH 0. −1.96 0 1.96
statistic underH 0
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 70 / 97

## PDF 第 286 页

Measure the distance in standard errors
Wooldridge 4.2.2 — the t statistic has a large-sample normal reference
t=
ˆβj −β j,0
se( ˆβj)
a
∼N(0,1)underH 0.
• Children under six:
t=−.06071/.08876≈ −.684.
• At 5%, reject a two-sided null
when|t|>1.96.
• Here: fail to rejectH 0. −1.96 0 1.96
statistic underH 0
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 70 / 97

## PDF 第 287 页

A confidence interval shows the uncertainty
Wooldridge 4.2.2 and 3.5.1 — a range of coefficients compatible with this calculation
General rule: ˆβj ±1.96se( ˆβj).
• Children under six:
−.06071±1.96(.08876)≈[−.235, .113].
• Zero and substantial values of either sign are included. Nonrejection does
not establish a negligible association.
• Across repeated samples, this procedure covers the fixed coefficient
approximately 95%of the time.
Back to slide 51 Back to slide 52
ECO6102 / L3 / 3a Inference: calculations and proofs App. 71 / 97

## PDF 第 288 页

A confidence interval shows the uncertainty
Wooldridge 4.2.2 and 3.5.1 — a range of coefficients compatible with this calculation
General rule: ˆβj ±1.96se( ˆβj).
• Children under six:
−.06071±1.96(.08876)≈[−.235, .113].
• Zero and substantial values of either sign are included. Nonrejection does
not establish a negligible association.
• Across repeated samples, this procedure covers the fixed coefficient
approximately 95%of the time.
Back to slide 51 Back to slide 52
ECO6102 / L3 / 3a Inference: calculations and proofs App. 71 / 97

## PDF 第 289 页

A p-value is a tail probability under the null
Wooldridge 4.2.2 and 3.5.2 — report how unusual the statistic would be
p=Pr

|Z| ≥ |t observed|

,Z∼N(0,1).
• Witht=−.684, the two-sided p-value is approximately.494.
• Reject at levelαwhenp< α;.494> .05, so we fail to reject here.
• The p-value is not the probability thatH 0 is true.
Back to slide 48 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 72 / 97

## PDF 第 290 页

A p-value is a tail probability under the null
Wooldridge 4.2.2 and 3.5.2 — report how unusual the statistic would be
p=Pr

|Z| ≥ |t observed|

,Z∼N(0,1).
• Witht=−.684, the two-sided p-value is approximately.494.
• Reject at levelαwhenp< α;.494> .05, so we fail to reject here.
• The p-value is not the probability thatH 0 is true.
Back to slide 48 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 72 / 97

## PDF 第 291 页

Two possible errors in a testing decision
Wooldridge 3.5.2; 4.2.2 — decisions can be wrong because estimates are random
H0 trueH 0 false
RejectH 0 Type I error Correct rejection
Fail to rejectH 0 Correct nonrejection Type II error
• Choose the significance level, such asα=.05, before applying the rule.
• A test with asymptotic size.05 falsely rejects with probability approaching
.05 under the null.
Back to slide 48 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 73 / 97

## PDF 第 292 页

Two possible errors in a testing decision
Wooldridge 3.5.2; 4.2.2 — decisions can be wrong because estimates are random
H0 trueH 0 false
RejectH 0 Type I error Correct rejection
Fail to rejectH 0 Correct nonrejection Type II error
• Choose the significance level, such asα=.05, before applying the rule.
• A test with asymptotic size.05 falsely rejects with probability approaching
.05 under the null.
Back to slide 48 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 73 / 97

## PDF 第 293 页

Power is the chance of detecting a false null
Wooldridge 3.5.2; 4.2.2 — precision affects what a test can detect
• Power: the probability of rejectingH 0 under a specified alternative.
• A noisy estimate can fail to detect a meaningful coefficient: a Type II error.
• Under the maintained conditions, larger samples improve detection of a
fixed nonzero coefficient; aconsistent testhas power tending to one.
Failure to reject can reflect limited precision. Read the interval as well as the
decision.
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 74 / 97

## PDF 第 294 页

Power is the chance of detecting a false null
Wooldridge 3.5.2; 4.2.2 — precision affects what a test can detect
• Power: the probability of rejectingH 0 under a specified alternative.
• A noisy estimate can fail to detect a meaningful coefficient: a Type II error.
• Under the maintained conditions, larger samples improve detection of a
fixed nonzero coefficient; aconsistent testhas power tending to one.
Failure to reject can reflect limited precision. Read the interval as well as the
decision.
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 74 / 97

## PDF 第 295 页

Ask a joint question about age and children
Wooldridge 4.2.2 — test three restrictions together
SAME MROZ MODEL
Education, experience and experience squared remain included.
H0 :β 4 =β 5 =β 6 =0.
• This asks whether age and both child counts jointly add a linear
association with wages.
• Three separate 5%tests do not generally give one joint test of size 5%. The
estimates can move together.
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 75 / 97

## PDF 第 296 页

Ask a joint question about age and children
Wooldridge 4.2.2 — test three restrictions together
SAME MROZ MODEL
Education, experience and experience squared remain included.
H0 :β 4 =β 5 =β 6 =0.
• This asks whether age and both child counts jointly add a linear
association with wages.
• Three separate 5%tests do not generally give one joint test of size 5%. The
estimates can move together.
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 75 / 97

## PDF 第 297 页

Write the joint restrictions as one vector
Wooldridge 4.2.2 — collect the departures from the null
d=


ˆβ4
ˆβ5
ˆβ6

 , bΣd =the corresponding 3×3 covariance block.
• Under the joint null, all three population coefficients are zero.
• To measure whetherdis far from zero, use both its component variances
and their covariances.
General restrictions: R beta = r
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 76 / 97

## PDF 第 298 页

Write the joint restrictions as one vector
Wooldridge 4.2.2 — collect the departures from the null
d=


ˆβ4
ˆβ5
ˆβ6

 , bΣd =the corresponding 3×3 covariance block.
• Under the joint null, all three population coefficients are zero.
• To measure whetherdis far from zero, use both its component variances
and their covariances.
General restrictions: R beta = r
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 76 / 97

## PDF 第 299 页

The Wald statistic measures the joint distance
Wooldridge 4.2.2; 3.3 — a covariance-adjusted squared distance
W=d ′bΣ−1
d d
a
∼χ 2
Q underH 0.
• Qis the number of independent restrictions. For MROZ,Q=3; the 5%
critical value is 7.81.
• Reject whenW>7.81; the p-value isPr(χ 2
3 ≥W observed).
• With the usual covariance, the usualFstatistic is exactlyW/Q. The usual
covariance is justified by OLS.3.
Why W = t squared, and how F relates
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 77 / 97

## PDF 第 300 页

The Wald statistic measures the joint distance
Wooldridge 4.2.2; 3.3 — a covariance-adjusted squared distance
W=d ′bΣ−1
d d
a
∼χ 2
Q underH 0.
• Qis the number of independent restrictions. For MROZ,Q=3; the 5%
critical value is 7.81.
• Reject whenW>7.81; the p-value isPr(χ 2
3 ≥W observed).
• With the usual covariance, the usualFstatistic is exactlyW/Q. The usual
covariance is justified by OLS.3.
Why W = t squared, and how F relates
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 77 / 97

## PDF 第 301 页

Separate tests can miss a joint departure
Wooldridge 4.2.2 — covariance changes which combinations are unusual
−2 0 2
−2
0
2
first estimate / SE
second estimate / SE
• Illustrative estimates:
(1.8,−1.8); both SEs are 1.
• Both individual tests fail to
reject: 1.8<1.96 (dashed
square).
• Estimated correlation.8:
opposite movements are
unusual. The point lies outside
the joint 5%nonrejection ellipse
(blue).
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 78 / 97

## PDF 第 302 页

Separate tests can miss a joint departure
Wooldridge 4.2.2 — covariance changes which combinations are unusual
−2 0 2
−2
0
2
first estimate / SE
second estimate / SE
• Illustrative estimates:
(1.8,−1.8); both SEs are 1.
• Both individual tests fail to
reject: 1.8<1.96 (dashed
square).
• Estimated correlation.8:
opposite movements are
unusual. The point lies outside
the joint 5%nonrejection ellipse
(blue).
Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 78 / 97

## PDF 第 303 页

Residual squares and the error variance
Wooldridge 4.2.2 — use the OLS normal equations
NOT A TION
∆= ˆβ−βand ˆu=u−X∆.
• Expanding the squared residuals gives
ˆu′ ˆu
N = u′u
N −2∆ ′ X′u
N +∆ ′ X′X
N ∆.
• The OLS normal equations implyX ′u=X ′X∆, so
SSR
N = 1
N
X
i
u2
i −∆ ′
X′X
N

∆.
Back to slide 46 Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 79 / 97

## PDF 第 304 页

Residual squares and the error variance
Wooldridge 4.2.2 — use the OLS normal equations
NOT A TION
∆= ˆβ−βand ˆu=u−X∆.
• Expanding the squared residuals gives
ˆu′ ˆu
N = u′u
N −2∆ ′ X′u
N +∆ ′ X′X
N ∆.
• The OLS normal equations implyX ′u=X ′X∆, so
SSR
N = 1
N
X
i
u2
i −∆ ′
X′X
N

∆.
Back to slide 46 Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 79 / 97

## PDF 第 305 页

Consistency of the residual variance
Wooldridge 4.2.2 — consistency is a large-sample statement
SSR
N = 1
N
X
i
u2
i −∆ ′
X′X
N

∆.
• I.i.d. sampling and finite second moments giveN −1 P
i u2
i
p
− →E(u2).
• Consistency:∆
p
− →0. SinceX′X/N
p
− →A, the quadratic term tends to zero.
• FixedK:N/(N−K)→1, hences 2 p
− →E(u2).
This consistency result needs no OLS.3; it does not establish unbiasedness.
Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 80 / 97

## PDF 第 306 页

Consistency of the residual variance
Wooldridge 4.2.2 — consistency is a large-sample statement
SSR
N = 1
N
X
i
u2
i −∆ ′
X′X
N

∆.
• I.i.d. sampling and finite second moments giveN −1 P
i u2
i
p
− →E(u2).
• Consistency:∆
p
− →0. SinceX′X/N
p
− →A, the quadratic term tends to zero.
• FixedK:N/(N−K)→1, hences 2 p
− →E(u2).
This consistency result needs no OLS.3; it does not establish unbiasedness.
Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 80 / 97

## PDF 第 307 页

Studentizing the estimator
Wooldridge 3.5.1–3.5.2; 4.2.2 — estimate the scale consistently
• Suppose
√
N( ˆβj −β j)
d
− →N(0,Vjj), withV jj >0, and ˆVjj
p
− →Vjj.
• Slutsky’s theorem gives
ˆβj −β j
q
ˆVjj/N
d
− →N(0,1).
• UnderH 0, substituteβ j,0 in the numerator. Invert this test to obtain the
confidence interval.
The lecture uses a large-sample normal reference.
Back to slide 47 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 81 / 97

## PDF 第 308 页

Studentizing the estimator
Wooldridge 3.5.1–3.5.2; 4.2.2 — estimate the scale consistently
• Suppose
√
N( ˆβj −β j)
d
− →N(0,Vjj), withV jj >0, and ˆVjj
p
− →Vjj.
• Slutsky’s theorem gives
ˆβj −β j
q
ˆVjj/N
d
− →N(0,1).
• UnderH 0, substituteβ j,0 in the numerator. Invert this test to obtain the
confidence interval.
The lecture uses a large-sample normal reference.
Back to slide 47 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 81 / 97

## PDF 第 309 页

Construct a restriction matrix
Wooldridge 4.2.3, (4.12) — R selects or combines coefficients
H0 :Rβ=r.(4.12)
RisQ×Kwith rankQ;risQ×1.
• For the MROZ joint null:
R=


0 0 0 0 1 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 1

 ,r=


0
0
0

 .
• Forβ j =β k, use one row with 1 atj,−1 atk, and zeros elsewhere.
Back to App. 76 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 82 / 97

## PDF 第 310 页

Construct a restriction matrix
Wooldridge 4.2.3, (4.12) — R selects or combines coefficients
H0 :Rβ=r.(4.12)
RisQ×Kwith rankQ;risQ×1.
• For the MROZ joint null:
R=


0 0 0 0 1 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 1

 ,r=


0
0
0

 .
• Forβ j =β k, use one row with 1 atj,−1 atk, and zeros elsewhere.
Back to App. 76 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 82 / 97

## PDF 第 311 页

Wald, t squared and the usual F statistic
Wooldridge 3.3; adapted (4.13) — covariance normalizes the restrictions
W=(R ˆβ−r) ′[RbΣR′]−1(R ˆβ−r)
a
∼χ 2
Q.
• A standardizedQ-dimensional normal vector has a chi-square squared
length. A consistent covariance estimate gives the same limit.
• With one restriction,W=t 2 using the same covariance estimate.
• WithbΣ =s 2(X′X)−1,F=W/Qexactly. Under the classical normal model
F∼F(Q,N−K); without it the justification here is asymptotic.
Back to App. 77 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 83 / 97

## PDF 第 312 页

Wald, t squared and the usual F statistic
Wooldridge 3.3; adapted (4.13) — covariance normalizes the restrictions
W=(R ˆβ−r) ′[RbΣR′]−1(R ˆβ−r)
a
∼χ 2
Q.
• A standardizedQ-dimensional normal vector has a chi-square squared
length. A consistent covariance estimate gives the same limit.
• With one restriction,W=t 2 using the same covariance estimate.
• WithbΣ =s 2(X′X)−1,F=W/Qexactly. Under the classical normal model
F∼F(Q,N−K); without it the justification here is asymptotic.
Back to App. 77 Main lecture: slide 50
ECO6102 / L3 / 3a Inference: calculations and proofs App. 83 / 97

## PDF 第 313 页

The full MROZ coefficient table
Wooldridge Example 4.1 — all 428 observations enter both calculations
Regressor Coefficient Usual SE HC1 SE
Intercept -.42091 .31690 .31833
Education .10783 .01440 .01362
Experience .03982 .01339 .01526
Experience squared -.000781 .000402 .000410
Age -.001465 .005292 .005935
Children under six -.06071 .08876 .10610
Older children -.01459 .02790 .02935
N=428,K=7,R 2 =.15824; one OLS fit.
Main lecture: slide 49
ECO6102 / L3 / 3a Inference: calculations and proofs App. 84 / 97

## PDF 第 314 页

Reproduce the inference calculation in Python
Wooldridge Example 4.1 — the companion script exposes each calculation
1 Select working women and the common complete sample; cast experience
to floating point before squaring it.
2 Fit OLS once; calculate usual and HC1 covariance matrices from the
residuals.
3 Use normal references for individual tests and intervals; useχ 2
3 for the
Wald tests.
Companion file:L3a inference mroz.py. Output includes every
coefficient, SE, interval, p-value and the joint tests.
Back to App. 91 Main lecture: slide 54
ECO6102 / L3 / 3a Inference: calculations and proofs App. 85 / 97

## PDF 第 315 页

Reproduce the inference calculation in Python
Wooldridge Example 4.1 — the companion script exposes each calculation
1 Select working women and the common complete sample; cast experience
to floating point before squaring it.
2 Fit OLS once; calculate usual and HC1 covariance matrices from the
residuals.
3 Use normal references for individual tests and intervals; useχ 2
3 for the
Wald tests.
Companion file:L3a inference mroz.py. Output includes every
coefficient, SE, interval, p-value and the joint tests.
Back to App. 91 Main lecture: slide 54
ECO6102 / L3 / 3a Inference: calculations and proofs App. 85 / 97

## PDF 第 316 页

Appendix roadmap
APPENDIX E · Wooldridge 4.2.3 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a Robust covariance and weighting

## PDF 第 317 页

Heteroskedasticity-robust inference
Wooldridge 4.2.3 — keep the OLS estimate and adjust its uncertainty
• If the disturbance spread changes across regressors, the usual SE can be
misleading.
• Robust SEs allow that spread to vary. Keep the OLS coefficient; use the
revised SE in the same tests and intervals.
Estimate Usual SE Robust SE (HC1)
−.06071.08876.10610
Robust SEs address heteroskedasticity; they do not remove endogeneity.
Robust covariance example
Back to slide 54 Back to contents
ECO6102 / L3 / 3a Robust covariance and weighting App. 86 / 97

## PDF 第 318 页

Heteroskedasticity-robust inference
Wooldridge 4.2.3 — keep the OLS estimate and adjust its uncertainty
• If the disturbance spread changes across regressors, the usual SE can be
misleading.
• Robust SEs allow that spread to vary. Keep the OLS coefficient; use the
revised SE in the same tests and intervals.
Estimate Usual SE Robust SE (HC1)
−.06071.08876.10610
Robust SEs address heteroskedasticity; they do not remove endogeneity.
Robust covariance example
Back to slide 54 Back to contents
ECO6102 / L3 / 3a Robust covariance and weighting App. 86 / 97

## PDF 第 319 页

The same estimates with robust standard
errors
Wooldridge 4.2.3; Example 4.1 data — HC1 rescales the sandwich
bΣHC1 = N
N−K
bΣHC0.
Regressor Estimate Usual SE HC1 SE
Education .1078 .0144 .0136
Experience .0398 .0134 .0153
Children under six -.0607 .0888 .1061
• For children under six, robustt=−.572 andp=.567: still fail to reject.
Back to App. 86 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 87 / 97

## PDF 第 320 页

The same estimates with robust standard
errors
Wooldridge 4.2.3; Example 4.1 data — HC1 rescales the sandwich
bΣHC1 = N
N−K
bΣHC0.
Regressor Estimate Usual SE HC1 SE
Education .1078 .0144 .0136
Experience .0398 .0134 .0153
Children under six -.0607 .0888 .1061
• For children under six, robustt=−.572 andp=.567: still fail to reject.
Back to App. 86 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 87 / 97

## PDF 第 321 页

Make the joint test robust in the same way
Wooldridge 4.2.3, adapted (4.13) with HC1 — keep the hypothesis; replace its
covariance
Wrobust =d ′[bΣd,HC1]−1d
a
∼χ 2
Q underH 0.
• The restriction vector and the OLS estimates stay the same.
• Use the HC1 covariance block. The joint chi-square reference remains
valid under the maintained sampling and moment conditions.
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 88 / 97

## PDF 第 322 页

Make the joint test robust in the same way
Wooldridge 4.2.3, adapted (4.13) with HC1 — keep the hypothesis; replace its
covariance
Wrobust =d ′[bΣd,HC1]−1d
a
∼χ 2
Q underH 0.
• The restriction vector and the OLS estimates stay the same.
• Use the HC1 covariance block. The joint chi-square reference remains
valid under the maintained sampling and moment conditions.
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 88 / 97

## PDF 第 323 页

Robust inference and weighted least squares
have different jobs
Wooldridge 4.2.3 — variance estimation versus changing the estimator
• Robust SEs: retain the OLS fit and allow heteroskedasticity in its
uncertainty calculation.
• Weighted least squares: change the fit by giving observations different
weights. Efficiency gains require a suitable conditional-mean and variance
model.
• HC1 is a finite-sample adjustment, not a guarantee of accurate
small-sample inference.
When weighting helps or changes the target Small-sample qualifications
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 89 / 97

## PDF 第 324 页

Robust inference and weighted least squares
have different jobs
Wooldridge 4.2.3 — variance estimation versus changing the estimator
• Robust SEs: retain the OLS fit and allow heteroskedasticity in its
uncertainty calculation.
• Weighted least squares: change the fit by giving observations different
weights. Efficiency gains require a suitable conditional-mean and variance
model.
• HC1 is a finite-sample adjustment, not a guarantee of accurate
small-sample inference.
When weighting helps or changes the target Small-sample qualifications
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 89 / 97

## PDF 第 325 页

The joint MROZ decision
Wooldridge 4.2.3; Example 4.1 data — the null concerns age and both child counts
JOINT NULL
H0 :β 4 =β 5 =β 6 =0, withQ=3.
Covariance WaldW pfromχ 2
3
Usual .711 .871
HC1 .493 .920
• The usualF=W/3=.237; usingF(3,421)also givesp≈.871.
• Both Wald statistics are below 7.81: fail to reject. The data do not establish
that all three coefficients are zero.
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 90 / 97

## PDF 第 326 页

The joint MROZ decision
Wooldridge 4.2.3; Example 4.1 data — the null concerns age and both child counts
JOINT NULL
H0 :β 4 =β 5 =β 6 =0, withQ=3.
Covariance WaldW pfromχ 2
3
Usual .711 .871
HC1 .493 .920
• The usualF=W/3=.237; usingF(3,421)also givesp≈.871.
• Both Wald statistics are below 7.81: fail to reject. The data do not establish
that all three coefficients are zero.
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 90 / 97

## PDF 第 327 页

From a dataset to an inference statement
Wooldridge 4.2.2–4.2.3 — one fit, explicit assumptions, a qualified conclusion
1 Specify the sample, model and hypothesis; fit OLS once.
2 Choose a justified covariance estimate and compute the statistic or
interval.
3 Report the estimate, uncertainty and what the evidence supports.
More precise estimates do not resolve an omitted-variable problem. Section
4.3 asks what happens when an important determinant is unobserved.
Python walkthrough and its reference conventions
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 91 / 97

## PDF 第 328 页

From a dataset to an inference statement
Wooldridge 4.2.2–4.2.3 — one fit, explicit assumptions, a qualified conclusion
1 Specify the sample, model and hypothesis; fit OLS once.
2 Choose a justified covariance estimate and compute the statistic or
interval.
3 Report the estimate, uncertainty and what the evidence supports.
More precise estimates do not resolve an omitted-variable problem. Section
4.3 asks what happens when an important determinant is unobserved.
Python walkthrough and its reference conventions
Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 91 / 97

## PDF 第 329 页

Why the usual covariance is a special case
Wooldridge 4.2.3 — simplify population moments, not individual residual squares
A=E(x ′x),B=E(u 2x′x),V=A −1BA−1,Σ =V/N.
• Under OLS.3,B=σ 2A, henceV=σ 2A−1.
• In data use ˆA=X ′X/Nand ˆB=N −1 P
i ˆu2
i x′
ixi for the sandwich.
• The simplification concerns population moments. Homoskedasticity does
not say that every fitted residual square equalss 2.
Back to slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 92 / 97

## PDF 第 330 页

Why the usual covariance is a special case
Wooldridge 4.2.3 — simplify population moments, not individual residual squares
A=E(x ′x),B=E(u 2x′x),V=A −1BA−1,Σ =V/N.
• Under OLS.3,B=σ 2A, henceV=σ 2A−1.
• In data use ˆA=X ′X/Nand ˆB=N −1 P
i ˆu2
i x′
ixi for the sandwich.
• The simplification concerns population moments. Homoskedasticity does
not say that every fitted residual square equalss 2.
Back to slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 92 / 97

## PDF 第 331 页

When weighted least squares helps
Wooldridge 4.2.3 — weighting needs its own justification
• With a correct conditional mean and variance model, inverse-variance
weighting can improve efficiency by downweighting noisier observations.
• WLS changes the coefficient estimate; robust standard errors leave OLS
coefficients unchanged.
• If onlyE(x ′u)=0 holds, weighting may failE[w(x)x ′u]=0 and change the
projection target.
Correct weighting is an additional modeling task. Chapter 12 develops these
methods further.
Back to App. 89 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 93 / 97

## PDF 第 332 页

When weighted least squares helps
Wooldridge 4.2.3 — weighting needs its own justification
• With a correct conditional mean and variance model, inverse-variance
weighting can improve efficiency by downweighting noisier observations.
• WLS changes the coefficient estimate; robust standard errors leave OLS
coefficients unchanged.
• If onlyE(x ′u)=0 holds, weighting may failE[w(x)x ′u]=0 and change the
projection target.
Correct weighting is an additional modeling task. Chapter 12 develops these
methods further.
Back to App. 89 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 93 / 97

## PDF 第 333 页

What HC1 does and does not promise
Wooldridge 4.2.3 — the correction changes covariance by N divided by N minus K
bΣHC1 = N
N−K
bΣHC0, 428
421 ≈1.0166.
• This degrees-of-freedom adjustment can improve small-sample
approximation, but it does not make robust tests exact.
• The textbook discusses finite-sample adjustments to robust covariance
estimates, including HC1.
• Heteroskedasticity robustness leaves exogeneity, sampling and moment
requirements in place.
Back to App. 89 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 94 / 97

## PDF 第 334 页

What HC1 does and does not promise
Wooldridge 4.2.3 — the correction changes covariance by N divided by N minus K
bΣHC1 = N
N−K
bΣHC0, 428
421 ≈1.0166.
• This degrees-of-freedom adjustment can improve small-sample
approximation, but it does not make robust tests exact.
• The textbook discusses finite-sample adjustments to robust covariance
estimates, including HC1.
• Heteroskedasticity robustness leaves exogeneity, sampling and moment
requirements in place.
Back to App. 89 Main lecture: slide 54
ECO6102 / L3 / 3a Robust covariance and weighting App. 94 / 97

## PDF 第 335 页

Appendix roadmap
APPENDIX F · Wooldridge 4.2.4 — current location in blue
Chapter 3 tools
The population model and economic interpretation
OLS calculations and estimator properties
Inference: calculations and proofs
Robust covariance and weighting
Optional LM tests
Back to contents
ECO6102 / L3 / 3a Optional LM tests

## PDF 第 336 页

The LM idea: look for what the restricted
model misses
Wooldridge 4.2.4 — start by imposing the joint null
1 Fit the wage equation without age and the two child counts: imposeH 0.
2 Keep the restricted residuals, ˜ui.
3 Ask whether the excluded regressors explain these residuals after
accounting for the included regressors.
The LM test uses a restricted fit. The Wald test measures the unrestricted
estimate’s departure from the null.
Back to contents Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 95 / 97

## PDF 第 337 页

The LM idea: look for what the restricted
model misses
Wooldridge 4.2.4 — start by imposing the joint null
1 Fit the wage equation without age and the two child counts: imposeH 0.
2 Keep the restricted residuals, ˜ui.
3 Ask whether the excluded regressors explain these residuals after
accounting for the included regressors.
The LM test uses a restricted fit. The Wald test measures the unrestricted
estimate’s departure from the null.
Back to contents Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 95 / 97

## PDF 第 338 页

The ordinary LM statistic
Wooldridge 4.2.4, (4.14)–(4.15) — the auxiliary regression must include all regressors
• Regress the restricted residuals ˜uonboththe retained regressorsX 1 and
the excluded regressorsX 2.
• With itsR 2
u, the statistic is
LM=NR 2
u
a
∼χ 2
Q underH 0 and OLS.3.
• MROZ:R 2
u =.001686,LM=.722,p=.868: fail to reject the three
restrictions.
Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 96 / 97

## PDF 第 339 页

The ordinary LM statistic
Wooldridge 4.2.4, (4.14)–(4.15) — the auxiliary regression must include all regressors
• Regress the restricted residuals ˜uonboththe retained regressorsX 1 and
the excluded regressorsX 2.
• With itsR 2
u, the statistic is
LM=NR 2
u
a
∼χ 2
Q underH 0 and OLS.3.
• MROZ:R 2
u =.001686,LM=.722,p=.868: fail to reject the three
restrictions.
Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 96 / 97

## PDF 第 340 页

The heteroskedasticity-robust LM calculation
Wooldridge 4.2.4, (4.17) — partial out the retained regressors first
1 Regress each excluded regressor onX 1; collect the residuals ˆri.
2 Regress the constant 1 on the products ˜uiˆri,without an intercept; call its sum
of squared residualsSSR 0.
3 UseLM robust =N−SSR 0
a
∼χ 2
Q underH 0 and the maintained moment
conditions.
MROZ:LM robust =.512,p=.916. The robust Wald and LM tests agree on
nonrejection here.
Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 97 / 97

## PDF 第 341 页

The heteroskedasticity-robust LM calculation
Wooldridge 4.2.4, (4.17) — partial out the retained regressors first
1 Regress each excluded regressor onX 1; collect the residuals ˆri.
2 Regress the constant 1 on the products ˜uiˆri,without an intercept; call its sum
of squared residualsSSR 0.
3 UseLM robust =N−SSR 0
a
∼χ 2
Q underH 0 and the maintained moment
conditions.
MROZ:LM robust =.512,p=.916. The robust Wald and LM tests agree on
nonrejection here.
Main lecture: slide 54
ECO6102 / L3 / 3a Optional LM tests App. 97 / 97
