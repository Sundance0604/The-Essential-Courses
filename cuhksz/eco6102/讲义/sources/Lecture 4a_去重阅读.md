### p.1
Lecture 4a:
Instrumental Variables
Enjie (Jack) Ma
Lecture 4 · Mondays 12 and 19 October 2026

### p.2
Instrumental variables across two lectures
Our teaching text for IV is Wooldridge, Introductory Econometrics, sixth edition
We useIntroductory Econometrics, Chapter 15, for these two lectures. The
graduate book’s Chapter 5 supplies optional formal detail.
Lecture 4a: Sections 15-1–15-2
Motivating example; one instrument: assumptions, estimation, uncertainty
and controls.
Lecture 4b: Sections 15-3–15-6
2SLS with several instruments, weak instruments and specification tests.
Our emphasis is intuition and the interpretation of assumptions.

### p.3
Today’s contents
Intro 15-1–15-2
1. Motivation: Omitted Variables in a Simple Regression Model
2. Statistical Inference with the IV Estimator
3. Properties of IV with a Poor Instrumental Variable
4. Computing R-Squared after IV Estimation
5. IV Estimation of the Multiple Regression Model

### p.4
Some Terminology
Keep the population quantity separate from the sample calculation
log(wage)=β 0 +β 1educ+u
Parameter / estimand
β1: the population schooling effect we want to learn.
Estimator
ˆβ1: a rule that turns sample data into an answer; it varies across samples.
Estimate
A realized number, such as .059 , obtained from one sample.

### p.5
Population↔Sample
The population target stays fixed while the estimate changes
Random sample
{(xi,y i)}n
i=1
Schooling and
log wage
Estimator: OLS rule
ˆβ1,OLS =P
i(xi − ¯x)(yi − ¯y)P
i(xi − ¯x)2
One realized
number
ˆβ1,OLS =.109
Population target:β 1. A new
sample can give a different estimate.
Statistical propertiesdescribe the estimator across possible samples.

### p.6
Contents
Intro 15-1
Instrument conditions and candidate instruments
Identification and the IV estimator

### p.7
Revisiting OVB
Running wage example: OLS can mix schooling with ability
log(wage)=β 0 +β 1educ+γq+v
|{z}
u
,q=ability
Blue: instrument candidate Orange: endogenous Red: omitted
Schooling Log wage
β1
Abilityq

### p.8
Two approaches to omitted ability
Proxy controls for ability; IV changes the variation used
Same target
log(wage)=β 0 +β 1educ+γq+v.
1. ProxyAdd a measured proxypforq. It must capture the ability variation
that is related to schooling.
If a suitable proxy is unavailable, keep ability in the error and look for a valid
instrument.
2. Instrumental variableUse schooling variation linked to an instrumentz
withCov(z,u)=0.
Recall the proxy conditions

### p.9
Intro 15-1: instrument conditions

### p.10
Two conditions for an instrument z
Assumption 1: instrument exogeneity; assumption 2: relevance
y=β 0 +β 1x+u,E(u)=0
1. Instrument exogeneity:Cov(z,u)=0 (15.4)
2. Instrument relevance:Cov(z,x),0 (15.5)

### p.11
IV changes the source of variation
The schooling effect is the target; omitted ability still exists
Wage equation
log(wage)=β 0 +β 1educ+u.
Schoolingx Log wagey
β1: our target
Ability inu
Instrument
z
Ideal comparisonChange schooling; holdufixed.
Observed dataSchooling can move with omitted ability.
IVUsez-linked schooling variation, withCov(z,u)=0. This supports
consistency; ability still matters.

### p.12
Verifying relevance + exclusion condition
Check the first stage; defend the remaining wage paths
x=π 0 +π 1z+r, π 1 = Cov(z,x)
Var(z)
• RelevanceRegressxonz; examine the estimated sign, magnitude and
uncertainty.
• RejectingH 0 :π 1 =0 is a minimum check; it need not imply a strong instrument.
• ExogeneityCov(z,u)=0. Becauseuis unobserved, we generally cannot test this
directly.
◦ Defend no separate effect ofzon the outcome outsidex.
◦ Defend no association betweenzand omitted causes inu, using economic
behavior and the assignment process.

### p.13
Relevance in the schooling example
Does the instrument predict differences in schooling?
Target
log(wage)=β 0 +β 1educ+u, with ability inu.
Candidate instrumentFather’s schooling,fatheduc.
1.Cov(fatheduc,u)=0,
2.Cov(fatheduc,educ),0.
Fathers with more schooling may encourage or support more schooling for
their children.
educ=π 0 +π 1fatheduc+v,H 0 :π 1 =0
Check the expected positive relationship; assess exogeneity separately.

### p.14
Exogeneity in the schooling example
Exclude a separate wage effect of the instrument
Cov(fatheduc,u)=0
ExclusionFather’s schooling must have no separate effect on wages once
own schooling and omitted wage determinants are held fixed.
For example, family connections could raise wages through a channel other
than own schooling. That would threaten exclusion.

### p.15
Exogeneity also concerns omitted causes -
ability
A schooling mechanism can support relevance and threaten validity
Father’s schooling must also be unrelated to ability and other omitted wage
determinants. Family background makes this assumption debatable.
We can observe the schooling relationship. We need a separate argument
about these unobserved wage determinants.

### p.16
Locate the two instrument conditions
Relevance uses the schooling link; exogeneity rules out other wage paths
Maintained conditions
1.Cov(fatheduc,u)=0 2.Cov(fatheduc,educ),0.
Father’s
schooling
Own
schooling Log wage2 β1
1: omitted-factor association?
1: separate wage path?
Defend condition 1 by ruling out the two red instrument links.

### p.17
Choosing a IV candidate - Not Easy!
One condition can hold while the other fails
Which condition is at risk for each candidate?
Candidate Relevance Exogeneity
Cov(z,educ),0Cov(z,u)=0
SSN last digit No schooling mechanism Plausibly unrelated to ability
IQ Related to schooling Tracks ability inu
A good ability proxy is usually a poor schooling IV: it tracks ability.

### p.18
Family background as an instrument
Plausible schooling links still need an exogeneity argument
Does a plausible schooling link settle instrument validity?
Candidate Relevance Exogeneity concern
Mother’s schooling Usually positive May track ability and nurturing
Number of siblings Usually negative Other family wage paths

