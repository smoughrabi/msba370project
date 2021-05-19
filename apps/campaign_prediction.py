import streamlit as st
import numpy as np
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = 'MSBA 370 Project',
    page_icon = '💵')

## Unpickling trained decision tree object
pickle_in = open("finalclassifier.pkl","rb")
classifier = pickle.load(pickle_in)

## Creating a dictionary for label encoded variables
wealthbracket_dict = {'Lowest':0,'Lower Middle':1, 'Middle':2, 'Upper Middle':3,'Highest':4}
education_dict = {'Unknown':0,'Primary':1,'Secondary':2,'Tertiary':3}
# For housing loan, credit in default, and personal loan
binary_dict = {'No':0,'Yes':1}

## Defining functions for predicting campaign performance and for mapping values from the selectbox to the dictionary

def predict_campaign_success(Age,LastContact_Month_apr, LastContact_Month_aug, LastContact_Month_dec, LastContact_Month_feb, LastContact_Month_jan, LastContact_Month_jul, LastContact_Month_jun, LastContact_Month_mar, LastContact_Month_may, LastContact_Month_nov, LastContact_Month_oct, LastContact_Month_sep,Marital_Status_divorced,Marital_Status_married,Marital_Status_single,PCampaign_Outcome_failure,PCampaign_Outcome_success,PCampaign_Outcome_unknown,LastContact_Period_Beginning_of_Month,LastContact_Period_End_of_Month,LastContact_Period_Mid_Month,Education_Level, Wealth_Bracket, Housing_Loan, Personal_Loan, Credit_in_Default,Job_Type_blue_collar, Job_Type_retired, Job_Type_self_employed, Job_Type_services, Job_Type_student, Job_Type_unemployed, Job_Type_unknown, Job_Type_white_collar,Days_Since_LastContact_BeforeCampaign,PCampaign_TimesContacted, Average_Balance):
    prediction=classifier.predict([[Age,LastContact_Month_apr, LastContact_Month_aug, LastContact_Month_dec, LastContact_Month_feb, LastContact_Month_jan, LastContact_Month_jul, LastContact_Month_jun, LastContact_Month_mar, LastContact_Month_may, LastContact_Month_nov, LastContact_Month_oct, LastContact_Month_sep,Marital_Status_divorced,Marital_Status_married,Marital_Status_single,PCampaign_Outcome_failure,PCampaign_Outcome_success,PCampaign_Outcome_unknown,LastContact_Period_Beginning_of_Month,LastContact_Period_End_of_Month,LastContact_Period_Mid_Month,Education_Level, Wealth_Bracket, Housing_Loan, Personal_Loan, Credit_in_Default,Job_Type_blue_collar, Job_Type_retired, Job_Type_self_employed, Job_Type_services, Job_Type_student, Job_Type_unemployed, Job_Type_unknown, Job_Type_white_collar,Days_Since_LastContact_BeforeCampaign,PCampaign_TimesContacted, Average_Balance]])
    print(prediction)
    return prediction

def get_value(val, dict):
    for key,value in dict.items():
        if val == key:
            return value

