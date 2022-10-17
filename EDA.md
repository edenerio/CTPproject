<h1><B>Poverty as a Persona</B></h1>
<h2> <B>Leveraging Predictive Modeling to Forecast Average Salaries in the United States</B> </h2>

<h3>Team Name - <B>Datanauts</B> 
<h3>Team Members:</h3>
 
<ul>
<li>Edison Enerio - Project Lead</li>
<li>Videsh Narine - Engineering Lead </li>
<li>Philip Park - R & D Lead </li>
</ul>

<center> <B> <big> Exploratory Data Analysis </big> </B>  </center>

**Definition:** Poverty is the perpetual state of insufficiency with regards to basic needs and sustainment of a moderate "quality of life." 

**Overview:** The topic of poverty is an inherently complex and layered topic of discourse, and solutions have been proposed that run the full gamut of analytics and statistics. The reality is that poverty is a systemic problem that persists and varies widely from state to state. According to a Census.gov report,
"The official poverty rate in 2021 was 11.6 percent, with 37.9 mil­lion people in poverty."<a name="cite_ref-1"></a>[<sup>[1]</sup>](#cite_note-1)


These staggering numbers sheds light on the vast number of individuals and families affected by poverty in the United States.


**Objective:** Leveraging the robust data provided by the U.S. Census can provide clarity on key factors that affect the AGI (Adjusted Gross Income). Utilizing our data analytical skills requires familiarization with the underlying and overarching aspects that contribute to the poverty issue at large. This blending of domain expertise and statistical aptitude requires data cleaning. The process of data cleaning reduced the number of columns used in our project from 45 to 13. The renovated dataset can be found in our <a href="https://github.com/edenerio/CTPproject/tree/main/Data">GitHub repository</a>.

The original dataset can be found in the following link: <a href="https://www.census.gov/data/datasets/time-series/demo/supplemental-poverty-measure/acs-research-files.html">ACS Supplemental Poverty Measures (SPM) Research Files: 2009 to 2019</a>. 

**Data Cleaning Process:** 

The guiding principle in parsing through and ultimately deciding which data to keep for our analysis was what data points would significantly affect the Adjusted Gross Income and if patterns can be identified in order to create a composite which would ultimately derive income-level personas that we can further test against as the analysis evolves. Here are the columns that we decided upon:

1.	**Age**- is applicable because income varies based on age. In addition, certain ages come with other responsibilities such as having children. 
2.	**Sex**- On average there are disparities in income based on sex
3.	**Mar** (Marital Status)- Income is affected based on marital status as people file taxes jointly. With marriage can possibly come along children and other responsibilities which in turn affect poverty levels as well
4.	**Education**- Studies show that higher education yields a higher lifetime income 
5.	**Race**- Historically minorities in America have a lower income due to socioeconomic factors 
6.	**Hispanic**- Similar explanation to race
7.	**OffPoor** (Official Poverty Status)- The class we want to visualize on the heatmap and in our regression model
8.	**MOOP_OTHER** (Medical Out of Pocket)- Depending on your job’s coverage(if any) people might have to pay more for their medical and may not be low income enough to qualify for free insurance
9.	**AGI** (Adjusted Gross Income)- One of the main columns we want to focus on is the income of these people, we will use this in our regression model with predicted income 
10.	**SPM_NumKids** - With more kids in the household expenses are much higher 
11.	**SPM_wCohabit** - We can take a look below the surface level here and see if people are living together and how that affects their poverty level
12.	**SPM_Totval** - We want to see how this differs from the adjusted gross income and what this means 
13.	**SPM_CapWkCCXpns** - Total expenses for work and children, the more children the more expenses 


So this begs the question... **Can Poverty Be Whittled to a Persona?**




<figure>
<center>
<img src='https://thumbs.dreamstime.com/b/jigsaws-puzzle-human-head-7705203.jpg'/>
<figcaption>Image Caption</figcaption></center>
</figure>

-----------------------------------------------------------------------
<a name="cite_note-1"></a>1. [^](#cite_ref-1) *Creamer, John, et al."Poverty in the United States: 2021".*Census*, 13 Sep. 2022.https://www.census.gov/library/publications/2022/demo/p60-277.html*
