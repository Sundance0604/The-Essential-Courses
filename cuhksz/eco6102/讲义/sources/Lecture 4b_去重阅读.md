### p.1
Lecture 4b:
Instrumental Variables
Enjie (Jack) Ma
Lecture 4 · Mondays 12 and 19 October 2026

### p.2
Midterm arrangements and Problem Set 2
Prepare the permitted sheet and finish the IV practice
• MidtermMonday 26 October 2026, 09:00–11:00;西丽小礼堂(tentative). Covers
L1–L4; 30% of the course grade.
• Formatclosed book and in person; one double-sided A4 cheat sheet is allowed.
No calculators or electronic dictionaries.
• Problem Set 2Due Friday 23 October 2026. Solutions will be released
immediately after the deadline.
Exam venue map

### p.3
Contents
Introductory Econometrics 15-3–15-6
1. Two Stage Least Squares
2. IV Solutions to Errors-in-Variables Problems
3. Testing for Endogeneity and Overidentifying Restrictions
4. 2SLS with Heteroskedasticity
Technical extensions are linked in the appendix; Midterm Review is a separate deck.
Continue with two stages and diagnostics for their estimates.

### p.4
Recap: IV
Moments connect the assumptions to the estimator
y=β 0 +β 1x+u,E(u)=0.
Cov(z,u)=0,Cov(z,x),0.
Cov(z,y)=β 1 Cov(z,x)=⇒ ˆβ1,IV =
P
i(zi − ¯z)(yi − ¯y)P
i(zi − ¯z)(xi − ¯x) .
Exogenous variables Potentially endogenous regressor Structural error

### p.5
Recall IV with included exogenous variables
Exogeneity is maintained; relevance must remain after the included variables
log(wage)=β 0 +β 1educ+β 2exper+u 1.
E(u1)=0,Cov(exper,u 1)=Cov(fatheduc,u 1)=0.
educ=π 0 +π 1exper+π 2fatheduc+v 2, π 2 ,0.

### p.6
A second instrument needs its own argument
Relevance and exogeneity are separate requirements
Same target
Mother’s education also predicts schooling. What additional assumption is
needed for it to be a valid IV?
Cov(motheduc,u 1)=0.
If both parents are credible instruments, how should we use their
information together?

### p.7
Intro 15-3a
A Single Endogenous Explanatory Variable
Multicollinearity and 2SLS
Detecting Weak Instruments
We have several credible instruments. How can we combine their information?

### p.8
Start with the model and the excluded
variables
One endogenous regressor; two candidates excluded from the outcome equation
y1 =β 0 +β 1y2 +β 2z1 +u 1.(15.22)
Already includedz 1 has its own effect ony 1. We maintain
E(u1)=0,Cov(z 1,u 1)=0.
Now add two candidatesz 2,z 3 do not enter this equation, and
Cov(z2,u 1)=0,Cov(z 3,u 1)=0.
These are the exclusion restrictions.
RelevanceTogether, the excluded variables must predicty 2 beyond the includedz 1.

### p.9
Why combine the instruments?
Using each instrument separately leaves information unused
y1 =β 0 +β 1y2 +β 2z1 +u 1.
Using either valid instrument separately generally leaves information unused; the
two IV estimators need not be efficient. A fixed combination remains uncorrelated
withu 1:
Cov(a0 +a 1z1 +a 2z2 +a 3z3,u 1)=
3X
j=1
aj Cov(zj,u 1)=0.
Exogeneity survives. Which linear combination is most strongly correlated withy 2?
Why combinations remain exogenous

### p.10
Choose the most strongly correlated
combination
The reduced form supplies the best linear prediction
Structural model
y1 =β 0 +β 1y2 +β 2z1 +u 1; allz j are maintained exogenous.
Choose the linear combination most highly correlated withy 2.
y2 =π 0 +π 1z1 +π 2z2 +π 3z3 +v 2.(15.33)
The population linear projection defines its remainder by
E(v2)=0,Cov(z j,v 2)=0(j=1,2,3).

### p.11
The reduced form gives the instrument
Combine the exogenous variables using their population coefficients
Reduced form
y2 =π 0 +π 1z1 +π 2z2 +π 3z3 +v 2.
y∗
2 =π 0 +π 1z1 +π 2z2 +π 3z3.(15.34)
Use the best linear prediction of the endogenous regressor as its instrument.
It is the best IV among linear combinations under the assumptions in Appendix15A,
including homoskedasticity.
Why this prediction maximizes correlation

### p.12
The excluded variables must add prediction
Relevance is prediction beyond the included exogenous variable
Structural equation
First stage
π2 ,0 orπ 3 ,0.(15.35)
If both are zero,y ∗
2 =π 0 +π 1z1. There is no separate predicted variation to identify
the effect ofy 2 while holdingz 1 fixed.
The population moment explanation

### p.13
Prediction and the schooling remainder
15-3a: the first-stage remainder is a vertical gap
y1 =β 0 +β 1y2 +β 2z1 +u 1, with valid IVs.
y2 =y ∗
2 +v 2.(15.33)
10 13 16
10
14
18
v2 =1 y2 =y ∗
2
Predicted schoolingy ∗
Schoolingy 2
One schooling value
14=13+1.
Cov(y∗
2,u 1)=0 follows from IV
exogeneity.
The remainderv 2 may shareu 1.
This is where endogeneity can
remain.

### p.14
Population to sample
The sample estimates the same projection rule
The population coefficientsπ j are unknown. Estimate the reduced form by
OLS:
by2 = ˆπ0 + ˆπ1z1 + ˆπ2z2 + ˆπ3z3.(15.36)
Check excluded-variable relevance: testH 0 :π 2 =π 3 =0.
This checks prediction, not exogeneity. Instrument strength follows in15-3c.
From population projection to sample OLS

### p.15
Use the fitted value as the instrument
Three equations jointly determine the IV coefficients
Structural residual
ˆui1 =y i1 − ˆβ0 − ˆβ1yi2 − ˆβ2zi1.
As in 15-2, (15.25), use byi2 in place of the single excluded IV:X
i
ˆui1 =0,
X
zi1 ˆui1 =0,
byi2 ˆui1 =0. (15.37)
Population and sample moments

### p.16
Compute the IV coefficients in two stages
OLS on the fitted regressor gives the same IV coefficients
Using by2 as the IV fory 2 gives the same coefficients as the second regression below.
Stage 1Regressy 2 onz 1,z 2,z 3 and an intercept:
Stage 2Run the OLS regression
y1 on by2,z 1 and an intercept.(15.38)
This is two-stage least squares (2SLS). Retain the same sample and included controls
in both stages.
Why the coefficients coincide

### p.17
Why the predicted component works
Substitution changes the error but keeps the structural coefficient
Splity 2 =y ∗
2 +v 2: prediction plus remainder. Substitute into the structural equation:
y1 =β 0 +β 1y∗
2 +β 2z1 +u 1 +β 1v2
|    {z    }
composite error
.(15.39)
The composite error has mean zero and is uncorrelated withy ∗
2 andz 1. This is why
the population regression retainsβ 1.
Why both covariances are zero

### p.18
Use IV software for standard errors
The two regressions compute coefficients but not ordinary OLS uncertainty
Population explanation
2 +β 2z1 +(u 1 +β 1v2).
• Different errorThe transformed error containsv 2; IV uncertainty uses the
structural erroru 1.
• Different standard errorsOrdinary second-stage OLS standard errors and tests
are not valid for 2SLS.
• Use IV softwareSupply the actual outcome, actual endogenous regressor,
included controls and complete IV list to a 2SLS command.
Residuals and standard errors Stata R Python

### p.19
One instrument is a special case of 2SLS
First connect to the father-only model; then combine both parents
Recap: Example 15.1
log(wage)=β 0 +β 1educ+u; one excluded IV:fatheduc.
Calculation on the same 428 women Schooling slope
Direct IV ratio.05917
Two-stage OLS using fitted schooling .05917
With one instrument, IV and 2SLS coincide. The optional pictures show the same
calculation. Next add experience controls and both parents, as in Example 15.5.
Why the coefficients are equal The two-stage pictures