### p.19
Skipping classes and exam scores
Distance may predict absence, but family income can threaten exogeneity
score=β 0 +β 1skipped+u(15.8)
ConcernAbility and motivation may affect both attendance and scores.
Candidate instrument
Distance from living quarters to campus may increase missed classes. Check
the expected positive first-stage relationship.
Exogeneity concern
Family income may affect both where a student lives and exam performance.
Distance could then be correlated withu.
Section 15-2 will show how to include observed controls.

### p.20
Intro 15-1: identification and estimation

### p.21
Recall identification
Would the population information determine one value of the target?
y=β 0 +β 1x+u
IdentificationUnder the model and maintained assumptions, the population
distribution of the observable variables(y,x,z)determines one value ofβ 1.
Population information
Cov(z,y),Cov(z,x)
Unique target
Model and
IV assumptions
Identification is a population question. We still need a sample to estimate
those moments.

### p.22
From identification to an estimate
First find the population answer, then use a sample to estimate it
y=β 0 +β 1x+u. We want the population slopeβ 1.
Population moments
Population target
Identification
{(yi,x i,z i)}n
Sample estimate
ˆβ1,IV
Sampling
Sample analogues
Inference
InferenceUse sampling variation to assess uncertainty aboutβ 1.

### p.23
Identification with IV
Population moments determine the target under the assumptions
IdentificationWe can writeβ 1 in terms of population moments that can be
estimated using a random sample from the population.
y=β 0 +β 1x+u,Cov(z,u)=0
Cov(z,y)=Cov(z, β 0 +β 1x+u)
Cov(z,y)=β 1 Cov(z,x)+Cov(z,u)|    {z    }
=0 by exogeneity

### p.24
The identified population slope
Relevance makes the covariance ratio well defined
Model and conditions
y=β 0 +β 1x+u.
Cov(z,u)=0,Cov(z,x),0.
β1 = Cov(z,y)
Cov(z,x) (15.9)
• ExogeneityRemoves the error covariance.
• RelevanceMakes division possible.
• Both remaining moments involve observable variables.
Next, replace these population moments with sample analog.

### p.25
A covariance is a population moment
The expectation tells us which sample average to calculate
Identified target
β1 =Cov(z,y)/Cov(z,x).
Numerator
Cov(z,y)=E[(z−Ez)(y−Ey)]
⇓
1
n
nX
(zi − ¯z)(yi − ¯y)
Denominator
Cov(z,x)=E[(z−Ez)(x−Ex)]
(zi − ¯z)(xi − ¯x)
Population averages become sample averages; population means become sample
means.

### p.26
The IV estimator
Replace population covariances with sample covariances
ˆβ1,IV =
Pn
i=1(zi − ¯z)(yi − ¯y)Pn
i=1(zi − ¯z)(xi − ¯x) (15.10)
ˆβ0,IV = ¯y− ˆβ1,IV ¯x
• The intercept makes the fitted line pass through( ¯x, ¯y).
• With exogenousx, usingz=xgives the OLS estimator.

### p.27
Taking stock: IV assumptions and estimator
Identify the population slope, then estimate it from a sample
y=β 0 +β 1x+u,Cov(z,u)=0,Cov(z,x),0.
Identified targetβ 1 =Cov(z,y)/Cov(z,x).
P
i(zi − ¯z)(yi − ¯y)P
i(zi − ¯z)(xi − ¯x)
p
− →β1
With random sampling and finite moments, IV is consistent.
Next, quantify samplinguncertaintywith a standard error.
Why the sample ratio is consistent

### p.28
Intro 15-1a
Precision and the return to education
Binary instruments and binary treatments

### p.29
Homoskedasticity for IV inference
The condition is stated relative to the instrument
y=β 0 +β 1x+u,E(u)=0,Cov(z,u)=0,Cov(z,x),0
E(u2 |z)=σ 2 =Var(u)(15.11)
This additional assumption concerns the structural erroruand the
instrumentz.
With random sampling and the required finite moments, IV has a
large-sample normal approximation.
Why the second moment equals the variance

### p.30
What determines IV precision?
Noise raises uncertainty; variation and relevance reduce it
y=β 0 +β 1x+u; validz, homoskedastic errors.
Avar(ˆβ1,IV)= σ2
nVar(x)ρ 2
xz
(15.12)
ρxz =Corr(x,z).

### p.31
Read the three ingredients of IV precision
Hold the other ingredients fixed when changing one
IV variance
Avar(ˆβ1,IV)=σ 2/[nVar(x)ρ 2
xz].
• Noiseσ 2
◦ More structural noise⇒larger SE.
• SpreadVar(x)
◦ More regressor variation⇒smaller SE.
• Relevanceρ 2
◦ Stronger instrument–regressor association⇒smaller SE.

