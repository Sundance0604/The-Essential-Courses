### p.1
Lecture 2:
Conditional Expectations
Enjie (Jack) Ma
Lecture 2 · Monday 14 September 2026

### p.2
Your survey
154 responses — thank you
• English: 69 of 154 respondents (44.8%) chose 3/5 for comfort with English
lectures.
• Your interests: trade, environment, macro, labour, and AI-assisted
economic research.
• Assessment: problem sets include Python programming; exams test
econometric concepts and reasoning, without requiring Python code.

### p.3
Roadmap
From conditional averages to regression
L1 L2 L3 L4 L5 Midterm L6 L7 L8 Final
Conditional Expectations — Wooldridge (2010), Chapter 2
1 Conditional expectations and models
2 Partial effects and elasticities
3 The error form
4 Properties of conditional expectations and LIE
5 Average partial effects, unobserved regressors and proxies

### p.4
SECTION 1 · Wooldridge 2.1–2.2.1
Conditional expectations and
models

### p.5
Terminology
Wooldridge 2.1 — one outcome, several explanatory variables
y,x=(x 1,x 2, . . . ,xK)
• y: explained variable, dependent variable, regressand, or response.
• x: explanatory variables, independent variables, regressors, controls, or
covariates.
• Example:y=wage;xincludes schooling, experience and IQ.

### p.7
The structural conditional expectation
Wooldridge 2.1 — the relationship we want to learn
How does schooling relate to mean wages when the relevant controls are
held fixed?
E(y|s,c)
• s: schooling;c: relevant controls, potentially including ability.
• A causal interpretation needs identification assumptions about the
economic setting and controls.
• With suitable data, we can estimate the CE. A parametric functional form
makes that task simpler.

### p.9
Complications
Wooldridge 2.1 — economic data do not always reveal the target
• Measurement error: we observe an imperfect version of a variable.
• Simultaneity: outcomes and explanatory variables may be determined
together.
• Selection: the available sample may not represent the population.
• Unobserved controls: ability may affect wages and schooling, but remain
unmeasured.

### p.10
Why conditional expectations?
Which average can the data reveal, and which average do we want?
• Target: mean wages at fixed schooling, experienceand ability:
E(wage|educ,exper,ability).
• Available data: perhaps we can group workers only by schooling and
experience:E(wage|educ,exper).
• CE notation distinguishes the two. Its properties and additional
assumptions help us relate them.
Everything right of the bar is the information set, what we know when we
form the average:E(y|information).

### p.13
Conditional expectation
Wooldridge 2.2.1 — a mean for each group of conditioning values
For an outcomeYwithE(|Y|)<∞, write
E(Y|X)=µ(X).
• The functionµassigns an average outcome to each set of conditioning
values.
• E(wage|educ,exper,IQ): average wage among workers with those
characteristics.
• Individual wages can differ even when these characteristics are the same.

### p.15
Conditional expectation: worked example
Illustrative population — average within each schooling group
8 12 16
0
4
8
12
education (years)
hourly wage (US$)
• X: schooling;Y: wage. Five
workers at each schooling
level.
• X=8: group mean 4.65.
• X=12: group mean 6.45.
• X=16: group mean 8.25.
Illustrative population; Wooldridge 2.2.1.

### p.16
4.65

### p.17
6.45

### p.18
8.25

### p.19
Each group mean is an ordinary average of five equally likely wages
HOURL Y WAGES IN DOLLARS; SCHOOLINGXIN YEARS
All five workers within each group have equal weight 1/5.
µ(8)= .65+2.65+4.65+6.65+8.65
5 =4.65.
µ(12)= 2.45+4.45+6.45+8.45+10.45
5 =6.45.
µ(16)= 4.25+6.25+8.25+10.25+12.25
5 =8.25.
We have assembled the conditional-mean function, one group at a time.

### p.22
Conditional expectation: three readings
The same example — a number, a function, and a random variable
Schoolingx 8 12 16
Mean hourly wageµ(x) 4.65 6.45 8.25
• A number:E(Y|X=12)=6.45.
• A function:µmaps each schooling value to its group mean.
• A random variable: select a worker at random. TheirXdetermines which
valueµ(X)=E(Y|X)takes.
These means describe differences across groups; causality needs more
assumptions.

### p.25
Conditional expectation: the weights
Wooldridge 2.2.1 — summation or integration within the group
For a discrete outcome,
E(Y|X=x)=
∑︂
y
y P(Y=y|X=x).
For a continuous outcome,
∫︂
y fY|X(y|x)dy.
Average the possible outcomes using their probabilities within the group.

