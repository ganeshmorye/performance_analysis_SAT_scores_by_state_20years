# A State-by-State Analysis of Performance in SAT from 2000 to 2019



## Contents:
  - [Problem Statement](#problem-statement)
  - [Background](#background)
  - [Data](#data)
  - [Data Dictionary](#data-dictionary)
  - [Outside Research](#outside-research)
  - [Observations](#observations)
  - [Conclusions and Recommendations](#conclusions-and-recommendations)
  - [References](#references)
  
## Problem Statement:

SAT has been a mainstay and a pivotal point in a student's academic career for over a century. Performance of a student in the SAT test is influenced by a number of factors such as state of residence, family background, academic performance in the school, amongst other things. All these factors combined with their SAT scores guide the student's decision of selecting a major and also their degree level goal. Here we take a look at the SAT scores over the last 20 years to identify any trends in the scores and the factors influencing the student's performance in this test.

## Background:

Over the years SAT has undergone lot of changes to better reflect the changing landscapes in the education era. After its inception in 1926, it has evolved to meet the educational standards of America's best colleges and universities. The current form of modern-day SAT which comprises of two main sections, Reading/Writing and Match traces back its origin to 1952. Since then it has never remained static and kept evolving. 1994 saw the first time where students were allowed to use calculators which continues to this day. 2005 brought a big change to the way how SAT was scored. A new scoring system of 2400 points was introduced in 2005. This change was brought about to better reflect the value of clear and effective writing. An essay was added as a separate section in addition to the Verbal and Math sections. In 2016, this essay section was made optional and reading and writing sections were combined and took the form of Evidence based Reading and Writing section.

***SAT changes over the years***

| SAT Changes Over Years      | 1994-2005 | 2006-2016     | 2017-Present     |
| :---        |    :----:   |          ---: |      ---: |
| Administration      | 1994-2005       | 2005-January 2016   |    March 2016-present |
| Score Range   | 400-1600        | 600-2400      |     400-1600 |
| Length of Test   | --        | 3 hours 45 minutes      |     3 hours (+50mins Optional Essay) |
| Sections   | Critical Reading<br>Math        | Critical Reading<br>Writing+Essay<br>Mathematics     |     Evidence based Reading + Writing<br>Math<br>Essay (Optional) |
                               

## Data:

There are 2 sets of analysis being carried out in this project<br>
1. [Set 1](downloaded_data/) One of the dataset conrresponds to data of SAT scores for each section and for all the states. These files follow the naming convention of sat_YEAR.xls. For eg sat_2000.xls correspond to SAT scores data for the year 2000. 
2. [Set 2](downloaded_data/) Other dataset correspond to data of SAT scores classified into distinct categories such as Family Income, GPA etc. These files follow the naming convention of sat_student_characteristics_YEAR.xls. 
3. Both dataset cover the period from 2000-2019 and downloaded in Excel format from National Center of Educational Statistics
4. These 2 datasets are individually processed in 2 python scripts:
    a. [Set 1 Data Cleaning Python Script](code/process_sat_scores.py)
    b. [Set 2 Data Cleaning Python Script](code/process_sat_charac.py)
5. [National Center for Educational Statistics](https://nces.ed.gov/programs/digest/)


## Data Dictionary

[Cleaned Up DataFrame Used in Analysis and Visualization](exported_data/)

| Feature                         | Type           | Dataset                           | Description                                                                        |
|---------------------------------|----------------|-----------------------------------|------------------------------------------------------------------------------------|
| State                           | object         | sat_2000_2019.xls                      | State for which the SAT scores are reported                                        |
| Year                            | datetime64 | sat_2000_2019.xls                 | Year for which the SAT scores are reported                                         |
| Reading                         | int64          | sat_2000_2019.xls                 | Reading section scores                                                             |
| Math                            | int64          | sat_2000_2019.xls                 | Math section scores                                                                |
| Writing                         | float64        | sat_2000_2019.xls                 | Writing section scores                                                             |
| Percent of Graduates taking SAT | float64        | sat_2000_2019.xls                 | Percent of Graduates taking SAT                                                    |
| Characteristics                 | object         | sat_characteristics_2000_2019.xls | Characteristics of the particular Category such as gpa, family income etc          |
| Category                        | object         | sat_characteristics_2000_2019.xls | Category under which the scores are reported                                       |
| Year                            | datetime64 | sat_characteristics_2000_2019.xls | Year for which the SAT scores are reported                                         |
| Reading                         | float64        | sat_characteristics_2000_2019.xls | Reading section scores                                                             |
| Math                            | float64        | sat_characteristics_2000_2019.xls | Math section scores                                                                |
| Writing                         | float64        | sat_characteristics_2000_2019.xls | Writing section scores                                                             |
| Percentage Distribution         | float64        | sat_characteristics_2000_2019.xls | Percent distribution of students beloging within a particular reporting   category |

## Outside Research:

The National Center for Education Statistics (NCES) is the primary federal entity for collecting and analyzing data related to education in the U.S. and other nations. NCES is located within the U.S. Department of Education and the Institute of Education Sciences. [NCES](https://nces.ed.gov/about/) fulfills a Congressional mandate to collect, collate, analyze, and report complete statistics on the condition of American education; conduct and publish reports; and review and report on education activities internationally.
Every year they publish digest tables providing a wide variety information. Data used in this study was downloaded from these annual digest tables specifically the tables related to Educational Achivement in the Elementary and Secondary Education chapter.

## Visualizations
[Participations Rates for All States Over the Years](imgs/TimeSeries_Plot_of_Percent_of_Graduates_Taking_SAT.png)<br>
[Percent of Graduates Taking SAT for Each State](imgs/Percent_of_Graduates_Taking_SAT_for_Each_State_(2000-2019).png)<br>
[Percent of Graduates Taking SAT and Mean Total Scores for Each State](imgs/Percent_of_Graduates_Taking_SAT_and_Mean_Total_Scores_for_Each_State_(2000-2019).png)<br>
[Trends in SAT Scores by High School Rank](imgs/Distribution_of_Total_SAT_Scores_by_High_School_Rank_Category.png)<br>
[Trends in SAT Scores by High School GPA](imgs/Distribution_of_Total_SAT_Scores_by_High_School_GPA.png)<br>
[Trends in SAT Scores by Familu Income](imgs/Distribution_of_Total_SAT_Scores_by_Family_Income.png)<br>
[Trends in SAT Scores by Parental Education](imgs/Distribution_of_Total_SAT_Scores_by_Highest_Level_of_Parental_Education.png)<br>
[Trends in SAT Scores by Degree Level Goal](imgs/Distribution_of_Total_SAT_Scores_by_Degree_Level_Goal.png)<br>
[Trends in SAT Scores by Intended College Major](imgs/Distribution_of_Total_SAT_Scores_by_Intended_College_Major.png)<br>


## Observations:

***Participation Rates***
* On the lower end, percentages have varied between 5-10% for 20 states with the Dakotas having the lowest rates
* D.C., Maine, Connecticut have participation rates over 80%
* Idaho started covering the fees of SAT tests from 2013-2014 which saw the states SAT participation rates jump from 20% to ~100% in 2014

***Participation Rates & SAT Scores***
* In general, states with lower participation rates tend to have higher scores and wider variability
* SAT scores should be adjusted for their corresponding participation rates for a real comparative analysis

***High School Performance & SAT Scores***
* Students performing better in school tend to have higher SAT scores
* Average SAT scores for the top performing students are around 1200 and at the lower end students score around 800

***Family Background & SAT Scores***
* Kids belonging to families with higher income and advanced degrees perform significantly better than those belonging to low-income and no high school diploma families

***Degree Level & SAT Scores***
* Students with higher SAT scores tend to aim for more advanced degrees in their careers

    
## Conclusions and Recommendations:

1. Certain states which have started covering the SAT test fees have a seen an increase in the student participation in the recent years
2. Students with a good academic performance also perform better in the SAT test. Although this should not come as a surprise, it does show that SAT does its job well as a standardized metric to evaluate student’s academic performance across wide ranges of schools, districts, states
3. Family’s background plays a huge role in the student’s performance in the SAT. If the colleges started to rely on a standardized metric as a sole admission’s criteria, it will end up severely disadvantaging the students coming from low-income families
4. Student’s academic choices and their acceptance into a particular major are greatly influenced by their SAT scores

## References
[WHAT IS THE SAT®?](https://www.kaptest.com/sat/what-is-the-sat) <br>
[Here's how the SAT has changed over the past 90 years and where it might be heading](https://www.insider.com/how-the-sat-has-changed-over-the-past-90-years-2019-8#the-us-army-a-eugenics-professor-and-thousands-of-universities-came-together-to-give-birth-to-the-worlds-biggest-standardized-exam-1)<br>
[Why Is the SAT Falling Out of Favor?](https://www.nytimes.com/2020/05/23/us/SAT-ACT-abolish-debate-california.html#:~:text=Critics%20of%20the%20tests%20cite,white%20and%20Asian%2DAmerican%20students.&text=Critics%20also%20say%20the%20tests,private%20coaching%20and%20test%20prep.)<br>
[How the SAT failed America](https://www.forbes.com/sites/susanadams/2020/09/30/the-forbes-investigation-how-the-sat-failed-america/?sh=51586cea53b5)<br>
[States That Provide A Free ACT/ SAT Test](https://www.collegeraptor.com/getting-in/articles/act-sat/states-act-sat-given-free/)<br>
