# Final-Project-JCDS09

## Consumers' Purchase Intention Towards Online Shopping

### This project is as one of the requirements for completing the Job Connector Data Science Programme in Purwadhika Startup & Coding School Jakarta, Batch 09.

### About Dataset
- The dataset consists of feature vectors belonging to 12,330 sessions.
- The dataset has been collected from www.columbia.com.tr which was provided by the Turkish Gözalan Group. 
- The Columbia Sportswear Company is an American company that manufactures and distributes outerwear and outdoor accessories.

### Purpose of the Project
- To predict the purchasing intention of the visitor using user information and aggregated pageview data track during the visit along with some session.
- Understanding consumer motivations that affect the online shopping behavior.

### Tech Stack
Written with Python in Jupyter Notebook and Visual Studio Code<br>
Libraries used: NumPy, Pandas, Matplotlib, Seaborn, Scipy, Plotly, Scikit-learn, Imbalanced-learn, Joblib<br>
Deployed with Flask

### In this project, there are 3 steps that I did:

Data Cleaning (Handle Missing Value and Outlier)
Exploratory Data Analysis
Modelling Machine Learning Algorithm to Make Classification for Revenue generating or not, based on features that provide in this dataset.

### Keywords
  *Classification, e-Commerce, Google Analytics, Digital Marketing, Conversion, Session, Channel*<br>
  *Target Imbalance, Feature Selection, Model Selection, Hyperparameter Tuning, Evaluation, Deployment*

## SECTION 1 - Data Cleaning

***The main aim of Data Cleaning is to identify and remove errors & duplicate data, in order to create a reliable dataset. This improves the quality of the training data for analytics and enables accurate decision-making.*** 

   We have to analyze each feature, especially each feature against our target variable, Revenue. we need to identify and remove errors & duplicate data, in        order to create a reliable dataset. So, we can find out and predict what features can provide the potential for greater revenue due to the final consumer decision to make a product purchase.

### Column Descriptions:

   ><font color=blue> **Administrative** : This is the number of pages of this type (administrative) that the user visited.

   ><font color=blue>**Administrative_Duration**: This is the amount of time spent in this category of pages.

   ><font color=blue>**Informational**: This is the number of pages of this type (informational) that the user visited.

   ><font color=blue>**Informational_Duration**: This is the amount of time spent in this category of pages.

   ><font color=blue>**ProductRelated**: This is the number of pages of this type (product related) that the user visited.

   ><font color=blue>**ProductRelated_Duration**: This is the amount of time spent in this category of pages.

   ><font color=blue>**BounceRates**: The percentage of visitors who enter the website through that page and exit without triggering any additional tasks.

   ><font color=blue>**ExitRates**: The percentage of pageviews on the website that end at that specific page.

   ><font color=blue>**PageValues**: The average value of the page averaged over the value of the target page and/or the completion of an eCommerce transaction. More information about how this is calculated

   ><font color=blue>**SpecialDay**: This value represents the closeness of the browsing date to special days or holidays (eg Mother's Day or Valentine's day) in which the transaction is more likely to be finalized. More information about how this value is calculated below.

   ><font color=blue>**Month**: Contains the month the pageview occurred, in string form.

   ><font color=blue>**OperatingSystems**: An integer value representing the operating system that the user was on when viewing the page.

   ><font color=blue>**Browser**: An integer value representing the browser that the user was using to view the page.

   ><font color=blue>**Region**: An integer value representing which region the user is located in.

   ><font color=blue>**TrafficType**: An integer value representing what type of traffic the user is categorized into. Read more about traffic types here.

   ><font color=blue>**VisitorType**: A string representing whether a visitor is New Visitor, Returning Visitor, or Other.

   ><font color=blue>**Weekend**: A boolean representing whether the session is on a weekend.

   ><font color=blue>**Revenue**: A boolean representing whether or not the user completed the purchase.















































