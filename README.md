#  ECommerce-Customer-Churn-Analysis
## Project Overview

This project performs Exploratory Data Analysis (EDA) and preliminary preprocessing on an E-commerce Customer Churn dataset to understand the factors influencing customer churn. The goal is to identify behavioral patterns and variables that contribute to customers leaving the platform.

Customer churn is a critical problem for online businesses because retaining existing customers is significantly cheaper than acquiring new ones. Through visualization and statistical analysis, this project aims to uncover insights that can help businesses improve customer retention strategies.

## 🎯 Objectives

1. Analyze customer behavior patterns in an e-commerce platform.

2. Identify factors that influence customer churn.

3. Perform data cleaning and preprocessing for reliable analysis.

4. Use data visualization techniques to reveal meaningful trends.

5. Prepare the dataset for future predictive modeling.

## 📊 Dataset Features

The dataset contains customer attributes related to their purchasing behavior and experience with the platform.

1. Tenure – Duration of customer relationship

2. WarehouseToHome – Distance between warehouse and customer

3. NumberOfDeviceRegistered – Devices used by the customer

4. PreferedOrderCat – Preferred order category

5. SatisfactionScore – Customer satisfaction rating

6. MaritalStatus

7. NumberOfAddress

8. Complain – Whether the customer filed complaints

9. DaySinceLastOrder – Recency of last purchase

10. CashbackAmount

11. Churn – Target variable indicating whether the customer left

## 🛠️ Tech Stack

### Programming Language

Python

### Libraries Used

1. Pandas – Data manipulation

2. NumPy – Numerical operations

3. Matplotlib – Data visualization

4. Seaborn – Advanced statistical plots

5. Scikit-learn – Machine learning preparation

### Development Environment
Jupyter Notebook

## 💡 Skills Demonstrated

This project showcases the following data analytics skills:

1. Data Cleaning

2. Handling Missing Values

3. Exploratory Data Analysis (EDA)

4. Data Visualization

5. Feature Understanding

6. Outlier Detection

7. Dataset Preparation for Machine Learning

8. Python Data Analysis Workflow

## 🧹 Data Preprocessing

Several preprocessing techniques were applied to prepare the dataset for analysis.

### Handling Missing Values

  1. Median imputation was used for numerical columns

  2. Remaining null values were removed where necessary.

### Data Preparation

1. Dataset converted into a structured Pandas DataFrame

2. Variables separated into numerical and categorical features

3. Data prepared for visualization and modeling


## 📈 Exploratory Data Analysis (EDA)

Multiple visualization techniques were used to understand the data distribution and relationships between variables.

1️⃣ Churn Distribution

Pie chart showing percentage of customers retained vs churned.

2️⃣ Category vs Churn

Count plots comparing churn across Preferred order categories or Marital status groups

3️⃣ Customer Satisfaction Analysis

Pie chart showing distribution of satisfaction scores.

4️⃣ Complaint Impact

Stacked bar chart analyzing the relationship between customer complaints and churn.

5️⃣ Outlier Detection

Boxplots used to inspect numerical variables such as:

1. Tenure

2. Warehouse distance

3. Days since last order

6️⃣ Behavioral Patterns

1. KDE plots used to analyze recency vs churn behavior.

2. Scatter plots used to visualize relationships such as DaySinceLastOrder vs CashbackAmount

7️⃣ Category Churn Heatmap

Heatmap visualization to identify which product categories have higher churn rates.

## 🔍 Key Findings/Insights

Some important patterns observed from the analysis:

1. Customers with higher recency (long time since last order) show higher churn probability.

2. Customer complaints strongly correlate with churn.

3. Certain product categories have noticeably higher churn rates.

4. Customer satisfaction scores influence retention.

5. Customers receiving higher cashback incentives show different purchasing behaviors.

These insights highlight the importance of customer experience, incentives, and engagement in preventing churn.

## 🤖 Machine Learning Preparation

The dataset was prepared for predictive modeling by:

1. Separating features (X) and target variable (y).

2. Performing train-test split using sklearn.

3. Identifying variables suitable for outlier removal and model training.

Future versions of this project will include machine learning models to predict churn probability.

## 🚀 Future Improvements

Planned enhancements for this project include:

### Implement machine learning models such as:

1. Logistic Regression

2. Random Forest

3. Gradient Boosting

### Feature engineering

### Model evaluation using:

1. Accuracy

2. ROC-AUC

3. Precision & Recall

### Building a customer churn prediction dashboard

## 📌 Conclusion

This analysis provides valuable insights into customer churn behavior in an e-commerce environment. By understanding factors such as customer satisfaction, complaints, purchase recency, and order categories, businesses can design better strategies to improve retention and customer experience.

## 📈 Project Status

🚧 Work in Progress  
Future updates will include machine learning models for churn prediction.
