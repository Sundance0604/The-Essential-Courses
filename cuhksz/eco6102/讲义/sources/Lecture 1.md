# 原始材料文本提取：Lecture 1.pdf

## PDF 第 1 页

ECO6102 / 2026–27 Term 1 (Fall)
Welcome to ECO6102:
Advanced Econometrics
Enjie (Jack) Ma
Lecture 1 · Monday 7 September 2026

## PDF 第 2 页

Teaching Team
Instructor
• Instructor: Enjie (Jack) Ma马恩杰(maenjie@cuhk.edu.cn)
◦ Econ Ph.D. @Cornell, Stats+Econ B.S. @UCLA
◦ Assistant Professor, CUHK SZ SME
◦ Specialty: Economics of Climate Change, Innovation, and
Technology
◦ Lectures: Xili Campus 6E506, Monday 09:00–11:50
◦ Office Hours: Xili Campus 6A204, Monday
13:00–14:00(no OH today)
◦ More about me: I am from Shenzhen, love sports, coffee,
and cat (here’s my cat oreo)
ECO6102 / L1 2 / 66

## PDF 第 3 页

Teaching Team
Instructor
• Instructor: Enjie (Jack) Ma马恩杰(maenjie@cuhk.edu.cn)
◦ Econ Ph.D. @Cornell, Stats+Econ B.S. @UCLA
◦ Assistant Professor, CUHK SZ SME
◦ Specialty: Economics of Climate Change, Innovation, and
Technology
◦ Lectures: Xili Campus 6E506, Monday 09:00–11:50
◦ Office Hours: Xili Campus 6A204, Monday
13:00–14:00(no OH today)
◦ More about me: I am from Shenzhen, love sports, coffee,
and cat (here’s my cat oreo)
ECO6102 / L1 3 / 66

## PDF 第 4 页

Teaching Team
Instructor
• Instructor: Enjie (Jack) Ma马恩杰(maenjie@cuhk.edu.cn)
◦ Econ Ph.D. @Cornell, Stats+Econ B.S. @UCLA
◦ Assistant Professor, CUHK SZ SME
◦ Specialty: Economics of Climate Change, Innovation, and
Technology
◦ Lectures: Xili Campus 6E506, Monday 09:00–11:50
◦ Office Hours: Xili Campus 6A204, Monday
13:00–14:00(no OH today)
◦ More about me: I am from Shenzhen, love sports, coffee,
and cat (here’s my cat oreo)
ECO6102 / L1 4 / 66

## PDF 第 5 页

Teaching Team
Teaching assistant and tutorial
• Teaching Assistant
◦ Xupeng Ruan (ruanxupeng@cuhk.edu.cn)
◦ T utorials: Xili Campus 6E506, Monday 18:00–18:50
◦ Office Hours: Xili Campus 6B320, Friday 09:00–10:00
ECO6102 / L1 5 / 66

## PDF 第 6 页

Required Textbook
Wooldridge,Econometric Analysis of Cross Section and Panel Data, 2nd ed., MIT Press, 2010
Second Edition, 2010
ECO6102 / L1 6 / 66

## PDF 第 7 页

Other References
Stock and Watson,Introduction to Econometrics, 4th ed., Pearson, 2019
Recommended for reading
ECO6102 / L1 7 / 66

## PDF 第 8 页

Software Package
• Data analysis is essential for learning econometrics. Be prepared to write
code for analyzing real-world data.
• In this course, we will use a software package called Python. It is free and
open-source. Python will be mostly taught in tutorials by the TA. You
should use Python to finish your homework.
• Python has become popular among economists, so it is beneficial for you
to learn this software package.
ECO6102 / L1 8 / 66

## PDF 第 9 页

Course Components
• Lectures: Lectures’ content will center around econometric concepts based
on the main textbook. In addition to the lecture slides, you should read
the main textbook. (10-min break time around half way 10:20am)
• Tutorials: Tutorial sessions will be hosted by the TA. During these
sessions, the TA will teach Python, discuss problem sets, explain difficult
materials, and answer questions.
• Office Hours: You may stop by during my office hours with any questions
or by appointment. Emails are not preferred since it is hard to type
equations in emails.
ECO6102 / L1 9 / 66

