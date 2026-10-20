### p.1
Lecture 3b:
Linear Regression
Enjie (Jack) Ma
Lecture 3 · Monday 28 September 2026

### p.2
Announcements
Office hours move; slides and Problem Set 1
• Office hours, new time:Monday 12:00–13:00, Xili Campus 6A204 — right
after class.
• Slides:the no-animation version of each lecture is now on Blackboard.
• Problem Set 1:due Sunday 11 October 2026.

### p.3
Roadmap (3b)
Uncertainty, omitted variables and measurement error
OLS Uncertainty and Inference
OLS Solutions to the Omitted Variables Problem
OLS under Measurement Error

### p.4
Where we stopped
Tests need the centre, the spread and the shape of the sampling distribution
0 0.01 0.02
0
50
100
150
pool slope .00813
OLS slope, samples of 500
samples
• Centre: ˆβ
p
− →βunder OLS.1–OLS.2
(unbiased ifE(u|x)=0). Done in 3a.
• Spread: how much ˆβvaries⇒its
variance and standard error. Today.
• Shape: normal, by either of two routes:
◦ normal homoskedastic errors⇒
exact normality givenX;
◦ no normality, largeN⇒
approximately normal (Theorem 4.2).

### p.5
Roadmap
Wooldridge 4.2.2–4.2.3 — current location in blue
OLS.3 and Standard Errors
Testing Hypotheses
OLS Ignoring the Omitted Variables
Proxy Variable–OLS Solution
Interactions in Unobservables: Random Coefficients
Measurement Error in the Dependent Variable
Measurement Error in an Explanatory Variable

### p.7
From sampling spread to a standard error
Homoskedasticity gives a familiar uncertainty formula
THE FAMILIAR ASSUMPTIONS
E(u|x)=0,Var(u|x)=σ 2 .
• Homoskedasticity: the error has the same spread at every value of the
regressors.
• Standard error: our estimate of how much ˆβj varies across samples.
• The assumptions above imply OLS.3, which simplifies this calculation.
How the assumptions imply OLS.3 From variance to standard error
Does the error have the same spread at every schooling level?
Standard errors in the attendance example

### p.8
Homoskedasticity in a picture
The mean line stays fixed; the spread changes
educ
wagedensity
E(wage|educ)
homoskedastic: constant spread
heteroskedastic: spread grows witheduc
Wages ateduc=8and ateduc=16: the same spread, or a wider one at16?
Which picture, and why?

### p.9
Why wages spread out with schooling
A wider range of jobs can produce a wider range of wages
wage=β 0 +β 1educ+u,E(u|educ)=0.
• More schooling may open a wider range of jobs and wages.
• With little schooling, wages may cluster near the minimum wage.
• A changing spread makes constant conditional variance doubtful.
How can one sample tell us about an unknown population coefficient?

### p.11
From a sample to the population
Inference concerns the unknown population coefficient
• Statistical inference: use sample data to draw conclusions about
population parameters.
Population Our sample
βj: fixed but unknown ˆβj: an estimate
Changes from sample to sample
• Hypothesis testing is based onpopulationparameters, using estimate from
a particularsample.

### p.12
Inference in one picture
The sample gives ˆβj; inference reasons back toβ j
Population
y,x
βj
fixed, unknown
Our sample
yi,x i
ˆβjvaries across
random sampling
tests and intervals
What would we expect to see ifβ j =0?

### p.13
The null hypothesis
Does this regressor have a nonzero partial effect?
y=β 0 +β 1x1 +· · ·+β j xj +· · ·+β KxK +u(4.1)
H0 :β j =0,H 1 :β j ,0 (two-sided alternative).
• H0: once the other regressors are accounted for,x j has no effect onE(y|x).
• We observe ˆβj, which is rarely 0. How far is ˆβj from zero?
◦ If ˆβj is very far, then it’s evidence against nullH0
◦ But ˆβj varies also because of sampling errors!⇒have to take that into
account.
One-sided alternatives

### p.14
The t statistic
Measure the estimate in standard-error units
H0 :β j =0: ˆtj =
ˆβj
se( ˆβj)
.
• ˆtj is the distance from zero in estimated standard deviations.
• A large| ˆtj|is evidence againstH 0: reject when| ˆtj|>c.
• UnderH 0: approximatelyN(0,1)under OLS.1–OLS.3 in large samples;
exactt N−K under the normal homoskedastic model.
The t distribution Testing a nonzero value
How far from zero should the rejection cutoff be?

### p.15
Type I error
Rejecting a true null hypothesis
• Type I error: rejectH 0 when it is true;
Pr(rejectH 0 |H 0 true)≈α.
• α=.05: ifH 0 is true, about 5 samples in 100
still reject.
• 2.5%per tail:−candcare the 2.5th and
97.5th percentiles.
• Smallerαor few degrees of freedom: larger
c(1.645, 1.96, 2.576 at 10, 5, 1%).
−1.96 0 1.96
2.5%2.5%
2.5th pct 97.5th pct
ˆtj underH 0
Table of critical values

### p.16
Type II error
Failing to reject a false null hypothesis
• Type II error: fail to rejectH 0 when it is false.
• A coefficient can be nonzero even when this sample does not detect it.
• Power: the probability of rejectingH 0 under a specified alternative.
Power=1−Pr(Type II error).
Sample size and power

### p.17
Two possible errors
Our decision and the population truth are different
Population truth
Our decisionH 0 trueH 0 false
RejectH 0 Type I error Correct
Fail to rejectH 0 Correct Type II error

### p.18
Example 4.1: the wage equation
Do young children predict working married women’s wages?
log(wage)=β 0 +β 1exper+β 2exper2 +β 3educ
+β 4age+β 5kidslt6+β 6kidsge6+u.(4.16)
• wage: hourly wage;exper: years of work experience.
• educ: years of schooling;age: age in years.
• kidslt6andkidsge6: children under six and six or older.

### p.19
Example 4.1: the young-children coefficient
One coefficient, one question
+β 4age+β 5 kidslt6+β 6kidsge6+u.(4.16)
• β5: holding the other regressors fixed, one more child under six is
associated with a wage difference of about 100·β 5 percent.
• Does it differ from zero?
H0 :β 5 =0,H 1 :β 5 ,0 (two-sided).

### p.20
Example 4.1: the estimates
The coefficients and their standard errors
Coefficient S.E.
Intercept−.421.317
exper.040.013
exper2 −.00078.00040
educ.108.014
age−.0015.0053
kidslt6−.061.089
kidsge6−.015.028
N=428R 2 =.158

### p.21
Example 4.1: one coefficient test
The estimate is less than one standard error from zero
T ARGET COEFFICIENT
log(wage)=β 0 +· · ·+β 5 kidslt6+β 6kidsge6+u,H 0 :β 5 =0
ˆt5 = −.061
.089 ≈ −.69
• |ˆt5|=.69<1.96: fail to rejectH 0 at 5%.
• This sample does not establish that the partial effect differs from zero.
Can we report the evidence without choosing just one significance cutoff?

### p.22
Why report a p-value?
The smallest significance level at which we would reject
• The choice ofαis arbitrary: researchers use 10%, 5%or 1%; there is no
“correct” level.
• “Not rejected at 5%” hides information: the same result may be rejected at
10%.
• p-value: given the observed ˆtj, the smallest significance level at whichH 0
would be rejected.
• Equivalently: the probability of atstatistic at least as extreme as ours ifH 0
is true.
• Smallp: evidence againstH 0. Largep: little evidence. Withp=.50, half of
all samples would give atthis extreme whenH 0 is true.

### p.23
The p-value for young children
How unusual is this result if the null is true?
THE T TEST
H0 :β 5 =0, ˆt5 =−.061/.089≈ −.69
p=Pr(|Z| ≥ | ˆt5|),Z∼N(0,1).
• Herep≈.49.
• Ifβ 5 =0, a| ˆt5|of.69 or more occurs in
about 49% of samples: weak evidence
againstH 0.
• Reject whenp< α.
−.69 .69
p≈.49
both shaded tails
ˆt5 underH 0
Two ways to run the test

