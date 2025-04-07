Amazon Sales Data Cleaning and Preprocessing

Project Overview

This project focuses on cleaning and preprocessing Amazon sales data to ensure it is structured, consistent, and ready for further analysis. The dataset may contain missing values, duplicates, inconsistent formats, and other issues that need to be addressed before conducting data analysis or building predictive models.

Dataset Description

The dataset includes Amazon sales records with the following attributes:

Order ID: Unique identifier for each order

Product Name: Name of the product

Category: Product category

Price: Price of the product

Quantity Sold: Number of units sold

Revenue: Total revenue generated (Price * Quantity Sold)

Customer ID: Unique identifier for each customer

Order Date: Date the order was placed

Shipping Address: Customer's shipping address

Order Status: Status of the order (Shipped, Pending, Cancelled, etc.)


Data Cleaning Steps

The following steps will be performed to clean the dataset:

1. Handling Missing Values: Identify and address missing values in key columns.


2. Removing Duplicates: Check for and remove duplicate records.


3. Standardizing Formats: Convert date formats, fix inconsistent text formatting, and standardize categorical values.


4. Handling Outliers: Detect and remove or adjust extreme values in numeric columns.


5. Correcting Data Types: Convert columns to appropriate data types (e.g., dates, numbers, categorical values).


6. Addressing Inconsistencies: Normalize variations in product names, categories, and order statuses.


7. Generating New Features: Create additional relevant features such as profit margins, customer purchase frequency, etc.



Preprocessing Steps

Once the data is cleaned, the following preprocessing steps will be performed:

1. Encoding Categorical Data: Convert categorical variables into numerical formats (e.g., one-hot encoding).


2. Feature Scaling: Normalize or standardize numerical features if needed.


3. Splitting Data: Divide the dataset into training and testing sets for modeling purposes.



Tools & Libraries Used

Python (pandas, numpy, matplotlib, seaborn, sklearn)

Jupyter Notebook for code execution and visualization


How to Use

1. Clone this repository:

git clone https://github.com/yourusername/amazon-sales-cleaning.git


2. Navigate to the project directory:

cd amazon-sales-cleaning


3. Install required dependencies:

pip install -r requirements.txt


4. Run the data cleaning script:

python clean_data.py


5. Explore the cleaned dataset for further analysis or modeling.