### p.32
Estimating the ingredients of IV variance
Start with the estimated variance, then read its ingredients
[Avar(ˆβ1,IV)= ˆσ2
SSTx R2
x,z
(15.13)
• SSTx = P
i(xi − ¯x)2:SST x/nestimatesVar(x).
• First-stageR 2
x,z estimatesρ 2
xz.
• ˆσ2 = P
i ˆu2
i /(n−2)estimates structural noise. We next calculate its
residuals.
Structural residuals R-squared and correlation

### p.33
Use the structural equation for IV residuals
The coefficients come from IV; the regressor is the observed x
Structural model
yi =β 0 +β 1xi +u i.
ˆui =y i − ˆβ0,IV − ˆβ1,IVxi
Useactualx i here. The instrument enters through the IV coefficient
estimates.

### p.34
Estimate noise from the structural residuals
Adjust for the two estimated structural coefficients
Structural residual
ˆui =y i − ˆβ0,IV − ˆβ1,IVxi.
ˆσ2 = 1
n−2
ˆui
2
There are two estimated coefficients: the intercept and slope. This
adjustment does not make the estimate exactly unbiased.

### p.35
The IV standard error
Estimate the variance, then take its square root
Estimated variance
[Avar(ˆβ1,IV)= ˆσ2/[SSTx R2
x,z].
se( ˆβ1,IV)=
s
ˆσ2
A smaller first-stageR 2 means a larger standard error, holding other
ingredients fixed. This is the uncertainty we use in tests and intervals.

### p.36
With SE→Hypothesis test and CI
The usual normal approximation is a large-sample claim
t=
ˆβ1 −β 1,0
se( ˆβ1)
a
∼N(0,1)underH 0 :β 1 =β 1,0
Approximate 95% CI: ˆβ1 ±1.96se( ˆβ1)

### p.37
Example 15.1: the return to schooling
Schooling and omitted ability: same target, one common sample
• Sample428 working married women; hourly wage and years of
education.
• InstrumentFather’s years of education,fatheduc.
• Maintained claimFather’s education is uncorrelated with omitted
determinants inu; family background makes this debatable.

### p.38
Example 15.1: OLS benchmark
An extra schooling year is associated with about eleven percent more pay
Outcome model
log(wage)=β 0 +β 1educ+u. Same 428 working women.
OLS term Coefficient SEtfor zero
Intercept−.1852.1852−1.00
Schooling .1086 .0144 7.55
One more schooling year is associated with roughly 10.9% higher pay.
To claim 10.9%as causal requires schooling to be exogenous in this equation (clearly,
its not!)

### p.39
Example 15.1: first-stage evidence
Father’s schooling predicts the daughter’s schooling
First stage and relevance
educ=π 0 +π 1fatheduc+r;Cov(fatheduc,educ),0. Samen=428.
First-stage term Coefficient SEtfor zero
Father’s schooling .2694 .0286 9.43
An extra year of father’s schooling predicts .27 more years for the daughter.
π1 ,0⇐ ⇒Cov(fatheduc,educ),0.
✓Evidence of relevance; exogeneity still needs an argument.
Why the slope measures relevance

### p.40
Example 15.1: IV estimate
The estimated return is smaller and much less precise
log(wage)=β 0 +β 1educ+u; instrument:fatheduc,n=428.
dCov(fatheduc,log(wage))
dCov(fatheduc,educ)
=.0592
IV term Coefficient SEtfor zero
Intercept.4411.4461.99
Schooling .0592 .0351 1.68
The estimated return is about 5.9% .

### p.41
Example 15.1: an interval for the return
The coefficient’s uncertainty matters for interpretation
Same wage equation
log(wage)=β 0 +β 1educ+u; IV estimate.0592, SE .0351 .
95%CI:.0592±1.96(.0351)≈[−.0096, .1280]
This is a large-sample interval under the maintained instrument and
inference assumptions.

### p.42
Example 15.1: what did IV change?
First compare the estimated schooling returns
log(wage)=β 0 +β 1educ+u. Same 428 women.
Method Schooling slope SE
OLS .1086 .0144
IV: father’s education .0592 .0351
ˆβ1,IV =.0592< .1086= ˆβ1,OLS: IV gives the smaller estimated return.
Can omitted-variable-bias logic explain why the OLS estimate is so much larger
than IV?

### p.43
Why omitted ability can push OLS upward
Schooling can receive credit for an omitted wage advantage
Model
log(wage)=β 0 +β 1educ+γability+v.
Omitted ability
positive γ >0
If ability raises both schooling and wages, OLS can give schooling credit for
an omitted wage advantage.

### p.44
IV focuses on variation linked to the
instrument
The ability paths remain while our attention shifts
Maintained condition
log(wage)=β 0 +β 1educ+u;Cov(fatheduc,u)=0.
schooling Schooling Log wage
IV uses the schooling variation linked to father’s schooling. The ability paths
still exist.

### p.45
The omitted-ability bias in the equation
The positive covariance adds to the schooling slope
AssumeCov(educ,v)=0.
plim ˆβ1,OLS =β 1 +γ
>0
Cov(educ,ability)
Var(educ)|                {z                }
> β1

### p.46
Why both omitted-ability signs are positive
The two wage-example mechanisms explain the bias direction
Bias term
OLS distortion:γCov(educ,ability)/Var(educ).
• γ >0: higher ability raises wages, holding schooling fixed.
• Cov(educ,ability)>0: people with higher ability tend to obtain more
schooling.
IV estimate lower than OLS is compatible with this upward-bias story.

### p.47
Example 15.1: compare the uncertainty
First observe the larger IV standard error
The IV standard error is about 2.44 times the OLS standard error in this
sample.
Why is the IV estimate less precise?

### p.48
Why IV can have a larger standard error
An exogenous-regressor benchmark: both OLS and IV are valid
Valid-OLS benchmark
y=β 0 +β 1x+u, withCov(x,u)=0. Both OLS and IV are valid; assume
homoskedasticity, random sampling and fixed nonzero relevance.
OLS
Avar(ˆβ1,OLS)= σ2
nσ 2
x
Uses all regressor variation:x
instruments itself.
IV
x ρ2
Uses the variation associated withz.

### p.49
The precision cost of instrument-linked
variation
A smaller instrument-regressor correlation raises the SE
Same valid-OLS benchmark
y=β 0 +β 1x+u,Cov(x,u)=0.
Avar(ˆβ1,IV)
Avar(ˆβ1,OLS)
= 1
ρ2
,0< ρ 2
xz ≤1
IV’s asymptotic SE is 1/|ρxz|times as large. A correlation of.5 doubles it.
Less instrument-linked variation means a larger SE.

### p.50
A guide to an IV analysis
Use the wage example to organize the design before estimation
Start here
log(wage)=β 0 +β 1educ+u. Target: the return to one more schooling year.
1 Name the concernAbility inumay be related to schooling.
2 Propose an instrumentWhy might father’s schooling predict own
schooling?
3 Defend exogeneityWhat other wage paths or shared omitted causes
could make this instrument invalid?
4 Check relevanceRegress schooling on father’s schooling. Examine sign,
magnitude and uncertainty.

### p.51
A guide to reading the IV results
Interpret the effect and its uncertainty under the stated assumptions
Same target and sample
log(wage)=β 0 +β 1educ+u. Compare OLS and IV for the same 428 women.
5 EstimateReport the IV coefficient and standard error. Keep OLS as a
benchmark.
6 InterpretIV gives about a 5.9%return per schooling year, if the
instrument assumptions hold.
7 Compare carefullyInterpret the IV-OLS difference within the OVB angle.
After the break, we ask whether IV must always give a lower return.

### p.52
Example 15.2: returns to education for men
An example where IV>OLS
WAGE2: 935 men, instrument: siblings
First stage
deduc=14.14− .228 sibs,SE( ˆπ1)=.030
One more sibling predicts about .23 fewer schooling years. (makes sense)
Relevance permits either sign:Cov(sibs,educ)<0 is nonzero.

### p.53
Example 15.2: compare the returns
IV can give a larger schooling coefficient than OLS
Same 935 men
log(wage)=β 0 +β 1educ+u. Instrument: number of siblings.
OLS .059 .006
IV: siblings .122 .026
ˆβ1,IV =.122> .059= ˆβ1,OLS: IV gives a larger estimated return.
IV also has the larger SE. This differs from the coefficient ordering in the
married women’s sample.

### p.54
Example 15.2: what should we conclude?
One possible story is that siblings is an invalid instrument
log(wage)=β 0 +β 1educ+γability+v. Instrument:sibs.
Siblings Schooling Log wage
π1 <0 β1
γ >0possible negative association
Less parental attention could link siblings to ability:Cov(sibs,u)<0.

### p.55
A possible upward distortion of the IV
estimate
Two negative covariances can produce a positive IV distortion
AssumeCov(sibs,u)<0; maintainCov(sibs,educ)<0.
plim ˆβ1,IV =β 1 +
Cov(sibs,u)|        {z        }
<0
Cov(sibs,educ)|            {z            }

### p.56
What the conditional sign story can establish
The observed ordering cannot diagnose either estimator’s distortion
Conditional conclusion
log(wage)=β 0 +β 1educ+u. If both covariances are negative,plim ˆβ1,IV > β1.
This hypothesis would push IV upward.
It does not establish downward OLS bias. The coefficient ordering alone
cannot tell us which estimator is closer to the true return.

### p.57
Intro 15-1a: binary instruments

### p.58
An instrument can also be binary
The same two conditions apply to numerical variables and indicators
Same requirements
So far, schooling and the instruments are quantitative variables: years of
father’s schooling or number of siblings.
We now allowx,z, or both to be binary variables.
Binary instrument candidate z
Was the man born in the first quarter? It may shift years of schooling.
Binary regressor x
Did the man serve in the military? A draft lottery may shift that probability.

### p.59
Quarter of birth and school leaving
Angrist and Krueger (1991): two clocks can change required schooling
How could your birth month affect how many years you spend in school?
log(wage)=β 0 +β 1educ+u;frstqrt=1 for a January–March birth, zero
otherwise.
• School entryHistorical US entry rules placed children into annual
cohorts. Early-year births tended to begin at an older age.
• School leavingAttendance laws generally required staying until a
specified birthday, often age 16; permission to leave did not require
high-school completion.
School-grade progress and chronological age are different clocks.

### p.60
The same school cohort, different birthdays
A January birthday reaches age sixteen eight months sooner
For this example, suppose children who turn six in the same calendar year
enter together in September.
January birth
Age 6 years 8 months
September birth
Age 6 years
Same September
entry 16th birthday
9 years 4 months after entry
16th birthday
10 years after entry
8 months

### p.61
Earlier permission does not force dropout
Calendar time since entry is different from completed grades
Our common-entry example
Both enter in September of the year they turn six; legal leaving age is 16.
Birthday Age at entry Time until age 16
January 6 years 8 months 9 years 4 months
September 6 years 10 years
The January-born student has an earlieropportunityto leave. It does not
force dropout or guarantee one fewer completed grade.

### p.62
Who responds to permission to leave?
The mechanism concerns students constrained by the leaving-age rule
Two clocks
Same school-entry cohort; different dates at which age 16 is reached.
• Would leave before the legal ageAn earlier sixteenth birthday can allow
less schooling.
• Would continue through graduationEarlier permission to leave need not
change schooling.
Birth timing changes required schooling for potential dropouts.
Because only part of the cohort responds, the average schooling difference
can be small.

### p.63
Birth quarter as a candidate instrument
Relevance links birth timing to schooling through the school rules
Model and relevance
log(wage)=β 0 +β 1educ+u;Cov(frstqrt,educ),0.
First-quarter
birth Schooling Log wage
School rules
Relevance
Birth quarter predicts only a small schooling difference: the first-stageR 2 is
small. That can make the IV estimate imprecise.

### p.64
Quarter of birth: what is still assumed?
The school-law mechanism does not settle other wage paths
Maintained exogeneity
log(wage)=β 0 +β 1educ+u;Cov(frstqrt,u)=0.
Family
background
/ health
Seasonal family or health differences could threaten exogeneity.

### p.65
Quarter of birth: another wage pathway?
Relative-age effects beyond completed schooling could threaten exclusion
Same model
log(wage)=β 0 +β 1educ+u. Instrument: first-quarter birth.
Another wage path?
Relative-age effects on later wages beyond completed schooling could
violate exclusion. This is a validity question, not an established path.

### p.66
Quarter of birth: estimates and uncertainty
A binary instrument can identify a return but leave substantial uncertainty
Sample
247,199 men born in 1920–1929.log(wage)=β 0 +β 1educ+u.
Method Schooling slope SE Approx.t
OLS .0801 .0004 200
IV: first-quarter birth .0715 .0219 3.26
ˆβ1,IV =.0715< .0801= ˆβ1,OLS: IV estimates about a 7.2% return.
The small first-stage relationship leaves IV much less precise than OLS, despite the
very large sample.
Optional paper calculation

### p.67
Binary regressor example: Veteran status and
lifetime earnings
A binary treatment can be endogenous because people select into it
log(earns)=β 0 +β 1veteran+u(15.18)
veteran=1 for a Vietnam War veteran, zero otherwise. We want the effect of
military service on earnings.
People who expect to gain more from military service may choose to join.
Their other characteristics may also affect earnings.
OLS can therefore mix the service effect with self-selection.

### p.68
Self-selection can confound military service
and earnings
Civilian opportunities can affect both the service decision and later earnings
log(earns)=β 0 +β 1veteran+u.
Military service Later earnings
β1: service effect
Prior civilian
opportunities / health

### p.69
We need variation unrelated to prior
opportunities
Veterans and nonveterans can differ before service
Selection concern
log(earns)=β 0 +β 1veteran+u;Cov(veteran,u),0.
Veterans and nonveterans may differ in earning potential before service. OLS
can mix the service effect with those prior differences.
What could change military service independently of prior opportunities?

### p.70
The draft lottery as a natural experiment IV
Random draft priority can change the probability of service
log(earns)=β 0 +β 1veteran+u. Instrument: draft lottery number.
• Random assignmentIn the randomized lotteries, numbers assigned draft
priority independently of pre-existing earning potential.
• RelevanceLow numbers raised the chance of being called to serve, so the
number predicted veteran status.
Letz=eligibleindicate a number low enough for call-up.Eligibilityis the
assignment;veteranis actual service.

### p.71
Random eligibility, nonrandom service
Assignment can be random even when the response to it is not
log(earns)=β 0 +β 1veteran+u;z=eligiblefrom randomized draft priority.
Random
eligibility Actual service Earnings
Prior opportunities
Some eligible men avoid or are exempted from service; some ineligible men
volunteer. Actual service need not be random.

### p.72
A natural experiment still needs exclusion
Draft avoidance could create another path to earnings
log(earns)=β 0 +β 1veteran+u. Instrument: draft eligibility.
Suppose low draft numbers induce more schooling to avoid service.
Eligibility Military
service Earnings
Extra schooling

### p.73
Random assignment leaves an exclusion
question
Behavior in response to assignment can create another earnings path
• The lottery could change earnings through schooling, as well as military
service. That would violate exclusion in this model.
• Random assignment addresses prior differences; it does not eliminate
additional paths created in response to assignment.

### p.74
Intro 15-1b

### p.75
OLS and IV use different variation
Consistency requires the estimating variation to be uncorrelated with the structural
error
y=β 0 +β 1x+u, withCov(z,x),0.
Which variable must be unrelated to the structural error?
OLS usesxCov(x,u)=0.
IV useszCov(z,u)=0.
IV can be consistent even whenCov(x,u),0; its instrument must provide
variation unrelated tou.

### p.76
OLS and IV probability limits
Any remaining IV error correlation is divided by instrument relevance
plim ˆβ1,OLS =β 1 +Corr(x,u) σu
σx
(15.20)
plim ˆβ1,IV =β 1 + Corr(z,u)
Corr(z,x)
σu
(15.19)
IV divides the exogeneity violation by relevance; both correlations matter.
OLS limit IV limit

### p.77
Weak relevance can magnify bias
A small instrument-error correlation can become a large asymptotic bias
Asymptotic biasIV = Corr(z,u)
HoldCorr(z,u)=.02 andσ u/σx =1 fixed.
What happens to the bias when instrument relevance falls?

### p.78
A weaker denominator gives a larger bias
Hold the instrument-error correlation fixed
Asymptotic biasIV =.02/Corr(z,x), withσ u/σx =1.
RelevanceCorr(z,x) .50 .05
Asymptotic bias of IV .04 .40
Weak relevance magnifies even a small exogeneity violation.
Exact exogeneity gives zero asymptotic bias. Weak relevance can still make
inference unreliable.

### p.80
Example 15.3: Weak IV
Cigarette price barely predicts packs smoked
log(bwght)=β 0 +β 1packs+u.n=1,388.
Higher cigarette prices might reduce smoking.
First stagepacks=π 0 +π 1cigprice+r.
First-stage term Coefficient SE
Cigarette price .0003 .0008
Does the first stage show a clear price–smoking relationship?
The slope is close to zero.
Its SE is much larger: there is little evidence that this price measure shifts smoking.

### p.82
Example 15.3: an unstable IV estimate
Weak first-stage evidence cannot establish that smoking has no effect
log(bwght)=β 0 +β 1packs+u.
IV coefficient on packs 2.99
SE 8.70
Does this show that smoking has no effect?
Uninformative and noisy estimate!
Weak first-stage evidence gives an uninformative IV design; a lack of significance
does not establish a zero effect.
Revisit the first stage IV R-squared

### p.84
Intro 15-1c

### p.85
Structural IV fit: first estimate the coefficients
Use the instrument moment conditions
dCov(z,y)
dCov(z,x)
, ˆβ0,IV = ¯y− ˆβ1,IV ¯x.
These coefficients use the instrument. They do not minimize the squared
errors from regressingyon observedx.

### p.86
Structural IV fit: calculate residuals
Use actual x in the original structural equation
Should this residual use actualx i or a first-stage prediction?
Use actualx i. The instrument enters through the IV coefficient estimates.
Even when a first stage computes those coefficients, use observedx i in the
structural residual.

### p.87
Structural IV fit: compare with the mean
A negative R-squared means worse squared-error fit than predicting the mean
R2
IV =1−
iP
i(yi − ¯y)2 .
The denominator is the squared error from predicting ¯yfor everyone.
OLS minimizes squared errors, so itsSSR≤SST. IV uses instrument
moments, soSSR IV >SSTis possible.
Negative fit and cross term Population variance intuition

### p.88
The IV line can fit worse than the mean
Structural R-squared measures sample fit; it does not establish instrument validity
yi =β 0 +β 1xi +u i. Suppose the structural slope is 1.
−2 −1 0 1 2
−2
0
y
Prediction Squared errors
Mean ¯y=0 1.25
OLS:.25x .625
IV: 1x 6.25
IV =1− 6.25
1.25 =−4.
IV:P ziyi/P zixi =10/10=1.

### p.89
Intro 15-2
Moment equations and conditional relevance
College proximity and program eligibility

### p.90
IV in a multiple regression model
An included exogenous regressor stays in the structural equation
y1 =β 0 +β 1y2 +β 2z1 +u 1 (15.22)
• Endogenous regressory 2 may be correlated withu 1.
• Included exogenous regressorz 1 has its own effect and is uncorrelated
withu 1.
• Excluded instrumentz 2 is uncorrelated withu 1, excluded from this
equation, and predictsy 2 afterz 1.

### p.91
The wage equation with an experience control
Education can remain endogenous after experience is included
log(wage)=β 0 +β 1educ+β 2exper+u 1 (15.23)
• ExperienceAssume it is exogenous. It has its own wage effect and
• Father’s educationA further excluded instrument is needed for
schooling. It must predict schooling after experience is held fixed.
Instrument roles Partial relevance

### p.92
Three population moment conditions
Assumptions supply equations for three structural coefficients
Wage mapping
y1 =log(wage),y 2 =educ,z 1 =exper,z 2 =fatheduc.
E(u1)=0,Cov(z 1,u 1)=0,Cov(z 2,u 1)=0 (15.24)
E(y1 −β 0 −β 1y2 −β 2z1)=0,
E[z1(y1 −β 0 −β 1y2 −β 2z1)] =0,
E[z2(y1 −β 0 −β 1y2 −β 2z1)] =0.
These equations identifyβ 0, β1, β2 when the relevance/rank condition makes
the system nonsingular.

### p.93
The sample method of moments
Solving these equations gives the multiple-regression IV estimator
ˆui1 =y i1 − ˆβ0 − ˆβ1yi2 − ˆβ2zi1.
Xn
ˆui1 =0 mean error
zi1 ˆui1 =0 experience
zi2 ˆui1 =0 father’s schooling
(15.25)
Solve these three sample equations for the three IV coefficients.

### p.94
Relevance after including a control
The instrument must predict schooling beyond experience
y2 =π 0 +π 1z1 +π 2z2 +v 2 (15.26)
y2 =educ,z 1 =exper,z 2 =fatheduc.
π2 ,0 (15.27)
Estimate this first stage and test the father’s-schooling coefficient. The
required association remainsafter experience is held fixed.

### p.95
The first stage with several controls
The excluded instrument has a partial effect beyond all included controls
y1 =β 0 +β 1y2 +β 2z1 +· · ·+β kzk−1 +u 1.
y2 =π 0 +π 1z1 +· · ·+π k−1zk−1 +π kzk +v 2 (15.30)
In the college example,y 2 =educ, and the excluded instrument isz k =nearc4.
πk ,0 means the instrument predicts schooling after the included controls.

### p.96
Intro 15-2: Example 15.4

### p.97
Example 15.4: college proximity
Access may shift schooling, but location needs an exclusion argument
log(wage)=β 0 +β 1educ+control effects+u.
• Sample3,010 men; wages and education measured in 1976; the same
observations and controls in OLS and IV .
• Instrumentnearc4: lived near a four-year college in 1966.
• Controls
◦ Experience and its square:exper,exper 2; black and South indicators:
black,south.
◦ Standard metropolitan statistical area (SMSA): currentsmsaand 1966
smsa66; 1966 regions:reg662, . . . ,reg669.

### p.98
Example 15.4: first-stage evidence
Nearby colleges predict more schooling after controls
educ=π 0 +π near nearc4+control effects+r.
Excluded instrument Coefficient SEtfor zero
Near a college .320 .088 3.64
Same 3,010 men and controls as the outcome equation.
Nearby colleges predict about one third of an additional schooling year,
holding the controls fixed.
This supports conditional relevance.π near ,0 in the population first stage
after the controls.

### p.100
Example 15.4: OLS and IV
Read the coefficient and its SE together
log(wage)=β 0 +β 1educ+controls+u.
Table 15.1 OLS IV (nearc4)
Schooling coefficient .075 .132
SE .003 .055
IV gives a larger point estimate with much greater uncertainty.

### p.102
The instrument can predict the outcome too
A first-stage coefficient and an outcome reduced-form coefficient have different units
y1 =β 0 +β 1y2 +controls+u 1.
How doesz k changey 2, after the controls?
Outcome reduced form
How does the samez k changey 1, after the same controls?
Use a program offer to distinguishparticipationfrom theoutcomeresponse.

### p.103
Program eligibility and participation
Distinguish eligibility, take-up and the outcome
zk =1: eligible;y 2 =1: participates;y 1: outcome. Some eligible people do not
participate.
y1 =β 0 +β 1y2 +controls+u 1 structural
y2 =π 0 +π kzk +controls+v 2 first stage
y1 =γ 0 +γ kzk +controls+e 1 outcome reduced form
The three coefficients describe different responses:β 1, outcome effect of
participation;π k, participation after eligibility;γ k, outcome after eligibility.

### p.104
The outcome also has a reduced form
Under IV exogeneity and exclusion, eligibility works through participation
y1 =β 0 +β 1y2 +controls+u 1,
y2 =π 0 +π kzk +controls+v 2,
y1 =γ 0 +γ kzk +controls+e 1.(15.32)
Eligibilityz k Participationy 2 Outcomey 1
πk β1
γk =β 1πk: combined outcome response to eligibility
Reduced-form substitution Exclusion and exogeneity

### p.105
Offering a program and participating in it
An eligibility effect allows for nonparticipation
y1 =β 0 +β 1y2 +controls+u 1, withγ k =β 1πk.
• πk: eligibility’s change in participation probability, after controls.
• β1: participation’s effect on the outcome under the constant-effect model.
• γk: eligibility’s effect on the outcome, allowing for nonparticipation: the
intention-to-treateffect.
Supposeπ k =.20 andβ 1 =5:γ k =5×.20=1 outcome unit.

### p.106
A practical guide to a good instrument
Assess the design and the evidence together
• Start with the population/structural modelState the causal coefficient
and what remains inu.
• MechanismExplain howzchanges the endogenous regressor.
• First stageCheck the sign, magnitude and strength after the same
controls.
• ExogeneityDefend both the absence of other outcome paths and the
absence of shared omitted causes.
• UncertaintyReport appropriate IV uncertainty; a strong first stage alone
does not establish validity.
Weak instruments

### p.107
What you should be able to do
Prepare to assess and interpret an instrumental-variables argument
• State the outcome equation, target effect, endogenous variable and be able
to propose reasonable IV candidate in different context.
• Explain exogeneity/exclusion and relevance in the application, including
relevance after controls.
• Interpret an IV estimate, its uncertainty and evidence of a weak
Deriving IV consistency is not required for assessment; the argument
remains available for further reading.

### p.108
Where to read further
Match today’s questions to further reading
Topic Intro 6e
Assumptions and estimation 15-1, pp.462–465
Uncertainty and examples 15-1a, pp.466–469
Poor instruments 15-1b, pp.469–471
Interpreting IV R-squared 15-1c, p.471
IV with controls 15-2, pp.471–475
Optional formal detail: the graduate book’s Chapter 5 and the IV
supplement.
Optional explanations

### p.109
Next lecture
More than one excluded instrument leads to two-stage least squares
• Lecture 4bTwo-stage least squares, weak instruments, measurement
error, specification tests and robust inference.
• ReadIntroductory Econometrics15-3–15-6, including endogeneity and
overidentification tests.
• Problem Set 2 due Friday 23 October 2026; Midterm: Monday 26 October
2026, 09:00–11:00. Coverage: L1–L4.
Adapted from slides by Shuyang Sheng and Qihui Chen

### p.110
Short derivations for the main lecture
Proxy substitution
Structural residuals
R-squared and correlation
OLS probability limit
IV probability limit
Simple-IV consistency
Negative IV R-squared
Sample cross term
Variance decomposition
First-stage slope and relevance
Extended proofs and applications:Instrumental Variables Supplement, contents
by Chapter 15 topic.

### p.111
The error second moment
A conditional restriction implies an unconditional second moment
E(u2 |z)=σ 2 =Var(u).(15.11)
The conditional-second-moment restrictionE(u 2 |z)=σ 2 is assumed. Also
assumeE(u)=0.
E(u2)=E
h
E(u2 |z)
i
=E(σ 2)=σ 2.
From second moment to variance Back to IV inference assumptions

### p.112
From the second moment to the variance
Mean-zero error makes its second moment equal its variance
E(u2)=σ 2 andE(u)=0.
Var(u)=E(u 2)−[E(u)] 2 =σ 2 −0=σ 2.
ThusE(u 2 |z)=σ 2 =Var(u): the second equality follows from LIE and the
mean-zero error.
Cov(z,u)=0 alone does not implyE(u|z)=0, or a constant conditional
second moment.
Back to IV inference assumptions

### p.113
What the proxy changes in the equation
Proxy review: the remaining error must be exogenous
y=β 0 +β 1educ+γ(δ 0 +δ pp+r)
|          {z          }
q
+v
=(β 0 +γδ 0)+β 1educ+γδ pp+(γr+v)
|  {z  }
e
.
Under the proxy conditions,E(e)=0 andCov(educ,e)=Cov(p,e)=0. With full rank
and the usual sampling and moment conditions, OLS on schooling and the proxy
consistently estimatesβ 1.
Back to proxy conditions

### p.114
Structural residuals estimate structural noise
Use the observed regressor when calculating the residual
ˆu2
• Two fitted structural coefficients: intercept and slope.
• zenters through the coefficient estimates. The adjustment does not make
ˆσ2 exactly unbiased.
Back to estimated IV variance

### p.115
R-squared equals squared correlation
Simple regression with an intercept; either direction gives the same R-squared
Centered sumsS ab = P
i(ai − ¯a)(bi − ¯b).
ˆπ1 = Sxz
Szz
,R 2
xonz =
ˆπ2
1Szz
Sxx
xonz = S2
SxxSzz
= [Corr(x,z) 2 =R 2
zonx .
Estimatesρ 2
xz, notρ xz. Requires an intercept and variation in both variables;
does not generally hold with multiple regressors.
Back to the IV standard error

### p.116
Derivation of the OLS probability limit
Expand the covariance; then use the correlation definition
Fory=β 0 +β 1x+u, use random sampling, finite moments andVar(x)>0.
plim ˆβ1,OLS = Cov(x,y)
Var(x)
=β 1 + Cov(x,u)
σ2
=β 1 +Corr(x,u) σu
.(15.20)
Back to the OLS probability limit

### p.117
Derivation of the IV probability limit
Relevance permits division; exogeneity removes the distortion
Fory=β 0 +β 1x+u, use random sampling, finite moments andCov(z,x),0.
plim ˆβ1,IV = Cov(z,y)
Cov(z,x) =β 1 + Cov(z,u)
Cov(z,x)
=β 1 + Corr(z,u)σ zσu
Corr(z,x)σ zσx
=β 1 + Corr(z,u)
.(15.19)
Back to the IV probability limit

### p.118
Consistency of simple IV
Scalar case of Intro Theorem 15A.1
With random sampling and the required finite moments,
− →Cov(z,y)
Cov(z,x) =β 1.
Thus ˆβ0,IV = ¯y− ˆβ1,IV ¯x
− →β0.
Intro Theorem 15A.1 gives the general consistency result under Assumptions
2SLS.1–2SLS.4.
Back to IV consistency

### p.119
Why IV R-squared can be negative
The IV line can fit worse than the mean-only prediction
ˆuIV
i =y i − ˆβIV
0 − ˆβIV
1 xi,R 2 =1− SSRIV
SST
Mean-only benchmarkPredicting ¯yfor everyone gives squared errorSST.
OLSWith an intercept, least squares guaranteesSSR OLS ≤SST.
IVInstrument moment conditions do not minimize squared errors.
StructuralSSR IV can exceedSST, giving negativeR 2.
Sample cross term Back to IV R-squared

### p.120
The OLS decomposition contains a cross term for IV
yi − ¯y=( ˆyi − ¯y)+ ˆui, ˆyi = ˆβ0 + ˆβ1xi
SST=
X
(ˆyi − ¯y)2 +
i +2
(ˆyi − ¯y) ˆui
• OLS residuals are orthogonal toxin the sample, even ifxis endogenous;
the cross term vanishes.
• Simple IV makes P
i zi ˆui =0; it does not generally make P
i xi ˆui =0.
These residuals use actualx i, not first-stage fitted ˆxi. Thus structuralSSRcan
exceedSST, giving 1−SSR/SST<0.
Back to IV R-squared

### p.121
Why structural error variance can exceed
outcome variance
The structural component and error can offset each other
Var(y)=β 2
1 Var(x)+Var(u)+2β 1Cov(x,u).
IfCov(x,u)=0, total variance sums two nonnegative pieces.
A sufficiently negative cross term can make total variance smaller than either
component. Negative structuralR 2 is possible, not inevitable.
Variance derivation Numerical example Back to structural IV fit

### p.122
Deriving the variance decomposition
The cross term is present before exogeneity is imposed
Centered structural equation
y−E(y)=β 1[x−E(x)]+[u−E(u)].
[y−E(y)] 2 =β 2
1[x−E(x)] 2 +[u−E(u)] 2
+2β 1[x−E(x)][u−E(u)].
1 Var(x)+Var(u)+2β 1 Cov(x,u).
Taking expectations yields the identity. Only the extra condition
Cov(x,u)=0 removes its last term.
Back to the variance identity

### p.123
A negative population fit measure
The components can offset each other
Supposeβ 1 =1,Var(x)=Var(u)=1, andCov(x,u)=−.75.
Var(y)=1+1+2(−.75)=.5,1− Var(u)
Var(y) =−1.
Under consistent IV and finite moments, this ratio is the large-sample limit of
structuralR 2, rather than separate variance shares.
Back to variance intuition

### p.124
Binary-instrument IV
Compare outcome changes with schooling changes
ˆβ1 = ¯y1 − ¯y0
¯x1 − ¯x0
• This identity applies to a single binary instrument and an intercept, with
no other controls.
• A hypothetical outcome gap of 0.08 and schooling gap of 1 gives 0.08 log
points per year.
• Interpretation as a structural effect still requires the maintained
instrument assumptions.
Back to the Wald estimate

### p.125
Why the first-stage slope measures relevance
Covariance with the instrument isolates its slope
Population first stage
x=π 0 +π 1z+v, withCov(z,v)=0 by linear projection.
Cov(z,x)=Cov(z, π 0 +π 1z+v)=π 1 Var(z).
π1 = Cov(z,x)
Var(z) , π 1 ,0⇐ ⇒Cov(z,x),0.
RequiresVar(z)>0 (implied by relevance: a constantzhas zero covariance
withx). For MROZ,z=fatheduc,x=educ.
Back to MROZ first-stage evidence

### p.126
Two responses to the instrument
The outcome reduced form is the response of wages to the instrument
Same structural equation
Compare schooling across instrument groups:∆ educ.
Compare log wages across the same groups:∆ log(wage).
Under the IV assumptions, their ratio gives log-wage units per schooling
year.
Back to birth-quarter results Paper sample calculation

### p.127
Birth quarter: scale two differences
The Wald estimate uses a small first-stage schooling difference
ˆβIV = ∆log(wage)/∆educ. Men born 1930–1939.
Published Table III, Panel B Estimate
Q1-minus-other log-wage difference−.01110
Q1-minus-other schooling difference−.1088
ˆβIV = −.01110
−.1088 ≈.1020
Angrist and Krueger (1991), Table III, Panel B.
Binary-instrument covariance identity
Back to the two responses

### p.128
The probability limit of OLS
Correlation with the structural error changes the limit
ˆβ1,OLS =
dCov(x,y)
dVar(x)
OLS relatesytox. The error covariance is thereforeCov(x,u).
Derivation of 15.20 Back to OLS and IV comparison

### p.129
The probability limit of IV
Instrument-error correlation is divided by instrument relevance
IV scalesCov(z,u)by instrument relevance,Cov(z,x).
Derivation of 15.19 Back to OLS and IV comparison

### p.130
Reduced form: substitute the first stage
The excluded instrument enters through the endogenous regressor
y1 =β 0 +β 1y2 +
Xk−1
j=1
βj+1zj +u 1,
y2 =π 0 +
πjzj +π kzk +v 2.
y1 =β 0 +β 1

π0 +
πjzj +π kzk +v 2

+
βj+1zj +u 1.
Collect the coefficients Back to the outcome reduced form

### p.131
Reduced form: collect the coefficients
Only the excluded instrument has no separate structural effect
y1 =γ 0 +
k−1X
γjzj +γ kzk +e 1.
γ0 =β 0 +β 1π0,
γj =β j+1 +β 1πj (j=1, . . . ,k−1),
γk =β 1πk,e 1 =u 1 +β 1v2.
For the excluded instrument,γ k/πk =β 1 whenπ k ,0.
Back to the outcome reduced form

### p.132
Why exclusion matters for the ratio
A direct instrument effect adds a second term
y1 =β 0 +β 1y2 +δz k +controls+u 1.
With a direct structuralδz k effect, substitute the first stage:
γk =δ+β 1πk, γk
πk
=β 1 + δ
The ratio isolatesβ 1 only when exclusion removesδ.
Why exogeneity matters Back to the outcome reduced form

### p.133
Why exogeneity matters for the reduced form
The new error must remain orthogonal to the exogenous regressors
e1 =u 1 +β 1v2, from substituting the first stage.
Cov(zj,e 1)=Cov(z j,u 1)
|      {z      }
assumed 0
+β1 Cov(zj,v 2)
projection: 0
=0.
Structural-error orthogonality is assumed. First-stage residual orthogonality
follows from projection.
With rank, sampling and moment conditions, OLS consistently estimates the
outcome reduced form.

### p.134
Example 15.1: controls are instruments
Instrument education while retaining the experience effects
log(wage)=β 0 +β 1educ+β 2exper+β 3exper2 +u.
Outcome-equation variable Instrument role
1,exper,exper 2 Included: instrument themselves
educEndogenous variable to instrument
fatheducExcluded from the outcome equation
The excluded instrument must have no remaining direct wage effect and no
association withu, after the model’s controls.
Back to the wage model with controls

### p.135
Example 15.1 revisited: partial relevance
A raw correlation is not the required first-stage evidence
educ=π 0 +π 1exper+π 2exper2 +θfatheduc+r.
θ,0.
• This is thepopulation linear projection; its residual is orthogonal to its
regressors by construction.
• θ,0 is an additional relevance condition, not a consequence of projection.
• Test the father’s schooling coefficient in the first stage with the same experience

### p.136
When a proxy removes omitted-variable bias
The proxy must remove the ability variation related to schooling
Structural equation
y=log(wage)=β 0 +β 1educ+γq+v, withE(v|educ,q)=0.
1. RedundancyE(y|educ,q,p)=E(y|educ,q).
Once ability and schooling are held fixed, the proxy adds no wage effect.
2. Sufficient capture
L(q|1,educ,p)=L(q|1,p)=δ 0 +δ pp.
After the proxy predicts ability, schooling must not predict the ability left
over. Merely being correlated with ability is insufficient.
Proxy substitution Quiz 2: can we test proxy conditions? Back to proxy and IV

### p.137
Quiz 2: can we test proxy conditions?
Unobserved skill prevents a direct check using this dataset alone
output=β 0 +β 1AIuse+γskill+v. Experience is the proxy.
Does a significant experience coefficient establish the proxy conditions?
No. Unobserved true skill prevents us from directly checking its remaining
relationship with AI use after experience, or holding skill fixed to test
redundancy.
A significant proxy coefficient does not show that it captures the skill
differences between users and nonusers.
Evidence for a proxy or another design Back to proxy conditions

### p.138
Quiz 2: what evidence would help?
Validate how much skill the proxy captures, or change the design
output=β 0 +β 1AIuse+γskill+v.
• ReasoningExplain why remaining skill should no longer be related to AI
use after controlling for the proxy.
• External validationWhen available, use an independent skill measure to
assess the proxy argument.
• Different designA randomized rollout supplies another route to the
causal effect.

### p.139
Why IV can be consistent
The sample ratio approaches the population ratio
Cov(z,x) =β 1
• Random sampling and suitable finite moments give convergence of the
sample covariances.
• Exogeneity gives the right target; nonzero relevance keeps the population
denominator away from zero.
• Consistent does not mean unbiased in a finite sample.
Back to the two IV conditions Consistency proof