### p.24
Confidence intervals
An interval of plausible values built from three numbers
ˆβj ±c·se( ˆβj),c≈1.96 for a large-sample 95% interval.
• Three ingredients: ˆβj,se( ˆβj)andc, chosen for the confidence level and
reference distribution. Roughly: ˆβj ±2se( ˆβj).
• Meaning: if samples were drawn over and over, the intervals would
contain the fixedβ j in approximately 95%of them. For our one sample we
cannot know.
• A test: rejectH 0 :β j =a j at 5%exactly whena j lies outside the interval.
What intervals and tests assume

### p.25
Example 4.1: an interval for young children
Insignificant does not mean economically small
YOUNG CHILDREN COEFFICIENT
ˆβ5 =−.061,se( ˆβ5)=.089
−.061±1.96(.089)=[−.235, .113].
• Zero lies inside: fail to rejectH 0 :β 5 =0, as with thettest.
• So do sizeable effects in both directions. The sample cannot rule out an
economically important effect.
Tests for other wage coefficients Statistical and economic significance
What if our question concerns several coefficients together?

### p.26
Testing several coefficients at once
A multiple, or joint, hypotheses test
EXAMPLE 4.1
log(wage)=β 0 +β 1exper+β 2exper2 +β 3educ+β 4age+β 5kidslt6+β 6kidsge6+u
• Question: once experience and schooling are controlled for, do age and
children matterat all?
H0 :β 4 =β 5 =β 6 =0,H 1 :at least one is nonzero.
• Several restrictions tested together: amultiple (joint) hypotheses test.
• Three separatettests do not answer it: correlated regressors can each look
insignificant yet matter together.
Why separate tests can disagree with a joint test

### p.27
Restricted and unrestricted models
Drop the tested group and see how much worse the fit gets
Unrestricted:log(wage)=β 0 +β 1exper+β 2exper2 +β 3educ
+β 4age+β 5kidslt6+β 6kidsge6+u
Restricted (H0):log(wage)=β 0 +β 1exper+β 2exper2 +β 3educ+u
• Dropping regressors can only raise the sum of squared residuals:
SSRr ≥SSR ur.
• In MROZ:SSR ur =187.988 andSSR r =188.305, a rise of only about.32.
How large must the rise in residual variation be to reject the joint null?

### p.28
The F statistic
The relative rise in the SSR, per restriction
F= (SSRr −SSR ur)/Q
SSRur/(N−K) ,Q=number of restrictions.
• In words: a large rise in the SSR when the
group is dropped says the group matters.
• UnderH 0, useF Q,N−K as an approximate
reference in large samples; exact with
normal homoskedastic errors.
• LargeFrejects: upper tail only.
0 1 2.63
5%
F3,421 underH 0
One restriction: t and F agree The large-sample Wald version

### p.29
Example 4.1: the joint decision
The sample does not establish an additional age or children effect
JOINT NULL
H0 :β 4 =β 5 =β 6 =0,Q=3,N−K=421(K=7)
F= (188.305−187.988)/3
187.988/421 ≈.24,p≈.87
• F=.24<2.63, the 5%critical value: fail to reject.
• Dropping a group is anexclusion restriction; testing exclusion restrictions
is the main use ofF.
• Many correlated measures of one idea (firm performance in CEO pay):
test them as a group.
Which test for which hypothesis

### p.30
From the sampling distribution to the tests
The sampling distribution supplies the reference for inference
Target
OLS.1–OLS.2:
consistent forβ
Spread
Standard error
estimates
sampling variation
Shape
Exact normal model
or large-sample
approximation
One coefficient: ˆtj =( ˆβj −a j)/se( ˆβj)
ttest,p-value, confidence interval
Several coefficients:F
fromSSR r andSSR ur
Can a precisely estimated coefficient still be the wrong effect?

### p.31
Wooldridge 4.3 — current location in blue

### p.32
Wooldridge 4.3.1 — current location in blue

### p.33
The omitted-variable model
The target holds the unobserved factor fixed
E(y|x,q)=β 0 +β 1x1 +· · ·+β KxK +γq.(4.18)
• qis an unobserved determinant ofy.
• We wantβ j: the partial effect ofx j, holding the other regressorsand qfixed.

### p.34
The schooling effect holds ability fixed
The wage equation gives each term an economic meaning
E(log(wage)|exper,educ,abil)=β 0 +β 1exper+β 2exper2
+β 3 educ+γabil.
• Schooling effect: compare workers with the same experience and ability.
• Ability contribution: ability can affect wages even though we cannot
observe it.
If ability is missing from our data, where does its effect go?

### p.35
Omitting a variable can create endogeneity
Its effect remains in the error of the observed equation
y=β 0 +β 1x1 +· · ·+β KxK +γq+v,
E(v|x,q)=0. (4.19–4.20)
vis the structural error: what remains after includingq.
y=β 0 +β 1x1 +· · ·+β KxK +u,u=γq+v.(4.21–4.22)
Cov(xj,u)=γCov(x j,q).
Ifqaffectsyand is correlated withx j, thenx j is endogenous.
Recall: the structural target from Lecture 3a

### p.36
Where the omitted contribution goes
Keep the original model in view while substituting for the omitted factor
Model:y=β 0 +
XK
j=1
βjxj +γq+v.
Projection:q =δ 0 +
δjxj +r.(4.23)
Substitute:y =(β 0 +γδ 0)+
(βj +γδ j)xj +(v+γr).
Blue: target effect. Red: omitted contribution.
Which coefficient will OLS estimate when we leaveqout?

### p.37
What is omitted-variable bias?
OLS converges to the composite slope instead of the target
REWRITTEN REGRESSION
y=(β 0 +γδ 0)+ PK
j=1(βj +γδ j)xj +(v+γr)
• The new error has mean zero and is uncorrelated with every regressor:
OLS.1 holds for the composite coefficients.
• With OLS.2 and random sampling, Theorem 4.1 gives
plim ˆβj =β j +γδ j.
• Large-sample omitted-variable bias:
plim ˆβj −β j =γδ j.
Why the textbook uses consistency here

### p.38
Two links determine the direction
An omitted factor must affect the outcome and be related to the regressor
SPECIAL CASE IN THE TEXTBOOK
q=δ 0 +δ KxK +r,Cov(x j,r)=0(j=1, . . . ,K)
plim ˆβK =β K +γδ K =β K +γ Cov(xK,q)
Var(xK) .(4.24)
1 γ: does the omitted factorqraise or lowery, holdingxfixed?
2 δK: do people with higherx K also tend to have higherq?
Two positive links give an upward distortion. In the general model,δ j is a
partial association.

### p.39
Omitted ability: the setup
Assume schooling captures the ability component related to the regressors
log(wage)=β 0 +β 1exper+β 2exper2 +β 3educ+γabil+v.
E(v|exper,educ,abil)=0.
abil=δ 0 +δ 3educ+r.
Assumerhas mean zero and is uncorrelated withexper,exper 2 andeduc.
log(wage)=(β 0 +γδ 0)+β 1exper+β 2exper2
+(β 3 +γδ 3)educ+(v+γr).

### p.40
Why the experience coefficients survive
The assumed ability projection contributes nothing to these slopes
GIVEN
abil=δ 0 +δ 3educ+r,ris uncorrelated with all regressors
plim ˆβ1 =β 1 +γ·0=β 1,plim ˆβ2 =β 2 +γ·0=β 2.
Under this assumption, the experience coefficients are consistently
estimated: their population coefficients did not change.

### p.41
Why the schooling coefficient is too high
Positive ability effects and positive sorting add an upward contribution
abil=δ 0 +δ 3educ+r, γ >0, δ 3 >0
log(wage)=· · ·+(β 3 +γδ 3)educ+(v+γr).
plim ˆβ3 =β 3 +γδ 3 > β3.
1 γ >0: higher ability raises wages, holding schooling fixed.
2 δ3 >0: higher-ability workers tend to have more schooling.
If ability is unobserved, can an observed proxy help us hold it fixed?
Revisiting quiz 1: AI and pay

### p.42
Wooldridge 4.3.2 — current location in blue

### p.43
Using IQ as a proxy for unobserved ability
A proxy provides information about the factor we cannot observe
THE SAME STRUCTURAL MODEL
log(wage)=β 0 +β 3educ+other controls+γabil+v.
• x: schooling and other observed controls;q: unobserved ability.
• z: observed IQ, our proposed proxy;v: the structural error.
• A proxy need not measure ability perfectly. It must remove the ability
component still related to schooling and the controls.
Map of the equations and symbols Imperfect and unsuitable proxies
If true ability were already known, should IQ still help explain wages?

