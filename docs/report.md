# Capstone Report
 
## 1. Title: Predictive Analysis for Injury Diagnosis and Localization

- **Author Name** - Michael Whittington
- **Prepared for** - UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- **Semester** - Fall 2023
- <a href="https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael"><img align="left" src="https://img.shields.io/badge/-Project GitHub Repo-181717?logo=github&style=flat" alt="icon | GitHub"/></a> 
  
- <a href="https://www.linkedin.com/in/michael-whittington-6a099137/"><img align="left" src="https://img.shields.io/badge/-LinkedIn: Lets Connect!-1E90FF?logo=linkedin&style=flat" alt="icon | LinkedIn"/></a>  
- <a href="https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/raw/main/docs/Final_Presentation%20-%20Predictive%20Analysis%20for%20Injury%20Diagnosis%20and%20Localization.pptx"><img src="https://img.shields.io/badge/-PowerPoint Presentation Download-B7472A?logo=microsoftpowerpoint&style=flat" alt="icon | GitHub"/></a>  

- <a href="https://youtu.be/ZiGtqlQvd7U"><img align="left" src="https://img.shields.io/badge/-YouTube Presentation-FF0000?logo=youtube&style=flat" alt="icon | YouTube"/></a> 
    
## 2. Background

In the realm of public health and safety, the ability to predict and subsequently prevent injuries is of great importance. By understanding patterns in consumer product-related injuries, industries can make informed decisions to refine their products, thereby reducing potential risks. Moreover, this predictive analysis can serve as a tool for healthcare providers. If medical professionals can swiftly and accurately diagnose injuries, they can expedite treatment plans, leading to better patient outcomes. This project not only aids in enhancing the safety measures of consumer products but also paves the way for advanced medical diagnostics using data-driven methodologies. It serves a dual purpose of fostering product safety and optimizing medical care, thus having broad societal implications.

Leveraging the United States Consumer Product Safety Commission's injury dataset, collected by NEISS, this project aims to accurately predict both the diagnosis of a patients injury and the specific body part that was affected. Through the use of machine learning models and data analysis techniques, the goal is to discern patterns and correlations that can lead to reliable predictions concerning the nature and location of injuries based on the given parameters in the dataset.

**Research Questions:**
- How effective are different machine learning models in predicting injury-related outcomes?
- What is the impact of data quality and quantity on the predictive accuracy of machine learning models in injury data analysis?
- Are there discernible patterns in the data that indicate a higher likelihood of injuries to specific body parts based on certain factors or circumstances?
- What role does feature selection and hyperparameter tuning play in enhancing the performance of machine learning models in injury data analysis?
- How do various consumer products correlate with the type and location of injuries? Are certain products more prone to cause injuries to specific body parts?


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

In an effort to fully understand the dataset and prepare for model training, Exploratory Data Analysis (EDA) was conducted. The National Institute of Standards and Technology (NIST) explains that "EDA is an approach to data analysis that postpones the usual assumptions about what kind of model the data follow with the more direct approach of allowing the data itself to reveal its underlying structure and model."<sup>1</sup> EDA serves as a crucial bridge between data collection and the predictive modeling process. Through this analysis, the project is able to gain insights into data variability and relationships, enabling informed decisions on methods and model choices. This project takes a multifaceted approach to EDA, including the use of Plotly Visualizations, Pandas Profiling, Pandas, and an EDA Application built using Streamlit.

**[Preliminary Exploration with Pandas](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/data_exploration/neiss_initial_data_exploration.ipynb)**

Leveraging the pandas library, the project starts the exploratory data analysis by observing an overview of the dataset, summarizing key statistics across all columns, checking for missing values, and determining the unique values of the target variables.
- `neiss.shape` - obtaining the shape of the dataset
- `neiss.head()` - previewing the intial rows of the dataset
- `neiss.dtypes` - determining the data types for each column in the dataset
- `neiss.describe(include='all')` - providing key summary statistics across all columns
- `neiss.isnull().sum()` - checking for missing values by column in the dataset
- `len(pd.unique(neiss['Diagnosis']))` and `len(pd.unique(neiss['Body_Part']))` - finding the unique values for the project target variables

Additional details on the preliminary data exploration can be found in the [notebook](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/data_exploration/neiss_initial_data_exploration.ipynb).

**Pandas Profiling**

Pandas Profiling was also used to explore the neiss dataset. Pandas Profiling is a powerful tool that provides an overview of the dataset with detailed insights on each column, correlations, missing values, and more. This is all packaged into an interactive HTML report. The code for developing the Pandas Profiling report can be found [here](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/data_exploration/Pandas_Profiling.ipynb). See below for images of the Pandas Profiling output for the neiss dataset:

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

The code for developing the streamlit application can be found [here](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/blob/main/src/data_exploration/eda_app.py). Additionally, some of the functionality can be seen in the images below:

**Project Application Overview**

![Streamlit-App-Overview](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/55cea973-b76c-4c82-868a-05182b4ca0b1)

**Dataset Descriptive Analysis**

![Streamlit-App-Descriptive-Analysis](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/a3960031-6ff8-46cf-9130-807d0c9c7a2b)

**Box Plots of Target Variables**

