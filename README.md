# Big Data Analytics & Predictive Intelligence

## E-Commerce Sales Analytics & Predictive Intelligence

This project is developed as part of the Cognevance Technologies Data Science & Data Analytics Level 3 project.

The project focuses on analyzing a large-scale e-commerce sales dataset, performing data preprocessing and feature engineering, conducting SQL and Python-based analysis, building machine learning models for predictive analytics, and creating an interactive Power BI dashboard.

## Project Objectives

- Analyze a large-scale e-commerce sales dataset.
- Perform data preprocessing and feature engineering.
- Perform business analysis using SQL.
- Perform data analysis using Python.
- Build machine learning models for predictive analytics.
- Compare Linear Regression and Random Forest models.
- Evaluate model performance using MAE, RMSE, and R² Score.
- Analyze customer behavior and sales trends.
- Create an interactive Power BI dashboard.
- Generate business insights and recommendations.
- Document the complete project workflow.

---

## Dataset

The project uses a large-scale e-commerce sales dataset containing **100,000 transaction records**.

The dataset includes information related to:

- Order ID
- Product Name
- Category
- Price
- Quantity
- Total Sales
- Customer ID
- Customer Age
- Customer Gender
- Purchase Date
- Purchase Time

The dataset is stored in:

```text
Dataset/ecommerce_sales_data.csv

Technologies Used
Programming Language
Python
Data Analysis
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Database and SQL
SQLite
SQL
Machine Learning
Scikit-learn
Linear Regression
Random Forest
Business Intelligence
Microsoft Power BI
Development Environment
Visual Studio Code
Jupyter Notebook


### Then:

Press **Ctrl + S** 💾

### Check your README

It should now have:

```text
# Big Data Analytics & Predictive Intelligence

## E-Commerce Sales Analytics & Predictive Intelligence

Project Objectives
        ↓
Dataset
        ↓
Technologies Used

---

## Project Architecture & Workflow

The project follows a complete analytics and predictive intelligence workflow:

```text
E-Commerce Sales Dataset
          ↓
Data Loading
          ↓
Data Preprocessing
          ↓
Feature Engineering
          ↓
     ┌────┴────┐
     ↓         ↓
Python      SQL Analysis
Analysis
     └────┬────┘
          ↓
Machine Learning
          ↓
   ┌──────┴──────┐
   ↓             ↓
Linear        Random
Regression    Forest
   └──────┬──────┘
          ↓
Model Evaluation
     MAE / RMSE / R²
          ↓
Sales Prediction
          ↓
Power BI Dashboard
          ↓
Business Insights
          ↓
Recommendations

---

## SQL Analysis

SQL was used to perform business-oriented analysis on the e-commerce sales data.

The dataset was loaded into a SQLite database for querying and analysis.

### SQL Database

Database:

```text
SQL/ecommerce_sales.db

---

## SQL Analysis

SQL was used to perform business-oriented analysis on the e-commerce sales data.

The dataset was loaded into a SQLite database for querying and analysis.

### SQL Database

Database:

```text
SQL/ecommerce_sales.db

---

## Machine Learning & Predictive Analytics

Machine learning models were developed to perform predictive analytics on the e-commerce sales data.

The following models were implemented:

- Linear Regression
- Random Forest Regressor

### Model Features

The predictive models use relevant numerical and engineered features from the dataset to learn patterns in sales behavior.

### Model Training

The dataset was divided into training and testing data.

The training data was used to train the machine learning models, while the testing data was used to evaluate their performance on unseen data.

### Model Evaluation

The models were evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Comparison

The performance of Linear Regression and Random Forest was compared using the evaluation metrics.

The model comparison results are stored in:

```text
Model/model_comparison_results.csv

---

## Power BI Interactive Dashboard

An interactive Power BI dashboard was created to visualize the e-commerce business performance and predictive analytics results.

### Dashboard Features

The dashboard includes:

- Total Sales KPI
- Total Orders KPI
- Total Customers KPI
- Total Quantity Sold KPI
- Monthly Sales Trend
- Yearly Sales Trend
- Sales by Category
- Sales by Customer Gender
- Sales by Customer Age Group
- Top 10 Products by Sales
- Actual vs Predicted Sales
- Model RMSE Comparison
- Model R² Score Comparison
- Random Forest Feature Importance
- Interactive Category filtering
- Interactive Customer Gender filtering
- Purchase Date filtering

### Dashboard Data

The dashboard uses prepared data files stored in:

```text
Dashboard/Data/

---

## Business Insights

The analysis of the e-commerce dataset provides the following business insights:

- Sales performance can be monitored using overall sales and quantity KPIs.
- Monthly and yearly sales analysis helps identify important sales trends.
- Category-wise analysis helps understand product category performance.
- Customer gender and age-group analysis provides insights into customer behavior.
- Top-selling products can be identified for better product planning.
- Actual versus predicted sales helps assess the performance of the forecasting models.
- Feature importance helps identify the variables that contribute to model predictions.
- SQL analysis provides additional business-oriented insights from the dataset.

## Business Recommendations

Based on the analysis, the following recommendations are proposed:

1. **Inventory Planning**  
   Use sales trends and predictions to maintain appropriate inventory levels.

2. **Product Management**  
   Give greater attention to high-performing product categories and products.

3. **Customer Analysis**  
   Use customer demographic information to understand purchasing behavior.

4. **Marketing Planning**  
   Use sales trends and customer insights to support targeted marketing campaigns.

5. **Sales Forecasting**  
   Use the predictive model to support future sales and inventory planning.

6. **Performance Monitoring**  
   Regularly monitor business KPIs through the Power BI dashboard.

7. **Data-Driven Decision Making**  
   Combine SQL analysis, machine learning predictions, and dashboard insights to support business decisions.

   ---

## Project Structure

```text
Big Data Analytics & Predictive Intelligence/
│
├── Dataset/
│   └── ecommerce_sales_data.csv
│
├── SQL/
│   ├── load_data_to_sql.py
│   ├── run_sql_analysis.py
│   └── ecommerce_sales.db
│
├── Model/
│   ├── predictive_model.py
│   ├── model_comparison.py
│   ├── model_comparison_results.csv
│   ├── prediction_results.csv
│   ├── feature_importance.py
│   └── feature_importance.csv
│
├── Charts/
│   ├── monthly_sales.png
│   ├── yearly_sales.png
│   ├── category_sales.png
│   ├── prediction_vs_actual.png
│   └── feature_importance.png
│
├── Dashboard/
│   ├── dashboard_data.py
│   └── Data/
│       ├── dashboard_sales_data.csv
│       ├── model_comparison_results.csv
│       ├── prediction_results.csv
│       └── feature_importance.csv
│
├── README.md
└── requirements.txtV