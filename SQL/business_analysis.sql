-- Big Data Analytics & Predictive Intelligence
-- SQL Business Analysis


-- 1. Total Sales
SELECT 
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data;


-- 2. Total Quantity Sold
SELECT 
    SUM(Quantity) AS Total_Quantity
FROM ecommerce_sales_data;


-- 3. Total Orders
SELECT 
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM ecommerce_sales_data;


-- 4. Total Customers
SELECT 
    COUNT(DISTINCT "Customer ID") AS Total_Customers
FROM ecommerce_sales_data;


-- 5. Sales by Category
SELECT 
    Category,
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 6. Sales by Gender
SELECT 
    "Customer Gender",
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY "Customer Gender"
ORDER BY Total_Sales DESC;


-- 7. Sales by Year
SELECT 
    EXTRACT(YEAR FROM "Purchase Date") AS Year,
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY EXTRACT(YEAR FROM "Purchase Date")
ORDER BY Year;


-- 8. Top 10 Products
SELECT 
    "Product Name",
    SUM("Total Sales") AS Total_Sales
FROM ecommerce_sales_data
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;


-- 9. Customer Total Spending
SELECT 
    "Customer ID",
    SUM("Total Sales") AS Total_Spending
FROM ecommerce_sales_data
GROUP BY "Customer ID"
ORDER BY Total_Spending DESC
LIMIT 10;


-- 10. Average Order Value
SELECT 
    AVG("Total Sales") AS Average_Order_Value
FROM ecommerce_sales_data;