### p.44
Redundancy
The proxy adds nothing once the underlying factor is known
E(y|x,q,z)=E(y|x,q).(4.25)
• Wage example: given ability and the observed controls, IQ adds nothing
to mean log wages.
Why redundancy gives error orthogonality
How much of ability must IQ capture for the schooling coefficient to be
consistent?

### p.45
Sufficiency
The proxy must capture the part of ability related to the regressors
L(q|1,x,z)=L(q|1,z).(4.26)
q=θ 0 +θ 1z|   {z   }
captured by the proxy
+r|{z}
left over
.(4.27)
• By construction:E(r)=0 andCov(z,r)=0.
• Additional assumption:Cov(x j,r)=0 for everyj.
IQ need not measure ability perfectly. The remaining ability must no longer
be linearly related to schooling or the other regressors.

### p.46
IQ as a proxy for ability: the setup
Example 4.3: the target is the schooling effect holding ability fixed
log(wage)=β 0 +β 1exper+β 2tenure+β 3married+β 4south
+β 5urban+β 6black+β 7educ+γabil+v. (4.29)
• Indicators:married, married;south, southern region;urban, metropolitan
area;black, Black.
• We observeIQ, notabil. We assume IQ satisfies the proxy conditions, next.

### p.47
The assumptions that make IQ useful
The two proxy conditions apply to different parts of the wage error
log(wage)=β 0 +· · ·+β 7educ+γabil+v,
abil=θ 0 +θ 1IQ+r.
1 Redundancy: once true ability and the controls are fixed, IQ adds nothing
to mean log wages. ThusE(IQ·v)=0.
2 Sufficiency: remaining abilityris uncorrelated with schooling and the
other controls.
The new errorγr+vis uncorrelated with the included regressors, including
IQ. With full rank, Theorem 4.1 gives consistency.
Check the error correlations The general proxy substitution

### p.48
Before seeing the estimates
We add observed IQ to the feasible wage regression
log(wage)=a 0 +b 1exper+b 2tenure+b 3married+b 4south
+b 5urban+b 6black+b 7educ+λIQ+ε.
First omitIQ; then include it, using the same workers and other regressors.
Without IQ, schooling also picks up a positive ability contribution.
If IQ removes that contribution, should the schooling coefficient rise or fall?

### p.49
Adding IQ lowers the schooling coefficient
Example 4.3: compare the same workers before and after adding the proxy
Without IQ With IQ
Coefficient S.E. Coefficient S.E.
Intercept 5.395 .113 5.176 .128
exper.014 .003 .014 .003
tenure.012 .002 .011 .002
married.199 .039 .200 .039
south-.091 .026 -.080 .026
urban.184 .027 .182 .027
black-.188 .038 -.143 .039
educ.065.006 .054 .007
IQ .0036 .0010
Other readings of the IQ table

### p.50
Why the schooling coefficient falls
A valid proxy removes the omitted ability contribution
log(wage)=β 0 +· · ·+β 7educ+γabil+v
Without IQ:plim ˆβ7,omit =β 7 +γδ 7,
Valid IQ proxy:plim ˆβ7,proxy =β 7.
1 γ >0: ability raises wages, holding the controls fixed.
2 δ7 >0: schooling and ability have a positive partial association.
A lagged outcome as a proxy
Could ability also change the return to schooling, rather than only the wage
level?

### p.51
Wooldridge 4.3.3 — current location in blue

### p.52
Interactions in unobservables
The effect of an observed regressor can depend on an unobserved characteristic
In some cases we might be concerned about interactions between
unobservables and observable regressors.
y=β 0 +β 1x1 +· · ·+β KxK +γ 1q+γ 2xKq+v,E(v|x,q)=0.(4.30–4.31)
• The coefficient ofx K isβ K +γ 2q: it can differ across people.
◦ Wage:log(wage)=· · ·+β Keduc+γ 2educ·abil+· · ·: a year of schooling
addsβ K +γ 2abil, more for abler workers ifγ 2 >0.
• For personi,β iK =β K +γ 2qi is a random coefficient.
◦ One slope coefficient is “random”—that is, it depends on
individual-specific unobserved heterogeneity.

### p.53
Partial effect and average partial effect
The effect differs across people; the APE averages those effects
MODEL
y=β 0 +β 1x1 +· · ·+β KxK +γ 1q+γ 2xKq+v,E(v|x,q)=0
∂E(y|x,q)
∂xK
=β K +γ 2q.(4.32)
The individual effect cannot be recovered from observables without further
information or assumptions aboutq.
APE=E(β K +γ 2q)=β K +γ 2E(q)=β K ifE(q)=0.(4.33)
When the mean of q is not zero Attendance effects can vary with prior GPA

### p.54
Average treatment effect
For a binary treatment, the average effect is called the ATE
y=β 0 +β 1x1 +· · ·+β KxK +γ 1q+γ 2xKq+v,E(q)=0
Letx K =1 for receiving a treatment, such as a job training program or a
school voucher, and 0 otherwise.
E(y|x 1, . . . ,xK−1,1,q)−E(y|x 1, . . . ,xK−1,0,q)=β K +γ 2q.
• The effect of the treatment differs across people with differentq.
• Its average over the distribution ofqisβ K: the average treatment effect
(ATE).
Chapter 19 of the book returns to treatment effects.

### p.55
What does the schooling coefficient mean?
The main effect is evaluated where the interacting variable equals zero
IQ IS THE PROXY FOR ABILITY
log(wage)=a 0 +· · ·+b 1educ+b 2IQ+b 3educ·IQ+ε.
Schooling effect at IQ=b 1 +b 3IQ.
The coefficientb 1 alone is not the schooling effect at every IQ.
Proxy assumptions for the average effect
At what IQ does the schooling effect equalb 1? How could we move that
reference to IQ100?

### p.56
Centring changes the reference person
The schooling coefficient now describes someone with average IQ
IQ0 =IQ−100,c 1 =b 1 +100b 3.
Raw IQ Centred IQ:IQ−100
Schooling coefficient.018 .052
Reference person IQ 0 IQ 100
Interaction coefficient.00034 .00034
.018+100×.00034≈.052.
Same fitted wages; a new reference person.
Population versus sample-mean centring