## PDF 第 10 页

Course Website
• Course Website: bb.cuhk.edu.cn
• The site contains the syllabus, lecture slides, problem sets, occasional
announcements, and other materials.
• You should check it regularly as you are responsible for any information
posted there in addition to any announcements made in class.
• Throughout the semester, I will make announcements via the course
website.
ECO6102 / L1 10 / 66

## PDF 第 11 页

Grading Policy
• Participation (10%)
• Problem Sets (20%): Group study and free discussion are encouraged, but
you should submit your own answers. No late assignments will be
accepted.
• Midterm Exam (30%) and Final Exam (40%): There will be no make-up
exams. In case of illness or accident at the time of the midterm—with
proper documentation from a doctor or the police—the final will be
weighted 70%.
• Regrading Request: If you think a mistake was made in grading your
exam, you may ask for a regrade. See the syllabus for more information.
ECO6102 / L1 11 / 66

## PDF 第 12 页

Learning Goals
By the end of the course, you should:
• Be skilled in using econometric tools and capable of critically evaluating
quantitative analyses conducted by other researchers.
• Be able to select appropriate empirical methods to tackle practical
questions in economics and related fields, while understanding the
assumptions, limitations, and potential improvements of these methods.
• Be able to use the statistical software package Python for empirical
analysis and simulation studies.
ECO6102 / L1 12 / 66

## PDF 第 13 页

Course Outline
• Introduction (Chapter 1)
• Conditional Expectations (Chapter 2)
• Linear Regression (Chapter 4)
• Instrumental Variables (Chapter 5)
• Simultaneous Equation (Chapter 9)
• Panel Data (Chapters 10 & 11)
• Binary Response (Chapter 15)
ECO6102 / L1 13 / 66

## PDF 第 14 页

Any Questions?
ECO6102 / L1 14 / 66

## PDF 第 15 页

Lecture 1:
Introduction
ECO6102 / Lecture 1

## PDF 第 16 页

Roadmap
L1 L2 L3 L4 L5 Midterm L6 L7 L8 Final
Introduction — Wooldridge (2010), Chapter 1 (Week 1)
1 Causality and Endogeneity
2 Data Structures
3 Examples and Random Regressors
ECO6102 / L1 16 / 66

## PDF 第 17 页

SECTION 1
Causality and Endogeneity
ECO6102 / Lecture 1

## PDF 第 18 页

Causal Inference
The goal of most empirical studies in economics and other social sciences is to
determine whether a change in one variablewcauses a change in another variabley.
For example,
• Does having another year of education cause an increase in monthly salary?
• Does reducing class size cause an improvement in student performance?
• Does lowering the business property tax rate cause an increase in the city’s
economic activity?
• Does access to AI coding tools raise a programmer’s pay?
• Other examples?
ECO6102 / L1 Causality and Endogeneity 18 / 66

## PDF 第 19 页

Correlation versus Causality
Correlation and causal relationships
• Because economic variables are properly interpreted as random variables,
we should use ideas from probability to formalize the sense in which a
change inwcauses a change iny.
• We learned from probability how to determine whether two random
variables are correlated (How?).
ECO6102 / L1 Causality and Endogeneity 19 / 66

## PDF 第 20 页

Correlation versus Causality
Detecting correlation
9 12 16 20
0
5
10
15
20
years of education
monthly wage (thousand yuan)
illustrative data,n=40
ρwy = Cov(w,y)
σw σy
∈[−1,1]
• Herewis education andyis
monthly wage.
• Sample analogue: ˆρfrom the
npairs(w i,y i).
• ρmeasures co-movement; it is
silent about which causes
which.
ECO6102 / L1 Causality and Endogeneity 20 / 66

## PDF 第 21 页

Correlation versus Causality
Detecting correlation
9 12 16 20
0
5
10
15
20
years of education
monthly wage (thousand yuan)
illustrative data,n=40
ρwy = Cov(w,y)
σw σy
∈[−1,1]
• Herewis education andyis
monthly wage.
• Sample analogue: ˆρfrom the
npairs(w i,y i).
• ρmeasures co-movement; it is
silent about which causes
which.
ECO6102 / L1 Causality and Endogeneity 21 / 66