### p.20
Combine both parents and retain experience
controls
Example 15.5: one prediction for the same structural schooling effect
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +u 1.(15.40)
• Potential endogeneityAbility remains inu 1.
• Included controlsExperience and its square enter both stages and are
maintained exogenous.
• Excluded instrumentsBoth parents’ education predict schooling. We assume no
remaining wage path through ability, connections or family resources:
Cov(motheduc,u 1)=Cov(fatheduc,u 1)=0.
Use the same 428 women for the OLS–2SLS comparison.

### p.21
First stage combines both parents
Example 15.5: test what the excluded parents add beyond experience
educ=π 0 +π 1exper+π 2exper2
+π 3motheduc+π 4fatheduc+v 2. (15.41)
H0 :π 3 =π 4 =0,F(2,423)=55.40(n=428).
The parents jointly add schooling prediction beyond the included controls. This is
relevance evidence.
Fit (15.41) by OLS to obtain deduci, the schooling prediction used next.
Calculate one woman’s predicted schooling

### p.22
Two stages give a 6.1 percent estimate
Example 15.5: read the fitted-schooling slope
Structural target
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +u 1.
Stage 2Regress log wages on fitted schooling and the included experience terms:
log(wagei)on deduci,exper i,exper 2
i ,and an intercept.
ˆβ1,2SLS =.06140.
Holding experience fixed, an additional schooling year is associated with about 6.1%
higher wages under the maintained IV assumptions.

### p.23
Compare OLS and IV on the same model and
sample
Example 15.5: the estimate difference needs an economic explanation
Same 428 women and model OLS 2SLS
Schooling estimate .1075 .0614
Conventional SE .0141 .0314
Smaller IV is consistent with upward ability bias if the IVs are valid.
Why is the 2SLS estimate less precise? Next, examine the variation left to estimate its
slope.
Omitted ability: diagram and bias formula

### p.24
Brief note on consistency and assumptions
Consistency and conventional inference require different assumptions
• ConsistencyMaintainE(u 1)=0,Cov(z j,u 1)=0 for every IV and excluded partial
relevanceπ 2 ,0 orπ 3 ,0.
• Asymptotically valid standard errorsAlso require the homoskedasticity
condition
E(u2
1 |z)=σ 2.
This is the conventional variance formula; robust standard errors allow
heteroskedasticity.
Full 2SLS assumptions

### p.25
Intro 15-3b
We have a two-stage estimate. Why can its standard error be much larger than
OLS’s?

### p.26
Two changes affect precision
Separate the familiar control-overlap cost from instrument prediction
OLS benchmarkExogenous regressors; homoskedastic errors.
Simple regression:Avar( ˆβ1,OLS)≈ σ2
SST2
,
Multiple regression:Avar( ˆβ1,OLS)≈ σ2
SST2(1−R 2
2) .
R2
2: regressy 2 on 1,z 1. At fixed noise and spread, overlap with the other included
regressor reduces precision.
Next, 2SLS uses predicted by2: a second loss of variation.
GPA and partialling-out illustration

### p.27
Use separate fitted variation in stage two
From OLS to fitted schooling: remove the included-variable prediction
Second stage
Regressy 1 on by2,z 1 and an intercept.
Avar(ˆβ1,2SLS)≈ σ2
dSST2(1− bR2
2)
.(15.43)
σ2 =Var(u 1)is the structural-error variance. dSST2 = P
i(byi2 − ¯y2)2: spread in fitted by2.
byi2 = ˆa0 + ˆa1zi1 + ˆri, bR2
2 is this regression’s fit.
A high bR2
2 leaves little fitted variation to distinguishβ 1. This is not the first-stageR 2.

### p.28
Why 2SLS can have a larger standard error
Compare the homoskedastic benchmark with exogenous regressors
Avar(ˆβ1,OLS)≈ σ2
2) ,Avar( ˆβ1,2SLS)≈ σ2
.
Less total spreadThe first stage decomposesy 2 =y ∗
2 +v 2, with orthogonal pieces:
Var(y2)=Var(y ∗
2)+Var(v 2).
Less separate spreadThe included variables may explain much of by2, leaving little
for its own coefficient.
The sample sums-of-squares identity

### p.29
The first stage separates explained and
residual spread
The sums-of-squares identity makes the lost variation visible
OLS first stage with an intercept
yi2 = byi2 + ˆvi2.
(yi2 − ¯y2)2
|          {z          }
SST
=
(byi2 − ¯y2)2
SSE:explained
+
ˆv 2
i2
|{z}
SSR:residual
Thus dSST2 =SSE≤SST 2: fitted schooling cannot contain more spread than actual
schooling. Included regressors then absorb part of this fitted spread too. Under
exogeneity and homoskedasticity, OLS uses the available variation more efficiently.

### p.30
College proximity and precision
Example 15.4: little separate schooling variation
log(wage)=β 0 +β 1educ+c ′γ+u.
• SampleThe same 3,010 men in each regression.
• Excluded IVnearc4: lived near a four-year college in 1966.
• Included exogenous variables cExperience and its square, black, South, current
and 1966 SMSA, and 1966 regional indicators.
educ=π 0 +π nearnearc4+c ′πc +v.
Nearby colleges predict schooling after the same included variables: ˆπnear =.320,
SE=.088,t=3.64.

### p.31
The 2SLS schooling estimate is larger but less
precise
Example 15.4: compare the same model and sample
log(wage)=β 0 +β 1educ+c ′γ+u; excluded instrument:nearc4.
Table 15.1 OLS 2SLS
Schooling coefficient.075.132
Standard error .003 .055
The much larger 2SLS standard error raises the next question: how much fitted
schooling variation remains afterc?

### p.32
How much schooling variation is explained?
Example 15.4: compare the regressions and their fit
c: the same controls as in the wage regression.
educi = ˆa0 +c ′
i ˆa+ ˆei,R 2
c =.4748.
educi = ˆπ0 +c ′
i ˆπc + ˆπnnearc4i
|                     {z                     }
deduci
+ˆvi2,R 2
FS =.4771.
deduci = ˆb0 +c ′
ˆb+ ˆri, bR2
2 =.9951.
The controls explain 99.51% of fitted schooling variation; only 0.49% remains for its
separate effect.

### p.33
Only separate fitted variation identifies the
slope
Example 15.4: fitted spread times its remaining share
log(wage)on 1,c, deduc.
Separate fitted spread10,287.62×(1−.9951478)≃49.92.
Regress deducon 1,c, excludingnearc4. Its small residual spread is the variance
denominator.

### p.34
Validity and precision answer different
questions
A credible identifying direction must also contain enough variation
ValidityExogeneity and relevance determine whether the IV variation can identify
the causal effect.
PrecisionStrength and the amount of separate fitted variation determine how
precisely it does so. Collinearity can be especially costly after prediction has already
reduced the spread.
Since IV can cost precision, we need to check its relevance and ask whether
endogeneity requires it at all.

### p.35
Intro 15-3c
Limited fitted variation reduces precision. Is first-stage significance enough for
reliable inference?

### p.36
What is a weak instrument?
The excluded variables predict little additional regressor variation
Weak instruments have little predictive power fory 2 after the included exogenous
variablez 1.
A weak first stage leaves little instrument-predicted variation for estimating the
structural slope.

### p.37
Recall why weak relevance matters
A small first-stage denominator magnifies a small violation
One-instrument recall
y=β 0 +β 1x+u, with candidate instrumentz.
plim ˆβIV =β 1 + Cov(z,u)
Cov(z,x) .
IfCov(z,x)is close to zero, even a small nonzeroCov(z,u)can cause a large
discrepancy.

### p.38
Test the excluded coefficients
Compare prediction with and without the excluded variables
Unrestricted first stage
educ=π 0 +π 1exper+π 2exper2 +π 3motheduc+π 4fatheduc+v 2.
H0 :π 3 =π 4 =0.
Restricted first stage
educ=π 0 +π 1exper+π 2exper2 +v R.
The restricted model removes only the parents. Does adding them improve
prediction beyond experience?
We use the same 428 observations as the outcome equation. An overall first-stage F
would ask a different question.

