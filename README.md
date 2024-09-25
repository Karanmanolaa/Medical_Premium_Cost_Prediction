# Project 2 - Medical_premium_cost_prediction

Explore the live application: [Medical Premium Cost Prediction](https://medical-premium-cost-prediction.onrender.com)

# Table of Content
- Overview
- Problem Statement and Motivation
- Technical Aspects
- Visualizations
- Challenges and Solutions


![high-health-care-costs-850x476](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/73c4a492-3fe9-4cbd-9bc6-c953400518af)

# 1- Overview :
The main aim of the "Medical Premium Cost Prediction" project is to create a machine learning model that estimates how much your health insurance premium will cost.The dataset is collected from kaggle which consists of around 1000 insurance premium values on the basis of columns like Age,	Diabetes,	BloodPressureProblems,	AnyTransplants,	AnyChronicDiseases,	Height,	Weight,	KnownAllergies,	HistoryOfCancerInFamily,	NumberOfMajorSurgeries.
At the last deployed the model in render using flask and docker.


# 2- Problem Statement and Motivation :

The project's main problem is accurately predicting medical insurance premium costs, which is essential for insurance companies and individuals. The motivation lies in helping insurance companies manage their risks and set competitive rates, while also empowering individuals to make informed healthcare coverage decisions. This project addresses a crucial need in the insurance industry, benefiting both insurers and policyholders. 

# 3- Technical Aspects :
In this project i have used python programming language and its libraries - scikit-learn,pandas,numpy,matplotlib,seaborn,xgboost,
for different purpose like
- Performed Explolatory data analysis using matplotlib and seaborn.
- Created new feature (feature engineering) age bins.
- I tried several models like Linear regression,decision trees.
- Used hyperparameter tuning and got the best model RandomForestRegressor with
- Mean Squared Error (MSE): 7073299.0357
- Mean Absolute Error (MAE): 1028.2545
- R-squared (R2) Score: 0.8161
- Deployed the model in render using Flask and Docker

# 4 - Challenges and Solutions:
- Challenges:
      -  Limited availability of data posed a significant challenge, 
      impacting the model's ability to generalize and make accurate 
      predictions
      -  Problem faced while deployment due to different 
      version of dependencies.
- Solutions :
      -  Utilized several models but Random Forest (with tuned       
      hyperparameters) was robust and less prone to overfitting,      
      making the model more reliable when dealing with limited data.
      -  To overcome deployment challenges related to different 
      version of dependencies , we adopted Docker for containerization .

# 5 - Visualizations:

### Categorical features Bargraph

![Medical images1](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/d757da78-ba12-408f-af60-d1b27fde552d)


### Histogram to visualize numerical features

![Medical images](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/74729565-dbe8-48f3-add2-a32519b59578)


### Correlation Matrix

![med corr](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/87b4fce2-0873-418a-a0b0-f7271a0731cd)


### Number of people opted for insurance based on premium-category on the basis of transplant history


![medical](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/0c962376-aeac-4ec9-92a1-928204d28e40)


#### Avg. price paid by people in each age category for their health insurance
![med](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/42ba69d9-1105-48cd-8361-add39a715fd7)



#### Number of people opted for insurance based on premium-category after how many surgeries:
![medic](https://github.com/Karanmanolaa/Medical_cost_premium_prediction/assets/144649975/f94da23d-d3d2-416e-bea8-e9176e5a208a)