## PDF 第 22 页

Correlation versus Causality
Education and earnings
• But correlation,causality!
• For example, individuals with higher
levels of education tend to earn more
(correlation).
• However, those with more education
are also likely to have higher abilities.
• We do not know whether the increase in
salary is caused by education or ability.
education wage?
ability
ECO6102 / L1 Causality and Endogeneity 22 / 66

## PDF 第 23 页

Correlation versus Causality
Education and earnings
• But correlation,causality!
• For example, individuals with higher
levels of education tend to earn more
(correlation).
• However, those with more education
are also likely to have higher abilities.
• We do not know whether the increase in
salary is caused by education or ability.
education wage?
ability
ECO6102 / L1 Causality and Endogeneity 23 / 66

## PDF 第 24 页

Ceteris Paribus Analysis
Holding other factors fixed
• The notion ofceteris paribus—that is, holding all other factors fixed—is at the
crux of establishing a causal relationship.
• Simply finding that two variables are correlated is rarely enough to conclude that
a change in one variable causes a change in another.
• This result is due to the nature of economic data: rarely can we run a controlled
experiment that allows a simple correlation analysis to uncover causality.
• Instead, we can use econometric methods to effectively hold other factors fixed –
core of this class, using econometric model to establish causality.
The core of this course: using econometric models to establish causality.
ECO6102 / L1 Causality and Endogeneity 24 / 66

## PDF 第 25 页

Ceteris Paribus Analysis
Holding other factors fixed
• The notion ofceteris paribus—that is, holding all other factors fixed—is at the
crux of establishing a causal relationship.
• Simply finding that two variables are correlated is rarely enough to conclude that
a change in one variable causes a change in another.
• This result is due to the nature of economic data: rarely can we run a controlled
experiment that allows a simple correlation analysis to uncover causality.
• Instead, we can use econometric methods to effectively hold other factors fixed –
core of this class, using econometric model to establish causality.
The core of this course: using econometric models to establish causality.
ECO6102 / L1 Causality and Endogeneity 25 / 66

## PDF 第 26 页

Ceteris Paribus Analysis
The average response
• Since economic variables are random, we cannot predict the response of
each individual; instead, we focus on the average response.
• A ceteris paribus analysis entails estimatingE (︁y|w,c )︁, the expected value
ofyconditional onwandc.
• The vectorcdenotes a set of control variables that we would like to
explicitly hold fixed when studying the effect ofwon the expected value
ofy.
• The reason we control for these variables is that we thinkwis correlated
with other factors that also influencey.
ECO6102 / L1 Causality and Endogeneity 26 / 66

## PDF 第 27 页

Partial Effect
• Ifwis continuous, interest centers on∂E (︁y|w,c )︁/∂w, which is usually
called the partial effect ofwonE (︁y|w,c )︁.
• Ifwis discrete, we are interested inE (︁y|w,c )︁evaluated at different values
ofw, with the elements ofcfixed at the same specified values.
E(wage|educ+1,c)−E(wage|educ,c)
• One extra year of schooling; the same controls in both terms.
ECO6102 / L1 Causality and Endogeneity 27 / 66

## PDF 第 28 页

Controls
What are ”good controls”c?
• Deciding on the list of proper controls is not always straightforward, and using
different controls can lead to different conclusions about a causal relationship
betweenyandw.
• This is where establishing causality gets tricky: it is up to us to decide which
factors need to be held fixed.
• If we settle on a list of controls, and if all elements ofccan be observed, then
estimating the partial effect ofwonE (︁y|w,c )︁is relatively straightforward.
ECO6102 / L1 Causality and Endogeneity 28 / 66

## PDF 第 29 页

Controls
Can you observe them?
• Unfortunately, in economics and other social sciences, many elements ofc
are not observed.
• For example, in estimating the causal effect of education on wage, we
might focus onE (︁wage|educ,exper,abil )︁, whereeducis years of schooling,
experis years of workforce experience, andabilis innate ability.
• In this case,c= (︁exper,abil )︁, whereexperis observed butabilis not.
ECO6102 / L1 Causality and Endogeneity 29 / 66

