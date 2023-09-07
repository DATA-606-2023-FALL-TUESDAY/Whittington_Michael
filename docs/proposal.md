# Capstone Proposal
 
## 1. Proposal Title: Predictive Analysis for Injury Diagnosis and Localization

- **Author Name** - Michael Whittington
- <a href="https://github.com/Michael-Whittington"><img align="left" src="https://img.shields.io/badge/-GitHub-CD5C5C?logo=github&style=flat" alt="icon | LinkedIn"/></a> 
  
- <a href="https://www.linkedin.com/in/michael-whittington-6a099137/"><img align="left" src="https://img.shields.io/badge/-LinkedIn-1E90FF?logo=linkedin&style=flat" alt="icon | GitHub"/></a>  
- Link to your PowerPoint presentation file
- Link to your YouTube video 
    
## 2. Background

Provide the background information about the chosen topic. 

- What is it about? 
- Why does it matter? 
- What are your research questions?

## 3. Data 

Describe the datasets you are using to answer your research questions.

- **Data sources** - This dataset is collected by a system called National Electronic Injury Surveillance System (NEISS), which is operated by the United States Consumer Product Safety Commission (CPSC).
  - **Dataset Link:** https://www.cpsc.gov/cgibin/NEISSQuery/home.aspx
  - **NEISS Information:** https://www.cpsc.gov/Research--Statistics/NEISS-Injury-Data  
- **Data size** - 46.7 MB
- **Data shape** -
  - Rows = 323,343
  - Columns = 25 
- **Time period** - 2022
- **Rows** - Patients
    
  | Column Name  | Data Type | Definition | Example Values |
  |--------------|-----------|------------|------------------|
  | CPSC_Case_Number | int64     | CPSC case number       | 220100687, 220100691, etc.           |
  | Treatment_Date | datetime64     | Date of Treatment       | 1/1/2022, etc.           |
  | Age          | int64       | Age of Patient        | 1, 2, 3, etc.              |
  | Sex | int64     | Sex of Patient       | 0, 1, 2, 3           |
  | Race | int64     | Race of Patient       | 0, 1, 2, 3, etc.           |
  | Other_Race | object     | Description of Other Race (Used with Race=3)       | WHITE, AFRICAN, LATINO, etc.            |
  | Hispanic | int64     | Hispanic, Latino/Latina, or of Spanish Origin       | 0, 1, 2          |
  | Body_Part | int64     | Injured Body Part       | 0, 30, 31, 32, etc.           |
  | Diagnosis | int64     | Injury Diagnosis       | 41, 42, 46, etc.           |
  | Other_Diagnosis | object     | Description of Other Diagnosis (Used with Diag=71)      | NECK PAIN, ELBOW PAIN, CARDIAC ARREST, etc.           |
  | Body_Part_2 | float64     | Injured Body Part 2       | 0, 30, 31, 32, etc.           |
  | Diagnosis_2 | float64     | Injury Diagnosis 2       | 41, 42, 46, etc.           |
  | Other_Diagnosis_2 | object     | Description of Other Diagnosis 2 (Used with Diag2=71)  - available from 2019       | NECK PAIN, ELBOW PAIN, CARDIAC ARREST, etc.           |
  | Disposition | int64     | Disposition       | 1, 2, 3, etc.           |
  | Location | int64     | Incident Location       | 1, 2, 3, etc.           |
  | Fire_Involvement | int64     | Fire Involvement/Fire Department Attended       | 1, 2, 3, etc.           |
  | Product_1 | int64     | Product Code (See NEISS Coding Manual for Details)       | 102, 106, 110, etc.           |
  | Product_2 | int64     | Product Code 2 (See NEISS Coding Manual for Details)       | 102, 106, 110, etc.           |
  | Product_3 | int64     | Product Code 3 (See NEISS Coding Manual for Details)       | 102, 106, 110, etc.           |
  | Alcohol | int64     | Consumed Alcohol Prior to or During the Incident       | 0, 1           |
  | Drug | int64     | Use of Drugs or Medication Contributed to the Incident or the Severity of the Injury       | 0, 1           |
  | Narrative_1 | object     | Description of Injury Event        | ex. 60 YOF C/O LOWER BACK PAIN AFTER GETTING UP OFF COUCH DX STRAINED LOWER BACK           |
  | Stratum | object     | Design Variable-Stratum       | S, V, M, etc.           |
  | PSU | int64     | Design Variable-Primary Sampling Unit (PSU)       | 2, 3, 4, etc.           |
  | Weight | float64     | Statistical Weight for National Estimates       | 5.8342, 77.9827, etc.           |


- **Target Variable(s)** - Body_Part, Diagnosis
- Which variables/columns may be selected as features/predictors for your ML models?

## 4. Exploratory Data Analysis (EDA)

- Perform data exploration using Jupyter Notebook
- You would focus on the target variable and the selected features and drop all other columns.
- produce summary statistics of key variables
- Create visualizations (I recommend using **Plotly Express**)
- Find out if the data require cleansing:
  - Missing values?
  - Duplicate rows? 
- Find out if the data require splitting, merging, pivoting, melting, etc.
- Find out if you need to bring in other data sources to augment your data.
  - For example, population, socioeconomic data from Census may be helpful.
- For textual data, you will pre-process (normalize, remove stopwords, tokenize) them before you can analyze them in predictive analysis/machine learning.
- Make sure the resulting dataset need to be "tidy":
  - each row represent one observation (ideally one unique entity/subject).
  - each columm represents one unique property of that entity. 

## 5. Model Training 

- What models you will be using for predictive analytics?
- How will you train the models?
  - Train vs test split (80/20, 70/30, etc.)
  - Python packages to be used (scikit-learn, NLTK, spaCy, etc.)
  - The development environments (your laptop, Google CoLab, GitHub CodeSpaces, etc.)
- How will you measure and compare the performance of the models?

## 6. Application of the Trained Models

Develop a web app for people to interact with your trained models. Potential tools for web app development:

- **Streamlit** (recommended for its simplicity and ease to learn)
- Dash
- Flask

## 7. Conclusion

- Summarize your work and its potetial application
- Point out the limitations of your work
- Lessons learned 
- Talk about future research direction

## 8. References 

List articles, blogs, and websites that you have referenced or used in your project.
