# Capstone Proposal
 
## 1. Proposal Title: Predictive Analysis for Injury Diagnosis and Localization

- **Author Name** - Michael Whittington
- **Prepared for** - UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- **Semester** - Fall 2023
- <a href="https://github.com/Michael-Whittington"><img align="left" src="https://img.shields.io/badge/-GitHub-CD5C5C?logo=github&style=flat" alt="icon | LinkedIn"/></a> 
  
- <a href="https://www.linkedin.com/in/michael-whittington-6a099137/"><img align="left" src="https://img.shields.io/badge/-LinkedIn: Lets Connect!-1E90FF?logo=linkedin&style=flat" alt="icon | GitHub"/></a>  
- <a href="https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/raw/main/docs/Final_Presentation%20-%20Predictive%20Analysis%20for%20Injury%20Diagnosis%20and%20Localization.pptx"><img src="https://img.shields.io/badge/-PowerPoint Presentation Download-B7472A?logo=microsoftpowerpoint&style=flat" alt="icon | GitHub"/></a>  
- **YouTube video** - In Progress 
    
## 2. Background

In the realm of public health and safety, the ability to predict and subsequently prevent injuries is of great importance. By understanding patterns in consumer product-related injuries, industries can make informed decisions to refine their products, thereby reducing potential risks. Moreover, this predictive analysis can serve as a tool for healthcare providers. If medical professionals can swiftly and accurately diagnose injuries, they can expedite treatment plans, leading to better patient outcomes. This project not only aids in enhancing the safety measures of consumer products but also paves the way for advanced medical diagnostics using data-driven methodologies. It serves a dual purpose of fostering product safety and optimizing medical care, thus having broad societal implications.

Leveraging the United States Consumer Product Safety Commission's injury dataset, collected by NEISS, this project aims to accurately predict both the diagnosis of a patients injury and the specific body part that was affected. Through the use of machine learning models and data analysis techniques, the goal is to discern patterns and correlations that can lead to reliable predictions concerning the nature and location of injuries based on the given parameters in the dataset.

**Research Questions:**
- What specific attributes within the NEISS data have the highest correlation with the type of injury diagnosis?
- Are there discernible patterns in the data that indicate a higher likelihood of injuries to specific body parts based on certain factors or circumstances?
- How do various consumer products correlate with the type and location of injuries? Are certain products more prone to cause injuries to specific body parts?
- How accurate are the machine learning models in predicting injury diagnosis and location based on the NEISS data?

## 3. Data 

The dataset used in this report is collected by a system called National Electronic Injury Surveillance System (NEISS), which is operated by the United States Consumer Product Safety Commission (CPSC). Each row in the dataset represents a patient and data collected during their emergency room visit. While NEISS has collected data across many years, this report uses 2022 patient data from participating hospitals. Below is more information on the dataset and its elements:
  - **Dataset Link:** https://www.cpsc.gov/cgibin/NEISSQuery/home.aspx
  - **NEISS Information:** https://www.cpsc.gov/Research--Statistics/NEISS-Injury-Data  
- **Data size** - 46.7 MB
- **Data shape** -
  - Rows = 323,343
  - Columns = 25 
- **Data Dictionary**
    
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
- **Potential Model Features/Predictors** - Product_1, Body_Part (for Diagnosis Prediction) and Diagnosis (for Body_Part Prediction)

## 4. Exploratory Data Analysis (EDA)

In an effort to fully understand the dataset and prepare for model training, Exploratory Data Analysis (EDA) was conducted. **Add in quote about the importance of EDA**. EDA serves as a crucial bridge between data collection and the predictive modeling process. Through this analysis, the project is able to gain insights into data variability and relationships, enabling informed decisions on methods and model choices. This project takes a multifaceted approach to EDA, including the use of Plotly Visualizations, Pandas Profiling, Pandas, and an EDA Application built using Streamlit.

**[Preliminary Exploration with Pandas](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/neiss_data_exploration.ipynb)**

Leveraging the pandas library, the project starts the exploratory data analysis by observing an overview of the dataset, summarizing key statistics across all columns, checking for missing values, and determining the unique values of the target variables.
- `neiss.shape` - obtaining the shape of the dataset
- `neiss.head()` - previewing the intial rows of the dataset
- `neiss.dtypes` - determining the data types for each column in the dataset
- `neiss.describe(include='all')` - providing key summary statistics across all columns
- `neiss.isnull().sum()` - checking for missing values by column in the dataset
- `len(pd.unique(neiss['Diagnosis']))` and `len(pd.unique(neiss['Body_Part']))` - finding the unique values for the project target variables

Additional details on the preliminary data exploration can be found in the [notebook](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/neiss_data_exploration.ipynb).

**Pandas Profiling**

Pandas Profiling was also used to explore the neiss dataset. Pandas Profiling is a powerful tool that provides an overview of the dataset with detailed insights on each column, correlations, missing values, and more. This is all packaged into an interactive HTML report. The code for developing the Pandas Profiling report can be found [here](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/Pandas_Profiling.ipynb). See below for images of the Pandas Profiling output for the neiss dataset:

**NEISS Pandas Profiling Overview Report**
![Pandas-Profiling-Overview-Report](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/fc04a4ef-0c0c-43aa-876e-ca987d222753)

**Pandas Profiling Target Variables Report**

![Pandas-Profiling-Target-Variables](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/19bcc3a6-7735-4190-9156-42fffc691a90)


**Streamlit EDA Application & Plotly Visualizations**

In an effort to better understand the dataset and provide an effective way for future data exploration, I created a streamlit application. This application is easy to use and provides the following functionality:
- Ability for the user to upload a dataset.
- Displays basic information about the dataset.
- Show information about missing values in the dataset.
- Provides statistical summaries of the dataset.
- Allows selection of a column and view its histogram.
- Shows distributions of numerical columns.
- Count plots of categorical columns.
- Box plots for numerical columns.
- Shows information about outliers in the dataset.
- Allows users to see how the target variable varies with categorical columns.

The code for developing the streamlit application can be found [here](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/app2.py). Additionally, some of the functionality can be seen in the images below:

**Project Application Overview**

![Streamlit-App-Overview](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/55cea973-b76c-4c82-868a-05182b4ca0b1)

**Dataset Descriptive Analysis**

![Streamlit-App-Descriptive-Analysis](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/a3960031-6ff8-46cf-9130-807d0c9c7a2b)

**Box Plots of Target Variables**

![Streamlit-App-BoxPlots](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/58a611ca-7870-4045-9ae6-72cbe19d0358)

Using plotly, I created a correlation matrix to understand the relationship between the target variables and also the potential model features/predictors. This visualization enabled a clearer view of how each feture correlates with one another, providing insights into potential multicollinearity issues and helping to identify the most influential variables for model prediction. See below for an image of the Correlation Matrix:

**NEISS Plotly Correlation Matrix**

![Plotly-Correlation-Matrix](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/c65ba6e7-aa32-4dd4-8ede-304920732832)



## 5. Model Training (Need more information added to this section)

- What models you will be using for predictive analytics?
  - Random Forest
  - XGBoost Classifier
  - LightGBM
  - CatBoost
  - K-Nearest Neighbors (KNN)
- How will you train the models?
  - The train vs test split of 80/20 will be used for the models
  - Python packages used for this project include:
     - scikit-learn
     - xgboost
     - catboost
     - lightgbm
  - The development environments used include:
     - Personal laptop
     - Google CoLab
- How will you measure and compare the performance of the models (NEED TO EXPAND ON THESE)?
  - Accuracy
  - Precision
  - Recall
  - f1-score
- Model Improvement Methods (NEED TO EXPAND ON THESE):
  - Hyperparameter Tuning
  - Feature Importance

## 6. Application of the Trained Models

Streamlit will be used to create an application for exploratory data analysis and to create an application that will allow users to interact with the best performing model. 

**Body Part and Diagnosis Prediction Application (NEED MORE INFORMATION AND AN IMAGE)**
The model interaction application will feature the following functionality:
  - Users will have a set of option to select from (sex, weight, race, age, and product)
  - Once user selects their options above, they will be given an output of the body parts most likely injured and diagnosis.

**Exploratory Data Analysis Application (NEED MORE INFORMATION AND AN IMAGE)**    
The exploratory data analysis application will feature the following functionality:
  - Users will be able to upload a dataset and see it's dimensions
  - View N/A Values
  - Gather descriptive analytics (mean, median, etc.)
  - Visualize a histogram for a target column
  - Show the distribution of numerical columns
  - Show count plots of categorical columns
  - Visualize box plots for numerical columns
  - View outliers in the dataset
  - Visualize how a target variable varies with categorical columns 

## 7. Conclusion

This project revealed some intruiging insights and challenges when dealing with the NEISS injury dataset. Notably, each model was more effective when predicting the diagnosis than predicting the body part affected. Among the machine learning models tested, XGBoost demonstrated a slight edge over its counterparts, including Random Forest, LightGBM, CatBoost, and KNN. Model optimization proved to also be complicated to achieve. Despite attempts at hyperparameter tuning and focusing on feature importance, the improvements to model performance were limited. This outcome suggests that the dataset likely lacks a clear pattern or distinction between classes. This project serves as a testament to the unpredictable nature of data science, where results may not always align with initial expectations, highlighting the importance of flexibility and adaptability in your approach.


## 8. Future Research Direction
While quite a bit was accomplished during this project, there are several avenues for enhancement and deeper exploration. Augmenting the dataset would be one of the primary focuses towards enhancement. Incorporating additional data could provide more clarity on whether the current limitations are data-related, potentially revealing more distinct patterns, and improving model accuracy. Additionally, expanding the scope of evaluation metrics beyond the traditional accuracy, precision, recall, and F1-score could offer a more nuanced understanding of model performance, especially in areas where conventional metrics might not capture the model's true predictive power. Lastly, addressing computational constraints is pivotal. The current dataset's size posed challenges, limiting the extent of hyperparameter tuning and analysis. With more powerful computational resources, a more thorough exploration of hyperparameters could be undertaken. Furthermore, it would be essential to increase computing power if the project decides to expand the dataset. This would ensure that the project can effectively analyze a larger amount of data, which could unlock new insights and enhance predictive accuracies.