## PDF 第 30 页

Controls
Can you observe them? (continued)
education wage
ability experience
c: what we hold fixed
?
• Dashed box = not observed; dashed arrows = paths that run through it.
ECO6102 / L1 Causality and Endogeneity 30 / 66

## PDF 第 31 页

Controls
Attendance and exam performance
• As a second example, consider establishing a causal relationship between
student attendance and performance on a final exam in a principles of
economicsclass.
• We might be interested inE (︁score|attend,SAT,priGP A)︁, wherescoreis the
final exam score,attendis the attendance rate,SATis the score on the
Scholastic Aptitude Test, andpriGP Ais the grade point average at the
beginning of the term.
• We can reasonably collect data on all of these variables for a large group
of students.
ECO6102 / L1 Causality and Endogeneity 31 / 66

## PDF 第 32 页

Controls
Remaining unobserved factors
• Is this setup enough to decide whether attendance has a causal effect on
performance?
Maybe not.
• WhileSATandpriGP Aare general measures reflecting student ability and
study habits, they do not necessarily measure one’s interest in or aptitude
for economics.
• Such attributes, which are difficult to quantify, may nevertheless belong in
the list of controls if we are going to be able to infer that the attendance
rate has a causal effect on performance.
ECO6102 / L1 Causality and Endogeneity 32 / 66

## PDF 第 33 页

Controls
Remaining unobserved factors
• Is this setup enough to decide whether attendance has a causal effect on
performance? Maybe not.
• WhileSATandpriGP Aare general measures reflecting student ability and
study habits, they do not necessarily measure one’s interest in or aptitude
for economics.
• Such attributes, which are difficult to quantify, may nevertheless belong in
the list of controls if we are going to be able to infer that the attendance
rate has a causal effect on performance.
ECO6102 / L1 Causality and Endogeneity 33 / 66

## PDF 第 34 页

Controls
Remaining unobserved factors (continued)
attendance exam score
?
SAT prior GPA
cobserved
interest, aptitude
• Observed controls can be held fixed; interest and aptitude cannot.
ECO6102 / L1 Causality and Endogeneity 34 / 66

## PDF 第 35 页

Controls
What makes setting good control hard?
• You choose c: no formula gives the list; it takes institutional knowledge of
the question.
• Not everything belongs: choose controls for the causal question; adding
variables is not automatically better.
• Part of c is unobservable: ability, interest, management quality — the
dashed boxes.
• The data may not exist, and differentcgive different answers — always
report which controls you used.
ECO6102 / L1 Causality and Endogeneity 35 / 66

## PDF 第 36 页

What Else Can Go Wrong?
Measurement error and simultaneity
• In addition to not being able to obtain data on all desired controls
(omitted variables), other problems can interfere with estimating causal
relationships.
• For example, even if we have good measures of the elements ofc, we
might not have very good measures ofyorw(measurement error).
• A more subtle problem is that we may only observe equilibrium values of
yandwwhen these variables are simultaneously determined (reverse
causality).
◦ An example is determining the causal effect of conviction rates (w) on
city crime rates (︁y)︁.
ECO6102 / L1 Causality and Endogeneity 36 / 66

## PDF 第 37 页

Obstacles to Establishing causality
Section summary
• Confounders: correlation is not causality.
• Controls: you choosec, and part of it is unobserved (omitted variables).
• Measurement error: classical error inyadds noise; error inwcan bias the
estimated effect.
• Simultaneity: we observe only equilibrium values.
• These problems can makeurelated to the regressors: endogeneity.
Whether this happens depends on the model.
ECO6102 / L1 Causality and Endogeneity 37 / 66

## PDF 第 38 页

SECTION 2
Data Structures
ECO6102 / Lecture 1

## PDF 第 39 页

Data Structures
• For much of this course, we adopt a random sampling assumption.
• More precisely, we assume that
1 A population model has been specified and
2 An independent, identically distributed (i.i.d.) sample can be drawn
from the population.
• Specifying a population model—which may be a model of
E (︁y|w,c )︁—requires us first to clearly define thepopulation of interest.
ECO6102 / L1 Data Structures 39 / 66

## PDF 第 40 页