### p.39
The first-stage F compares prediction errors
A large reduction in SSR points away from the null
Same test
H0 :π 3 =π 4 =0; restricted excludes parents, unrestricted includes them.
F= (SSRR −SSR UR)/2
SSRUR/423 .
0 3 6 9
5% cutoff
F(2,423)underH 0
Same-sample MROZ
F=55.40, far to the right of the plotted
range.
Reject: the parents jointly add
predictive power after experience.

### p.40
One excluded instrument: use a t test
The same single-coefficient test gives F equal to t squared
One excluded IV
y2 =π 0 +π 1z1 +π 2z2 +v 2; included:z 1, excluded:z 2.
H0 :π 2 =0,F=t 2
π2.
A large|t|(one excluded IV), or a large F (several), is evidence against zero
excluded-variable relevance.
Rejecting zero relevance is not enough to rule out weak instruments; the stronger
screening guideline follows next.

### p.41
Common threshold
Strength requires more than the usual significance cutoff
Same first stage
Test the excluded instruments after all included exogenous variables.
F>10,|t|>
√
10≃3.2 for one excluded IV.

### p.42
Weak IV - testing relevance
State what the first-stage evidence establishes
• State the first-stage equation and identify the excluded coefficients.
• Read the t or joint F and the strength guideline in the context of the design.
• Keep relevance evidence separate from the instrument-exogeneity argument.
Several endogenous variables: optional extension Optional coefficient testing

### p.43
Intro 15-4
IV can avoid omitted-variable bias. Can it also avoid noise in a measured regressor?

### p.44
A new source of endogeneity: measurement
error
15-4: IV can address omitted causes and noise in a regressor
Identification threat
y=β 0 +β 1x+u, withCov(x,u),0.
• Omitted variablesA regressor shares an unobserved cause with the outcome.
We used IV to isolate variation avoiding that cause.
• Measurement errorThe observed value differs from the true value. Does it affect
the outcome or a regressor?
• Classical noise inyadds uncertainty. Classical noise inxcan create endogeneity;
a valid IV can help.

### p.45
Noise in the outcome need not bias the slope
From omitted variables to measurement error: start with outcome noise
True model
y∗ =β 0 +β 1x+u, withCov(x,u)=0.
yobs =y ∗ +e y =β 0 +β 1x+(u+e y).
IfCov(x,e y)=0, then
plim ˆβ1,OLS −β 1 =
Cov(x,u+e y)
Var(x) =0.
Independent outcome noise increases error variance and reduces precision.
Systematic measurement error related toxcan also bias the slope.

### p.46
Start from the true regressor and its observed
measure
Equation 15.45 defines what is measured with error
y=β 0 +β 1x∗
1 +β 2x2 +u.(15.45)
x1 =x ∗
1 +e 1.
The classical measurement-error assumptions give
Cov(e1,x ∗
1)=Cov(e 1,x 2)=Cov(e 1,u)=0.
The true regressors are uncorrelated withu; the measured regressor contains
additional noise.

### p.47
Measurement noise enters the regression error
The measured regressor and transformed error share the same noise
y=β 0 +β 1x1 +β 2x2 +(u−β 1e1).(15.46)
Under the classical assumptions,
Cov(x1,u−β 1e1)=−β 1 Var(e1).
Positive measurement-error variance creates endogeneity whenβ 1 ,0. In the
classical case the OLS slope is biased toward zero.

### p.48
Noise in a regressor attenuates its slope
Classical measurement error adds variation without adding signal
Simple model: omit the control
1 +u, observedx 1 =x ∗
plim ˆβ1,OLS =β 1
Var(x∗
1)
1)+Var(e 1)
|                {z                }
signal share
Under classical noise, the signal share lies between zero and one: the slope moves
toward zero (attenuation). More data does not fix this bias; a valid IV can.
Deriving attenuation

### p.49
Two IV remedies avoid the same
measurement noise
Use the shared signal while avoiding the transformed outcome error
Observed-regressor equation
y=β 0 +β 1x1 +β 2x2 +(u−β 1e1), wherex 1 =x ∗
1 Another measureReport the same true variable through a second measurement
process. Separate sources of error can make uncorrelated measurement noise
plausible.
2 An outside instrumentUse another exogenous variable that predicts the
regressor without correlating withu−β 1e1.

### p.50
Two measures, one true signal
Separate reporting noise needs its own argument
First report, then second report
1 +e 1,z 1 =x ∗
1 +a 1
truex ∗
1
measurex 1 measurez 1
noisee 1 noisea 1
Shared signal motivates relevance; the noise restrictions determine exogeneity.

### p.51
Three conditions for a second measure
Signal, outcome-error exogeneity and separate noise
y=β 0 +β 1x1 +β 2x2 +(u−β 1e1).
• Same signalz 1 =x ∗
1 +a 1: both reports share the true variable; maintain classical
noise restrictions.
• Original outcome errorCov(z 1,u)=0: the second report avoids the other
omitted determinants ofy.
• First report’s noiseCov(a1,e 1)=0: when one report overstates, the other does not
systematically overstate too.
Why relevance holds Why exogeneity holds

### p.52
Example of unrelated measurement errors
A concrete reason to examine the separate-noise assumption
Same true annual salary
1 +e 1 is the worker report;z 1 =x ∗
1 +a 1 is the employer report.
• Possible separate errors
◦ A worker forgets an irregular bonus when recalling annual pay;
◦ An employer assigns a payment to the wrong worker because of a payroll
matching error.
• These mechanisms need not move together.
When a second report is unavailable, consider the other remedy: an outside
instrument.

### p.53
An outside instrument must avoid the
The second remedy does not require a second report
Observed schooling equation
log(wage)=β 0 +β 1educobs +c ′γ+(u−β 1e).
ccontains the included exogenous variables;educ obs =educ ∗ +e. An outside variable
such as parental education is a candidate if it:
• predicts schooling after the included exogenous variables - relevance
• is uncorrelated with both omitted wage determinantsuand schooling-report
noisee. - exogenous
Then it avoids the composite erroru−β 1e. Family-background association withu
remains a reason to question this candidate.

### p.54
Understand the measurement process before
choosing a remedy
Where the error enters determines the bias and the useful extra information
• Locate itIs the noisy variable the outcome or a regressor? Is the error related to
the regressors or true signal?
• Explain itRecall mistakes, recording mistakes and shared omissions imply
different error correlations and potentially different bias directions.
• Find informationA second measure or outside instrument helps only if its noise
and outcome-error relations satisfy the needed IV conditions.
Numerical attenuation example Optional ability indicators

### p.55
Intro 15-5a
Testing for Endogeneity
Testing Overidentifying Restrictions
IV can solve endogeneity problems, but costs precision. Do we need it for this
regressor?

### p.56
Why test for endogeneity?
OLS is more efficient when its explanatory variables are exogenous
Same structural target
y1 =β 0 +β 1y2 +β 2z1 +β 3z2 +u 1.
• Under exogeneity and homoskedasticity, OLS is consistent and more efficient.
• IV uses instrument-predicted variation and can have much larger standard
errors.
• Is the regressor endogenous, making the IV correction necessary?
Under endogeneity, OLS and valid IV generally have different probability
limits.
Recall OLS and IV precision The Hausman comparison

### p.57
Testing for endogeneity
Compare OLS and IV under maintained instrument exogeneity
y1 =β 0 +β 1y2 +β 2z1 +β 3z2 +u 1.(15.49)
Additional excluded IVs:z 3,z 4. Maintain IV exogeneity and the rank condition.
H0 : Cov(y2,u 1)=0.
Under the null, both OLS and 2SLS are consistent. A statistically meaningful
difference can provide evidence of endogeneity.

### p.58
Locate the potentially endogenous component
Equation 15.50 separates prediction from the remaining variation
y1 =β 0 +β 1y2 +β 2z1 +β 3z2 +u 1; allz j are maintained exogenous.
y2 =π 0 +π 1z1 +π 2z2 +π 3z3 +π 4z4|                                  {z                                  }
+v2.(15.50)
Cov(y2,u 1)=Cov(y ∗
2,u 1)+Cov(v 2,u 1)=Cov(v 2,u 1).
The first term is zero because eachz j is uncorrelated withu 1. Any remaining
regressor–error association must come throughv 2.