### p.57
Reading the centred schooling coefficient
Under the proxy assumptions, the centred slope estimates the average partial effect
EXAMPLE 4.5
[log(wage)=· · ·+.052educ−.00094IQ 0 +.00034educ·IQ 0,IQ 0 =IQ−100.
• At IQ 100, one more year of schooling is associated with about 5.2%
higher wages.
• If the proxy assumptions hold andE(IQ)=100, this estimates the average
partial effect of schooling.
What changes if we observe the variable itself, but measure it inaccurately?

### p.58
Wooldridge 4.4 — current location in blue

### p.59
Another source of endogeneity
The model’s variable is well defined, but our data record it with error
LECTURE 3A: THREE SOURCES OF ENDOGENEITY
Omitted variables·Measurement error·Simultaneity
• We have treatedomitted variables. Next:measurement error.
• The model’s variable has a clear meaning, such as actual annual income;
our data contain a measure of it with error.
• Two cases, each with its own consequence for OLS:
◦ error in the dependent variabley: harmless for consistency unless
related to the regressors;
◦ error in an explanatory variable: classical error pulls the slope toward
zero.

### p.60
Measurement error versus a proxy
A similar statistical structure, but conceptually very different problems
Proxy variable Measurement error
We look for a variable that is
somehow associated with the
unobserved one.
The unobserved variable has
a well-defined, quantitative
meaning; our measure of it
contains error.
IQ score is a proxy for ability. Reported annual income is a
measure of actual annual income.
The effect of the omitted variable
itself cannot be estimated.
The mismeasured variable is often
the one whose effect we want.

### p.61
Wooldridge 4.4.1 — current location in blue

### p.62
Measurement error in the outcome
We observe the true outcome plus a measurement error
Maintain OLS.1–OLS.2 for the true model:
y∗ =β 0 +β 1x1 +· · ·+β KxK +v,e 0 =y−y ∗.(4.37–4.38)
What matters is how the measurement error in the population is related to
other factors.
y=β 0 +β 1x1 +· · ·+β KxK +(v+e 0)|  {z  }
new error
.(4.39)
When does OLS withyin place ofy ∗ produce consistent estimators of the
βj?

### p.63
When outcome error leaves slopes consistent
Reporting error must be uncorrelated with the regressors
OBSERVED EQUA TION
y=β 0 +β 1x1 +· · ·+β KxK +(v+e 0)
• The true-model errorvis already uncorrelated with the regressors.
• IfCov(x j,e 0)=0 for everyj, the slope estimators remain consistent.
• A nonzero average reporting error shifts the intercept, not these slopes.
What if treated firms systematically underreport a bad outcome?

### p.64
Example 4.7: reported scrap rates
Underreporting by grant recipients can make the programme look better
• Question: does a job-training grant reduce defective output?
• scrap∗: true scrap rate (defective output); lower is better.grant=1 for a
grant recipient.
log(scrap∗)=β 0 +β 1grant+v,log(scrap)=log(scrap ∗)+e 0.
• Suppose recipients underreport more:Cov(grant,e 0)<0.
• The grant coefficient is pushed downward: the measured reduction in
scrap looks too large.
Another example: reported saving

### p.65
Outcome error: what changes the slope?
Systematic reporting can look like an effect of the regressor
ONE-REGRESSOR CASE
plim ˆβ1 =β 1 + Cov(x1,e 0)
Var(x1) .
• If reporting errors tend to be more positive at highx 1, the estimated slope
is pushed up; more negative, down.
• If reporting error is uncorrelated with the regressors, the slopes remain
consistent.
If outcome noise leaves the slope consistent, does it still have a cost?

### p.66
Outcome noise can reduce precision
The slope remains consistent, but the estimate becomes less precise
For independent added noise,
Var(v+e 0)=Var(v)+Var(e 0).
Recorded log wage With independent noise added
Schooling slope.060 .057
Standard error.006 .008
The estimate changes little; its standard error rises.
Would noise in schooling itself have the same consequence?

### p.67
Wooldridge 4.4.2 — current location in blue

### p.68
Measurement error in a regressor
Replacing the true input puts measurement error into the regression error
y=β 0 +β 1x1 +· · ·+β Kx∗
K +v.(4.41)
• We observex K =x ∗
K +e K, withE(e K)=0. (4.42)
• Substitutex ∗
K =x K −e K:
y=β 0 +β 1x1 +· · ·+β KxK +(v−β KeK)
|     {z     }
.(4.44)
The observed regressorx K and the new error both containe K. Under the
maintained error assumptions,Cov(x K,e K)=0 (4.43) preserves consistency;
details in the appendix. Error uncorrelated with the recorded value

### p.69
Classical error creates endogeneity
The observed regressor and the new error share the same recording noise
xK =x ∗
K +e K,u=v−β KeK.
Classical error: noise is uncorrelated with the truth,
Cov(x∗
K,e K)=0.(4.45)
MaintainE(e K)=0,Cov(v,x ∗
K)=Cov(v,e K)=0 andCov(e K,x j)=0 forj<K.
Cov(xK,u)=−β K Var(eK).
Ifβ K ,0, OLS.1 fails.
What happens to the fitted slope when the input moves without the
outcome?

### p.70
Classical error attenuates a single slope
The slope is multiplied by the share of variation coming from the true input
ONE REGRESSOR
y=β 0 +β 1x1 +(v−β 1e1),x 1 =x ∗
1 +e 1
plim ˆβ1 =β 1
Var(x∗
1)
1)+Var(e 1)
|               {z               }
true-input share of recorded variation
.(4.48)
• Between 0 and 1: slopes move toward zero; more data do not help.
Deriving the attenuation factor Attenuation with several regressors

### p.71
Measurement error flattens the fitted line
Same observations and outcomes; extra movement only in the measured input
−2 0 2
−4
4
x∗: true input
y
Fitted slope: 2.01
x=x ∗ +e: recorded input
Fitted slope: 1.42
More horizontal variation, with the same outcomes: a flatter fitted line.
Responses to measurement error

### p.72
Example 4.8: reported family income
Attenuation makes a real effect harder to detect
colGP A=β 0 +β 1faminc∗ +β 2hsGP A+β 3SAT+v,faminc=faminc ∗ +e 1.
• College GPA, high-school GPA and SAT come from school records;
students report family income.
• Under classical error, the income coefficient is biased toward zero.
• A test ofH 0 :β 1 =0 then has a higher probability of Type II error: a real
effect can look insignificant.

### p.73
When classical measurement error is doubtful
The attenuation result rests on the classical assumption
CLASSICAL ERROR
K +e K,Cov(x ∗
K,e K)=0
• Days of marijuana use: nonsmokers report 0 exactly, while smokers
miscount, and reports cannot fall below 0 or exceed 30. The error is then
very likely correlated with the true value.

### p.74
Measurement error: what to take into practice
Error in an explanatory variable is usually the more serious problem
1 Error iny: if it is uncorrelated with the regressors, OLS slopes remain
consistent. Independent noise can make estimates less precise.
2 Error inx: under the classical assumptions, the mismeasured regressor’s
slope is attenuated toward zero. More observations do not remove this
distortion.
3 Before interpreting a small coefficient: check how the variable was
recorded. A weak estimate may reflect noisy data; outside the classical
case, the direction is not guaranteed.
Practice: which way does the bias go?
What should we check before calling a regression coefficient an effect?

### p.75
Wrap-up (3b)

### p.76
What to take into empirical work
Read the coefficient, assess uncertainty, then examine what could distort it
1 OLS and inference: define the target; use standard errors,tandFto
assess sampling uncertainty. (4.2.1–4.2.3)
2 Omitted variables: name the missing factor and sign its two links before
giving a causal interpretation. (4.3.1)
3 Proxies: explain why the proxy removes the remaining regressor–error
link; adding a control alone is not enough. (4.3.2)
4 Interactions: centre at the relevant mean to read an average effect, under
the identifying assumptions. (4.3.3)
5 Measurement error: unrelated outcome noise can cost precision; classical
regressor noise attenuates the slope. (4.4)
Reading map and assumption checklist

### p.77
Next lecture
No lecture on the holiday Monday; then instrumental variables
Today: Linear Regression, 3b — Wooldridge (2010), Chapter 4, Sections
4.2.2–4.4.
Next: Instrumental Variables, Wooldridge (2010), Chapter 5 (Weeks 6–7):
what to do when a regressor stays correlated with the error.
No lecture on Monday 5 October 2026 (National Day holiday);
Instrumental Variables begins the following Monday.
Problem Set 1 due Sunday 11 October 2026. Will be posted this week.
Appendix contents
Adapted from slides by Shuyang Sheng and Qihui Chen

### p.78
Appendix
Back to contents

### p.79
Optional explanations with returns to the relevant concept
C Lagrange multiplier tests App. 1
D Inference: derivations and test details App. 7
E OVB, selection and proxies App. 30
F Measurement error: derivations and practice App. 58
Back to next lecture and PS1

### p.80
Appendix roadmap
APPENDIX C · Wooldridge 4.2.4 — current location in blue
Lagrange Multiplier Tests
Inference Illustrations
OVB, Selection and Proxies
Measurement Error

### p.81
The LM (score) statistic
estimate underH 0, then ask whether the excluded regressors explain the residuals
• Partitiony=x 1β1 +x 2β2 +uand testH 0 :β 2 =0(K 2 restrictions).
• Estimate therestrictedmodel (yonx 1) and keep its residuals ˜ui. UnderH 0,
xi2 should be uncorrelated with ˜ui up to sampling error.
• Regress ˜uonallofx 1,x 2 (includingx 1 is essential) and computeLM=NR 2
u.
UnderH 0 and OLS.3,LM
a
∼χ 2
K2
. Also called theN-R 2 test.
• Example 4.1(MROZ,H 0: no age or children effects):R 2
u ≈.0017; from
unroundedR 2
u,LM≈.722,p-value≈.87 — the same verdict asF=.24
(p≈.87).
Back to the Wald rejection rule Back to the F statistic Robust LM