### p.27
Conditional expectation: real data
NLS80, 935 men — a model summarises the sample group means
9 10 11 12 13 14 15 16 17 18
500
1,000
1,500
2,000
years of education
monthly wage (US$, 1980)
NLS80: sample group means and a subset of workers • Grey dots: a subset of
individual workers,
grouped by schooling.
• Dark dots: sample mean
wages at each schooling
• The fitted line is a simple
parametric summary. It
need not pass through every
mean.
Wooldridge (2010), Example 4.3 data; course file:nls80.dta. All 935 men determine means and fit.

### p.30
Parametric models
Wooldridge 2.2.1, Example 2.1 — models A and B restrict the shape of the CE
A parametric model describesµ(x 1,x 2)using finitely many coefficients.
MODEL A: LINEAR
µA =β 0 +β 1x1 +β 2x2
Linear in the regressors and in the coefficients.
MODEL B: QUADRA TIC
µB =β 0 +β 1x1 +β 2x2 +β 3x2
2
Curved inx 2, but still linear in the coefficients.

### p.32
Wooldridge 2.2.1, Example 2.1 — model C is linear in coefficients; model D is nonlinear
MODEL C: INTERACTION
µC =β 0 +β 1x1 +β 2x2 +β 3x1x2
Linear in each regressor holding the other fixed; jointly nonlinear in(x 1,x 2).
Linear in coefficients.
MODEL D: EXPONENTIAL MEAN
µD =exp[β 0 +β 1 logx 1 +β 2x2]
Nonlinear in the coefficients. Suitable for a positive mean;x 1 >0.
Each model answers the same question differently: how does the group
mean move when one regressor moves? That is the next section.

### p.34
SECTION 2 · Wooldridge 2.2.2
Partial effects and elasticities

### p.35
Partial effects
Wooldridge 2.2.2 — from deterministic to stochastic relationships
• In a deterministic model,y=f(x): the inputs determine the outcome.
• In economic data, workers with the same observed characteristics can
earn different wages. This is a stochastic relationship.
• We describe howE(y|x)changes as one regressor changes, holding the
others fixed.

### p.36
Wooldridge 2.2.2, (2.6) — a local change in the conditional mean
For a continuous regressorx j,
PEj(x)= ∂µ(x)
∂xj
.
∆E(y|x)≈PE j(x)∆x j.
• Hold every other regressor fixed.
• Units: units ofyper unit ofx j.
• A derivative gives a local rate; finite changes can differ in a curved model.

### p.38
Partial effects of a discrete regressor
Wooldridge 2.2.2 — finite differences compare two group means
Letd∈ {0,1}and letccontain the other regressors.
E(y|d=1,c)−E(y|d=0,c).
• Compare two groups at the same values ofc.
• Example: a qualification indicator, with schooling and experience held
fixed.
• The difference is in units ofy. There is no derivative with respect to the
binary indicator.

### p.40
Partial effects in models A–D
Model A — both slopes are constant
MODEL A
What are the partial effects ofx 1 andx 2?
PE1 =β 1,PE 2 =β 2
Both partial effects are constant.

### p.42
Model B — thex 2 slope changes withx 2
MODEL B
PE1 =β 1,PE 2 =β 2 +2β 3x2
Thex 2 effect depends on the value ofx 2.

### p.44
Model C — one regressor changes the other’s slope
MODEL C
PE1 =β 1 +β 3x2,PE 2 =β 2 +β 3x1
Hold the other regressor fixed when taking each derivative.

### p.46
Model D — slopes depend on the conditional mean
MODEL D
PE1 =µ D
β1
x1
,PE 2 =µ Dβ2
Hereµ D means the entire exponential expression above.

### p.48
Partial effects: worked example
Hypothetical wage model — the experience slope falls with experience
CONDITIONAL MEAN
µ(x)=14+0.9x−0.03x 2,x=years of experience.
0 2 6 10
14
16
18
20
22
experience (years)
mean hourly wage (US$)
• PE(x)=0.9−0.06x.
• At two years: 0.78 dollars per
hour, per year of experience.
• At ten years: 0.30 in the same
units.

### p.49
slope 0.78

### p.50
slope 0.30

### p.51
Why elasticities?
Changing units changes the number, not the relationship
Suppose one more year of schooling is associated with a $60 increase in
mean monthly earnings.
Wage units Partial effect Economic comparison
Dollars 60 One extra schooling year
Cents 6,000 The same extra year
Percentage changes remove the arbitrary scale of measurement.
Elasticity uses a percentage change on both sides of the comparison.

