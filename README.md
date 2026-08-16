# Big Data Analytics & Predictive Intelligence

## E-Commerce Sales Analytics & Predictive Intelligence

This project is developed as part of the Cognevance Technologies Data Science & Data Analytics Level 3 project.

The project focuses on analyzing a large-scale e-commerce sales dataset, performing data preprocessing and feature engineering, conducting SQL and Python-based analysis, building machine learning models for predictive analytics, and creating an interactive Power BI dashboard.

---

# 1. Project Objectives

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

# 2. Dataset

The project uses a large-scale e-commerce sales dataset containing **100,000 transaction records**.

### Dataset Features

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

### Dataset Location

```text
Dataset/ecommerce_sales_data.csv

3. Technologies Used
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
Random Forest Regressor
Business Intelligence
Microsoft Power BI
Development Environment
Visual Studio Code
Jupyter Notebook
4. Project Architecture & Workflow
The project follows a complete analytics and predictive intelligence workflow:

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

## Workflow Steps
Data Loading – Load the e-commerce dataset.
Data Preprocessing – Clean and prepare the dataset.
Feature Engineering – Prepare useful features for analysis and modeling.
Python Analysis – Perform data analysis and visualization using Python.
SQL Analysis – Perform business-oriented analysis using SQLite and SQL.
Machine Learning – Implement Linear Regression and Random Forest.
Model Evaluation – Evaluate models using MAE, RMSE, and R² Score.
Sales Prediction – Generate predicted sales results.
Power BI Dashboard – Present KPIs, trends, customer behavior, and predictions.
Business Insights – Identify important patterns and trends.
Recommendations – Generate data-driven business recommendations.
5. Data Preprocessing

The following preprocessing activities were performed:

Loaded the dataset using Pandas.
Checked the number of rows and columns.
Examined dataset structure and data types.
Checked for missing values.
Checked for duplicate records.
Converted date columns into appropriate formats.
Prepared numerical and categorical features.
Created useful features for analysis.
Prepared the data for machine learning.
6. Feature Engineering

Feature engineering was performed to prepare useful variables for analytics and predictive modeling.

Relevant information from product, customer, price, quantity, sales, purchase date, and purchase time was prepared for analysis and machine learning.

7. Exploratory Data Analysis

Python was used to explore the e-commerce dataset and understand business patterns.

The analysis includes:

Sales analysis
Category analysis
Customer analysis
Age-group analysis
Gender analysis
Monthly sales trends
Yearly sales trends
Top product analysis
8. SQL Business Analysis

SQL was used to perform business-oriented analysis on the e-commerce sales data.

The dataset was loaded into a SQLite database for querying and analysis.

SQL Database
SQL/ecommerce_sales.db
SQL Files
SQL/business_analysis.sql
SQL/load_data_to_sql.py
SQL/run_sql_analysis.py
SQL Analysis Includes
Total sales calculation
Category-wise sales analysis
Customer-related analysis
Quantity analysis
Business-oriented queries
9. Machine Learning & Predictive Analytics

Machine learning models were developed to perform predictive analytics on the e-commerce sales data.

Models Implemented
Linear Regression
Random Forest Regressor
Model Training

The dataset was divided into training and testing data.

The training data was used to train the machine learning models, while the testing data was used to evaluate their performance on unseen data.

Model Evaluation Metrics

The models were evaluated using:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score
Model Comparison

The performance of Linear Regression and Random Forest was compared using the evaluation metrics.

Results are stored in:

Model/model_comparison_results.csv
10. Sales Prediction

The machine learning model was used to generate predicted sales values.

Prediction results are stored in:

Model/prediction_results.csv

The prediction results contain:

Actual Sales
Predicted Sales
Prediction Error
11. Feature Importance

Random Forest feature importance was analyzed to identify the features contributing to model predictions.

The results are stored in:

Model/feature_importance.csv

Visualization:

Charts/feature_importance.png
12. Data Visualizations

The project includes the following visualizations.

Monthly Sales
Charts/monthly_sales.png
Yearly Sales
Charts/yearly_sales.png
Category Sales
Charts/category_sales.png
Actual vs Predicted Sales
Charts/prediction_vs_actual.png
Feature Importance
Charts/feature_importance.png
13. Power BI Interactive Dashboard

An interactive Power BI dashboard was created to visualize e-commerce business performance and predictive analytics results.

Dashboard KPIs
Total Sales
Total Orders
Total Customers
Total Quantity Sold
Dashboard Visualizations
Monthly Sales Trend
Yearly Sales Trend
Sales by Category
Sales by Customer Gender
Sales by Customer Age Group
Top 10 Products by Sales
Actual vs Predicted Sales
Model RMSE Comparison
Model R² Score Comparison
Random Forest Feature Importance
Interactive Filters
Category
Customer Gender
Purchase Date
Dashboard Data

Prepared dashboard data is stored in:

Dashboard/Data/
14. Business Insights

The analysis provides the following business insights:

Sales performance can be monitored using overall sales and quantity KPIs.
Monthly and yearly sales analysis helps identify important sales trends.
Category-wise analysis helps understand product category performance.
Customer gender and age-group analysis provides insights into customer behavior.
Top-selling products can be identified for better product planning.
Actual versus predicted sales helps assess predictive model performance.
Feature importance helps identify variables contributing to model predictions.
SQL analysis provides additional business-oriented insights.
15. Business Recommendations

Based on the analysis, the following recommendations are proposed.

1. Inventory Planning

Use sales trends and predictions to maintain appropriate inventory levels.

2. Product Management

Give greater attention to high-performing product categories and products.

3. Customer Analysis

Use customer demographic information to understand purchasing behavior.

4. Marketing Planning

Use sales trends and customer insights to support targeted marketing campaigns.

5. Sales Forecasting

Use predictive results to support future sales and inventory planning.

6. Performance Monitoring

Regularly monitor business KPIs through the Power BI dashboard.

7. Data-Driven Decision Making

Combine SQL analysis, machine learning predictions, and dashboard insights to support business decisions.

16. Project Structure
Big Data Analytics & Predictive Intelligence/
│
├── Dataset/
│   └── ecommerce_sales_data.csv
│
├── SQL/
│   ├── business_analysis.sql
│   ├── load_data_to_sql.py
│   ├── run_sql_analysis.py
│   └── ecommerce_sales.db
│
├── Model/
│   ├── predictive_model.py
│   ├── model_comparison.py
│   ├── feature_importance.py
│   ├── model_comparison_results.csv
│   ├── prediction_results.csv
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
│
├── Notebook/
│   └── level3_analysis.ipynb
│
├── Report/
│   └── Big_Data_Analytics_Predictive_Intelligence_Report.docx
│
├── README.md
└── requirements.txt
17. How to Run the Project
Step 1 – Install Required Libraries
pip install -r requirements.txt
Step 2 – Load Dataset into SQLite
python SQL/load_data_to_sql.py
Step 3 – Run SQL Analysis
python SQL/run_sql_analysis.py
Step 4 – Run Machine Learning
python Model/predictive_model.py
Step 5 – Run Model Comparison
python Model/model_comparison.py
Step 6 – Prepare Dashboard Data
python Dashboard/dashboard_data.py
Step 7 – Open Power BI

Open Power BI Desktop and load the prepared files from:

Dashboard/Data/
18. Limitations
Prediction performance depends on the quality of the available dataset.
External factors such as market conditions and promotions are not included.
Customer behavior may change over time.
The current models may not capture every complex relationship in e-commerce sales.
Model performance depends on feature quality and data distribution.
19. Future Enhancements
Implement advanced time-series forecasting.
Explore seasonal sales patterns.
Add more customer behavior features.
Include external business factors.
Compare additional machine learning algorithms.
Perform hyperparameter tuning.
Develop more advanced Power BI dashboards.
Deploy the predictive model as a web application.
Implement automated data pipelines.
Explore distributed big-data technologies for larger datasets.
20. Conclusion

The E-Commerce Sales Analytics & Predictive Intelligence project demonstrates a complete data analytics and predictive intelligence pipeline.

The project uses a 100,000-record e-commerce dataset and applies data preprocessing, feature engineering, Python analytics, SQL business analysis, machine learning, predictive analytics, and Power BI visualization.

Linear Regression and Random Forest models were implemented and evaluated using MAE, RMSE, and R² Score.

The Power BI dashboard provides an interactive view of business KPIs, sales trends, customer behavior, product performance, model performance, and prediction results.

The project demonstrates how data analytics and machine learning can transform raw e-commerce data into useful business insights and support data-driven decision-making.

21. References
Python Documentation
Pandas Documentation
NumPy Documentation
Matplotlib Documentation
Seaborn Documentation
Scikit-learn Documentation
SQLite Documentation
Microsoft Power BI Documentation