### p.82
Heteroskedasticity-robust LM
three auxiliary regressions andN−SSR 0
• Regress each element ofx 2 onx 1 and keep the residuals ˆri1, . . . ,ˆriK2 (the
part ofx 2 not explained byx 1).
• Regress the constant 1 on ˜uiˆri1, . . . , ˜uiˆriK2 without an intercept; withSSR 0 its
sum of squared residuals,LM=N−SSR 0
underH 0 whatever the
form of heteroskedasticity.
• Example 4.1continued:LM=.51,p≈.92; the robust Wald statistic gives
p≈.92. Tiny statistics either way: these tests do not establish an
additional linear association with age or children in this sample.
Back to the Wald rejection rule Back to the F statistic Back to the LM statistic

### p.83
APPENDIX D · Wooldridge 4.2.2–4.2.3 — current location in blue

### p.84
Homoskedasticity implies OLS.3
Constant conditional variance is sufficient, not necessary
Assumed: zero conditional mean and constant conditional variance,
E(u|x)=0,Var(u|x)=σ 2.
Implied:E(u 2 |x)=σ 2, and then, by iterated expectations,
E(u2x′x)=σ 2E(x′x)(OLS.3).
• The reverse can fail: OLS.3 is the weaker condition.
• Homoskedasticity:Var(u|x)=σ 2.
Why constant variance implies OLS.3 Back to the homoskedasticity recap
OLS.3 in the textbook

### p.85
Assumption OLS.3
The weakest form of homoskedasticity
E(u2x′x)=σ 2E(x′x), σ 2 =E(u 2).
Element by element:u 2 is uncorrelated with everyx j, everyx 2
j and every
productx jxk,
Cov(u2,x jxk)=0 for allj,k.
Back to the homoskedasticity recap Variance and standard error
Back to the OLS.3 implication

### p.86
What OLS.3 buys
A simple variance with three ingredients
Under OLS.1–OLS.3 (Theorem 4.2), withA=E(x ′x),
Avar(ˆβ)= σ2
N A−1.
One coefficient (R2
j : share ofx j explained by the other regressors):
Avar(ˆβj)= σ2
NVar(x j) (1−R 2
j ) .
Next: estimate numbers onσ 2 andAfrom one sample, and read a standard
error.
Back to the homoskedasticity recap Estimating the standard error
Back to Assumption OLS.3

### p.87
From the variance to a standard error
Estimate the two unknowns from our one sample
Avar(ˆβ)=σ 2[E(x′x)]−1/Nunder OLS.1–OLS.3.
• From the sample (Kcounts the intercept):
ˆσ2 = SSR
N−K , X′X
N =⇒ ˆV= ˆσ2(X′X)−1.(4.10)
• Standard error:se( ˆβj)=
q
ˆVjj, the number software prints beside each
coefficient.
• If OLS.3 fails, use robust standard errors; ˆβis unchanged.
Robust standard errors Back to the homoskedasticity recap
Back to the variance formula

### p.88
Why constant variance implies OLS.3
Two steps: a second-moment identity, then iterated expectations
ASSUME
E(u|x)=0,Var(u|x)=σ 2
E(u2 |x)=Var(u|x)+[E(u|x)] 2 =σ 2.
By iterated expectations, for every pairj,k,
E(u2xjxk)=E
h
xjxk E(u2 |x)
i
=σ 2E(xjxk).
Stacked over all pairs, this is OLS.3. OLS.3 need not imply either conditional
restriction.
Back to homoskedasticity and OLS.3 Back to the OLS.3 implication

### p.89
Robust standard errors
Allow unequal error variances; keep the OLS coefficients
Without OLS.3:Avar( ˆβ)=A −1BA−1/N, withB=E(u 2x′x).
ˆVrobust =(X ′X)−1
 NX
i=1
ˆu2
i x′
ixi

(X′X)−1.(4.11)
• Each squared residual enters the uncertainty calculation separately.
• Diagonal square roots give heteroskedasticity-robust standard errors.
• With OLS.1–OLS.2 and the usual regularity conditions, these remain
asymptotically valid when OLS.3 fails.
Robust variance: derivation and adjustment The robust column in the wage example
Back to standard errors Back to estimating the standard error

### p.90
Estimating the robust variance
Replace the unknown errors by OLS residuals
Avar(ˆβ)= A−1BA−1
N ,B=E(u 2x′x).
• EstimateAbyX ′X/NandBby ˆB=N −1 P
i ˆu2
ixi.
• Substitution gives (4.11). TheHC1 adjustmentmultiplies that variance
matrix byN/(N−K).
Small-sample performance and weighted least squares Back to robust standard errors
Back to standard errors

### p.91
Reading the robust column
Same coefficient; a different uncertainty estimate
ˆVHC1 = N
N−K (X′X)−1
(X′X)−1.
• Robust S.E.=
corresponding diagonal element.
• Example 4.1,kidslt6: ˆβ5 =−.061 either way; the usual S.E. is.089 and the
robust S.E. is.106.
Back to robust standard errors Back to standard errors

### p.92
Robust standard errors: costs; why not WLS?
robust is free asymptotically, not in small samples
• (4.11) is consistent underanyheteroskedasticity, including none. In small
samples it can be less accurate than the usual estimator when OLS.3
holds; the degrees-of-freedom correctionN/(N−K)(MacKinnon and
White 1985) helps a little, and software (HC1) uses it.
• Weighted least squares needs a correct model ofVar(y|x). More subtly,
WLS is generally inconsistent for the linear projection whenE(u|x),0
but OLS.1 holds — so it is the wrong tool for a projection.
• With largeN, heteroskedasticity rarely threatens inference by OLS; the
point is only to compute the standard errors appropriately.
Back to the robust variance derivation Back to robust standard errors

