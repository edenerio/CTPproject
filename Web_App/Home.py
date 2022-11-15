import streamlit as st
st.set_page_config(page_title="Home")
st.title("Home page")
mission, img = st.columns(2, gap="large")

with mission:
    st.markdown('''Leveraging the robust data provided by the U.S. Census can provide clarity on key factors that affect the AGI (Adjusted Gross Income). 
                Utilizing our data analytical skills requires familiarization with the underlying and overarching aspects that contribute to the poverty issue at large. 
                This blending of domain expertise and statistical aptitude requires data cleaning. The process of data cleaning reduced the number of columns used in our project from 45 to 13. 
                The renovated dataset can be found in our [GitHub repository](https://github.com/edenerio/CTPproject/tree/main/Data)''')

with img:
    st.image("./Assets/home_img.png")