### p.54
Elasticities
Wooldridge 2.2.2, (2.9)–(2.10) — a proportional change in the conditional mean
For a positive conditional meanµ(x)andx j >0,
ηj(x)= ∂µ(x)
xj
µ(x) .
A 1% increase inx j is associated with approximately anη j% change in the
conditional mean, holding the other regressors fixed.
ηj(x)= ∂logµ(x)
∂logx j
These are two equivalent expressions for the same elasticity.

### p.57
Elasticities in models A–D
Model A —η j =PE j xj/µ; positive mean and regressors
What are the elasticities with respect tox 1 andx 2?
η1 = β1x1
µA
, η 2 = β2x2
A coefficient can be constant even though an elasticity varies with the

### p.59
Model B —η j =PE j xj/µ; positive mean and regressors
µB
, η 2 = (β2 +2β 3x2)x2

### p.61
Model C —η j =PE j xj/µ; positive mean and regressors
η1 = (β1 +β 3x2)x1
µC
, η 2 = (β2 +β 3x1)x2

### p.63
Model D —η j =PE j xj/µ; positive mean and regressors
η1 =β 1, η 2 =β 2x2
Thex 1 elasticity is constant; thex 2 elasticity generally is not.

### p.65
Elasticities: real data
NLS80 — a log–log slope is a percentage comparison
ILLUSTRA TIVE FITTED REGRESSION; 935 MEN
ˆ︁log(wage)= ˆ︁a+0.83log(educ).
• Take logs of both variables, then fit the regression.
• A 1% increase in schooling is associated with about a 0.83% increase in the
fitted geometric mean wage.
Wooldridge Example 4.3 data;nls80.dta. Bivariate illustration, not a causal estimate.

### p.67
Semielasticities
Wooldridge 2.2.2, (2.13)–(2.14) — percent change in the mean per unit ofx j
Forµ(x)=E(Y|x)>0, the arithmetic-mean semielasticity is:
sj(x)= ∂logµ(x)
• A one-unit increase inx j changes the arithmetic conditional mean by
approximately 100sj percent.
• For a log-wage fit,log(wage)=β 0 +β 1 educ+β 2 exper+u. Here 100β 1 is the
approximate percent change in fitted geometric mean wage per extra
schooling year.
Mean-log and log-mean slopes can differ. Their relation is in Appendix A. In model D,s 2 =β 2.
Appendix: two elasticity definitions

### p.69
Three slopes, three interpretations
NLS80 — level–level, log–level and log–log, all on schooling
Letµ(X)=E(Y|X)andℓ(X)=E(logY|X).
Model Slope definition Fitted wage interpretation
Level–level
µ=a+bX
b=∂µ/∂XDollars/month per year:
b=60.2: +1 year⇒about
+$60/month
Log–level
ℓ=a+bX
b=∂ℓ/∂X Percent per year:
b=.060: +1 year⇒about +6%
Log–log
ℓ=a+blogX
b=∂ℓ/∂logX Percent per 1%:
b=.83: +1% schooling⇒about
+.83%
NLS80 bivariate fits. Log rows describe fitted geometric mean wage.X: schooling (years);Y: monthly earnings
(dollars).

### p.72
SECTION 3 · Wooldridge 2.2.3
The error form

### p.73
The conditional-expectation error
Wooldridge 2.2.3, (2.15)–(2.16) — a decomposition that always holds
We have described group averages. Individual outcomes still vary.
Y=E(Y|X)⏞   ⏟⏟   ⏞
group mean
+u ⏞ ⏟⏟ ⏞
individual deviation
u≡Y−E(Y|X),E(u|X)=0.
Subtract each group’s true mean: its deviations average to zero.
The CE error has zero conditional mean by definition.
WhyE(u|X)=0 follows from the definition

### p.76
The CE error: worked example
Illustrative population — errors average to zero within every group
• Schooling groups: 8, 12, 16
years. Means: 4.65, 6.45, 8.25.
• u=Y−E(Y|X)is a worker’s
vertical distance from the
group mean.
• Every group’s errors are
−4,−2,0,2,4.
E(u|X)=0.

### p.77
u= +4
u=−4

### p.79
The error assumption: house prices
Wooldridge Example 2.2 — what does the distance coefficient measure?
hprice=β 0 +β 1 sqrft+β 2 distance+u.
• hprice: price in thousands of dollars;sqrft: floor area in square feet.
• distance: kilometres from a city incinerator. These units are chosen for this
illustration.
If the linear part is the CE, what doesβ 2 measure: a partial effect, an
elasticity, or a semielasticity?
A partial effect:β 2 thousand dollars per additional kilometre, at fixed floor
area.

