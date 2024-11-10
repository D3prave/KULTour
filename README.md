# KULTour: Personalization by culture and personality 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Use Case](#usecase)
- [Challenges](#challenges)
- [PNG_Report](#pdfreport)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [Data set](#dataset)

## About KULTour
Attention: Do you want to explore the world? KULTour is the perfect app for you!

Every year, millions of tourists from around the world visit Austria. Our goal is to enhance their experience by making data-driven assumptions about their preferences. To tackle this exciting challenge, we will employ machine learning techniques, specifically using Collaborative Filtering with Singular Value Decomposition (SVD).

Before diving into the modeling, we'll thoroughly investigate our dataset, perform data visualization to gain initial insights, and ensure the data is properly cleaned.

Our ultimate aim is to provide an API endpoint for the Frontend Team, enabling data-driven decisions for each individual user to be accessed through the web application.

## Requirements 
- We recommend using Docker 
- KULTour uses NodeJS, Google API and Python 
- KULTour uses TAILWIND CSS framework, for UI

## Commands

- First of all we have to install all dependencies needed for the project using this composer command: 
cd frontend
npm install

- To generate a new .env file for SIA, you should run this command: 
mv .env.example .env

- To start the frontend run:
cd frontend
npm start

- To run the Google API Server run (in a new terminal):
cd frontend
node src/server.js

- To install all the Backend requirements:
pip install -r requirements.txt

- To run the Backend run:
python backend/app.py

## Use Case

Here's a guide on how to handle the various files in our project:

Frontend:
1. **App.js**: 
   Main React App File
2. **MapContent.js**: 
   Handles the Google Map UI, and request to take the API.
3. **server.js**:
    Server side API to make request to Google API

Backend:
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
- **React**: A JavaScript library for building user interfaces.
- **React-Leaflet**: A React wrapper for Leaflet, a leading open-source JavaScript library for mobile-friendly interactive maps.
- **Axios**: A promise-based HTTP client for the browser and Node.js.
- **Bootstrap**: A popular CSS framework for developing responsive and mobile-first websites.
- **Font Awesome**: A toolkit for vector icons and social logos.

## API Endpoints
- **GET `https://ipapi.co/json/`**: Fetches the user's location based on their IP address.
- **POST `http://127.0.0.1:5000/category`**: Fetches the recommended category based on the user's country.
- **GET `http://localhost:5001/api/place?category={category}`**: Fetches places based on the recommended category.
- **GET `Google API`**: Fetches places description, pictures and addresses from Google Maps
- [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview)

## Contributors
- **Eternals** - GitHub_Repository: `https://github.com/denishotii/TourismTechnologyFestival`

- **Southik Nath Banerjee** - GitHub: `Southik Nath Banerjee`
- **Veronika Rybak** - GitHub: `vrnccr`
- **Denis Hoti** - GitHub: `denishotii`

## Contributors
- **Eternals** - GitHub_Repository: `https://github.com/denishotii/TourismTechnologyFestival`

- **Jakub Wisniewski** - GitHub: `D3prave`
- **Lukas Lang** - GitHub: `GezaLang`
- **Ali Guliyev** - GitHub: `CoraEpiro`



## Data set 
The original data set was published by the organisators of the Tourism Technology Hackathon 2024 on a privat basis. We promise to delete the data set after the 10.11.2024.  
################


## Project Organization

    ├── backend                         <- backend related stuff
    ├── frontend                        <- frontend related stuff
    └── .env.example           <- API Keys

---


## Collaborators

- [Denis Hoti](https://www.linkedin.com/in/denishoti/)
- [Veronika Rybak](https://www.linkedin.com/in/veronika-rybak-55379a337/)
- [Jakub Wisniewski](https://www.linkedin.com/in/jakub-wiśniewski-720150337/)
- [Ali Guliyev](https://www.linkedin.com/in/ali-guliyev-389837238/)
- [Southik Banarjee](https://www.linkedin.com/in/southik-nath-banerjee-74077a202/)
- [Lukas Lang](https://www.linkedin.com/in/lukas-lang-26628730b/)
