![Alt Text](https://github.com/Sashafirce/global-ai-job-markets-and-salary-trends-2025/blob/23eab21a245918b7367c9d0508d73fbbe8c4ad58/Global%20AI%20Jobe%20Markets%20%26%20Salary%20Trend%202025.png)

## Global Ai Job Markets and Salary Trend 2025
### INTRODUCTION 
The "Global AI Job Markets and Salary Trend 2025" project analyses global tendencies in employment opportunities in AI. It is focused on the variation of salaries based on job role, location, benefit package, level of experience, and work-from-home availability. The objective is to convey actionable insights through data display and text that help job applicants, recruiters, and policy makers make informed decisions regarding employment within the evolving AI workforce.

Built on a design thinking methodology, this project combines empathy-driven research, quantitative analysis, and interactive visualisation. The output includes a confirmed set of hypotheses, a user-oriented dashboard in Tableau, empathy maps for some of the personas, and a strategy blueprint for further application development.

#### Team Roles and Responsibilities

**Project Manager**
Overseer of the project timeline, scope, and delivery. Led collaborative planning sessions and ensured alignment of data work, and design thinking goals. Maintained stakeholders in sight and facilitated handoff, documentation, and final presentation.

**Design Thinker**
Led Empathise and Define phases of the design thinking process. Created user personas (job seeker and recruiter) and empathy maps to understand their needs and pain points. Led the creation of "How Might We" statements and rephrased data questions in a human-centric way to ensure all deliverables addressed actual-world user issues.

**Data Architect**
Prepared and cleaned data for analysis. Built the data schema, handled missing values, field transformation, and data quality validation, and created a summary of the statistics. Set up the environment and developed well-organised datasets for downstream purposes, including analysis and dashboarding.

**Data Analyst**
Analysed salary, job type, benefits, and experience data. Hypothesis tested on remote work, pay, and level of experience. Built exploratory charts and extracted important insights to influence visual storytelling and stakeholder recommendations.

**Data Visualiser**
Created and refined the Tableau dashboard. Created simple-to-use visuals to explore trends by role, region, and experience. Worked with the Design Thinker and Analyst to present findings effectively using graphs, filters, and layout options created for different types of users.


### Dataset Content
The data is sourced from Kaggle public domain and contains different attributes of salary information, job requirements, company insights, and geographic trends. https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025/ddata

### Business Requirement
**Project Objectives**
- Uncover salary trends in AI jobs globally
- Compare pay for remote work vs. in-office work
- Examine the influence of benefits and amount of experience on salary
- Provide filtered, user-centered visualizations to guide decision-making
- Create a prototype dashboard or application that is advantageous for job seekers and workforce planners
  
**Target Stakeholders**
- **Job Seekers**: Explore actual salary ranges by occupation, location, and level of experience
- **Recruiters**: Compare salary proposals and gain insights on market trends in order to recruit the best talent

**Functional Requirements**
- Clean and process raw AI job data sets
- Examine wage trends using grouped statistical analysis
- Create interactive visualisations and dashboards (Tableau + Streamlit)
- Use design thinking to guide hypotheses and user experience
- Create a scalable app interface for public or stakeholder consumption
  
**Non-Functional Requirements**
- Must be understandable to non-technical users (good labelling and narration)
- Must be ethically sound (no deceiving or biased assertions)
-Have to be flexible and extendable enough for future time-based or regional revisions

### Hypothesis and how to validate?

** Hypothesis 1: Higher benefits scores correlate with higher salaries (USD equivalent)**
![hypothesis1testing](data/inputs/images/hypothesis_1_testing.jpg)

**Rationale**: Companies offering better benefits may also tend to provide more competitive salaries to attract top AI talent.
**Validation Method**: Boxplot: Compare salary distributions across benefits categories
**Hypothesis Testing Results**: Correlation between Benefits Score and Salary: 0.0010
Interpretation: Weak positive correlation
* Do not support Hypothesis 1
  
**Implication** 
* Companies with excellent benefits (>8.5) do NOT necessarily offer higher salaries
* Benefits and salary appear to be independent compensation components
* High-benefit companies may use benefits as a substitute rather than a complement to high salaries
  
### Hypothesis 2: Remote roles tend to offer higher salaries compared to fully in-office roles[]
![hypothesis2testing](data/inputs/images/hypothesis_2_testing.png)

**Rationale**: Remote work may be used as an incentive or may reflect more specialised roles that command higher pay.
**Validation Method**: Matplotlib Boxplot: Compare salary distributions across remote work arrangements

**Hypothesis Testing Results**: 
* Fully Remote ($116,161) > On-site ($114,140) - Salary premium confirmed
* Statistical Significance: The difference is measurable and consistent
* Modest salary premium: +1.8% difference between remote and on-site
* Supported Hypothesis 2
  
**Implication**
* Remote Premium Exists: Companies do pay slightly more for remote flexibility
* Competitive Advantage: Remote work can be a modest salary differentiator
* Talent Strategy: Remote roles may attract candidates seeking both flexibility AND competitive pay
  
### Hypothesis 3: Experience level significantly affects salary, especially at the executive (EX) level.
![hypothesis3testing ](data/inputs/images/hypothesis_3_testing.png)

### Rationale: Experience level has a direct impact on salary
**Validation Method**: ANOVA Testing Matplotlib Bar Chart: Compare salary distributions across remote work arrangements

**Hypothesis Testing Results**:  
* Entry-level ($63,133) → Mid-level ($87,955) → Senior ($122,188) → Executive ($187,724)
* Executive level highest: Executive positions offer the highest average salaries at $187,724
* Significant salary gaps: $124,590 salary range between entry and executive levels
* Statistical significance: ANOVA p-value ≈ 0.000000 (highly significant)
* Supported Hypothesis 3

### Project Plan

**1. Project Framing & Design Thinking Setup**

Empathise: Mapped out two main user personas with empathy maps to record needs, frustrations, and goals.

    Define: Used persona pain points to set up "How Might We" questions that led to hypothesis creation.

 Ideate: Brainstormed initial features, filters, and dashboard visuals to fix user problems.

Output: User-driven research agenda on salary trends, benefits, remote work effects, and experience level.

**2. Data Gathering & Preparation**

 Data Sources: Comprised two data sets of AI job postings from around the globe; variables were job title, company, salary, benefits, location, employment type, remote status, and experience level.

 Data Storage: Files are version-controlled and stored for team access in VS-Code and Git Hub.

 Data Cleaning: ETL pipeline handled by the Data Architect through Python for preprocessing.

**3. Exploratory Data Analysis (EDA)**

Investigated distributions and associations between key variables:
        
Built early visualisations to validate trends and guide hypotheses.

Exploration guided by the hypotheses built using design thinking.

**4. Hypothesis Testing & Analysis**

    Three data-driven hypotheses were tested using grouped statistics, visual comparisons, and correlation analysis:

       
**5. Data Visualisation & Interpretation**

    Designed a Tableau dashboard with interactive filters:
Visuals were aligned to the initial user needs to maintain relevance and clarity.

** 6. Presentation & Final Delivery**

    The following deliverables were provided: Empathy maps, project summary, hypotheses, findings, Tableau dashboard, and final PPT presentation. 

### ETL Steps
**Data Extraction & Combination**
- Loaded two raw datasets:
`ai_job_dataset.csv` (19 columns)
`ai_job_dataset1.csv` (20 columns, includes salary_local)
- Aligned missing columns (added salary_local to the first dataset).
- Merged datasets into one unified file: `ai_jobs_combined.csv`.
**Handling Missing Values**
  
- Filled missing `salary_local` values with "Not Provided".
- Checked critical columns (`job_id`, `job_title`, `salary_usd`):
- Dropped rows where these were missing.
  
**Data Cleaning & Quality Checks**
- Standardise column names to `snake_case`.
- Cleaned text fields (e.g., job titles, company names) — stripped spaces, applied Title Case.
- Converted date fields (`posting_date`, `application_deadline`) to datetime.
- Ensured salary_usd is numeric (missing values replaced with median).
- Removed duplicate rows based on `job_id`.
- Removed unrealistic salary outliers (below $1,000 or above $1,000,000).
  
**Data Transformation & Feature Engineering**
- New Features Created:
`salary_category `→ Low (< $50k), Mid ($50k–$100k), High (>$100k)
`remote_status` → On-site, Hybrid, Fully Remote
`posting_year` & `posting_month` extracted from posting_date
- Mapped categorical fields (`experience_level`, `employment_type`, `company_size`) to descriptive names.
- Reordered columns for readability.
- Saved the final cleaned dataset as ai_jobs_final.csv in the cleaned directory.
**Final Output**
- Clean, structured dataset: ai_jobs_final.csv
Ready for:
 Data Analysis & Dashboards (Power BI, Tableau, etc.)
 Statistical insights & trend reporting
 
### EDA Steps
This notebook explores the **cleaned dataset** (`ai_jobs_final.csv`) created during the ETL phase. 
Using Matplotlib, Seaborn, and Plotly, we generate visualisations to uncover patterns, relationships, and trends in the AI job market.
- Goal of This Notebook
 Understand how salaries vary by experience, industry, and work setup 
 Identify job posting trends over time
 Explore top AI job titles and hiring company characteristics
- Data Source
 Input file: `../data/inputs/cleaned/ai_jobs_final.csv` 
- This file is the output of our ETL process (01_etl_ai_jobs.ipynb).  
Tools Used
Pandas & NumPy – Data wrangling and summaries 
Matplotlib & Seaborn – Static, high-resolution plots 
Plotly – Interactive charts for deeper exploration  
Key Visuals Generated
Salary by Experience Level (Box Plot) – Seaborn
Compares salary distributions across:
Entry-level
Mid-level
Senior
Executive roles 

Monthly AI Job Postings Trend (Line Chart) – Plotly
Shows how AI job postings evolved over time. 
 Interactive HTML version included for deeper exploration.  

Salary by Industry (Box Plot) – Seaborn  
Focuses on top 15 industries, showing salary variation.  

Company Size vs. Remote Preference (Count Plot) – Seaborn 
 Displays how remote/hybrid/on-site jobs are distributed by company size.  

Top 10 AI Job Titles (Bar Plot) – Seaborn  
Highlights the most frequent AI-related job titles in the dataset. 

| Chart | Description | Tool | File |
|------|-------------|------|-----|
|  Salary by Experience Level | Boxplot comparing Entry–Executive salaries | Seaborn | `eda_salary_by_experience.png` |
|  AI Job Posting Trends | Interactive line chart of monthly postings | Plotly | `eda_job_posting_trends_plotly.html` |
|  Salary by Industry | Salary ranges across top 15 industries | Seaborn | `eda_salary_by_industry.png` |
|  Company Size vs Remote Work | Countplot comparing remote preferences by company size | Seaborn | `eda_company_size_remote_preference.png` |
|  Top Job Titles | Bar plot of most frequent AI job titles | Seaborn | `eda_top_job_titles.png` |
 

#### Conclusion
The ETL phase successfully transformed raw AI job market data into a clean, structured dataset, ensuring reliability for further analysis. Key steps like currency normalization, experience level categorization, and duplicate removal built a solid foundation for data-driven insights.

Building on this, the EDA phase revealed important trends and patterns:
- Salaries rise with experience level, with executives earning the highest pay. 
- Industries such as tech and finance offer consistently higher compensation. 
- Remote roles are increasingly common, especially in mid-sized companies. 
- A few job titles dominate hiring trends, indicating where AI demand is strongest.

These findings create a clear analytical baseline for the next stages of the project — including statistical testing and dashboard creation — to deepen our understanding of the evolving AI job market landscape.

### Analysis techniques used

 **ETL Phase Techniques:**
Data Profiling: Assessed raw dataset quality, structure, and completeness.
Data Cleaning: Removed duplicates, handled missing values, and standardised formats.
Data Transformation: 
- Converted salary data to a common USD baseline. 
- Categorised experience levels (Entry, Mid, Senior, Executive). 
- Unified inconsistent naming conventions for roles and companies.
- 
Data Validation: Ensured the processed dataset aligned with the expected schema and integrity rules.

**EDA Phase Techniques**
Descriptive Statistics: Calculated mean, median, min/max, and salary distribution for each experience level.
Data Visualisation: Used histograms, bar charts, and boxplots to reveal trends in salaries, industries, and company sizes.
Categorical Analysis: Compared salary trends across job titles, industries, and employment types.
Trend Identification: Highlighted patterns in remote work adoption and company hiring behaviour.
Outlier Detection: Flagged unusual salary values and extreme cases for further review.

**Dashboard Techniques**
The analysis was performed using Python libraries including pandas, numpy, seaborn, matplotlib, scipy, and wordcloud. Salary outliers were handled using Winsorization based on IQR detection. Data cleaning involved parsing and cleaning skill-related fields. Feature engineering included creating a skills column and applying one-hot encoding to extract and analyze in-demand skills effectively.


### Ethical considerations
**1. Data Privacy**
The project data included publicly available AI job postings with no sensitive or personal data about individuals. Still, we were cautious about:
 Anonymity: Avoiding the use of any fields that could potentially identify individuals indirectly (e.g. personal email addresses or applicants by name, if any).
Transparency: Recording the origin and nature of the dataset so that users understand the scope and limitations.
Action Taken: Removed or anonymised fields that could have compromised anonymity. No user data was gathered or retained by the project in analysing or utilising the dashboards.
**2. Bias and Fairness**
Bias can be present in employment market data sets — especially when looking at salary, seniority, and access to jobs by nations or regions. Some jobs could reflect:
 Geographic or gender wage gaps
 Hiring bias or tech elitism
Over-representation of particular industries or countries
Action Taken: We treated the data as descriptive, not predictive, avoiding conclusions implying causality or reinforcing stereotypes. Insights were presented with caveats, particularly around experience level and remote salary disparities. Visualisations were neutrally labelled (e.g. "EX = Executive" rather than "Top-level"), and filters enabled exploration, not judgment.

**3. Legal and Societal Impact**
Using worldwide employment market data introduces legal and moral responsibility for:
 Cross-border salary comparison (differing tax and cost-of-living situations)
Social implications of prioritising one region or function over another
Use of data to justify discriminatory hiring
  ** Action Taken:** Guidelines for interpretation are displayed in every dashboard and report to prevent misuse of findings. Put inclusivity and diverse user needs first by incorporating empathy maps and user stories into design thinking. Gave no prescriptive advice on pay, simply offered comparative data and trends for decision-making.
**Summary**
We developed this project with an acute ethical sensitivity, with fairness, transparency, and inclusiveness in analysis and communication. Data were handled with care, and all results were communicated to empower users, rather than reinforcing inequalities.
### Dashboard Design

The dashboard includes multiple pages and visual blocks that address key business questions through intuitive design. Key components include a bubble chart for job locations, bar charts for in-demand skills and country-wise salaries, a line chart for salary trends, a box plot for salary by experience level, an area chart comparing company size and experience, and a scatter plot analyzing benefits vs salary. Interactive filters level help users explore specific segments. To communicate insights effectively, technical users can engage with tooltips and layered data, while non-technical audiences benefit from simple titles, explanatory captions, and clean visuals that highlight core trends and comparisons.

**AI Careers Dashboard: Global Demand, Skills & Salaries**

This dashboard answers key questions about the global AI job market, following a clear story flow:
Where
 Where are AI jobs located globally?
 → Helps users explore top regions for AI roles.


What Skills
 What AI skills are most in demand?
 → Guides learners on what to focus on when upskilling.


Market Trends
 How have AI salaries changed over time?
 → Shows salary growth and market evolution.


Geographic Pay
 Which countries offer the highest salaries?
 → Useful for comparing earning potential across countries.


Experience Impact
 How does experience level affect salary?
 → Helps candidates and employers understand fair pay.


Company Size Effect
 Do salaries differ by company size?
 → Explores pay patterns in startups vs large companies.


Total Compensation
 How do benefits relate to salary?
 → Shows the full picture beyond base pay.

Explore this Tableau dashboard to understand AI job market dynamics from location and skills to compensation: To view the Tableau dashboard, [click here](https://public.tableau.com/app/profile/angel.jayakumar/viz/AIJobsSalaryAnalytics/AIJobsSalaryAnalytics)

### Development Roadmap

**Phase 1: Project Setup & Design Thinking**
 Identified key user personas (Recruiter, Job Seeker, Policy-Maker)
Scanned pain points and re-framed them as data-driven "How Might We" questions
Aligned team roles (Project Manager, Data Architect, Analyst, Visualiser, Design Thinker)
** Outcome:** A user-centred foundation and research focus driven by empathy, not just numbers.

**Phase 2: Data Preparation & ETL**
Collected and cleaned AI job data sets from various sources
Standardised currency values to USD, standardisation of experience and job title
Introduced new fields.

**Challenges Overcome:** Unconventional benefit structures and absence of salary details
** Solution:** Created a scoring system for benefits; used median imputations and external references for missing salaries.

**Phase 3: Exploratory Analysis & Hypothesis Testing**
Examined salary by benefit level, experience, region, remote status, and role
Hypotheses tested on: Remote work vs. salary,  Salary vs. benefits,  Salary vs. experience leve

**Challenges Encountered:** BIAS-free interpretation of regional differences
           **Method:** Visual comparison and normalised measures (e.g. salary by experience band)
           
**Phase 4: Dashboard & Visualisation
 Designed interactive visualisations using Tableau and Streamlit (prototype level)
Prioritised simplicity, user intent, and useful real-world uses
Utilised visuals and filters for every persona (e.g. Reem the job applicant, Amanda the talent manager)
**Challenges Overcome: Balance between depth and clarity in dashboard design.

**Phase 5: Presentation, Delivery & App Planning**

    Final PPT presentation including  user-focused empathy maps and final dashboard views, summary of findings and final recommendations
**Skills & tools  planning to learn based on this Project**
Master level Tableau skills (Level-of-detail calculations, story point sequencing)
Streamlit API integration (e.g., live job market data feeds)
Heroku & CI/CD pipelines for automated app deployment
Data ethics auditing tools (for fair hiring insights)
R for comparative analysis (adding multi-language tool flexibility)
### SUMMARY OF FINDINGS AND FINAL RECOMMENDATIONS

 **Key Findings**
Remote roles tend to offer higher salaries: They consistently show higher median salaries compared to in-office roles. This trend suggests remote work is often used as a financial incentive or reflects more specialised, in-demand roles.

 Higher benefits score correlates with higher salary: Jobs that offer more comprehensive benefits programs (e.g. equity, education benefits, medical) tend to also provide better wages, implying that successful businesses invest in both.

Experience level has a strong influence on compensation: There is a dramatic step-up in compensation from junior to executive levels. The step-up to the executive level is even more dramatic, illustrating the impact of seniority and leadership experience on compensation.

Uneven distribution of roles by regions: High-paying jobs are located primarily in Western Europe and North America, and fewer entry-level and lower-paying jobs are advertised in emerging economies. Remote jobs reduce this imbalance to some degree, but not completely.

 Certain jobs demand higher compensation regardless of where the job is located: Specialised roles like Machine Learning Engineer, AI Researcher, and Data Architect pay significantly more than non-specialised roles, even across regions and ranges of experience.

**Recommendations**

For Job Seekers:

Optimise remote-friendly roles in high-demand specialisations to maximise salary opportunities
Use dashboards to compare expected salary based on experience and location before applying
 Seek roles with strong benefit packages as an indirect indicator of competitive compensation

    For Recruiters & Hiring Teams
Use salary and benefit benchmarks to remain competitive when hiring AI talent. 
Provide remote or hybrid solutions to broaden access to talent and enhance pay equity.
Customise job postings to expectations around experience levels and specify growth opportunities.

### Main Data Analysis Libraries
This project utilised data manipulation, visualisation, and analysis libraries based on Python for pre-processing the dataset, pattern identification, hypothesis execution, and data preparation for incorporation into the dashboard.
1. pandas: Used for loading, cleaning, changing data structure, and filtering data.
2. numpy: Used for handling missing data and basic numerical computations.
3. matplotlib & seaborn: Used for creating static visualisations to understand data distributions and trends.
4. plotly: Used for interactive and dynamic visuals
### Credits

In the spirit of openness and responsible project practice, the following materials were used to aid in the creation, analysis, and presentation of this project. All code snippets, design pieces, and datasets not created in-house are credited below.

 **Academic references**
Mckinsey(2025).McKinsey: A new operating model for people management: More personal, more tech, more human.Available at: https://www.mckinsey.de/capabilities/people-and-organizational-performance/our-insights/a-new-operating-model-for-people-management-more-personal-more-tech-more-human 
geeksforgeeks(2025).Difference between t-test and ANOVA. Available at:https://www.geeksforgeeks.org/data-science/difference-between-t-test-and-anova/ 

 **Content & Code References**

Pandas Documentation – used for data cleaning and grouping
Seaborn Gallery – salary and boxplots visualisations styling
Plotly Express Examples – interactive visual charts
Code Institute LMS for coding and statistical material.

**Generative AI Contributions**

ChatGPT and Copilot were used to polish documentation in the Jupyter notebook


**Media & Visual Assets**

Canva assets – empathy maps and persona visuals
 Fonts for final cover slides and mockups were borrowed from Canva's free license library
 Cover image design and empathy maps were designed using free-use templates in Canva.
 
### Acknowledgements (optional)
Thanks to our tutor Emma and all the instructors, Niel, Spencer, Mark, and John. Also, to our peers who supported us throughout the course.