### p.59
Delta measures the endogenous association
Project the structural error on the first-stage residual
From the first stage
Cov(y2,u 1)=Cov(v 2,u 1), because the predicted part uses valid instruments.
u1 =δ 1v2 +e 1, δ 1 = Cov(v2,u 1)
Var(v2) .
This definese 1, the remainder orthogonal tov 2. Therefore
Cov(y2,u 1)=Cov(v 2,u 1)=δ 1 Var(v2).
With positive residual variance,δ 1 =0 is exactly the regressor-exogeneity condition.

### p.60
Schooling and unexplained wages
15-5a: the null is that schooling is exogenous
NullH 0 :δ 1 =0: schooling is exogenous.
v2: extra schooling;u 1: other wage factors, such as ability.
−3 0 3
−3
0
3 δ1 =0
Extra schoolingv 2
Unexplained wageu 1
Exogenous schooling: its leftover part is
also unrelated to other wage factors.
3 δ1 =.8
Ability can raise both schooling and
wages, creating the upward link.

### p.61
Test whether schooling is endogenous
15-5a: does the extra-schooling component predict wages?
Step 1Predict schooling from both parents andc=(exper,exper 2)′; save
ˆv2 =educ− deduc.
Step 2Add ˆv2 to the wage regression:
log(wage)=β 0 +β 1educ+γ ′c+δ 1 ˆv2 +error.(15.51)
NullH 0 :δ 1 =0: schooling is exogenous. Reject for a significant extra-schooling
coefficient.
MROZ (conventional test) ˆδ1 =.058,t=1.67,p≃.095. At 5%, do not reject:
insufficient evidence of schooling endogeneity.
2SLS coefficient equality Worked schooling test Several regressors

### p.62
Intro 15-5b
We maintained valid instruments. Can extra instruments help us examine that
assumption?

### p.63
One excluded instrument identifies this
equation
Keep the same included variables and structural effect
Same structural model
• The included exogenous variablesz 1,z 2 act as their own instruments.
• Usez 3 as the excluded IV fory 2: maintainCov(z 3,u 1)=0 and relevance after
z1,z 2.
• One excluded IV for one endogenous regressor: the equation isjust identified.

### p.64
A second instrument adds a restriction, not a
parameter
The same equation now has one overidentifying restriction
Cov(z3,u 1)=Cov(z 4,u 1)=0; each IV predictsy 2 beyondz 1,z 2.
Estimate the sameβ 1 usingz 3 alone orz 4 alone.
Two nonredundant excluded IVs, one endogenous regressor:one overidentifying
restriction.
Valid IVs target one slope. Are their estimates compatible?

### p.65
Two parents provide two estimates of the
same effect
Example 15.5: keep the wage model, experience controls and sample fixed
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +u 1. Same 428 women. Instrument
schooling with each parent separately:
Instrument choice Schooling slope SE (rounded)
Mother only.0493.037
Father only .0702.034
Valid parents target the same slope. Are the differences more than sampling
variation?

### p.66
Can both instruments fit one wage effect?
15-5b: extra restrictions let us examine what remains unexplained
Same model
Parents’
education Schooling Log wage
Excluded pathway: assumed absent
Under valid IV restrictions, the parents should not predict the error left after
removing schooling and experience effects. Check the leftovers next.

### p.67
Can the instruments predict the structural
residual?
15-5b: use actual schooling, then regress the leftovers on all exogenous variables
First estimate 2SLSUse both parents, retaining experience and its square. Save the
structural residual
ˆui1 =log(wage i)− ˆβ0 − ˆβ1educi − ˆβ2experi − ˆβ3exper2
i .
Then ask what predicts it
ˆui1 =a 0 +a 1experi +a 2exper2
+a 3motheduci +a 4fatheduci +e i.
The residual regression’sR2
1 measures remaining fit. This is not the first-stage
residual ˆv2.

### p.68
Can parents still explain the leftover wages?
15-5b: look for a wage link beyond schooling and experience
NullParents’ education is unrelated to the other factors inu 1.
Parents’ education Schooling Log wage
Possible link through other wage factors
Large residualR 2
1: parents still explain wages after removing schooling and
experience effects.
Unusually largenR 2
1: reject the IV restrictions.
nR2
a∼χ 2
1. Assumes homoskedasticity and strong identification.
Limits and exact identification Which diagnostic answers which question?

### p.69
The parents pass the residual-fit check
Example 15.8: little remaining wage prediction by the parents
Same residual regression
ˆu1 on 1,exper,exper 2,motheduc,fatheduc.
n R 2
1 nR2
1 p-value
428 .0008833 .3781 .539
Do not rejectH 0 at 5%: parents explain very little of the leftover wage variation.
Compare the three diagnostic questions

### p.70
Intro 15-6
Even with valid instruments, what if the structural error spread varies across
observations?

### p.71
Heteroskedasticity and IV inference
2 solutions
z
u1density
constant spread
changing spread
Illustration only:E(u 1 |z)=0; the variance can vary.
Robust SEs: keep the 2SLS coefficients; recompute uncertainty.
Reweighting: changes estimation under extra variance and exogeneity conditions.
Robust output and interval Weighting intuition

### p.72
Key takeaways from instrumental variables
One target, a credible source of variation, and honest uncertainty
• Identify the effectExogeneity rules out the error channel; relevance supplies
separate regressor variation.15-1–15-2.
• Estimate it2SLS combines valid instruments in a first-stage prediction. Strength
and collinearity determine precision.15-3.
• Diagnose the problemMeasurement mechanisms guide IV remedies. Residual
tests probe regressor endogeneity; extra-IV comparisons probe instrument
compatibility.15-4–15-5.
• Report the evidenceInterpret the effect and uncertainty together. Explain the
economic argument for instrument exogeneity.15-6.
Appendix contents

### p.73
Next Lecture
Prepare for the midterm and Problem Set 2
• Today: Instrumental Variables
Introductory Econometrics, 15-3–15-6
Advanced reference: Wooldridge (2010), Chapter 5
• Next: Midterm Exam (30%), Monday 26 October 2026, 09:00–11:00 —
covers L1–L4
• Then: Additional Single-Equation Topics
Wooldridge (2010), Chapter 6 (Week 9)
• Problem Set 2 due Friday 23 October 2026
Exams are closed book and in person; one double-sided A4 cheat sheet is
allowed.
Adapted from slides by Shuyang Sheng and Qihui Chen

### p.74
Choose an explanation, diagnostic or research application
Estimation and uncertainty
Assumptions and large-sample results
Best linear prediction
One-IV and two-stage equality
Residuals and IV standard errors
Stata, R and Python commands
Diagnostics and applications
Midterm venue map
Measurement error and tests
Midterm Review is a separate slide deck.
Research applications
Back to lecture takeaways

### p.75
Appendix contents: measurement and tests
Detailed arguments stay behind the main intuition
Partialling-out algebra
Attenuation derivation
Second-measure relevance
Second-measure exogeneity
Several endogenous regressors
Coefficient tests after 2SLS
Residual-augmentation algebra
Overidentification limits
Testing changing error variance
Weighted 2SLS
Back to appendix contents

### p.76
西丽小礼堂
Back to midterm arrangements Appendix contents

### p.77
More noise leaves a smaller signal share
L3b simple-model recap: the OLS probability limit moves toward zero
1 +u,x 1 =x ∗
1 +e 1; maintain classical noise and true-regressor exogeneity.
1)+Var(e 1) .
The signal share lies between zero and one. This is a probability limit, not an exact
finite-sample bias formula.
Attenuation after included variables Back to attenuation intuition

### p.78
Shared signal supplies partial relevance
Remove included-variable variation before checking the second report
Two reports
1 +a 1.
AssumeCov(a 1,e 1)=0,Cov(e 1,x ∗
1)=Cov(e 1,x 2)=0, and
Cov(a1,x ∗
1)=Cov(a 1,x 2)=0. Tildes remove population linear predictions on 1,x 2:
Cov(ez1,ex1)=Var( ex∗
1)>0.
The shared true signal must retain positive variance afterx 2.
Back to second-measure conditions

