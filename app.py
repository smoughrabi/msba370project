import streamlit as st
from multiapp import MultiApp
import home
import customer_dataexp
import campaign_metrics
import campaign_prediction # importing app modules

## This multi-page app was prepared using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar]

app = MultiApp()


## Setting the Width (Streamlit Wide Layout is too wide)
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
       max-width: {1450}px;
    }}
    .reportview-container .main {{
        color: {'OffBlack'};
    }}
</style>
""",
        unsafe_allow_html=True,
    )

## Title
st.image('header1.jpeg',width= 1450)
st.markdown(f"<h1 style='text-align:center;' >{'<b>Decision-Making Web App</b>'}</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center;' >{'by Sarah El Moughrabi'}</h3>", unsafe_allow_html=True)

# skipping some lines
st.write("")
st.write("")
st.write("")
st.write("")

## Adding the Applications
app.add_app("Home", home.app)
app.add_app("Customer Data Exploration", customer_dataexp.app)
app.add_app("Previous Campaign Metrics", campaign_metrics.app)
app.add_app("Campaign Performance Prediction", campaign_prediction.app)

# The main app
app.run()

# Footer, code source: https://discuss.streamlit.io/t/streamlit-footer/12181

footer= """<style>
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: teal;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/sarah-el-moughrabi/" target="_blank">Sarah El Moughrabi</a></p>
<p>as part of Data-Driven Digital Marketing (MSBA 370) course taught at OSB-AUB.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