def app():
    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Predicting Telemarketing Campaign Performance</b>'}</h2>", unsafe_allow_html=True)

    st.subheader("The data collected by the bank regarding their campaign performance was used to create a classification model that can predict whether a customer will subscribe or not with close to 90% accuracy.If the bank has a target customer in mind, they can use the tool below to predict their potential reaction to an upcoming telemarketing campaign!")
    st.subheader("The input variables can be categorized along three dimensions, customer demographic information, customer banking behavior, and information about previous points of contact.")
    st.write("")
    st.write("")


    html_page_divider = """
        <div style="background-color:teal;padding:8px">
        <h2 style="color:white;text-align:center;"> </h2>
        </div>
        """

    st.markdown(html_page_divider,unsafe_allow_html=True)

    ## Setting all the one-hot encoded variables to zero
    LastContact_Period_Beginning_of_Month = 0
    LastContact_Period_End_of_Month = 0
    LastContact_Period_Mid_Month = 0
    PCampaign_Outcome_failure = 0
    PCampaign_Outcome_success = 0
    PCampaign_Outcome_unknown = 0
    Marital_Status_divorced = 0
    Marital_Status_married = 0
    Marital_Status_single = 0
    LastContact_Month_apr = 0
    LastContact_Month_aug = 0
    LastContact_Month_dec = 0
    LastContact_Month_feb = 0
    LastContact_Month_jan = 0
    LastContact_Month_jul = 0
    LastContact_Month_jun = 0
    LastContact_Month_mar = 0
    LastContact_Month_may = 0
    LastContact_Month_nov = 0
    LastContact_Month_oct = 0
    LastContact_Month_sep = 0
    Job_Type_blue_collar = 0
    Job_Type_retired = 0
    Job_Type_self_employed = 0
    Job_Type_services = 0
    Job_Type_student = 0
    Job_Type_unemployed = 0
    Job_Type_unknown = 0
    Job_Type_white_collar = 0


    # Made 5 columns to have a padding between the columns
    col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])

    ## Setting the variables that the end-user can control (three categories)
    #Customer Demographic Information
    with col1:
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Customer Demographic Information</b>'}</h3>", unsafe_allow_html=True)
        Age = st.slider('Age', min_value=1, max_value=100)
        wealth_bracket = st.selectbox("Wealth Bracket", ['Lowest','Lower Middle','Middle','Upper Middle','Highest'])
        Wealth_Bracket = get_value(wealth_bracket, wealthbracket_dict)
        job_type = st.selectbox("Job Type", ['Blue-Collar','White-Collar','Retired','Self-Employed','Services','Student','Unemployed','Unknown'])

        if job_type == 'Blue-Collar':
            Job_Type_blue_collar = 1
        elif job_type == 'White-Collar':
            Job_Type_white_collar = 1
        elif job_type == 'Retired':
            Job_Type_retired = 1
        elif job_type == 'Self-Employed':
            Job_Type_self_employed = 1
        elif job_type == 'Services':
            Job_Type_services = 1
        elif job_type == 'Student':
            Job_Type_student = 1
        elif job_type == 'Unemployed':
            Job_Type_unemployed = 1
        elif job_type == 'Unknown':
            Job_Type_unknown = 1

        marital_status = st.selectbox("Marital Status",['Divorced','Married','Single'])

        if marital_status == 'Divorced':
            Marital_Status_divorced = 1
        elif marital_status == 'Married':
            Marital_Status_married = 1
        elif marital_status == 'Single':
            Marital_Status_single = 1

        education_level = st.selectbox("Education Level",['Primary','Secondary','Tertiary','Unknown'])
        Education_Level = get_value(education_level, education_dict)
    #Customer Banking Behavior
    with col3:
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Customer Banking Behavior</b>'}</h3>", unsafe_allow_html=True)
        Average_Balance = st.number_input('Average Bank Account Balance')
        housing_loan = st.selectbox('Does the customer have a housing loan?', ['Yes','No'])
        Housing_Loan = get_value(housing_loan, binary_dict)
        personal_loan = st.selectbox('Does the customer have a personal loan?', ['Yes','No'])
        Personal_Loan = get_value(personal_loan, binary_dict)
        credit_default = st.selectbox('Does the customer have any credit in default?', ['Yes','No'])
        Credit_in_Default = get_value(credit_default, binary_dict)
    #Last Contact/Previous Campaign Details
    with col5:
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Previous Contact/Campaign Response</b>'}</h3>", unsafe_allow_html=True)
        last_contact_month = st.selectbox('In which month was the customer last contacted?', ['January','February','March','April','May','June','July','August','September','October','November','December'])
        if last_contact_month == 'January':
            LastContact_Month_jan = 1
        elif last_contact_month == 'February':
            LastContact_Month_feb = 1
        elif last_contact_month == 'March':
            LastContact_Month_mar = 1
        elif last_contact_month == 'April':
            LastContact_Month_apr = 1
        elif last_contact_month == 'May':
            LastContact_Month_may = 1
        elif last_contact_month == 'June':
            LastContact_Month_jun = 1
        elif last_contact_month == 'July':
            LastContact_Month_jul = 1
        elif last_contact_month == 'August':
            LastContact_Month_aug = 1
        elif last_contact_month == 'September':
            LastContact_Month_sep = 1
        elif last_contact_month == 'October':
            LastContact_Month_oct = 1
        elif last_contact_month == 'November':
            LastContact_Month_nov = 1
        elif last_contact_month == 'December':
            LastContact_Month_dec = 1

        last_contact_period = st.selectbox('At what time of the month was the customer last contacted?', ['Beginning of Month','End of Month','Mid-Month'])

        if last_contact_period == 'Beginning of Month':
            LastContact_Period_Beginning_of_Month = 1
        elif last_contact_period == 'End of Month':
            LastContact_Period_End_of_Month = 1
        elif last_contact_period == 'Mid-Month':
            LastContact_Period_Mid_Month = 1

        Days_Since_LastContact_BeforeCampaign = st.slider('How many days since the last point of contact with the customer? (-1 if the customer has not been contacted before)', min_value=-1, max_value=500)
        PCampaign_TimesContacted = st.slider('How many times has the customer been contacted before?', min_value=0, max_value=50)

        prev_campaign_outcome = st.selectbox('How did the previous campaign with the customer go?', ['Success','Failure','Unknown or No Previous Campaign'])

        if prev_campaign_outcome == 'Success':
            PCampaign_Outcome_success = 1
        elif prev_campaign_outcome == 'Failure':
            PCampaign_Outcome_failure = 1
        elif prev_campaign_outcome == 'Unknown or No Previous Campaign':
            PCampaign_Outcome_unknown = 1

    st.markdown(html_page_divider,unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    predict_button = st.button('Click for Prediction!')
    result = ""

    if predict_button:
        result = predict_campaign_success(Age,
                LastContact_Month_apr, LastContact_Month_aug, LastContact_Month_dec, LastContact_Month_feb, LastContact_Month_jan, LastContact_Month_jul, LastContact_Month_jun, LastContact_Month_mar, LastContact_Month_may, LastContact_Month_nov, LastContact_Month_oct, LastContact_Month_sep,
                Marital_Status_divorced,Marital_Status_married, Marital_Status_single,
                PCampaign_Outcome_failure, PCampaign_Outcome_success,PCampaign_Outcome_unknown,
                LastContact_Period_Beginning_of_Month,LastContact_Period_End_of_Month,LastContact_Period_Mid_Month,
                Education_Level, Wealth_Bracket, Housing_Loan, Personal_Loan, Credit_in_Default,
                Job_Type_blue_collar, Job_Type_retired, Job_Type_self_employed, Job_Type_services, Job_Type_student, Job_Type_unemployed, Job_Type_unknown, Job_Type_white_collar,
                Days_Since_LastContact_BeforeCampaign,PCampaign_TimesContacted, Average_Balance
                )
        if result == 1:
            st.success('There is a 90% chance that this customer will subscribe to your telemarketing campaign')
        else:
            st.success('There is a 90% chance that this customer will not subscribe to your telemarketing campaign')

## Some code was inspired by the following sources:
## https://github.com/Jcharis/black-friday-sales_streamlit-app/blob/main/ml_app.py
## https://github.com/krishnaik06/Dockers