### p.79
Separate noise supplies instrument
exogeneity
Check the second report against the entire transformed error
Outcome error
u−β 1e1; instrumentz 1 =x ∗
Cov(z1,u−β 1e1)=Cov(z 1,u)−β 1 Cov(z1,e 1).
The first term is zero by assumption; the second is zero because
Cov(z1,e 1)=Cov(x ∗
1,e 1)+Cov(a 1,e 1)=0.
ThereforeCov(z 1,u−β 1e1)=0.

### p.80
Assumptions 2SLS.1–2SLS.4
Intro 15A states the conditions for consistency
• 2SLS.1: Linear in parameters
y=β 0 +β 1x1 +· · ·+β kxk +u.
• 2SLS.2: Random samplingA random sample ony, thex j and thez j.
• 2SLS.3: RankNo perfect linear relationships among IVs; the rank condition for
identification holds.
• 2SLS.4: Exogenous IVs
E(u)=0,Cov(z j,u)=0 for every IV .
Theorems and homoskedasticity
Back to the 2SLS conditions

### p.81
Intro 15A: consistency and normal inference
Homoskedasticity is an additional condition
Theorem 15A.1Under Assumptions 2SLS.1–2SLS.4, the 2SLS estimator is consistent.
2SLS.5: HomoskedasticityFor the collection of IVsz,
E(u2 |z)=σ 2.
Theorem 15A.2Under Assumptions 2SLS.1–2SLS.5, the 2SLS estimators are
asymptotically normally distributed.
Estimate the variance using the structural residuals and the IV variance formula.
With heteroskedasticity, adjust the covariance.

### p.82
Linear combinations preserve exogeneity
Relevance is a separate requirement
Maintained moments
E(u1)=0,Cov(z j,u 1)=0 forj=1,2,3.
For fixed coefficientsa j, leta=a 0 + P3
j=1 ajzj.
Cov(a,u 1)=
This establishes orthogonality. A particular linear combination can still have zero
predictive power through cancellation.
Back to combining the instruments

### p.83
Why the projection maximizes correlation
Projection orthogonality and Cauchy–Schwarz give the result
2 +v 2, withCov(z j,v 2)=0. Letabe a nonconstant linear combination of the
IVs.
Cov(y2,a)=Cov(y ∗
2,a).
Corr(y2,a) 2 ≤
Var(y∗
2) Var(a)
Var(y2) Var(a) =
Var(y2) .
Equality holds fora=y ∗
2 when its variance is positive. Other combinations can be
irrelevant despite being exogenous.
Back to the population prediction

### p.84
The projection minimizes squared prediction
Population coefficients are pi; candidate coefficients are a
For candidate coefficientsa=(a 0,a 1,a 2,a 3), the population projection solves
π=arg min
a
E[(y2 −a 0 −a 1z1 −a 2z2 −a 3z3)2].
The first-order conditions giveE(v 2)=0 andE(z jv2)=0, where
v2 =y 2 −π 0 −π 1z1 −π 2z2 −π 3z3.
The minimizing coefficients areπ j; hats denote their sample estimates.
The correlation bound Back to the population prediction

### p.85
Why excluded relevance identifies the scalar
effect
Included-variable moments alone leave one slope undetermined
E(u1)=0,E(z 1u1)=0.
Two moments cannot generally determineβ 0, β1, β2. An excluded instrument must
supply information beyondz 1.
The remaining scalar moment
Back to excluded predictive variation

### p.86
Use an excluded IV after removing the
included variable
A nonzero denominator determines the remaining slope
Residualized equation
˜y1 =β 1 ˜y2 +u 1. Tildes remove population predictions on 1,z 1;z j,j∈ {2,3}, is an
excluded IV .
E(˜zju1)=0=⇒β 1 =
E(˜zj ˜y1)
E(˜zj ˜y2) ,E( ˜zj ˜y2),0.
Relevance requires a nonzero denominator.

### p.87
Population projection and sample OLS
Both solve least-squares prediction problems
Letz i =(1,z i1,z i2,z i3)′.PopulationMinimize expected squared error:
E[(y2 −z ′a)2].
SampleMinimize the sample average:
ˆπ=arg min
n
(yi2 −z ′
i a)2.
This is OLS; multiplying bynleaves the minimizer unchanged.
Compare their normal equations Back to population and sample

### p.88
Matching normal equations
Both concern prediction residuals, not the structural error
Prediction residual Orthogonality
v2 =y 2 −z ′πE(zv 2)=0
ˆvi2 =y i2 −z ′
i ˆπ P
i zi ˆvi2 =0
IV exogeneity is a separate maintained assumption:E(zu 1)=0.
Back to population and sample

### p.89
First stage: predict schooling
One-IV recap: the father-only model just introduced
educ=π 0 +π 1fatheduc+r
0 5 10 15
5
15
A
B
Father’s education
Education
Each dot is one woman.
Keep the fitted schooling deduci.
Separate the remaindereduc i − deduci.
Instrument exogeneity is the
maintained assumption about the
fitted part.
Second-stage picture Back to one-IV equivalence

### p.90
Second stage: use predicted schooling
Example 15.1: retain the instrument-linked component
log(wage)i =a+b deduci +η i
10 11 12 13 14 15
−2
−1
3 A
Predicted education
log(wage)
Same women A and B
Use fitted schooling on the
horizontal axis; log wages stay
fixed.
IV slope.0592.
Back to one-IV equivalence

### p.91
A fitted value is predicted schooling, not a
wage
Example 15.5: calculate one woman’s first-stage prediction
First woman
exper=14,motheduc=12,fatheduc=7.
deduc=9.1026+.0452exper−.0010exper 2 +.1576motheduc+.1895fatheduc.
What fitted education does this rule assign to her?
9.1026+.0452(14)−.0010(14 2)+.1576(12)+.1895(7)≃12.76.
Use her fitted value with her wage and controls in stage two.
Back to the first-stage prediction

### p.92
First stage: predict the regressor with one IV
The same sample and an intercept in both regressions
yi =β 0 +β 1xi +u i; one IV:z i.
First-stage OLS
ˆxi = ˆπ0 + ˆπ1zi, ˆπ1 =
dCov(z,x)
dVar(z)
The direct IV formula is
ˆβ1,IV =
dCov(z,y)
Sample moments: dVar(z)>0 and dCov(z,x),0.
Substitute the fitted value Back to one-IV equivalence

### p.93
Second stage: substitute the fitted value
Constants drop from sample covariance and variance
First-stage fit: ˆxi = ˆπ0 + ˆπ1zi. OLS ofy i on ˆxi, with an intercept, gives
ˆβ1,2SLS =
dCov(ˆx,y)
dVar(ˆx)
Substitute the first-stage fit:
dCov(ˆx,y)= ˆπ1 dCov(z,y),
dVar(ˆx)= ˆπ2
dVar(z).
Cancel the first-stage slope Back to one-IV equivalence

### p.94
Cancel the first-stage slope
One excluded IV makes the coefficient formulas identical
Use ˆπ1 = dCov(z,x)/ dVar(z),0.
ˆβ1,2SLS = ˆπ1 dCov(z,y)
ˆπ2
ˆπ1dVar(z)
Substitute ˆπ1 and cancel the sample variance:
[ dCov(z,x)/ dVar(z)]dVar(z)
= ˆβ1,IV.
First-stage OLS gives ˆx= ¯x, so the intercepts also agree. Coefficients agree; inference
still needs IV standard errors.

### p.95
The residuals differ at every candidate
coefficient
Actual schooling and predicted schooling define different regression errors
Define ˆvi2 =y i2 − byi2. At anyb=(b 0,b 1,b 2)′:
ui1(b)=y i1 −b 0 −b 1yi2 −b 2zi1,
ei1(b)=y i1 −b 0 −b 1byi2 −b 2zi1.
Subtract:
ui1(b)=e i1(b)−b 1 ˆvi2.
Why the moment equations coincide Back to IV and OLS equivalence