### p.81
The error mean can change the distance slope
PRICE: THOUSAND DOLLARS; DIST ANCE: KM; FLOOR AREA: SQUARE FEET
E(hprice|sqrft,distance)=β 0 +β 1 sqrft+β 2 distance
+E(u|sqrft,distance).
∂E(hprice|sqrft,distance)
∂distance =β 2 + ∂E(u|sqrft,distance)
∂distance .
The observed mean-price slope can include a systematic change in omitted
factors.

### p.84
What mustE(u|sqrft,distance)=0 rule out?
THE PROPOSED MODEL
What could be inu, and could its average change with distance even among
houses of the same size?
• Neighbourhood quality or housing age could change systematically with
distance.
• A sufficient model condition isE(u|sqrft,distance)=0.
• Causality also needs a credible economic justification for the restriction
and controls.

### p.87
SECTION 4 · Wooldridge 2.2.4
Properties of conditional
expectations and LIE

### p.88
Properties of conditional expectations
Wooldridge 2.2.4, App. 2A — known functions pass through; the operator is linear
A known function
E[g(x)|x]=g(x).
Once schooling is known, its square is known too: nothing is left to average.
Linearity
E(aY+bZ|x)=aE(Y|x)+bE(Z|x).
For constantsa,b, averaging a sum gives the sum of the averages.
Next, the rule that matters most: averaging over information we lack.
More: taking out what is known More: transformed regressors

### p.93
Law of iterated expectations (LIE)
Wooldridge 2.2.4, (2.19); App. 2A, CE.2 — unconditional form: average within groups,
then across groups
Y: outcome;X: grouping variable.
1 Inner average: find each group’s mean,E(Y|X).
2 Outer average: combine those means using the group probabilities.
E[E(Y|X) ]⏞        ⏟⏟        ⏞
average of group means
=E(Y)⏞ ⏟⏟ ⏞
overall mean
Law of iterated expectations; Stat 110 calls this form Adam’s law.E(|Y|)<∞; use all groups and their correct
probabilities. Independence is not required.

### p.95
Law of iterated expectations: the bottle story
HarvardX, Stat 110 — what can a bottle label tell us?
Every label says:Contains 200 mg of Bayesium.
Sources: Discretown, Continuopolis and/or Bayesville.
For a random bottle, what content do you expect?
A) 200 mg B) more C) less D) it depends
Fictional example adapted from HarvardX (Blitzstein), Understanding Conditional Expectation.Y: bottle content
(mg);X: source city.

### p.96
Discretown
mean160 mg
Continuopolis
mean190 mg
Bayesville
mean250 mg

### p.98
From equal counts to the actual bottle counts
3 bottles 3 bottles 3 bottles
160 mg 190 mg 250 mg
200 mg
160+190+250
3 =200 mg.
Equal counts give equal probability weights.

### p.99
12 bottles 3 bottles 3 bottles
160 mg 190 mg
250 mg
Actual counts: 12, 3 and 3 bottles. Which way must the balance point
move?
Each bottle is equally likely; the heavier left stack moves down.

### p.100
180 mg
18 ×160+ 3
18 ×190+ 3
18 ×250=180 mg.
Bottle counts determine the city probability weights.

### p.101
The balance calculation becomes the law of iterated expectations
Xis the city;Yis the content of a randomly selected bottle.
Discretown Continuopolis Bayesville
City meanE(Y|X=x)160 190 250
WeightP(X=x) 2/3 1/6 1/6
Appendix D: continue with variance Appendix C: regrouping people
Wooldridge App. 2A, CE.2; Stat 110 calls this Adam’s law.

### p.102
E(Y)= 2
3 ×160+ 1
6 ×190+ 1
6 ×250=180.

### p.103
E(Y)=
x
P(X=x)E(Y|X=x)=E[E(Y|X) ].

### p.104
Wooldridge (2.20)–(2.21), CE.3 — conditional LIE inside a fixed group
AddingZmakes(X,Z)finer information thanXalone:
E[E(Y|X,Z)|X]=E(Y|X).
• Inner: means within(X,Z)groups.Outer: average overZ withineachX
group: the weights are conditional onX.
• The nested, less informative setXremains;Zis averaged out with its
distributiongiven X.
The next example starts with all eight people, then applies the same rule
within the six women.
Rule: which information set survives?

### p.106
LIE: worked example
Unconditional mean — start with the full men-and-women population
Draw one of these eight people with equal probability.Y: IQ;X: sex (MorF).
Men (M): 2 Women (F): 6
A
80
B
90
C
D
100
E
F
110
G
H
120
Mean IQ: 85 Mean IQ: 105
Find the mean for men, the mean for women, and the overall mean.
Now keep only the six women: the target becomesE(Y|F)=105.
Invented IQ scores and memberships.E(Y|M)andE(Y|F)abbreviate conditioning on sex.

