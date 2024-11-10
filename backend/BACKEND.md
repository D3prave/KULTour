# Project Title: Personalization by culture and personality 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Use Case](#usecase)
- [Challenges](#challenges)
- [PNG_Report](#pdfreport)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [Data set](#dataset)

## Introduction
Welcome to the Backend ReadMe file for the Eternals' 4th Challenge: Personalization by Culture and Personality.

Every year, millions of tourists from around the world visit Austria. Our goal is to enhance their experience by making data-driven assumptions about their preferences. To tackle this exciting challenge, we will employ machine learning techniques, specifically using Collaborative Filtering with Singular Value Decomposition (SVD).

Before diving into the modeling, we'll thoroughly investigate our dataset, perform data visualization to gain initial insights, and ensure the data is properly cleaned.

Our ultimate aim is to provide an API endpoint for the Frontend Team, enabling data-driven decisions for each individual user to be accessed through the web application.


## Use Case

Here's a guide on how to handle the various files in our project:

1. **app.py**: 
   This file serves as the API access point for our backend code. It handles requests and directs them to the appropriate functions.

2. **collab_filt_svd.py**: 
   This file contains a class that performs collaborative filtering using Singular Value Decomposition (SVD). It is the core of our recommendation system.

3. **data_loader.py**: 
   The primary purpose of this file is to provide access to the dataset, specifically `prepared_data.csv`. While it was intended to be used in multiple files such as `collab_filt_svd.py` and `data_prep.py`, it ended up being primarily utilized in `data_visualization.py`. Although we could have managed without it, our focus was on addressing more critical tasks.

4. **data_prep.py**: 
   This script is responsible for cleaning the data. It removes empty columns and features, and merges similar inputs for the `event_name` column to ensure consistency and accuracy in our dataset.

5. **data_visualization.py**: 
   As the name suggests, this file is dedicated to visualizing the data. We plotted several graphs to gain insights. However, due to the small size of the dataset, many plots are limited in their usefulness.

6. **original_data.csv**: 
   This is the CSV file containing the originally provided data. It serves as the raw data source before any preprocessing.

7. **prepared_data.csv**: 
   This is the cleaned and preprocessed dataset that we use for our algorithms. It is the final version of the data after all transformations.

8. **requirements.txt**: 
   This file lists the dependencies required for the API. It ensures that all necessary libraries are installed for the project to run smoothly.

## Challenges

In any project of this nature, unforeseen problems are bound to arise. It was crucial for us to face these issues head-on and find solutions tailored to our specific needs. Here’s how we addressed the main challenges:

- **Sparse Features**: Our dataset contained numerous "empty" features that were not relevant to our problem. We tackled this by thoroughly cleaning the data, removing the sparse columns, and focusing only on the features that were pertinent.

- **Small Dataset**: More data is always preferable for machine learning tasks. However, our dataset was relatively small, with around 250 data points after cleaning. To enhance the reliability of our algorithm, we upsampled the training data.

- **Unbalanced Dataset**: The dataset was highly imbalanced, with approximately 85% of the data points representing Austria, while other countries were significantly underrepresented. 

- **Event Names**: Our target feature, the event names, often referred to the same or similar events but were written differently. To address this, we encoded the event names and merged similar events, ensuring consistency in our data.


## PNG_Report 
In the following we will provide some pdf files and their explaination. 
- **Plot after rebalancing the data**: [here](./PNG/after.png).

- **Plot before rebalancing the data**:[here](./PNG/before.png).

- **Demographic Map of the Datapoints**:[here](./PNG/demographic_map.png).

- **Plot of event frequency by visitor type**: [here](./PNG/event_frequency.png).

- **Heatmap of visitor types and countries**:[here](./PNG/heatmap_visitor_types_country.png).

- **Pie Chart of new and returning tourists**:[here](./PNG/pie_chart_new_return.png).

- **Scatter Plot of Visit count vs. target**: [here](./PNG/scatter_visit_count_target.png).
- **TreeMap Plot Visitor Types Countries**: [here](./PNG/treemap_visitor_types_countries.png).


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
- **Ali Guliyev** - GitHub: `CoraEpiro`



## Data set 
The original data set was published by the organisators of the Tourism Technology Hackathon 2024 on a privat basis. We promise to delete the data set after the 10.11.2024.  
################

