# Streamlit Project 
### by Sarah El Moughrabi

##### This is a prototype of a decision-making web application intended to illustrate just how accessible data-driven insights can be to key decision makers who do not necessarily have a technical background. 
The mock data used for this tool is a Portuguese bank’s customer data (referenced below), which includes information about their previous and current telemarketing campaigns. Although this is a specific use case, this web app can be adapted to accommodate many use cases and is not solely restricted to the banking industry.

##### Deployed App Link : https://share.streamlit.io/smoughrabi/msba370project/main/app.py 


#### Guide to navigate your way around the files

**ML.py** : includes the data cleaning, preprocessing, feature extraction, and model building and evaluation. This was prepared on Google Colab

**multiapp.py** : this .py file contains a framework for running multiple streamlit applications as a single app (developed by Praneel Nihar) This helps to organize the code and segment it properly. All other .py files are added to a select box for easy navigation

**app.py** : this is the main .py file used for deployment which links all the other .py files containing the different app sections with the multiapp framework

The complete streamlit web app relies on 4 .py files found in the folder **apps**: 

-**home.py**: this .py file contains the about section of the app
-**customer_dataex.py** : customer demographic and banking behavior visualizations & insights
-**campaign_metrics.py** : metrics of the previous campaign of the bank
-**campaign_prediction** : ML application, predicting whether a customer will subscribe to a bank deposit. This .py file relies on the final classifier.pkl file to make the predictions 


The datasets used can be found in the **Datasets** folder and are: 

- **df.csv** : the original bank marketing dataset, Dataset Source: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, In press, http://dx.doi.org/10.1016/j.dss.2014.03.001

- **data_viz.csv**: the cleaned and processed dataset before converting the variables to one hot and ordinal encoded to be used for visualization purposes

**images** folder 

Includes two pictures that were used within the web app 