### p.107
E(Y)=E[E(Y|X) ]= 2
8E(Y|M)+ 6
8 E(Y|F)
= 2
8 ×85+ 6
8 ×105=100.

### p.109
Conditional (nested) LIE: worked example
Within women — split by smoking status, then average the subgroup means
The same six women:E(Y|F)=105
Z=S: 2 smokers Z=NS: 4 nonsmokers
Mean IQ: 95 Mean IQ: 110
Find the smoker and nonsmoker mean IQs among these women.
Average over smoking status; keep “female” in every mean and weight.
Invented data; adapted from Ben Lambert, Nested LIE. Blue: group kept fixed; orange: subgroup averaged over.

### p.110
120Mean IQ: 95 Mean IQ: 110
How can those two subgroup means recover 105? Which population
supplies the weights?

### p.111
E(Y|F)=E[E(Y|F,Z)|F]
=P(Z=S|F)E(Y|F,Z=S)+P(Z=NS|F)E(Y|F,Z=NS)
6 ×95+ 4
6 ×110=105.

### p.113
SECTION 5 · Wooldridge 2.2.4–2.2.5
Average partial effects, unobserved
regressors and proxies

### p.114
Average partial effects (APE)
Wooldridge 2.2.5 — average the effect over unobserved heterogeneityq
• Return to wages:xis schooling and experience;qis ability, an example of
unobserved heterogeneity. ConsiderE(y|x,q).
• The partial effect∂E(y|x,q)/∂x j generally depends onq.
• Usually of more interest: the effect averaged across the population
distribution ofq, at fixedx, the average partial effect (APE):
APEj(x)=E q
[︄∂E(y|x,q)
]︄
• Can we learn the APE from CEs that involve only observed variables?
Wages:xis schooling and experience,qability.qis averaged with its population weights; ability and the covariates
may be related.

### p.118
Unobserved regressor
Wooldridge 2.2.4 — the target CE and the CE we can actually study
T ARGET (TRUE MODEL):sSCHOOLING,eEXPERIENCE,qUNOBSERVED ABILITY
E(y|s,e,q)=β 0 +β ss+β ee+γq.
• We observey,s,ebut notq. The data can reveal the CE on theobserved
variables. For this illustration, assume it is linear:E(y|s,e)=α 0 +α ss+α ee.
• Three objects: targetβ; observedα; and, next, the auxiliary link between
ability and the regressors.
What do theα’s measure? Mustα s equalβ s?

### p.120
Unobserved regressor: derivation
Wooldridge (2.24) — LIE replaces missing ability by its group average
STRUCTURAL CE; ABILITYqIS UNOBSERVED. T ARGET SLOPES IN BLUE, THE AVERAGED ABILITY TERM IN ORANGE
E(y|s,e) =E[E(y|s,e,q)|s,e] conditional LIE
=E[β 0 +β ss+β ee+γq|s,e] substitute the structural CE
=β 0 +β ss+β ee+γE(q|s,e). linearity;s,eare known
Among people with a particular schooling and experience level, replace
ability by that group’s average ability.
Wooldridge (2.24): “by the LIE, and the linearity of the CE operator”. Properties used: App. 2A, CE.3, then CE.1.
Why LIE is needed: the error route

### p.124
Substitute the average ability in each schooling–experience group
FROM LIE
E(y|s,e)=β 0 +β ss+β ee+γE(q|s,e).
Suppose the auxiliary mean is
E(q|s,e)=δ 0 +δ ss+δ ee.
E(y|s,e)=β 0 +β ss+β ee+γ(δ 0 +δ ss+δ ee).
The last term can change with schooling and experience. Now collect like
terms.

### p.126
Unobserved regressor: composite slopes
Observed slopes combine the target and the auxiliary relationship
AFTER SUBSTITUTION: T ARGET SLOPES IN BLUE, AUXILIARY P ARAMETERS IN ORANGE, COMPOSITE (OBSERVED)
COEFFICIENTS IN RED
E(y|s,e)=α 0 +α ss+α ee,
α0 =β 0 +γδ 0, α s =β s +γδ s, α e =β e +γδ e.
These composite coefficients describe the observed CE. The schooling slope
equals its target whenγδ s =0.
Real data: adding IQ Omitted interactions

### p.129
Wrap-up

### p.130
Key takeaways
What we defined, assumed and learned
• Define: the conditional mean and its error; the best linear predictor waits
in the appendix.
• Interpret: partial effects, elasticities, semielasticities and explicitly defined
averages of effects.
• Relate: LIE connects finer and coarser information sets.
• Assume: correct specification and credible identifying restrictions are
needed for the intended economic interpretation.
• Recover: suitable proxies can recover target slopes; an arbitrary proxy can
leave bias.