### p.96
First-stage orthogonality removes the
difference
The instruments and second-stage regressors are the same vector
Forw i =(1, byi2,z i1)′, first-stage OLS gives P
i wi ˆvi2 =0: each element is a first-stage
regressor or their linear combination. Weight the residual identity byw i and sum:
wiui1(b)=
wiei1(b).
SSR normal equations Back to coefficient equality

### p.97
Second-stage least squares solves the IV
equations
Full rank gives the same unique coefficients
IV definitionSolve P
i wiui1(b)=0. Second-stage OLSMinimize P
i ei1(b)2. Its
normal equations are
∂
∂b
ei1(b)2 =−2
wiei1(b)=0.
Full rank gives the same unique coefficients on the same sample and controls.
The minimized SSR usese, not structuralu. Validity remains a separate assumption.
Back to IV and OLS equivalence

### p.98
Population and sample IV moments
The structural residual is the same in all three sample conditions
Population condition Sample analogue
E(u1)=0 P
i ˆui1 =0
E(z1u1)=0 P
i zi1 ˆui1 =0
E(y∗
2u1)=0 P
ibyi2 ˆui1 =0
These three sample equations jointly determine ˆβ0, ˆβ1, ˆβ2.
Back to IV equations

### p.99
Why the composite error is orthogonal
IV exogeneity is assumed; projection orthogonality follows from least squares
Composite error
˜u1 =u 1 +β 1v2.
Two sources of zero covariance
• IV exogeneity:Cov(y ∗
2,u 1)=0, sincey ∗
2 is a linear combination of valid IVs.
• Projection orthogonality:Cov(y ∗
2,v 2)=0.
2, ˜u1)=Cov(y ∗
2,u 1)+β 1 Cov(y∗
2,v 2)
=0+β 1(0)=0.
Back to the substitution intuition

### p.100
Compute structural residuals
Use actual schooling in the wage equation
Schooling standard error Value
IV: structural residuals .03144
Naive second-stage OLS .03296
IV versus naive SEs Two residuals Variance calculation
Back to IV software and uncertainty

### p.101
Structural and second-stage residuals
The difference is the fitted coefficient times the first-stage residual
ˆei1 =log(wage i)− ˆβ0 − ˆβ1 deduci − ˆβ2experi − ˆβ3exper2
ˆei1 − ˆui1 = ˆβ1(educi − deduci).
Back to structural residuals

### p.102
Same woman, two different residuals
Actual schooling gives the structural error estimate
log(wagei)= ˆβ0 + ˆβ1educi +c ′
i ˆγ+ ˆui.
For this woman,educ=12, deduc=12.7560,log(wage)=1.2102.
Schooling used Predicted log wage Residual
Actual: 12 1.2270 −.0169
Fitted: 12.7560 1.2735 −.0633

### p.103
Estimating structural error variance
Use the number of structural coefficients in the degrees of freedom
Two-parent MROZ
n=428; intercept plus 3 slopes, sok+1=4.
ˆσ2 =
i ˆui12
n−k−1 = 193.0200
424 =.45524.
dVar(ˆβ)= ˆσ2(bX′bX)−1.
Columns of bX: 1, deduc,exper,exper 2. This conventional covariance uses Intro
2SLS.1–2SLS.5.

### p.104
Estimate 2SLS in Stata
Specify the outcome, explanatory variables and excluded instruments
Same MROZ model
Outcome:lwage; endogenous:educ; included exogenous:exper,expersq; excluded IVs:
motheduc,fatheduc.
ivregress 2sls lwage exper expersq ///
(educ = motheduc fatheduc), small
The small option matches the conventional degrees-of-freedom correction shown
here.
R command Python command Back to IV software and uncertainty

### p.105
Estimate 2SLS in R
ivreg(lwage ˜ educ + exper + expersq |
exper + expersq + motheduc + fatheduc,
data = d)
Use theivregpackage. Its conventional covariance matches the comparison shown

### p.106
Estimate 2SLS in Python
lwageoneduc,exper,expersq; excluded IVs:motheduc,fatheduc.
IV2SLS.from formula(
"lwage ˜ 1 + exper + expersq + "
"[educ ˜ motheduc + fatheduc]",
data=d).fit(cov type="unadjusted",
debiased=True)
linearmodels.iv; options match the conventional covariance.

### p.107
The partialling-out algebra
Residual regressor variation determines a separate slope
OLS model
For observationi, letr i2 be the sample OLS residual from regressingy 2 on 1,z 1; letr i1
be the analogous outcome residual.
ˆβ1 =
i ri2ri1
i r2
r2
i2 =SST 2(1−R 2
2).
With fittedby2, repeat the same removal of 1,z 1 to obtain the IV denominator in
equation15.43.
Back to the remaining-variation picture

