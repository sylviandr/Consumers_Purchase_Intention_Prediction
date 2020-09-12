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

- Data Cleaning (Handle Missing Value and Outlier)
- Exploratory Data Analysis
- Modelling Machine Learning Algorithm to Make Classification for Revenue generating or not, based on features that provide in this dataset.

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

## SECTION 2 - Exploratory Data Analysis

***The goal of this section is to understands and analyze consumers' behavior to predict Revenue Generated or not from Customer's Online Purchasing from E-Commerce.*** 

We have to analyze each feature, especially each feature against our target variable, Revenue. So, we can find out and predict what features can provide the potential for greater revenue due to the final consumer decision to make a product purchase.

## SECTION 3 - MACHINE LEARNING MODEL BUILDING

***The goal of this section is to build and selecting the best model to predict Revenue Generated or Not from Customer's Online Purchasing from E-Commerce.*** 

In order to achieve this goal, we will be focusing on searching the best model using some conditions below : 

- First, we split the data into 80% Train data and then we split the data into 90% Train data.


- Then we scale the data so that the're having the same scale.


- In each attempts we will be conducting the Logistic Regression, Random Forrest Classifier, Decision Tree Classifier and KNearest Neighbors Models.


- Also we try to do the hyperparameter tuning then compare it between it's default models.


- In last part we compare the result between models to achieve our goals.

### MODEL SUMMARY

>Now, we will summarize our findings. But before that, we must answer the question I mentioned before. 
What is a Confusion Matrix ? What does it implies ? A confusion matrix is simply a table that is often used to describe the performance of a classification model on a set of test data. 

> Let's now define the most basic terms in this matrix :

> - True Positives (TP): Cases in which are predicted as *positives* and in reality are also *positives*.


> - True Negatives (TN): Cases in which are predicted as *negatives* and in reality are also *negatives*.


> - False Positives (FP): Cases in which are predicted as *positives*, but in reality are *negatives*.


> - False Negatives (FN): Cases in which are predicted as *negatives*, but in reality are *positives*.

> This is a list of rates that are often computed from a confusion matrix for a binary classifier:

> - Accuracy : Overall, how often is the classifier correct?


> - Recall : When it's actually true, how often does it predict as true ?


> - Precision : When it predicts true, how often is it correct ?

### DASHBOARD

#### HOME

<img width="1440" alt="Screen Shot 2020-09-12 at 18 34 28" src="https://user-images.githubusercontent.com/61573559/92994801-b48eab80-f527-11ea-8bea-77c16c4e3328.png">

#### Data Visualization

<img width="1440" alt="Screen Shot 2020-09-12 at 18 34 57" src="https://user-images.githubusercontent.com/61573559/92994946-1b609480-f529-11ea-9800-a563867fdf8e.png">

<img width="1440" alt="Screen Shot 2020-09-12 at 18 35 39" src="https://user-images.githubusercontent.com/61573559/92994978-5bc01280-f529-11ea-9d0f-0b5849b08a1d.png">

#### Dataset

<img width="1440" alt="Screen Shot 2020-09-12 at 18 36 08" src="https://user-images.githubusercontent.com/61573559/92995008-b6f20500-f529-11ea-8410-44a751a9f27d.png">

#### Prediction

<img width="1440" alt="Screen Shot 2020-09-12 at 18 36 30" src="https://user-images.githubusercontent.com/61573559/92995050-fb7da080-f529-11ea-9f65-74085e2b9416.png">

<img width="1440" alt="Screen Shot 2020-09-12 at 18 36 35" src="https://user-images.githubusercontent.com/61573559/92995087-4d262b00-f52a-11ea-9cbd-2332a48f3d0b.png">

#### Result

<img width="1440" alt="Screen Shot 2020-09-12 at 18 37 22" src="https://user-images.githubusercontent.com/61573559/92995129-b3ab4900-f52a-11ea-8cfa-913cfac44a44.png">









































