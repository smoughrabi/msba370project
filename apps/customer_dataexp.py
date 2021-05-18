import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly.figure_factory as ff
from plotly.offline import iplot

## Setting an icon and page title for the App + enabling caching to improve the website speed
st.set_page_config(
    page_title = 'MSBA 370 Project',
    page_icon = '💵')
@st.cache(persist=True)
def load_data():
    data = pd.read_csv('Datasets/df_viz.csv')
    return data

df_viz = load_data()

print(df_viz.columns)

## Renaming some columns to improve user friendliness
df_viz = df_viz.rename(columns={'Age_Group': 'Age Group', 'Wealth_Bracket': 'Wealth Bracket', 'Education_Level': 'Education Level','Job_Type' :'Job Type','Credit_in_Default?':'Credit in Default'})

## Adding a column with all 1's to be used for barcharts
df_viz['count'] = 1

## Renaming some values to improve user friendliness
df_viz['Credit in Default'] = df_viz['Credit in Default'].replace('yes','Has Credit in Default')
df_viz['Credit in Default'] = df_viz['Credit in Default'].replace('no','Does not have Credit in Default')

df_viz['Personal Loan?'] = df_viz['Personal Loan?'].replace('yes','Has Personal Loan')
df_viz['Personal Loan?'] = df_viz['Personal Loan?'].replace('no','Does not have Personal Loan')

df_viz['Housing Loan?'] = df_viz['Housing Loan?'].replace('yes','Has Housing Loan')
df_viz['Housing Loan?'] = df_viz['Housing Loan?'].replace('no','Does not have Housing Loan')


