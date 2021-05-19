import streamlit as st
import pandas as pd
import numpy as np

##Importing visualization dataset
df_viz = pd.read_csv('https://raw.githubusercontent.com/smoughrabi/msba370project/main/df_viz.csv')

st.set_page_config(
    page_title = 'MSBA 370 Project',
    page_icon = '💵')

def app():
    st.markdown(f"<h2 style='text-align:left; font-family:arial' >{'<b>Previous Telemarketing Campaign Metrics</b>'}</h2>", unsafe_allow_html=True)
    st.subheader('Dive into the metrics & figures of the bank\'s latest telemarketing campaign aimed at getting customers to subscribe to a bank-term deposit.')
    st.write("")

    ## Calculating the metrics

    #Conversion Rate
    conversion_count = df_viz[df_viz['Subscribed?'] == 'yes'].shape[0]
    customer_count = df_viz.shape[0]

    conversion_rate = np.round((conversion_count/customer_count) * 100)

    # To make calculations easier, the dataframes were split among subsribed and unsubscribed Customers
    subscribed = df_viz[df_viz['Subscribed?'] == 'yes']
    unsubscribed = df_viz[df_viz['Subscribed?'] == 'no']

    # Average Balance (subscribed vs unsubscribed customers)
    avg_balance_sub = np.round((subscribed['Average_Balance'].mean()))
    avg_balance_unsub = np.round((unsubscribed['Average_Balance'].mean()))

    #Average Duration of Phone Call (in minutes)
    avg_contact_duration_sub = np.round((subscribed['LastContact_Duration'].mean())/60)
    avg_contact_duration_unsub = np.round((unsubscribed['LastContact_Duration'].mean())/60)

    # Average Touchpoints (prior to campaign)

    avg_touch_sub = np.round((subscribed['BeforeCampaign_TimesContacted'].mean()))
    avg_touch_unsub = np.round((unsubscribed['BeforeCampaign_TimesContacted'].mean()))


    ## Creating a Dashboard-like structure (3 columns and two rows)

    st.markdown(f"<h2 style='text-align:left; font-family:arial; color: black;' >{'<b>Conversion Rate (%)</b>'} </h2>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:left; font-family:arial; color: black;' >{'Percentage of Targeted Customers who Subscribed'} </h4>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align:left; color: offblack;' >{conversion_rate} </h1>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    st.markdown(f"<h2 style='text-align:left; font-family:arial; color: teal;' >{'<b>Subscribed Customers</b>'} </h2>", unsafe_allow_html=True)
    st.write("")

    col1a, col2a, col3a = st.beta_columns(3)

    with col1a:
        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: teal;' >{'<b>Average Contact Duration</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: teal;' >{'Duration of Phone Call in Minutes'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_contact_duration_sub}</h1>", unsafe_allow_html=True)

        st.write("")
        st.write("")
        st.write("")

    with col2a:
        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: teal;' >{'<b>Average Balance</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: teal;' >{'Bank Balance in €'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_balance_sub}</h1>", unsafe_allow_html=True)

        st.write("")
        st.write("")
        st.write("")

    with col3a:
        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: teal;' >{'<b>Average Touchpoints Before Campaign</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: teal;' >{'# of Contacts with the Customer Before Campaign'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_touch_sub}</h1>", unsafe_allow_html=True)

        st.write("")
        st.write("")
        st.write("")


    st.markdown(f"<h2 style='text-align:left; font-family:arial; color: Crimson;' >{'<b>Unsubscribed Customers</b>'} </h2>", unsafe_allow_html=True)
    st.write("")

    col1b, col2b, col3b = st.beta_columns(3)

    with col1b:

        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: Crimson;' >{'<b>Average Contact Duration</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: Crimson;' >{'Duration of Phone Call in Minutes'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_contact_duration_unsub}</h1>", unsafe_allow_html=True)

    with col2b:

        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: Crimson;' >{'<b>Average Balance</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: Crimson;' >{'Bank Balance in €'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_balance_unsub}</h1>", unsafe_allow_html=True)

    with col3b:

        st.markdown(f"<h2 style='text-align:left; font-family:arial; color: Crimson;' >{'<b>Average Touchpoints Before Campaign</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:left; font-family:arial; color: Crimson;' >{'# of Contacts with the Customer Before Campaign'} </h4>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color: offblack;'>{avg_touch_unsub}</h1>", unsafe_allow_html=True)
