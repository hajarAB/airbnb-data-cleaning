# Airbnb NYC Dataset Cleaning & Analysis (2019) [Python]

## 1️⃣ Project Context

This project focuses on cleaning and analyzing the **New York City Airbnb Open Data (2019)** dataset.  
The goal is to demonstrate strong Python skills in **data cleaning, feature engineering, and exploratory data analysis (EDA)**.

The dataset contains approximately **48,895 listings** with **16 columns**, including:
- `price`, `minimum_nights`, `number_of_reviews`, `reviews_per_month`, `availability_365`
- `neighbourhood_group`, `neighbourhood`, `room_type`
- `host_id`, `host_total_listings`, etc.

---

## 2️⃣ Project Objectives

- Clean the dataset (missing values, outliers, data types)
- Create **business-oriented features** for analysis or machine learning
- Perform **exploratory data analysis (EDA) with visualizations**
- Prepare a dataset ready for analysis or modeling

---

## 3️⃣ Project Steps

### a. Structural Cleaning
- Column renaming using `snake_case`
- Removal of irrelevant columns (`name`, `host_name`)
- Data type correction (`last_review` → datetime)
- Duplicate detection and removal

### b. Missing Values Handling
- `reviews_per_month`: missing values replaced with `0`
- `last_review`: missing values kept (business-relevant information)
- Creation of `has_reviews` feature to indicate whether a listing has reviews

### c. Outlier Treatment
- `price`: filtered between **$10 and $1000**
- `minimum_nights`: filtered between **1 and 365**
- `availability_365`: kept as is

### d. Feature Engineering
- `host_total_listings`: number of listings per host
- `host_is_professional`: host with more than one listing
- `avg_price_neighbourhood`: average price per neighborhood
- `availability_pct`: annual availability percentage
- `reviews_per_month_scaled`: normalized reviews metric
- One-hot encoding for `room_type`
- Rounded latitude and longitude for visual clustering

### e. Exploratory Data Analysis (EDA)
- Price distribution by room type
- Average price by neighborhood
- Number of listings per host
- Relationship between price and number of reviews
- Simplified NYC listings map
- Distribution of `minimum_nights` (log scale)

---

## 5️⃣ Technologies Used

- Python 3.x
- Pandas / NumPy (data manipulation)
- Matplotlib / Seaborn (data visualization)
- Jupyter Notebook (analysis & documentation)

---

## 6️⃣ Key Insights

- Most hosts own a single listing → mainly casual hosts
- Manhattan is the most expensive and densest area
- Entire homes/apartments are generally more expensive than private rooms
- Very expensive listings often have few reviews → business logic consistency
- `minimum_nights` distribution shows most listings target short stays

---

### 📊 Some Key Exploratory Visualizations

- **Distribution of Airbnb prices  NYC**
   <img src="images/Distribution of Airbnb prices  NYC.png"
     width="900"/>
     
- **Minimum Stay Distribution (Log Scale)**
 <img src="images/Distribution of Minimum Nights (Log Scale).png"
     width="900"/>
     
- **Monthly Review Activity per Listing**
 <img src="images/Reviews per Month.png"
     width="900"/>
     
- **Average Airbnb Prices by Neighborhood**
 <img src="images/Average Price by Neighborhood.png"
     width="900"/>

- **Geographical Distribution of Airbnb Listings Across NYC**
  <img src="images/Distribution of Airbnb Listings in NYC by Neighbourhood.png"
     width="900"/>

