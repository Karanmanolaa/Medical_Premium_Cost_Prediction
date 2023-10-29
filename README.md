# Project 2 - Medical_cost_price_prediction

# Table of Content
- Overview
- Problem Statement and Motivation
- Technical Aspects
- Visualizations
- Challenges and Solutions

# 1- Overview :
The main aim of the "Medical Premium Cost Prediction" project is to create a machine learning model that estimates how much your health insurance premium will cost.The dataset is collected from kaggle which consists of around 1000 insurance premium values on the basis of columns like Age,	Diabetes,	BloodPressureProblems,	AnyTransplants,	AnyChronicDiseases,	Height,	Weight,	KnownAllergies,	HistoryOfCancerInFamily,	NumberOfMajorSurgeries.


# 2- Problem Statement and Motivation :

The project's main problem is accurately predicting medical insurance premium costs, which is essential for insurance companies and individuals. The motivation lies in helping insurance companies manage their risks and set competitive rates, while also empowering individuals to make informed healthcare coverage decisions. This project addresses a crucial need in the insurance industry, benefiting both insurers and policyholders. 

# 3- Technical Aspects :
In this project i have used python programming language and its libraries - scikit-learn,pandas,numpy,matplotlib,seaborn,xgboost,
for different purpose like
- Performed Explolatory data analysis using matplotlib and seaborn.
- Created new feature (feature engineering) age bins.
- I tried several models like Linear regression,decision trees.
- Used hyperparameter tuning and got the best model RandomForestRegressor with r2 score of 0.8080 and
-  MSE: 7386012.305294765
-  MAE: 1069.7527665859436

# 4 - Challenges and Solutions:
- Challenges: Limit data
- Solutions : Utilized models like Random Forest (with tuned hyperparameters) that are robust and less prone to overfitting, making the model more reliable when dealing with limited data.

# 5 - Visualizations:

  