Cross Section Data
• Because we will rely heavily on
random sampling, it is important to
know what it allows and what it rules
out.
• Random sampling is often reasonable
for cross section data, where, at a given
point in time, units are selected at
random from the population.
• In this setup, any explanatory variables
are treated as random outcomes, along
with data on response variables.
population at timet
random draw
(yi,x i),i=1, . . . ,6
ECO6102 / L1 Data Structures 40 / 66

## PDF 第 41 页

Cross Section Data
• Because we will rely heavily on
random sampling, it is important to
know what it allows and what it rules
out.
• Random sampling is often reasonable
for cross section data, where, at a given
point in time, units are selected at
random from the population.
• In this setup, any explanatory variables
are treated as random outcomes, along
with data on response variables.
population at timet
random draw
(yi,x i),i=1, . . . ,6
ECO6102 / L1 Data Structures 41 / 66

## PDF 第 42 页

Pooled Cross Section Data
• Random sampling does exclude cases of some interest for cross section
analysis.
• For example, the identical distribution assumption is unlikely to hold for
a pooled cross section, where random samples are obtained from the
population at different points in time.
• Example: a random sample of workers in 2019 and another in 2020,
stacked. Each year is a fine random sample, but a 2020 worker is not
drawn from the same population as a 2010 worker.
• This case is covered by independent, not identically distributed (i.n.i.d.)
observations.
ECO6102 / L1 Data Structures 42 / 66

## PDF 第 43 页

Spatial Data
• A situation that does require special consideration occurs when cross
section observations are not independent of one another.
• An example is spatial correlation models. This situation arises when
dealing with large geographical units that cannot be assumed to be
independent draws from a large population, such as the 50 states in the
United States.
• It is reasonable to expect that the unemployment rate in one state is
correlated with the unemployment rate in neighboring states.
• Spatially correlated shocks are everywhere inenvironmental economics: a
heat wave, a flood or a smog episode hits neighbouring firms and cities
together.
ECO6102 / L1 Data Structures 43 / 66

## PDF 第 44 页

Spatial Data
Neighbours share shocks
SZ
DGGZ
far city
temperature anomaly, one week
• A heat wave ignores city borders:
Shenzhen, Dongguan and Guangzhou are
hot in the same week.
• Firms next door share the shock. If it is not
in the model it sits inu, so their errors are
correlated: the estimate may be fine, the
standard errors are not.
ECO6102 / L1 Data Structures 44 / 66

## PDF 第 45 页

Cluster Data
• Cluster sampling also induces correlation in a cross section data set, but in
most cases, it is relatively easy to deal with econometrically.
• For example, retirement savings of employees within a firm may be
correlated because of common characteristics of workers within a firm or
because of features of the firm itself (e.g., retirement plan).
• Each firm represents a group or cluster, and we may sample several
workers from a large number of firms.
• Provided the number of clusters is large relative to the cluster sizes,
standard methods can correct for the presence of within-cluster
correlation.
ECO6102 / L1 Data Structures 45 / 66

## PDF 第 46 页

Cluster Data
Groups share shocks
Cohort A
Xili
Cohort B
Longgang
Another
programme
one shared shock
ECO6102 / L1 Data Structures 46 / 66

## PDF 第 47 页

Panel Data
• For panel data (or longitudinal data), which consists of repeated
observations on the same unit (e.g., individuals, households, firms, cities)
over time, the random sampling assumption initially appears much too
restrictive.
• However, the random sampling assumption, properly stated, does allow
for temporal correlation.
• What we will do is to assume random sampling in the cross section
dimension. The dependence in the time series dimension can be entirely
unrestricted.
• This approach is justified in panel data applications with many cross
section observations spanning a relatively short time period.
ECO6102 / L1 Data Structures 47 / 66

## PDF 第 48 页

Cross Section versus Panel
One grid
t=1 t=2 t=3 t=1 t=2 t=3 t=1 t=2 t=3
i=1
i=2
i=3
i=4
i=5
cross section pooled cross sections panel
dependence overt
• iruns down the rows (units),tacross the columns (time); a panel keeps the same
rows in every period: random across rows, anything goes along a row.
ECO6102 / L1 Data Structures 48 / 66