### p.93
Two standard errors on the ATTEND fit
the same slope, the usual and the robust se
[stndfnl=-.634+.00813atndrte,N=680,R 2 =.0196
slope ˆβ1 usual se robust se (HC1)
atndrte.00813 .00221 .00212
t= ˆβ1/se3.68 3.84
Both standard errors lead to rejection of a zero slope at the 5%level.
Back to standard errors (4.2.2)

### p.94
When theory says which sign to expect
• H0 :β j =0 againstH 1 :β j >0 (orH 1 :β j <0).
• Reject in favour ofβ j >0 if ˆtj >c, wherecis the 95th percentile: all 5%in
one tail (c=1.645 for largeN−K).
• A negative ˆtj, however large, never rejects in favour ofβ j >0.
0 1.645
H1 :β j >0
−1.645 0
H1 :β j <0
Back to the null hypothesis

### p.95
The t distribution
Like the standard normal, with heavier tails when degrees of freedom are few
Definition: ifZ∼N(0,1)andX∼χ 2
ν are independent,
T= Z√
X/ν
∼t ν.
• Symmetric around zero; heavier
tails thanN(0,1).
• Asνgrows,t ν approachesN(0,1).
• With normal errors, ˆtj ∼t N−K.
1.96 2.571
N(0,1)
t5
Back to the t statistic

### p.96
Testing a value other than zero
Distance from the hypothesized value, in standard errors
H0 :β j =a j : ˆtj =
ˆβj −a j
= estimate−hypothesized value
standard error .
• It counts how many standard errors ˆβj lies froma j; witha j =0 it is the
usual ˆtj.
• Example 4.1, is the return to schooling 10%?H 0 :β 3 =.10:
ˆt3 =(.108−.10)/.014≈.57<1.96, fail to reject.

### p.97
Critical values of the t distribution
Two-sided, by significance level and degrees of freedom
Degrees of freedomα=10%α=5%α=1%
5 2.015 2.571 4.032
10 1.812 2.228 3.169
20 1.725 2.086 2.845
30 1.697 2.042 2.750
60 1.671 2.000 2.660
120 1.658 1.980 2.617
∞(N(0,1)) 1.645 1.960 2.576
• Smallerα, largerc; more degrees of freedom, smallerc. WithN−K>120,
use theN(0,1)row.
Back to Type I error

### p.98
More observations can make a fixed alternative easier to detect
• Aconsistent testsatisfies, for a
fixed alternative,
lim
N→∞
Pr
N
(rejectH 0 |H 1)=1.
• Supposeβ j/se( ˆβj)≈2.5 at sample
sizeN.
• At 4N, the S.E. approximately
halves; the signal becomes 5 S.E.s.
−1.96 0 1.96 5
power≈.71
ˆtj
Illustrative normal approximation. Orange: rejection under the null; blue:
rejection under the specified alternative.
Back to Type II error and power

### p.99
power≈.999

### p.100
Two ways to run a t test
A critical value or ap-value gives the same decision
ONE COEFFICIENT
H0 :β j =0, ˆtj = ˆβj/se( ˆβj)
Critical value
1 Chooseα, say 5%.
2 Findc: the 97.5th percentile
(≈1.96).
3 Compute ˆtj.
4 Reject if| ˆtj|>c.
p-value
1 Compute ˆtj.
2 Computep=Pr(|T| ≥ | ˆtj|).
3 Reject ifp< α.
4 Reportp: it shows how strong the
evidence is.
Same decision:p< αexactly when| ˆtj|>c.
Back to the p-value example

### p.101
Statistical versus economic significance
Significant is not the same as large; insignificant is not the same as zero
WHA T MOVES THE ST ANDARD ERROR
Avar(ˆβj)=σ 2/[NVar(x j) (1−R 2
j )]: noise, sample size, own variation ofx j.
1 Significant: now judge the size (units, logs). With a largeN, tiny effects
become significant.
2 Not significant: is the estimate still large? Report thep-value; a large
estimate with a largepis imprecise, not zero. The young-children
estimate: about−6%per child,p=.49.
3 Unexpected sign: check uncertainty, coding and the model; consider
omitted variables.
Back to the young-children interval

### p.102
An interval is only as good as the assumptions behind it
• Omitted factorscorrelated with the regressors: OLS is inconsistent, so the
interval is centred in the wrong place. The next section.
• Heteroskedasticity: the usual standard error is not valid, so the interval is
not truly 95%. Use robust standard errors.
• Normal errors: not important with hundreds of observations; the
large-sample route gives the same intervals.
Back to confidence intervals

### p.103
Other wage coefficients
Apply the same test coefficient by coefficient
Usual Robust
Coefficientt p t p
educ7.49< .001 7.92< .001
exper2.97.003 2.61.009
• Reject each corresponding zero-coefficient null at 5%, using either
variance estimate.

### p.104
Separate tests and a joint test
a joint test uses covariance between estimates
−2
2
first estimate / se
second estimate / se
• IllustrativeH 0 :β 1 =β 2 =0;
estimates(1.8,−1.8), both se=1,
estimated correlation.8.
• Separate tests: both
|t|=1.8<1.96.
• JointFtest:F=16.2>3.00;
reject at 5%.
Blue ellipse: joint 5%nonrejection region; dashed square: both individual 5%
tests fail to reject.
Back to several restrictions at once (4.2.2)

### p.105
The Wald statistic
The large-sample version of the F test
EXCLUSION HYPOTHESIS
y=x 1β1 +x 2β2 +u,H 0 :β 2 =0
W= ˆβ′
2 ˆV−1
22 ˆβ2
K2 underH 0.
• ˆV22 estimates the variance matrix of ˆβ2, using the usual or robust formula.
• The matrix accounts for both variances and covariances among the
estimates.
• W=Q·FwithQ=K 2; with one restriction,W= ˆt 2. A robust ˆVgives a
robust joint test.
The Wald rejection rule General linear restrictions Back to the F statistic

### p.106
The Wald rejection rule
Large values are unusual under the joint null
THE WAGE HYPOTHESIS
H0 :β 4 =β 5 =β 6 =0,K 2 =3,W a∼χ 2
3
• At 5%, reject whenW>7.81.
Pr(χ2
3 >7.81)≈.05.
• Equivalently, reject when
p=Pr(χ 2
3 >W)< .05.
0 3 7.81
WunderH 0
Example 4.1: usualW=.711=3F, robustW=.493;p=.87 and.92. Fail to
reject either way.
The LM alternative Back to the Wald statistic Back to the F statistic

### p.107
General linear restrictions
A matrix can collect several coefficient restrictions
H0 :Rβ=r.(4.12)
• βisK×1;RisQ×Kwith rankQ≤K;risQ×1.
• To testβ 2 =0,
R=(0 I K2),r=0,Q=K 2.
• ThusR ˆβ−r= ˆβ2.
Wald formula for general restrictions Back to the exclusion Wald statistic
Back to the F statistic

### p.108
The general Wald statistic
Scale the restriction errors by their covariance matrix
GENERAL LINEAR HYPOTHESIS
H0 :Rβ=r,Qrestrictions
W=(R ˆβ−r) ′(R ˆVR′)−1(R ˆβ−r).(4.13)
• UnderH 0,W
Q.
• ˆVis the usual or robust estimated variance matrix, according to the
maintained assumptions.
Back to general linear restrictions Back to the exclusion Wald statistic

### p.109
One restriction: t and F agree
Use t for one coefficient and F for a group
• For one restriction,F= ˆt 2
j andt 2
N−K has anF 1,N−K distribution: the same
two-sided decision.
• Thetstatistic is more flexible for one coefficient: it also handles one-sided
alternatives.
• A jointFcan hide one significant variable inside a group of insignificant
ones. Report the separatettests too.

### p.110
The hypothesis determines the statistic and its reference distribution
Hypothesis Reference underH 0
One coefficient:β j =a j ˆtj =( ˆβj −a j)/se( ˆβj):t N−K, orN(0,1)for largeN
An interval forβ j ˆβj ±c·se( ˆβj)
A group:QexclusionsF:F Q,N−K; large-sampleW=Q·F
Q
• The usual standard errors require OLS.3; robust ones allow its failure.
• With one restriction,F= ˆt 2.
Back to the wage joint-test decision

### p.111
The big picture, backwards
why we needed today for the causal goal, with where to read further
• Goal: a causalβ K — the effect ofx K holding everything else, observed or
not, fixed (4.1).
• OLS reaches itunder OLS.1–OLS.2 and the regularity conditions; it is
consistent and approximately normal (4.2.1–4.2.2), and a standard error
makes the estimate usable (4.2.2–4.2.3, today’s first hour).
• What threatens OLS.1: an omittedq(4.3.1), a mismeasuredx K (4.4.2),
simultaneity (Chapter 9).
• Today’s fixes and their limits: a proxy that is redundant and sufficient
(4.3.2–4.3.3); better measurement (4.4); otherwise an instrument (Chapter
5, next).
Back to the lecture takeaways

### p.112
APPENDIX E · Wooldridge 4.1, 4.3.1–4.3.3 — current location in blue

### p.113
Recall: the structural target
A structural coefficient describes a specified ceteris paribus relationship
• The targetβ 3 compares schooling while holding experience and ability
fixed.
• Ability remains in this population relationship even when the dataset
does not measure it.
• A regression omitting ability estimates a different projection unless the
required orthogonality conditions hold.
Back to omission and endogeneity

### p.114
Why the argument uses probability limits
Orthogonality gives consistency; unbiasedness needs stronger conditions
y=(β 0 +γδ 0)+
KX
(βj +γδ j)xj +e,
e=v+γr,E(e)=0,E(x je)=0.
• With full rank and random sampling, these OLS.1 moments give
consistency by Theorem 4.1.
• They need not implyE(e|x)=0, so finite-sample unbiasedness does not
follow.
Back to the omitted-variable probability limit

### p.115
The quiz question about controls
A control must address the omitted factor under stated assumptions
A QUESTION FROM QUIZ 1
“Can controls really remove self-selection bias if motivation can’t be measured?
By what approaches?”
• An observed proxy can help if it supplies information about the missing
factor.
• Redundancy and sufficiency make the remaining error orthogonal to the
• Merely adding controls, or observing more workers, does not establish
those conditions.
Back to the two proxy requirements Back to Quiz 1

### p.116
From redundancy to error orthogonality
The conditional-mean restriction implies the moment used by OLS
E(y|x,q,z)=E(y|x,q)=β 0 +xβ+γq.
v=y−β 0 −xβ−γq=⇒E(v|x,q,z)=0.
E(zv)=E zE(v|x,q,z)  =0.
The reverse implication does not follow: one zero moment does not fix an
entire conditional-mean function.
Back to redundancy

### p.117
What if the proxy is imperfect?
Remaining ability related to schooling leaves a remaining distortion
q=θ 0 +ρ 1x1 +· · ·+ρ KxK +θ 1z+η,
whereηis orthogonal to(1,x,z)by projection.
plim ˆβj,proxy =β j +γρ j.
• Sufficiency is the restrictionρ 1 =· · ·=ρ K =0.
• A proxy can reduce the distortion without eliminating it; improvement is
not guaranteed.
How an unsuitable control can worsen bias Back to the two proxy requirements

### p.118
An unsuitable control can amplify bias
A variable explaining only the exogenous part of the regressor can hurt
y=β 0 +β 1x+u,Cov(x,u),0.
• Consider addingawithCov(a,u)=0 butCov(a,x),0.
• Partialling outaremoves variation fromxwithout removing its
covariance withu.
• The remaining variation inxcontains a larger share of the endogeneity.
The scalar bias calculation Back to imperfect proxies Main: proxy requirements

### p.119
The scalar bias-amplification calculation
The covariance is unchanged and the denominator falls
s=x−L(x|1,a),Cov(a,u)=0.
Cov(s,u)=Cov(x,u),0<Var(s)<Var(x).
plim ˆβomita −β 1 = Cov(x,u)
Var(x) ,
plim ˆβincludea −β 1 = Cov(x,u)
Var(s) .
The absolute inconsistency increases when the numerator is nonzero.
Back to unsuitable controls Main: proxy requirements

### p.120
Fit, precision and identification answer different questions
• R2 rises from.253 to.263; fit improves only slightly.
• The schooling coefficient falls from.065 to.054; a small change in fit can
accompany a meaningful change in a coefficient.
• Its standard error rises from.006 to.007: adding a proxy need not improve
every coefficient’s precision.
• Neither the change in fit nor the change in coefficient proves proxy
validity.
The schooling estimates with intervals Back to the schooling-coefficient decline

### p.121
Return to the AI-and-pay quiz question
Self-selection can make AI users different before adoption
AI use Pay
causal effectβ 1
Reported comparison: AI users earn about 15%more.
Skill (omitted)
Suppose workers who use AI also have higher skill, and skill raises pay.
How much of the reported pay gap might be the skill difference?
Sign the two links Original quiz question Back to the two links in omitted ability

### p.122
Why the pay gap can overstate the AI effect
The same two-link omitted-variable argument applies
y=log(pay)=β 0 +β 1D+γq+v;q=δ 0 +δ 1D+r
plim ˆβ1 =β 1 +γδ 1.
1 γ >0: greater skill raises pay, holding AI use fixed.
2 δ1 >0: AI users have higher average skill than nonusers.
The positive skill contribution makes the pay comparison overstate the AI
effect.
Group-gap derivation Back to the AI diagram Return to OVB

### p.123
Revisiting quiz 1: the AI-and-pay headline
A pay comparison leaves a causal question open
THE SETUP
Workers who use generative-AI tools earn about 15%more than similar workers
who do not (hypothetical). Headline: “Using AI raises your pay by 15%.”
• The headline compares AI users with non-users.
• Would the same worker earn more because of using AI?
Back to the AI-and-pay diagram Return to omitted ability
Quiz question about controls

### p.124
The AI comparison and OVB
For a binary regressor, the auxiliary slope is a group-mean difference
WITHIN THE SAME OBSERVED CHARACTERISTICS
y=β 0 +β 1D+γq+v,E(v|D,q)=0
q=δ 0 +δ 1D+r,D∈ {0,1}.
δ1 = Cov(D,q)
Var(D) =E(q|D=1)−E(q|D=0).
plim ˆβ1,omit −β 1 =γ[E(q|D=1)−E(q|D=0)].
Positive sorting on a wage-raising skill gives a positive selection
contribution.
Back to the AI two-link explanation Return to omitted ability

### p.125
Checking the proxy regression’s error
Both parts of the new error must be orthogonal to every regressor
e=γr+v,abil=θ 0 +θ 1IQ+r.
E(e)=γE(r)+E(v)=0,
E(xje)=γE(x jr)+E(x jv)=0,
E(IQ·e)=γE(IQ·r)+E(IQ·v)=0.
• E(xjr)=0: sufficiency;E(IQ·r)=0: projection.
• E(xjv)=0: structural conditional mean;E(IQ·v)=0: redundancy.
Back to the assumptions that make IQ useful

### p.126
Two proxies
More proxies still require redundancy and sufficiency
E(y|x,q,z 1,z 2)=E(y|x,q).
L(q|1,x,z 1,z 2)=L(q|1,z 1,z 2).
• Under these two conditions, include both proxies in the additive
regression.
• NLS80 also records KWW, a knowledge-of-work score (Problem 4.11).
Back to the assumptions that make IQ useful Back to the equation map

### p.127
How the equations fit together
The same structural target; two different ways to replace the unobserved factor
y=β 0 + P
j βjxj +γq+v.
1 Omitq: project it on the observed regressors.
q=δ 0 + P
j δjxj +r=⇒slope:β j +γδ j.
2 Use a proxyz: projectqonzand impose the two proxy assumptions.
q=θ 0 +θ 1z+r=⇒slope:β j;error:γr+v.
The tworterms are different residuals.δ j linksqtox j;θ 1 linksqto the proxy.
Back to the proxy setup Two proxies

### p.128
Why the proxy regression works
The new error satisfies the orthogonality condition for OLS
y=(β 0 +γθ 0)+β 1x1 +· · ·+β KxK
+γθ 1z+(γr+v)
|  {z  }
. (4.28)
• Sufficiency:ris uncorrelated with everyx j, asvalready is.Redundancy:
zis uncorrelated withv; projection makes it uncorrelated withr.
• Thus OLS.1 holds for(1,x,z). With OLS.2, Theorem 4.1 gives consistent
estimates of the original slopesβ j.

### p.129
Adding IQ changes the schooling coefficient
compare estimates and uncertainty on the same sample
0.03 0.04 0.05 0.06 0.07 0.08 0.09
With IQ
Without IQ
schooling coefficient in log wage per year
• Same 935 men and observed controls; only the IQ regressor changes.
• The schooling coefficient falls from 0.0654 to 0.0544. This sample
comparison does not verify the proxy assumptions.
Bars: coefficient±1.96se, usual standard errors. Overlap is not a test.
Back to other readings of the IQ table Main: schooling decline

### p.130
Example 4.4: a lagged outcome as a proxy
last year’s scrap rate stands in for unobserved firm productivity
• JTRAIN1, Michigan manufacturing firms, 1988:grant=1 for a job-training
grant (19 of 54 firms). Grants were not random:q= unobserved
productivity, possibly related to getting one.
log(scrap)=β 0 +β 1grant+γq+v,q=θ 0 +θ 1 log(scrap−1)+r.
• Without the proxy: [log(scrap)=.409
(.241)
+.057
(.406)
grant,R 2 =.0004: the point
estimate is positive but imprecise.
Back to reading the change in the schooling coefficient (4.3.2)
The lagged-outcome regression

### p.131
Example 4.4: the proxy regression
with last year’s scrap rate included, the grant effect changes sign and size
• With it: [log(scrap)=.021
(.089)
−.254
(.147)
grant+.831
(.044)
log(scrap−1),R 2 =.873: a grant
goes with a scrap rate about 22.4%lower than at a firm with the same rate
last year (t=−1.73).
Exact effect 100[exp(−.254)−1]=−22.4%.
Back to the lagged-outcome setup

### p.132
When the mean of q is not zero
Rewriting q around its mean shows the coefficient is still the APE
Letµ q =E(q)and writeq=µ q +(q−µ q):
y=(β 0 +γ 1µq)+β 1x1 +· · ·+(β K +γ 2µq)xK
+γ 1(q−µ q)+γ 2xK(q−µ q)+v.
• This is (4.30) with the mean-zero unobservableq−µ q: the coefficient onx K
isβ K +γ 2µq.
• The APE isE(β K +γ 2q)=β K +γ 2µq, the same number: assumingE(q)=0
loses no generality.
Back to partial and average effects

### p.133
Attendance effects can vary with prior GPA
The effect of attendance can vary with a student’s prior achievement
stndfnl=β 0 +β 1atndrte+β 2priGP A
+β 3atndrte·priGP A+β 4priGP A2 +u.
• Partial effect:β 1 +β 3priGP A, evaluated at a student’s prior GPA.
• APE:β 1 +β 3E(priGP A), averaged over the population.

### p.134
Population and sample-mean centring
Only the intercept and the schooling coefficient move; the interaction and the fit do not
IQ entered asIQ IQ−100 IQ− IQ
educ.018 .052 .053
(.041) (.007) (.007)
IQ term−.00094 −.00094 −.00094
(.00516) (.00516) (.00516)
educ×IQ term .00034 .00034 .00034
(.00038) (.00038) (.00038)
R2 .263 .263 .263
• .052−100×.00034≈.018: the same model, read at IQ 100 instead of IQ 0.
• Population mean unknown? Centre at the sample mean, here IQ=101.3.
Back to centring the IQ proxy

### p.135
A proxy with an interaction
Redundancy stays the same; sufficiency becomes a conditional-mean restriction
UNOBSERVED TERMS
γ1q+γ 2xKq
• Redundancy
• Conditional-mean sufficiency, withE(q)=E(z)=0:
E(q|x,z)=E(q|z)=θ 1z.(4.34)
• Oncezis known,xadds no information about the mean ofq.
Back to the meaning of the schooling coefficient Replace the unobserved interaction

### p.136
Replace the unobserved interaction
Include the proxy and its interaction with the observed regressor
PROXY ASSUMPTION
E(q|x,z)=θ 1z,E(q)=E(z)=0
E(xKq|x,z)=x KE(q|x,z)=θ 1xKz.
E(y|x,z)=β 0 +β 1x1 +· · ·+β KxK
+γ 1θ1z+γ 2θ1xKz. (4.35)
OLS includeszandx Kz; the coefficient ofx K estimates the APE,β K.
Back to the stronger proxy assumption Main: the schooling coefficient
Centre the proxy at its mean Random coefficients and variance

### p.137
Centre the proxy at its mean
Move the reference person from a zero proxy value to the population mean
UNCENTRED REGRESSION
E(y|x,z)=a 0 + PK−1
j=1 βjxj +δx K +az+λx Kz
• The partial effect isδ+λz: the coefficientδrefers toz=0.
• Letµ z =E(z). Rewrite the same terms as
δxK +λx Kz=(δ+λµ z)
|    {z    }
APE
xK +λx K(z−µ z).
• Usez−µ z andx K(z−µ z): the coefficient onx K is now the APE.
Back to replacing the unobserved interaction Main: the schooling coefficient
Centring an observed interaction

### p.138
Centre the observed interaction
Centring changes the coefficient’s interpretation, not the fitted model
SAME MODEL
stndfnl=α 0 +α 1atndrte+β 2priGP A
+β 3atndrte(priGP A−µ)+β 4priGP A2 +u, µ=E(priGP A).
• Expanding givesα 1 =β 1 +β 3µ: the APE is one coefficient.
• Use a knownµ, or the sample mean if it is unknown. ATTEND: sample
mean ofpriGP A2.59, and ˆα1 =.0018 (OLS se.0026).
Back to centring the proxy Main: the schooling coefficient

### p.139
Random coefficients and heteroskedasticity
A random coefficient can induce heteroskedasticity whenγ 2 ,0
CENTRED PROXY
E(q|x,z)=θ 1z
• Random coefficienty=β 0 +· · ·+β KxK +γ 1q+γ 2xKq+vwith
E(q|x,z)=θ 1z: assumeE(v|x,q,z)=0,Var(v|x,q,z)=σ 2. Then
Var(y|x,z)=σ 2 +(γ 1 +γ 2xK)2 Var(q|x,z).
Ifγ 2 ,0, this can vary withx K even if both component variances are
constant.
Back to the average schooling return Back to the average-effect assumptions

### p.140
APPENDIX F · Wooldridge 4.4 — current location in blue

### p.141
Example 4.6: reported saving
The question is whether the reporting error moves with the regressors
E(sav∗ |inc,size,educ,age)=β 0 +β 1inc+β 2size+β 3educ+β 4age.
• We observe reported savingsav, not actual savingsav ∗.
• It may be reasonable that the error is uncorrelated with income, family
size, education and age.
• Higher-income families may report more accurately.
• Different accuracy does not itself establish a biased slope.
Back to reported scrap rates

### p.142
Error uncorrelated with the recorded measure
This alternative assumption preserves consistency
COMPOSITE ERROR
Cov(xK,e K)=0.(4.43)
• With the maintained assumptions,v−β KeK is uncorrelated with every
regressor: OLS is consistent.
• This differs from classical error, which assumesCov(x ∗
K,e K)=0.
Compare the two covariances Neither polar assumption
Back to measurement error in a regressor

### p.143
The covariance partner matters
Uncorrelated with the recorded value is different from uncorrelated with the truth
SHARED SETUP
K +e K,u=v−β KeK,Cov(x K,u)=−β K Cov(xK,e K)
• Recorded value:Cov(x K,e K)=0 impliesCov(x K,u)=0; OLS remains
• True value:Cov(x ∗
K,e K)=0 impliesCov(x K,e K)=Var(e K); a nonzero slope
is attenuated.
Back to alternative covariance Main: measurement error in a regressor

### p.144
Nonclassical error has no universal direction
The direction depends on correlation with the true input
x1 =x ∗
1 +e 1,u=v−β 1e1,Cov(x 1,v)=0
• Letc=Cov(x ∗
1,e 1),0. ThenCov(x 1,e 1)=c+Var(e 1).
• The scalar probability limit becomes
"
1− c+Var(e 1)
Var(x1)
#

### p.145
Deriving scalar attenuation
Classical noise enlarges input variance without adding signal about the outcome
y=β 0 +β 1x1 +u,u=v−β 1e1,x 1 =x ∗
plim ˆβ1 =β 1 + Cov(x1,u)
=β 1 − β1 Var(e1)
=β 1
1)+Var(e 1) .
Back to the attenuation factor

### p.146
Responses to a mismeasured regressor
Improve the measure or obtain additional identifying information
• Measure better: reducing error variance brings the attenuation factor
closer to one.
• Interpret cautiously: under classical error, the OLS probability limit is
smaller in magnitude than the true slope.
• Use additional information: a valid second measure or instrument can
identify the effect; this requires new assumptions developed in Chapter 5.
Back to the attenuation picture

### p.147
Attenuation with several regressors
Controls absorb part of the signal but none of the noise
PROJECT THE TRUE INPUT ON THE OTHER REGRESSORS
x∗
K =δ 0 +δ 1x1 +· · ·+δ K−1xK−1 +r ∗
K
plim ˆβK =β K
σ2
r∗
+σ 2
eK
.(4.47)
• r∗
K: the part not explained by the other regressors. More collinear: worse.
• NLS80, noise as variable as schooling:.060→.031 alone;.065→.030 with
controls.
• The other coefficients are generally inconsistent too, in either direction.
Deriving (4.47) Attenuation at every noise level Back to the attenuation factor

### p.148
Deriving the multivariate attenuation formula
Partial out the other regressors, then repeat the one-regressor argument
• Partialling out:plim ˆβK =Cov(r K,y)/Var(r K), wherer K is the error from
projecting the recordedx K on 1,x 1, . . . ,xK−1.
• Project the truth:x ∗
K. Becausee K is
uncorrelated with 1,x 1, . . . ,xK−1, the recorded input hasr K =r ∗
K +e K.
• Cov(rK,y)=β K Cov(r∗
K +e K,r ∗
K)=β Kσ2
, sinceCov(e K,r ∗
K)=0 under
classical error andvis uncorrelated with every regressor.
• Var(rK)=σ 2
eK. Dividing gives (4.47).
Back to attenuation with controls Return to the attenuation factor

### p.149
Attenuation at every noise level
Controls push the estimates further below the one-regressor line
0 0.25 0.5 0.75 1
0.25
0.5
0.75
1
true share of recorded variance
estimate÷noise-free estimate
• NLS80: add noise to
recorded schooling,
re-estimate the log-wage
slope.
• Alone: points on the line
(4.48).
• With the six controls: below
it.
• The dashed curve is (4.47).

### p.150
Decide the direction, and whether classical error is believable, before discussing
1 Students report family income; regress college GPA on it and on
high-school GPA and SAT.
2 The same, also controlling for parents’ education and occupation.
3 Years of schooling reported in round numbers, in a wage equation.
4 Self-reported days of marijuana use in the last month, in a wage equation.
5 App users’ self-reported age, in a spending regression.
Back to the practical question