### p.131
Next lecture
Lecture 3 builds on today’s definitions
• Today: Conditional Expectations — Wooldridge (2010), Chapter 2.
• Next: Linear Regression, Wooldridge (2010), Chapter 4 (Weeks 3–4).
• OLS estimates a linear projection. We will study when its coefficients have
the economic interpretation we want. Appendix: linear projections
• No lecture on Monday 5 October 2026; Instrumental Variables begins the
following Monday.
Adapted from slides by Shuyang Sheng and Qihui Chen

### p.132
Appendix

### p.133
Appendix contents
Reached from the buttons in the main lecture; every frame has a return button
A Elasticities: two definitions App. 1
B The error form App. 4
C More on conditional expectations and LIE App. 6
D Variance decomposition: the bottle story continued App. 15
E Omitted variables and proxies App. 18
F Linear projections App. 23

### p.134
APPENDIX A · Wooldridge 2.2.2
Elasticities: two definitions

### p.135
Wooldridge 2.2.2 — logging before averaging changes the object
Elasticity of the arithmetic conditional mean
ηj = ∂logE(Y|x)
Alternative based on the conditional mean of log wages
˜︁ηj = ∂E(logY|x)
The second requiresY>0. The first can apply when some outcomes are zero
but their conditional mean is positive.
Back to main lecture

### p.138
Two equally likely wages — taking logs and averaging do not commute
Average, then take logs
E(Y)= 4+16
2 =10
logE(Y)=log10≈2.30
Take logs, then average
E(logY)=
log4+log16
=log8≈2.08
Exponentiating the mean log gives the geometric mean ($8), not the
arithmetic mean ($10).
Jensen:E(logY)≤logE(Y), also within each group.
Wooldridge 2.2.2, p. 17; Appendix 2A, CE.7.

### p.141
A sufficient condition for the two to agree in a log-outcome model
LOG–LOG INx 1, LOG–LEVEL INx 2
logY=β 0 +β 1 logx 1 +β 2x2 +u.
• IfE(u|x)=0, the mean-log definition gives ˜︁η1 =β 1.
• Ifuis also independent ofx, withE(e u)<∞, both definitions give
η1 = ˜︁η1 =β 1.
• Independence makes the adjustment from the geometric mean to the
arithmetic mean constant acrossx.

### p.144
APPENDIX B · Wooldridge 2.2.3

### p.145
WhyE(u|X)=0 follows from the definition, not from an assumption
Definition:u≡Y−E(Y|X). Take the conditional expectation of both sides,
givenX:
E(u|X) =E
[︂
Y−E(Y|X)
⃓⃓⃓X
]︂
=E(Y|X)−E
E(Y|X)
linearity of the CE operator
=E(Y|X)−E(Y|X)=0. E(Y|X)is a function ofX: already known
By construction; achosenmodel earns it only if it equals the true CE (next
frame).
Wooldridge 2.2.3, (2.15)–(2.16); rules CE.1 and known-function, App. 2A; properties in the main lecture.

### p.149
Misspecification
Wooldridge 2.2.3 — a chosen model can leave systematic errors
Letµ(x)be the true CE andm(x)a proposed model.
v=Y−m(X)=Y−µ(X)
⏞    ⏟⏟    ⏞
CE error
+µ(X)−m(X)
⏞        ⏟⏟        ⏞
misspecification
SoE(v|X)=µ(X)−m(X):
• Zero conditional mean requires the proposed model to equal the true CE
on the population’s support.
• A linear model can miss curvature or interactions in group averages.

### p.151
APPENDIX C · Wooldridge 2.2.4
More on conditional expectations
and LIE

### p.152
Eight equally likely people — one population, one overall mean
LetYbe the IQ score of a randomly selected person.
Person A B C D E F G H
IQ score 80 90 90 100 100 110 110 120
What is the expected IQ? Could we get it by averaging within groups first?
E(Y)= 80+90+90+100+100+110+110+120
8 =100.
Invented population. Partition intuition: Ben Lambert, The Law of Iterated Expectations: an introduction.

### p.154
Average within sex groups first — a larger group must get more weight
Male: 2 people Female: 6 people
Mean: 85 Mean: 105
Is the overall mean(85+105)/2=95?
Equal weights overrepresent people in the smaller group.
Invented population and group memberships; IQ scores are in points.

### p.157
Regroup by age — the overall mean stays 100
Under 40: 4 people 40 or older: 4 people
Mean: 95 Mean: 105
E(Y)= 4
8 ×95+ 4
Regrouping changes the means and weights, but preserves the overall mean.
Invented population. Every person appears in exactly one age group, including age 40 in the second group.