### p.108
Partialling out reproduces the OLS slope
The partialled regression reproduces the full OLS slope
Full OLS
colGP Ai =β 0 +β 1hsGP Ai +β 2ACTi +u i.
1 RegresshsGP Aon an intercept andACT. Keep ˆri1 =hsGP Ai − [hsGP Ai.
2 RegresscolGP Aon an intercept and ˆri1; call its slope ˆb1.
ˆb1 = ˆβ full OLS
1 .
ˆri1 isolates GPA variation beyond ACT. ThisFWL identityconcerns the coefficient,
not causality.
GPA residual gaps Back to OLS precision

### p.109
More overlap leaves smaller residual gaps
College GPA on high-school GPA and ACT: compare residual gaps
colGP A=β 0 +β 1hsGP A+β 2ACT+u,SST 2 =1.12.
15 20 25 30
2.5
3
3.5
4 R2
2 =0.25
ACT
hsGP A
2 =0.90
Residual-regression plots Back to OLS precision

### p.110
Smaller gaps leave less horizontal spread
Less unique spread reduces precision; the two samples need not have equal slopes
−0.5 0 0.5
3 R2
ˆb1 = ˆβ1 =.702
ˆri1
colGP A
ˆb1 = ˆβ1 =1.190
Partialling-out algebra Back to the precision benchmark

### p.111
More than one endogenous regressor
15-3d: optional; use every instrument in every first stage
y1 =β 0 +β 1y2 +β 2y3 +β 3z1 +β 4z2 +β 5z3 +u 1.(15.44)
Supposez 4,z 5 are additional exogenous variables excluded from this model.
• Regress each ofy 2,y 3 on all five IVs and an intercept.
• In stage two retainz 1,z 2,z 3 and replace both endogenous regressors by their
fitted values.
• Two endogenous regressors require at least two excluded IVs; this count is
necessary, not sufficient.
Why counts alone are insufficient Back to first-stage prediction

### p.112
Order and rank
Two instruments can supply only one direction of variation
After controls
y=β 1x1 +β 2x2 +u, with exogenous instruments.
Population reduced-form slopes after controls:
Excluded IV Slope forx 1 Slope forx 2
z1 1 2
z2 2 4
Both identify onlyβ 1 +2β 2. The second direction repeats the first.
Alternative slope pairs Rank condition Back to first-stage prediction

### p.113
Identification requires unique coefficients
Different slope pairs can fit the same population moments
Same first-stage directions
z1 : (1,2),z 2 : (2,4). Outcome responses are 3 and 6.
Candidate slopesβ 1 +2β 2 2β1 +4β 2
(1,1)3 6
(3,0) 3 6
Both fit the moments: the two slopes are not separately identified.
Back to first-stage prediction

### p.114
Rank and population moments
The matrix statement supports Intro Assumption 2SLS.3
Column vectors
y=x ′β+u. Herexis(k+1)×1 andzisL×1; both include the intercept, andzincludes
all exogenous regressors.
E(zu)=0=⇒E(zx ′)β=E(zy).
rankE(zz ′)=L,rankE(zx ′)=k+1.
The second condition gives enough independent moment restrictions to determine
the coefficient vector;L≥k+1 alone is insufficient.
Practical rank checks Back to independent directions

### p.115
Practical checks of the rank condition
Check relevance for the whole instrument–regressor system
Identification requirement
rankE(zx ′)=k+1, with all included exogenous regressors inz.
One endogenous variable
Run its full first stage and jointly test only the excluded-IV coefficients. A
conventional F uses first-stage homoskedasticity; a robust Wald test allows it to fail.
Rejection supplies evidence of nonzero partial relevance. Strong identification and
instrument exogeneity require further assessment.
Several endogenous variables Back to independent directions

### p.116
Rank checks with several regressors
Significant separate regressions can still repeat one direction
Same requirement
rankE(zx ′)=k+1.
Use the same complete IV list in every first stage.
Full rank requires independent prediction directions across the regressors.
Sample moment matrix:Z ′X/n.
Check these directions jointly in the system.
Back to independent directions

### p.117
Test a coefficient with its IV standard error
15-3e: optional; use the large-sample IV reference
H0 :β 1 =b 1,0,t=
ˆβ1 −b 1,0
seIV( ˆβ1)
a∼N(0,1).
Null Estimate IV SEt
β1 =0.06140.03144 1.953
This does not reach the approximate two-sided 5% cutoff 1.96.
Joint coefficient test Back to the first-stage block

### p.118
A joint test asks a joint economic question
Use the covariance from the IV estimate
H0 :β 2 =β 3 =0.
Do the experience terms matter jointly, conditional on schooling?
Conventional IV test Degrees of freedomp
Waldχ 2 =19.64 2 .000054
The usual OLS SSR-difference formula is not a valid shortcut after 2SLS.
Why the IV fit shortcut fails Back to first-stage prediction

### p.119
Why IV R-squared is not an OLS fit measure
Use IV covariance for joint tests, not an OLS SSR shortcut
ˆui =y i −x ′
i ˆβIV,R 2
IV =1−
i ˆui2
i(yi − ¯y)2 .
• IV does not minimize the outcome equation’s residual sum of squares. ItsSSR
can exceedSST, making thisR 2 negative.
• Restricted and unrestricted IV fits need not have the OLS SSR ordering.
• Use the covariance-based joint test reported by IV software. Fit measures
prediction; validity rests on the IV assumptions.
Back to joint coefficient tests

### p.120
The Hausman comparison
Evaluate the coefficient difference against its sampling uncertainty
Null
The regressor is exogenous; the instruments are maintained valid.
Under the efficient-OLS assumptions, compareβ 1. Let bV1,j estimateVar( ˆβ1,j), for
j=IV,OLS.
d= ˆβ1,IV − ˆβ1,OLS,H= d2
bV1,IV − bV1,OLS
1.
Require a positive variance difference. A largeHsupplies evidence of endogeneity;
robust comparisons need an appropriate covariance.
Back to why test for endogeneity

### p.121
Why residual augmentation reproduces the
IV coefficient
The fitted and residual parts span the actual regressor
Identity
y2 = by2 + ˆv2, with first-stage residual orthogonal to the instruments.
β1y2 +δ 1 ˆv2 =β 1by2 +(β 1 +δ 1)ˆv2.
In the augmented regression,by2 is orthogonal to ˆv2, conditional on included
variables. Its coefficient is the same as the two-stage coefficient.
Why the new error is orthogonal Back to the residual-augmentation test

### p.122
Why the new error is orthogonal
The error projection removes the endogenous component
Error decomposition
u1 =δ 1v2 +e 1, withCov(v 2,e 1)=0; first stagey 2 =y ∗
2 +v 2.
Cov(zj,e 1)=Cov(z j,u 1)−δ 1 Cov(zj,v 2)=0.
The first term is zero by IV exogeneity; the second by first-stage projection. Sincey ∗
is a linear combination of thez j,
Cov(y2,e 1)=Cov(y ∗
2,e 1)+Cov(v 2,e 1)=0.
Back to the component-slope argument

### p.123
Reading an endogeneity test
Read significance and economic size together
• RejectionEvidence of regressor endogeneity, maintaining valid
instruments and the model.
• NonrejectionThe data did not distinguish the estimates sufficiently;
assess precision and economic differences.
• Several suspect regressorsSave each first-stage residual, add them all to
the structural regression and test them jointly.
Back to the residual-augmentation test

### p.124
Why omitted ability can raise the OLS
Two positive links suggest an upward omitted-variable contribution
log(wage)=β 0 +β 1educ+c ′γ+θabil+e.
education
ability
log wage
+ +
Ability raises wages; schooling and ability tend to move together after the included
variables.
Conditional bias formula Back to OLS versus IV

### p.125
The omitted-variable-bias interpretation
The observed estimate difference is consistent with this mechanism
Same full model
plim ˆβOLS =β 1 +θ Cov( geduc, gabil)
Var( geduc)
The tildes remove the included experience terms. Positiveθand positive covariance
of residualized schooling and ability imply an upward contribution.
This mechanism predicts a higher OLS slope when ability raises both schooling and
wages.
Back to the OLS and IV comparison

### p.126
What an overidentification test can establish
Interpret the restrictions jointly for the instrument set
• RejectionReview the instrument set: at least one maintained restriction conflicts
with the model.
• NonrejectionRetain the joint restrictions at the chosen significance level; assess
the economic argument for each IV .
• Exact identificationIfq=0, the residual regression hasR 2 =0 algebraically.
There is no overidentification test.
With heteroskedasticity, use an appropriate robust overidentification test.
Back to the residual-fit test

### p.127
Three diagnostic questions
Use the test that matches the assumption at issue
Question Evidence
Are the IVs relevant after
controls?
Excluded-instrument first-stage test.
Is the suspect regressor
endogenous?
Add its first-stage residual to the structural
equation.
Are extra IV restrictions
compatible?
Overidentification test using structural
residuals.

### p.128
Testing for heteroskedasticity after 2SLS
Local two-parent reproduction; the textbook uses three IVs
NullIntro 2SLS.5:E(u 12 |z)=σ 2.
ˆui1 2 =a 0 +a 1zi1 +· · ·+a mzim +e i.
TestH 0 :a 1 =· · ·=a m =0 under the additional regularity conditions linked below.
Local two-parent MROZ Degrees of freedomp
F=3.160(4,423) .0141
The test rejects constant variance. Robust IV SEs require no pretest.
Test conditions Back to changing error spreads

### p.129
Conditions behind the auxiliary
heteroskedasticity test
A squared-residual test has requirements beyond robust estimation
Auxiliary regression
Sufficient additional conditions for the auxiliary F test include
E(u1 |z)=0,E(u 14 |z)constant,Cov(x,u 1 |z)constant.
Robust IV standard errors do not require a preliminary rejection of constant
variance.
Back to changing error spreads

### p.130
Weighted two-stage least squares
Transform the outcome, regressors and instruments together
MaintainE(u i |z i)=0 andVar(u i |z i)=h i >0. Suppose the variance model can be
consistently estimated by ˆhi.
yi
q
ˆhi
xij
zij
• Divide the intercept too: it becomes 1/
ˆhi.
• Apply 2SLS to the transformed equation using the transformed instruments.
Back to the changing-spread summary

### p.131
Theorem 15A.3: efficiency
Efficiency is conditional on the assumptions and comparison class
Theorem 15A.3Under Assumptions 2SLS.1–2SLS.5, the 2SLS estimator is
asymptotically efficient in the class of IV estimators that uses linear combinations of
the exogenous variables as instruments.
• This is an asymptotic statement with valid instruments and homoskedasticity.
• Under heteroskedasticity, robust SEs adjust inference; ordinary 2SLS need not be
efficient.
• Adding instruments requires additional valid restrictions and may create
finite-sample problems.

### p.132
Noise can halve the OLS slope
Numerical attenuation example: true slope two
y=2x ∗ +u,x 1 =x ∗ +e 1.
Assume mutually uncorrelatedx ∗,u,e 1, withVar(x ∗)=Var(e 1)=1. What happens to
slope two?
plim ˆβOLS = Cov(x1,y)
Var(x1) = 2
1+1 =1.
The observed regressor has twice the true signal’s variance, while its covariance
withyis unchanged.
Recover the signal with a second report Back to measurement-error remedies

### p.133
A separate report recovers the signal
The same example: IV probability limit two
y=2x ∗ +u,x 1 =x ∗ +e 1,z 1 =x ∗ +a 1.
The componentsx ∗,u,e 1,a 1 are mutually uncorrelated;Var(x ∗)=Var(e 1)=1. Then
Cov(z1,y)=2 andCov(z 1,x 1)=1.
plim ˆβIV = Cov(z1,y)
Cov(z1,x 1) = 2
1 =2.
The shared true signal links the reports; uncorrelated measurement noise does not
enter their covariance.
Back to measurement-error remedies

### p.134
Two indicators of ability
Separate the latent variable from both test-score errors
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +abil+u.(15.47)
test1 =γ 1abil+e 1,test 2 =δ 1abil+e 2, γ 1, δ1 >0.
With ability included, schooling is exogenous relative tou. Let
x=(educ,exper,exper 2). The maintained error assumptions include
Cov(ej,x)=0,Cov(e j,abil)=0,j=1,2,
Cov(e1,e 2)=0,Cov(test j,u)=0,Cov(x,u)=0.
Substitute the first indicator Back to measurement-error remedies

### p.135
Substitute the first ability indicator
Its measurement noise enters the outcome error
Indicator
test1 =γ 1abil+e 1, soabil=test 1/γ1 −e 1/γ1.
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2
+α 1test1 +(u−α 1e1), α 1 =1/γ 1. (15.48)
The new error isε=u−α 1e1. A noisy indicator is included; ability no longer
remains entirely omitted.
Which variable needs the IV? Back to measurement-error remedies

### p.136
The noisy indicator needs the instrument
Schooling is exogenous under the stated indicator assumptions
Transformed model
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +α 1test1 +ε, whereε=u−α 1e1.
Under the preceding assumptions,
Cov(educ, ε)=0.
Cov(test1, ε)=−α 1 Var(e1),Cov(test 2, ε)=0.
IQ and KWW example Back to measurement-error remedies

### p.137
IQ is instrumented by KWW
Example15.6: schooling remains included
Wage equation
log(wage)=β 0 +β 1educ+α 1IQ+control effects+ε; IV for IQ:KWW.
KWWis a knowledge-of-the-world-of-work test score. Included controls:
experience, tenure, marital status, south, urban and race indicators.
Schooling estimate Conventional SEn
.0250 .0166 935
The schooling estimate is small and imprecise. Shared measurement noise could
explain the puzzle.
Compare the two ability strategies Back to measurement-error remedies

### p.138
Two ability strategies use different
assumptions
The outcome error determines which variable needs an instrument
Ability remains omitted A noisy ability indicator is included
Schooling may correlate with
omitted ability in the error.
Indicator noise enters the
transformed error.
Use an IV for schooling unrelated to
that error.
Use a second valid indicator as an
IV for the first.
An IV that is credible for one equation may fail for the other. Specify the model and
error before judging validity.

### p.139
Example 15.7: is schooling endogenous?
The two-parent MROZ test gives limited evidence
Augmented wage regression
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +δ 1 ˆv2 +error.
The first stage uses both parents and the same experience terms;n=428.
Residual coefficient SEtApprox.p
.0582.0348 1.67 .095
At 5%, do not reject schooling exogeneity: the sample gives insufficient evidence of
endogeneity. Report the OLS and IV estimates.
Back to endogeneity-test sequence

### p.140
When would error spreads vary?
Different observations can have different conditional uncertainty
Var(u1 |z)=h(z).
• Conditioning variablesIn the wage example,zincludes experience and the
parental-education instruments.
• Wage uncertaintyWorkers with different experience can have different error
spreads, even after allowing experience to affect the fitted mean.
• The mean relation can remain correctly specified while the error spread changes
with these exogenous variables.
Optional heteroskedasticity test
Back to changing-spread summary

### p.141
MROZ: the coefficient stays fixed
The covariance choice changes uncertainty for the same model
Schooling coefficient Conventional HC1 robust
Estimate.06140.06140
SE .03144 .03334
Same 428 observations, included variables and instruments. Robust covariance
changes the standard error, not the coefficient.
In Stata, addvce(robust) smallto the earlier IV command;smallapplies the
degrees-of-freedom correction.
Read the robust interval Back to changing-spread summary

### p.142
MROZ: read the robust interval
An interval describes uncertainty under the maintained IV assumptions
Two-parent model
ˆβ1 =.06140,se HC1 =.03334.
.06140±1.96(.03334).
Approximate 95% interval:[−.0039, .1267].
The interval includes zero. Robust SEs may be larger or smaller than
conventional SEs.
Why error spread can vary Back to changing-spread summary

### p.143
A weighted alternative
Downweight observations with larger conditional error variance
Two distinct tasks
Robust standard errors allow changing error spreads when calculating uncertainty.
Weighted 2SLS additionally changes the estimation weights: observations with
larger estimated error variance receive less weight.
The variance model needs justification. Transform the outcome, explanatory
variables and instruments together.
Optional weighted-2SLS procedure Optional efficiency theorem

### p.144
Attenuation with included variables
Use the signal remaining after included variables
1 +β 2x2 +u; observedx 1 =x ∗
Tildes remove the linear prediction on 1,x2. Maintain classical noise and
true-regressor exogeneity.
Var(ex∗
Other coefficients need not attenuate toward zero.
Back to the attenuation formula

### p.145
Further IV applications
Optional research examples beyond the main lecture
El Ni˜no and trade: short overview
Pollution and exports
Appendix contents Lecture takeaways

### p.146
Climate shocks can synchronize harvest risks
El Nino and trade — shared shocks can limit gains from trade
• Economic setting: countries can use trade to share local cereal-production
risks.
• Complication: when climate shocks move harvests together, trading
partners may be hit at the same time.
• Dingel, Meng and Hsiang study how cereal productivity and its global
spatial correlation relate to domestic expenditure shares.
Temperature and ENSO supply candidate productivity variation; a physical
shock still needs an outcome-specific exclusion argument.
Back to lecture takeaways IV argument

### p.147
Climate variation still needs an exclusion
argument
El Nino and trade — relevance and validity remain separate
Temperature
and ENSO
Cereal
productivity
Domestic
expenditure
share
Direct
trade costs
Know the restriction: climate must not shift domestic shares through
unmodeled trade-cost pathways.
Back to lecture takeaways El Nino summary

### p.148
Pollution can reduce export revenue
He, Sheng and Zhang — a recent study of Chinese manufacturers
log(exports)=β 0 +β 1 log(PM2.5)+included factors+u
• Chinese firm-product export observations, 2000–2007.
• More production can generate more pollution; local economic conditions
can also move both variables.
• The study uses thermal inversion days as an instrument for pollution.
He, Sheng and Zhang, Journal of Public Economics (2026).
Back to lecture takeaways Inversion mechanism

### p.149
A warm upper layer traps ground-level
pollution
The inversion mechanism supplies first-stage relevance
Warmer air above
Cooler air and trapped pollutants
Mechanism: warmer air limits vertical dispersion.
Back to lecture takeaways First-stage evidence

### p.150
Inversion days predict pollution
The first stage addresses relevance
log(PM2.5)=π 0 +π 1 log(inversion days)+included factors+v
• More inversion days predict higher pollution after the included
adjustments.
• The published first-stage coefficient is 0.0653, with standard error 0.007.
Back to lecture takeaways Exclusion

### p.151
A physical instrument still requires
Weather and other pollutants are concrete exclusion concerns
Inversion
days Pollution Exports
Other weather
pathway
Weather and copollutant pathways need scrutiny.
Back to lecture takeaways Published estimate

### p.152
Interpret the IV estimate in percentage units
Published Table 2, column 2 — separate relevance from validity
IV export-value specification Estimate (SE)
First stage:log(inversion days)0.0653(0.007)
Export equation:log(PM 2.5)−0.9179(0.410)
Observations 3,046,936
• Under the assumptions, 1% higher pollution implies about 0.92% lower
export revenue.
• Relevance uses the first stage; exclusion uses the institutional argument.
Back to lecture takeaways Pollution and exports