## PDF 第 49 页

Why Data Structure Matters
• Structure tells you who may share shocks: separate units (cross section),
the same unit over time (panel), neighbours (spatial), members of a group
(cluster).
• Shared shocks change inference: we must justify independence across
sampled units or account for their dependence. A cross section is not
automatically i.i.d.
• It does not remove confounding: the controls problem of Section 1 is still
there. Structure is the second question, not a substitute for the first.
ECO6102 / L1 Data Structures 49 / 66

## PDF 第 50 页

SECTION 3
Examples and Random Regressors
ECO6102 / Lecture 1

## PDF 第 51 页

Some Examples
Example 1.1: Wage Offer Function
• Earlier we used wage in money units. This model useslog(wage o): the
natural log of the wage offer.
log(wageo)=β 0 +β 1educ+β 2exper+β 3married+u
• educ: years of schooling;exper: years of work experience;married: a binary
indicator. The superscriptomeans offer.
• The error termucontains unobserved wage determinants; theβ j are the
unknown parameters.
ECO6102 / L1 Examples and Random Regressors 51 / 66

## PDF 第 52 页

Some Examples
Example 1.1: Wage Offer Function
log(wageo)=β 0 +β 1educ+β 2exper+β 3married+u
• Population: working women. We observe wages for the women in this
population.
• Population: all women over age 18. A random sample also includes
women who are not working; their wage offers are unobserved.
• Randomly sampling people does not ensure that the outcome is observed
for everyone.
ECO6102 / L1 Examples and Random Regressors 52 / 66

## PDF 第 53 页

Some Examples
Example 1.1: Wage Offer Function
log(wageo)=β 0 +β 1educ+β 2exper+β 3married+u
• Writex=(educ,exper,married). The key assumptions concernugivenxin
the population.
1. Conditional mean
E(u|x)=0?
Do observed characteristics predict
unobserved wage determinants on
average?
2. Conditional variance
Var(u|x)=σ 2 ?
Is the spread of unobserved wage
determinants the same across
groups?
ECO6102 / L1 Examples and Random Regressors 53 / 66

## PDF 第 54 页

Some Examples
Example 1.1: Wage Offer Function
• For cross section data, it is useful to write the model as a generic draw
from the population
log
(︂
wageo
i
)︂
=β 0 +β 1educi +β 2experi +β 3marriedi +u i
whereiindexes individuals.
• Throughout the course, theisubscript is reserved for indexing cross
section units (e.g., individuals, firms, cities).
• Thetsubscript is reserved for time (next example);j,g,hindex variables,
parameters and equations.
ECO6102 / L1 Examples and Random Regressors 54 / 66

## PDF 第 55 页

Some Examples
Example 1.2: Effect of Spillovers on Firm Output
• Suppose that the population is all manufacturing firms in a country
operating during a given three-year period.
• A production function describing output in the population of firms is
log (︁outputt
)︁ =δ t +β 1 log (labort) +β 2 log (︁capitalt
)︁
+β3spillovert +quality+u t,t=1,2,3.
• Here,spillover t is a measure of foreign firm concentration in the region
containing the firm.
ECO6102 / L1 Examples and Random Regressors 55 / 66

## PDF 第 56 页

Some Examples
Example 1.2: Effect of Spillovers on Firm Output
log (︁outputt
)︁ =δ t +β 1 log (labort) +β 2 log (︁capitalt
)︁
+β3spillovert +quality+u t,t=1,2,3.
• The termqualitycontains unobserved factors (e.g., unobserved
managerial, worker quality), which affect productivity and are constant
over time.
• The erroru t represents unobserved shocks in each time period.
ECO6102 / L1 Examples and Random Regressors 56 / 66

## PDF 第 57 页

Some Examples
Example 1.2: Effect of Spillovers on Firm Output
log (︁outputt
)︁ =δ t +β 1 log (labort) +β 2 log (︁capitalt
)︁
+β3spillovert +quality+u t,t=1,2,3.
• When we study panel data methods, there are several issues in deciding
how best to estimate theβ j.
• An important one is whether the unobserved productivity factorsquality
are correlated with the observable inputslabor t andcapital t.
• Also, can we assume thatspillover t at, say,t=3 is uncorrelated with the
error terms in all time periods?
ECO6102 / L1 Examples and Random Regressors 57 / 66

