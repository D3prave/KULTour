TODOS: 
add how problems solving down in readme, encoder
add github 
API kinda weird  
CHECK DATA VISUALIZATION 
DO COMMENTS for the code. 

# Project Title: Personalization by culture and personality 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Use Case](#usecase)
- [Problems](#problems)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [Data set](#dataset)

## Introduction
Welcome to the Backend-ReadME-file of the Eternals for the 4th Challenge -Personalization by culture and personality. Millions of tourists from all over the world visit Austria every year. We want to optimize their experience in Austria by making data-based assumptions about their preferences. We will tackle this exciting challenge using machine learning. We will create a Collaboration Filtering with Singular Value Decomposition. But before, we will have to investigate our dataset a bit, do some data visualization to get a rough feeling about our dataset, and of course clean it properly. 
In the end we want to provide an API-endpoint for the Frontend-Team, such that the data-based decision for every individual person can be accessed in the web application. 

## Use Case 
Here's how to use the Ski Resort Management System:

1. **app.py**: The `DataLoader` class in `data_loader.py` handles data loading and preprocessing. It reads data from a CSV file, splits it into training and testing sets, and prepares the data for model training.

2. **collab_filt_svd.py**: Use `train_model.py` to train the recommendation model. It utilizes collaborative filtering to provide personalized location recommendations based on user data.

3. **data_loader.py**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

4. **data_prep.py**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

5. **data_visualization.py**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

6. **original_data.csv**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

7. **output.csv**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

8. **prepared_data.csv**: `analyze_data.py` allows for the analysis of visitor data, providing insights into visitor patterns and behavior.

## Problems 
As always in such a Challenge, there will be (unpredictable) problems that might occur in the process of the project. It was important that we faced the problems and didn´t resign on them and in the end, we solved all of them in our individual way: 
- **'Sparse' Features**:   The data set provided a lot of "empty" features. Additionally, a lot of them weren´t correlated to our problem. We got rid of those sparse columns while cleaning and investing the data.
- **Small Data Set**:      The more data the better. The main problem for our machine  learning task was a more or less small data set of around 250 after the cleansing. We managed to upsample the train data set to get a more reliable algorithm.
- **Unbalanced Data Set**: Another quite tricky option was the unbalanceness of the data set. Roughly 85% of the cleaned data consisted of Austrian data points, whereas other countries are drastically underrepresented. SMOTE took care of that. 
- **Event_names**: Our target feature, the event names often referred to same or similar things, but have been written in different ways. In order for that, we encoded this feature and basically merged similar events. 

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
- **Denis Hoti** - GitHub: `denishotii`
- **Jakub Wisniewski** - GitHub: `D3prave`
- **Lukas Lang** - GitHub: `GezaLang`
- **Teammate 4** - GitHub: `teammate3`
- **Teammate 5** - GitHub: `teammate3`
- **Teammate 6** - GitHub: `teammate3`

## Data set 
The original data set was published by the organisators of the Tourism Technology Hackathon 2024 on a privat basis. We promise to delete the data set after the 10.11.2024.  
################