![Streamlit-App-BoxPlots](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/58a611ca-7870-4045-9ae6-72cbe19d0358)


**NEISS Plotly Correlation Matrix**
Using plotly, I created a correlation matrix to understand the relationship between the target variables and also the potential model features/predictors. This visualization enabled a clearer view of how each feature correlates with one another, providing insights into potential multicollinearity issues and helping to identify the most influential variables for model prediction. See below for an image of the Correlation Matrix:

![Plotly-Correlation-Matrix](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/c65ba6e7-aa32-4dd4-8ede-304920732832)



## 5. Model Training

- The project used the following machine learning models for predictive analytics:
  - Random Forest (`RandomForestClassifier`)
  - XGBoost (`XGBClassifier`)
  - LightGBM (`LGBMClassifier`)
  - CatBoost (`CatBoostClassifier`)
  - K-Nearest Neighbors (`KNeighborsClassifier`)
- The models will be trained using the following methods:
  - The train vs test split of 80/20 will be used for the models.
  - Python packages used for this project include:
     - scikit-learn<sup>2</sup>
     - xgboost<sup>3</sup>
     - catboost<sup>4</sup>
     - lightgbm<sup>5</sup>
  - The development environments used include:
     - Personal laptop
     - Google CoLab
- The project performance will be measured using the following:
  - Accuracy
  - Precision
  - Recall
  - f1-score
- This project used the following model improvement methods:
  - Hyperparameter Tuning - Part of the scikit-learn library is a hyperparameter tuning technique called `RandomizedSearchCV`. Being that the dataset is large, this was the optimal hyperparameter tuning technique, as it randomly selects combinations of parameters to try. 
  - Feature Importance - This improvement technique assigns a score to the machine learning models input features based on how useful they are at predicting a target variable. Once these values are assigned, it can help us improve and interpret the models.

## 6. Model Results - Accuracy

![Model_Results](https://github.com/DATA-606-2023-FALL-TUESDAY/Whittington_Michael/assets/107943021/884b0d5a-1037-41c4-8dc8-0e606aca2691)


## 7. Application of the Trained Models

Part of this research project was finding a way to effectively apply the predictive models that were trained against the NEISS dataset. The goal was to create a user-friendly application that will be both a practical tool and bridge the gap between complex models and end-users, such as healthcare professionals, researchers, or injured citzens. The highest performing model was XGBoost, which was used as the machine learning prediction model. The application offers a range of functionalities, providing users with various options to input and obtain tailored results. These functionalities include:
- **User Input Options** - Users can input specific details related to injury incidents, such as age, sex, race, and the type of product involved. This level of detail allows for a more personalized analysis.
- **Predictive Analytics** - Based on the input data, the application predicts the most likely body part injured and the type of injury (diagnosis), utilizing the trained XGBoost models.
- **Accessibility and Ease of Use** - Designed with a focus on user experience, the application facilitates easy navigation and interpretation of results, making it accessible to a broad audience.

## 8. Conclusion

This project revealed some intruiging insights and challenges when dealing with the NEISS injury dataset. Notably, each model was more effective when predicting the diagnosis than predicting the body part affected. Among the machine learning models tested, XGBoost demonstrated a slight edge over its counterparts, including Random Forest, LightGBM, CatBoost, and KNN. Model optimization proved to also be complicated to achieve. Despite attempts at hyperparameter tuning and focusing on feature importance, the improvements to model performance were limited. This outcome suggests that the dataset likely lacks a clear pattern or distinction between classes. This project serves as a testament to the unpredictable nature of data science, where results may not always align with initial expectations, highlighting the importance of flexibility and adaptability in your approach.


## 9. Future Research Direction
While quite a bit was accomplished during this project, there are several avenues for enhancement and deeper exploration. Augmenting the dataset would be one of the primary focuses towards enhancement. Incorporating additional data could provide more clarity on whether the current limitations are data-related, potentially revealing more distinct patterns, and improving model accuracy. Additionally, expanding the scope of evaluation metrics beyond the traditional accuracy, precision, recall, and F1-score could offer a more nuanced understanding of model performance, especially in areas where conventional metrics might not capture the model's true predictive power. Lastly, addressing computational constraints is pivotal. The current dataset's size posed challenges, limiting the extent of hyperparameter tuning and analysis. With more powerful computational resources, a more thorough exploration of hyperparameters could be undertaken. Furthermore, it would be essential to increase computing power if the project decides to expand the dataset. This would ensure that the project can effectively analyze a larger amount of data, which could unlock new insights and enhance predictive accuracies.

## 10. Project Sources
[1] What is EDA?. Exploratory Data Analysis - NIST. (2012, June 27). https://www.itl.nist.gov/div898/handbook/toolaids/pff/eda.pdf 

[2] Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

[3] Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785–794). New York, NY, USA: ACM. https://doi.org/10.1145/2939672.2939785

[4] Anna Veronika Dorogush, Vasily Ershov, Andrey Gulin. Workshop on ML Systems at NIPS 2017

[5] Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., … Liu, T.-Y. (2017). Lightgbm: A highly efficient gradient boosting decision tree. Advances in Neural Information Processing Systems, 30, 3146–3154.