def app():
    st.markdown(f"<h2 style='text-align:left; font-family:arial' >{'<b>Get to Know your Customers</b>'}</h2>", unsafe_allow_html=True)

    #To organize the file, one section will be for demographic info, and the other for banking behavior
    customer_demographics = st.beta_container()
    customer_bankingbehavior = st.beta_container()

    ## Creating a page divider to improve design
    html_title_sec1= """
            <div style="background-color:teal;padding:4px">
            <h2 style="color:white;text-align:center;"> Section I. Customer Demographics </h2>
            </div>
            """

    html_title_sec2= """
            <div style="background-color:teal;padding:4px">
            <h2 style="color:white;text-align:center;"> Section II. Customer Banking Behavior </h2>
            </div>
            """

    html_space1= """
            <div style="background-color:teal;padding:4px">
            <h2 style="color:OffBlack;text-align:center;"></h2>
            </div>
            """



    with customer_demographics:
        st.markdown(html_title_sec1, unsafe_allow_html=True)
        st.write("")
        st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'This section explores the bank&#x27s customer demographic data. This has multiple uses, from allowing decision makers to understand who the bank&#x27s main customers are along several dimensions such as age group and wealth bracket, to enabling them to check if the bank is attracting the intended customer base.' }</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])
        col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Choose a Variable to Explore'}</h3>", unsafe_allow_html=True)


        ## Creating bar charts for customer demographics
        variable_selection = col1.selectbox('', ['Age Group','Job Type','Wealth Bracket','Education Level'])
        fig1 = go.Figure()
        if variable_selection:
            #fig1.add_trace(go.Bar(y= df_viz[variable_selection].value_counts(), x= df_viz[variable_selection]))
            fig1.add_trace(go.Bar(y= df_viz['count'], x= df_viz[variable_selection]))
            fig1.update_layout(title= 'Customers by {}'.format(variable_selection), yaxis_title='# of Customers', titlefont_size=24, template = 'plotly_white', xaxis={'categoryorder':'total descending'})
            fig1.update_traces(marker_line_color='#008080',marker_line_width=1.5, opacity=0.6, hoverinfo = 'skip')
            col3.plotly_chart(fig1)

        ## Adding customized insights per condition
        st.markdown(f"<h3 style='text-align:left; font-family:arial; color:Teal' >{'<b>Key Insight:</b>'}</h3>", unsafe_allow_html=True)
        if variable_selection == 'Age Group':
            mostfrequent_age_count = df_viz['Age Group'].value_counts()[0]
            mostfrequent_age_category = df_viz['Age Group'].value_counts().index[0]
            st.subheader('**Currently, the majority ({}) of the bank\'s customers are {}**'.format(mostfrequent_age_count,mostfrequent_age_category))
        elif variable_selection == 'Job Type':
            mostfrequent_job_count = df_viz['Job Type'].value_counts()[0]
            mostfrequent_job_category = df_viz['Job Type'].value_counts().index[0]
            st.subheader('**Currently, the majority ({}) of the bank\'s customers have the {} job type**'.format(mostfrequent_job_count,mostfrequent_job_category))
        elif variable_selection == 'Wealth Bracket':
            mostfrequent_wealth_count = df_viz['Wealth Bracket'].value_counts()[0]
            mostfrequent_wealth_category = df_viz['Wealth Bracket'].value_counts().index[0]
            st.subheader('**Currently, the majority ({}) of the bank\'s customers are in the {} wealth bracket**'.format(mostfrequent_wealth_count,mostfrequent_wealth_category))
        elif variable_selection == 'Education Level':
            mostfrequent_ed_count = df_viz['Education Level'].value_counts()[0]
            mostfrequent_ed_category = df_viz['Education Level'].value_counts().index[0]
            st.subheader('**Currently, the majority ({}) of the bank\'s customers have a {} education level**'.format(mostfrequent_ed_count,mostfrequent_ed_category))
        st.write("")
        st.write("")


    with customer_bankingbehavior:
        st.markdown(html_title_sec2,unsafe_allow_html=True)
        st.write("")
        st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'This section explores data on customer banking behavior, including the proportion of customers that have taken out a personal loan or that have credit on default' }</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        col1,col2,col3,col4= st.beta_columns([30,10,30,10])

        with col1:
            ## Pie Chart Showing the Proportion of Customers with Personal Loans
            fig3 = go.Figure()
            color_list = ['teal', 'lightgray']
            fig3.add_trace(go.Pie(labels= df_viz['Personal Loan?'], values= df_viz['count']))
            fig3.update_traces(hoverinfo='label+percent', textinfo='label+percent',insidetextorientation='radial', textfont_size=14, marker=dict(colors= color_list, line=dict(color='#000000', width=2)))
            fig3.update_layout(title= 'Proportion of Customers who have taken out Personal Loans', titlefont_size=18, template = 'plotly_white',showlegend = False)
            st.plotly_chart(fig3)
            st.write("")
            st.write("")
            no_personal_loan_count = df_viz['Personal Loan?'].value_counts()[0]
            personal_loan_count = df_viz['Personal Loan?'].value_counts()[1]
            st.subheader('Currently, **{}** of the bank\'s customers do not have a personal loan, while only **{}** of the bank\'s customers do. Perhaps the bank should consider decreasing interest rates on personal loans to attract more customers.'.format(no_personal_loan_count,personal_loan_count))



            ## Pie Chart Showing the Proportion of Customers with Credit in Default
            #fig2 = go.Figure()
            #fig2.add_trace(go.Pie(labels= df_viz['Credit in Default'], values= df_viz['count']))
            #fig2.update_traces(hoverinfo='label+percent', textinfo='label+percent',insidetextorientation='radial', textfont_size=14, marker=dict(colors= color_list, line=dict(color='#000000', width=2)))
            #fig2.update_layout(title= 'Proportion of Customers with Credit in Default', titlefont_size=18, template = 'plotly_white', showlegend = False)
            #st.plotly_chart(fig2)
            #st.write("")
            #st.write("")

            fig5 = go.Figure()
            fig5.add_trace(go.Histogram(x= df_viz["Average_Balance"]))
            fig5.update_layout(title= 'Distribution of Average Account Balances',titlefont_size=18,template = 'plotly_white')
            fig5.update_xaxes(range=[-2000,3000])
            st.plotly_chart(fig5)
            st.subheader('As shown above, a large chunk of the customers\' average account balances are between **€0** and **€100**, this could be an indication of a serious churn rate and customer loss')


        with col3:
            color_list = ['teal', 'lightgray']
            fig4 = go.Figure()
            fig4.add_trace(go.Pie(labels= df_viz['Housing Loan?'], values= df_viz['count']))
            fig4.update_traces(hoverinfo='label+percent', textinfo='label+percent',insidetextorientation='radial', textfont_size=14, marker=dict(colors = color_list, line=dict(color='#000000', width=2)))
            fig4.update_layout(title= 'Proportion of Customers who have taken out Housing Loans', titlefont_size=18, template = 'plotly_white',showlegend = False)
            st.plotly_chart(fig4)
            st.write("")
            st.write("")
            housing_loan_count = df_viz['Housing Loan?'].value_counts()[0]
            no_housing_loan_count = df_viz['Housing Loan?'].value_counts()[1]
            st.subheader('Currently, **{}** of the bank\'s customers have a housing loan, while **{}** do not. It seems that housing loans are a popular type of bank loan among this bank\'s customers'.format(housing_loan_count,no_housing_loan_count))


            #scatter plot with Age of Customers vs Average Account Balance
            fig6 = go.Figure()
            fig6.add_trace(go.Scatter(x = df_viz['Age'],y=df_viz['Average_Balance'],mode='markers',marker_color='teal'))
            fig6.update_layout(title='Scatterplot of Age vs Average Bank Balance', titlefont_size=18,
              yaxis_zeroline=False, xaxis_zeroline=True, template = 'plotly_white')
            st.plotly_chart(fig6)
            st.subheader("In the scatterplot above, there is an indication of a positive correlation between Age and Average Bank Balance, as seen by the larger bank figures on the top-right hand side.")



        st.markdown(html_space1,unsafe_allow_html=True)