### p.160
Unconditional LIE — read the inner and outer expectations
For a grouping variableW, letµ(w)=E(Y|W=w).
E[E(Y|W)]=
w
P(W=w)⏞     ⏟⏟     ⏞
group share
µ(w)
⏞ ⏟⏟ ⏞
=E(Y).
E[E(Y|sex)]=E[E(Y|age group)]=100.
Use every group and its correct probability. Independence is not required.
Discrete-group version, with finiteE(|Y|). For continuousW, the outer average is an integral.
Visual: balance point Sample: NLS80

### p.163
Wooldridge App. 2A, CE.4 — pull a known factor outside the average
E[Yg(x)|x]=g(x)E(Y|x).
Within a conditioning group, everyone has the same value ofg(x).
E[educ·Y|educ]=educ·E(Y|educ).
This rule lets us manipulate interactions and conditional-mean errors.

### p.166
Wooldridge (2.27)–(2.29) — transformations do not add information
SupposeE(y|x)=g[f(x)]and definez=f(x).
E(y|z)=E(y|x)=g(z).
• Addinge 2 andseto(s,e)does not change what is known.
• More generally,f(x)may compress information. Replacingxbyf(x)
preserves the CE here because the assumed mean depends only on that
function.

### p.168
Conditional (nested) LIE: wages
Hold schooling and experience fixed — average over unobserved ability
E(Y|x)=E [︁E(Y|x,q)|x ]︁.
• Inner average: wages within schooling, experienceand abilitygroups.
• Outer average: average those means over abilitywithin each
schooling–experience group.
• This links a CE involving an unobservedqto a CE involving only
observedx.
The outer weights are the distribution ofqgivenx, not necessarily its overall
population distribution.

### p.171
LIE: sample analogue
NLS80, 935 men — the same weighting rule works in a sample
Schooling group Men Mean wage (US$)
9–11 years 88 774.25
12 years 393 862.67
13–18 years 454 1,076.02
Can we give these means equal weight?
Equal weights give $904.32, but the groups have different sizes.
¯Y=
g
ng
935
¯Yg = 68,134+339,030+488,515
935 =957.95.
Sample illustration of LIE: weight each group mean by its share.nls80.dta; rounded means, exact totals.

### p.174
LIE: which information set survives?
Wooldridge p. 20 — “the smaller information set always dominates”
Y: wage;X: sex;Z: age group. Conditioning on a variable means knowing it.
Iterated expectation Equals Averaged out
E[E(Y|X,Z)|Z]E(Y|Z)sex, within each age group
E[E(Y|X,Z)|X]E(Y|X)age, within each sex
E[E(Y|X,Z) ]E(Y)both
E[E(Y|Z)|X,Z]E(Y|Z)nothing: already known given(X,Z)
E[E(Y|X)|Z] no simplification information sets need not be nested
Rule: for nested information sets, the less informative set survives. The
dropped variable is averaged with its distributiongiventhe kept ones.
Wooldridge (2.19)–(2.21); App. 2A, CE.3. Row four is (2.20): the inner mean is already known given(X,Z).

### p.177
APPENDIX D · Wooldridge App. 2A
Variance decomposition: the bottle
story continued

### p.178
Variance decomposition: the bottle story
Every city has SD 10 mg — what is the overall SD of a random bottle?
Each city: SD 10 mg around its mean. The overall SD of a random bottle is
A) 10 mg B) more C) less D) it depends
Same bottle shares; curves illustrate within-city spread. Adapted from HarvardX, Stat 110.

### p.179
within each city
between cities
Bottles varywithineach city; city means varybetweencities. Is total variance
just the weighted average of the city variances?

### p.180
Average of the separate variances, plus variance of the separate averages
Var(Y)=E[Var(Y|X)]⏞          ⏟⏟          ⏞
average of the separate variances
+Var[E(Y|X)]⏞          ⏟⏟          ⏞
variance of the separate averages
With multiple sources of water, there are multiple sources of variation.
Adapted bottle shares 2/3,1/6,1/6 throughout. Wooldridge App. 2A, CV .2.

### p.181
Within: every city has variance 102 =100, so the weighted average is
3 (100)+ 1
6 (100)+ 1
6(100)=100 mg 2.

### p.182
Between: the city means 160,190,250 around the overall mean 180, with the
bottle shares:
3(160−180) 2 + 1
6 (190−180) 2 + 1
6(250−180) 2 =1100 mg 2.

### p.183
Total:Var(Y)=100+1100=1200 mg 2, so
SD(Y)=
√
1200≈35 mg>10 mg.

