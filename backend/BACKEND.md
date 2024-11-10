TODOS: 
-add how problems solving down in readme, encoder
-add github of nika 
-CHECK DATA VISUALIZATION 

# Project Title: Personalization by culture and personality 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Use Case](#usecase)
- [Problems](#problems)
- [PDF_Report](#pdfreport)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [Data set](#dataset)

## Introduction
Welcome to the Backend ReadMe file for the Eternals' 4th Challenge: Personalization by Culture and Personality.

Every year, millions of tourists from around the world visit Austria. Our goal is to enhance their experience by making data-driven assumptions about their preferences. To tackle this exciting challenge, we will employ machine learning techniques, specifically using Collaborative Filtering with Singular Value Decomposition (SVD).

Before diving into the modeling, we'll thoroughly investigate our dataset, perform data visualization to gain initial insights, and ensure the data is properly cleaned.

Our ultimate aim is to provide an API endpoint for the Frontend Team, enabling data-driven decisions for each individual user to be accessed through the web application.


## Use Case 
Here's how to handle the files:

1. **app.py**: app.py is the API-access point for our backend code..

2. **collab_filt_svd.py**: In this file, we provide a class that performs collaborative filtering using singular value decomposition.

3. **data_loader.py**: This file is solely to provide access for the dataset. In this case, we use prepared_data.csv.

4. **data_prep.py**: In this file, we are cleaning the data, removing empty columns/features, and merging similar inputs for event_name.

5. **data_visualization.py**: The name says it all: This file is about visualizing the data. We plotted several graphs. However, the dataset is not that big and hence, a lot of plots are not suitable as there are just too few datapoints.

6. **original_data.csv**: This is the csv file for the originally provided data.

7. **prepared_data.csv**: This is our ready data set that we used for our algorithm. 

## Challenges

In any project of this nature, unforeseen problems are bound to arise. It was crucial for us to face these issues head-on and find solutions tailored to our specific needs. Here’s how we addressed the main challenges:

- **Sparse Features**: Our dataset contained numerous "empty" features that were not relevant to our problem. We tackled this by thoroughly cleaning the data, removing the sparse columns, and focusing only on the features that were pertinent.

- **Small Dataset**: More data is always preferable for machine learning tasks. However, our dataset was relatively small, with around 250 data points after cleaning. To enhance the reliability of our algorithm, we upsampled the training data.

- **Unbalanced Dataset**: The dataset was highly imbalanced, with approximately 85% of the data points representing Austria, while other countries were significantly underrepresented. We used SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset.

- **Event Names**: Our target feature, the event names, often referred to the same or similar events but were written differently. To address this, we encoded the event names and merged similar events, ensuring consistency in our data.


## PDF_Report 
In the following we will provide some pdf files and their explaination. 
- **Pie Chart: New and Returning Tourists**: fill
   You can view the PDF [here](./PDF/pie_chart_new_return.pdf).
- **Pie Chart: New and Returning Tourists**: fill
   You can view the PDF [here](./PDF/pie_chart_new_return.pdf).
- **Pie Chart: New and Returning Tourists**: fill
   You can view the PDF [here](./PDF/pie_chart_new_return.pdf).
- **Pie Chart: New and Returning Tourists**: fill
   You can view the PDF [here](./PDF/pie_chart_new_return.pdf).

## Technologies Used
- **Python** 
- **Pandas**         (Dataframe)
- **Scikit-learn** 
   - **Surprise**    (for collaborative filtering)
- **Matplotlib**     (for data visualization)
- **Seaborn**        (for data visualization)
- **Squarify**       (for data visualization-Tree Map)
- **Flask**          (for API)
- **Pickle**         (for API (loading ml-algorithms))

## Contributors
- **Eternals** - GitHub_Repository: `https://github.com/denishotii/TourismTechnologyFestival`

- **Jakub Wisniewski** - GitHub: `D3prave`
- **Lukas Lang** - GitHub: `GezaLang`
- **Ali Guliyev** - GitHub: `fill that`
- **Southik Nath Banerjee** - GitHub: `Southik Nath Banerjee`
- **Veronika Rybak** - GitHub: `CoraEpiro`
- **Denis Hoti** - GitHub: `denishotii`


## Data set 
The original data set was published by the organisators of the Tourism Technology Hackathon 2024 on a privat basis. We promise to delete the data set after the 10.11.2024.  
################