## PDF 第 58 页

Some Examples
Example 1.2: Effect of Spillovers on Firm Output
• For panel data, it is especially useful to add anisubscript indicating a
generic cross section observation:
log (︁outputit
)︁ =δ t +β 1 log (laborit) +β 2 log (︁capitalit
)︁
+β3spilloverit +quality i +u it,t=1,2,3.
• qualityi is a firm-specific term that is constant over time and also has the
same effect in each time period, whileu it changes across time and firm.
• The assumptions describe a generic firmidrawn from the population.
Bonus: what couldδ t capture for a firm?
ECO6102 / L1 Examples and Random Regressors 58 / 66

## PDF 第 59 页

Some Examples
Example 1.2: Effect of Spillovers on Firm Output
• For panel data, it is especially useful to add anisubscript indicating a
generic cross section observation:
log (︁outputit
)︁ =δ t +β 1 log (laborit) +β 2 log (︁capitalit
)︁
+β3spilloverit +quality i +u it,t=1,2,3.
• qualityi is a firm-specific term that is constant over time and also has the
same effect in each time period, whileu it changes across time and firm.
• The assumptions describe a generic firmidrawn from the population.
Bonus: what couldδ t capture for a firm?
ECO6102 / L1 Examples and Random Regressors 59 / 66

## PDF 第 60 页

Fixed Regressors?
• In the above examples, the error in an equation can be correlated with one
or more of the explanatory variables.
• This possibility is common in social science applications.
• The assumption of fixed regressors rules out such correlation a priori.
ECO6102 / L1 Examples and Random Regressors 60 / 66

## PDF 第 61 页

Shortcoming of Fixed Regressors
The fixed-regressor assumption
• To illustrate the shortcomings of the fixed regressor assumption, consider
a linear model for cross section data:
yi =β 0 +x iβ+u i,i=1,2, . . . ,N.
• In the wage example:y i =log(wage o
i )andx i =(educ i,exper i,married i). In
general,x i is 1×KandβisK×1.
• The “ideal” assumptions for this model are commonly stated as “The
errors {ui,i=1,2, . . . ,N } are i.i.d. withE(u i)=0 andE(u 2
i )=σ 2.”
• This statement omits the most important consideration: What is assumed
about the relationship betweenu i andx i?
ECO6102 / L1 Examples and Random Regressors 61 / 66

## PDF 第 62 页

Shortcoming of Fixed Regressors
Implications for the error term
yi =β 0 +x iβ+u i
• If thex i are taken as nonrandom (i.e. constant), thenu i andx i are
independent of one another.
• In nonexperimental environments, this assumption rules out too many
situations of interest.
• Some important questions, such as efficiency comparisons across models
with different explanatory variables, cannot even be asked in the context
of fixed regressors.
• Randomx i forces the real questions:E (u|x ) =0? Var (u|x ) constant?
• Thus we assume random regressors throughout the course.
ECO6102 / L1 Examples and Random Regressors 62 / 66

## PDF 第 63 页

Wrap-up
ECO6102 / Lecture 1

## PDF 第 64 页

Key Takeaways
Ceteris paribus: holding all other factors fixed; correlation,causality
Partial effects and control variables, observed and unobserved
Endogeneity:urelated to the regressors — omitted variables,
mismeasured regressors, simultaneity
Data structures: cross section, pooled cross section, spatial, cluster, panel
Random regressors, not fixed, throughout the course
ECO6102 / L1 Wrap-up 64 / 66

## PDF 第 65 页

Next Lecture
Today: Introduction
Wooldridge (2010), Chapter 1
Next: Conditional Expectations
Wooldridge (2010), Chapter 2 (Week 2)
Adapted from slides by Shuyang Sheng and Qihui Chen
ECO6102 / L1 Wrap-up 65 / 66

## PDF 第 66 页

Attendance and Background survey
https://v.wjx.cn/vm/h0uQynL.aspx#
ECO6102 / L1 Wrap-up 66 / 66