### p.184
Law of total variance
Wooldridge App. 2A, CV .2 — total = within + between (Eve’s law)
Y: outcome;X: group;µ(X)=E(Y|X).
Within groups: outcomes differ from their own group mean.
E[Var(Y|X)]=E
(Y−µ(X)) 2
Between groups: group means differ from the overall mean.
Var[E(Y|X)]=E
(µ(X)−E(Y)) 2
Var(Y)=E[Var(Y|X)]+Var[E(Y|X)] .
Wooldridge, App. 2A, CV .2. Finite second moment. Use group probabilities; standard deviations do not add.

### p.187
APPENDIX E · Wooldridge 2.2.4–2.2.5
Omitted variables and proxies

### p.188
Unobserved regressor: the error-form route
Why LIE is needed — start from the error form instead of the conditional mean
ERROR FORM; ABILITYqIS UNOBSERVED; T ARGET SLOPES IN BLUE
y=β 0 +β ss+β ee+γq+v,E(v|s,e,q)=0.
TakeE(· |s,e)of both sides; linearity leaves conditional expectations of
ability and the error:
E(y|s,e)=β 0 +β ss+β ee+γE(q|s,e)+E(v|s,e).
OnlyE(v|s,e,q)=0was assumed. Why isE(v|s,e)zero as well?

### p.190
The error’s mean on the coarser information: one application of LIE
ASSUMED ON THE FINER INFORMA TION(s,e,q)
E(v|s,e,q)=0.
E(v|s,e)=E[E(v|s,e,q)|s,e]=E[0|s,e]=0.
Zero conditional mean on the finer information(s,e,q)implies zero on the
coarser(s,e). The extra term drops out, and the main-route equation results.
Wooldridge 2.2.3, (2.15)–(2.16) define the error; 2.2.4, (2.21) is the LIE used; App. 2A, CE.3.

### p.192
Unobserved regressor: real data
NLS80 — why adding IQ changes the schooling coefficient
Without IQ With IQ
6
·10−2
.060
schooling coefficient
• Outcome:log(wage). Regressors:
schooling, with or without IQ.
• Adding IQ changes the schooling
coefficient from .060 to .039.
• Identity:
.03912+.005863×3.53383=.05984.
Omitted-variable algebra at work; no proof that IQ is a valid proxy.
Wooldridge Example 4.3 data;nls80.dta; regressions include an intercept.

### p.193
.039

### p.195
Unobserved regressor: interactions
Wooldridge 2.2.4, (2.26) — omitted interactions can create curvature
SCHOOLINGs, EXPERIENCEe, UNOBSERVED ABILITYq
E(y|s,e,q)=β 0 +β ss+β ee+γq+θsq,
E(y|s,e)=β 0 +β ss+β ee+(γ+θs)(δ 0 +δ ss+δ ee).
Expanding introducess 2 andse. More flexible fitting can describe the
observed CE without recovering the structural schooling effect.

### p.198
Proxy variables with interactions
Reading ahead — Lecture 3 and Wooldridge Chapter 4
If ability interacts with schooling, the structural partial effect varies with
ability:
E(y|s,e,q)=β 0 +β ss+β ee+γq+θsq,PE s =β s +θq.
The structural APE isβ s +θE(q); recovering it from a proxy requires more
algebra than the additive example.
• Read Wooldridge Chapter 4 on proxy variables.
• Lecture 3 develops the schooling–ability interaction and proxy calculation.

### p.200
APPENDIX F · Wooldridge 2.3
Linear projections

### p.201
Wooldridge 2.3, (2.38)–(2.42) — the best linear predictor of a curved mean
Which line, when conditional means are curved? The linear projection:
L(y|1,x)=b 0 +xb.
Its coefficients minimiseE[(y−b 0 −xb) 2], the mean squared prediction error.
Best among linear functions of the regressors; it need not equal the CE.
b1 = Cov(x,y)
Var(x) ,b 0 =E(y)−b 1E(x)(one regressor).
Finite second moments, nonsingular Var(x); general caseb=[Var(x)] −1Cov(x,y);v=y−L(y|1,x)hasE(v)=0 and
Cov(xj,v)=0.

### p.204
Linear projections: worked example
The best line can make systematic group errors
10
group means
schooling (years)
• Each schooling group has
probability 1/3; CE means are
4,8,10.
• Best line:
L(Y|1,X)=−5/3+.75X.
• CE matches each mean. The
best line misses them.
Withv=Y−L(Y|1,X):E(v)=0, butE(v|X=12)=2/3.
Illustrative population. Connecting group means is a visual guide.

### p.206
+2/3
−1/3