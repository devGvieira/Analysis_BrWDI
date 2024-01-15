import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go
import base64

df_original = pd.read_csv('Data_Wrangled.csv')
header = df_original.iloc[0,:]
df = df_original.iloc[3:,:]
df.columns = header
df = df.drop(0, axis=1)

st.set_page_config(page_title="Development Indicators of Brazil", page_icon=":flag-br:", layout="wide")

# Setting up the flag on the sidebar's top
st.markdown(
        f"""
            <style>
                [data-testid="stSidebar"] {{
                    background-image: url(https://cdn-icons-png.flaticon.com/512/630/630591.png);
                    background-repeat: no-repeat;
                    background-size: 50% auto;
                    padding-top: 80px;
                    background-position: top;
                }}
            </style>
            """,
        unsafe_allow_html=True,
    )

# Setting up my logo on the sidebar's bottom
logo_url = 'https://media.licdn.com/dms/image/D4D16AQHzD-Ujyw2Vkg/profile-displaybackgroundimage-shrink_350_1400/0/1698418610960?e=1709769600&v=beta&t=dFkyg8xGgGNExKCRp8KOoY73q251JSD_bNUVEhBlRrM'

st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] + div {{
                position:relative;
                bottom: 0;
                height: 72%;
                background-image: url({logo_url});
                background-size: 98% auto;
                background-repeat: no-repeat;
                background-position-x: center;
                background-position-y: bottom;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.success("Select above the aspect you want to know more.")

st.title(":chart_with_upwards_trend: Development Indicators of Brazil")
st.markdown("##")

st.write("This work contains an anaysis of Brazilian development indicators, wherein the data utilized concerns the years 2013 to 2022 and was obtained from the World Bank's DataBank. Given the variety of indicators present in the dataset, such analysis was divided in three main aspects to  better visualize their temporal evolution, these being nature, economy and population. Still on improving visualization of the data, the behaviour through time of different indicators was plotted.")

nature, economy, population = st.columns(3)

with nature:
    st.header("Nature")

    st.write("Considering the increasing effects of global warming, an analysis of nature management becomes of importance for a better comprehension of Brazil's efforts on diminishing it. Therefore, in the nature page, indicators such as forest area, carbon dioxide emissions and electric power consumption per capita are plotted through time.")

with economy:
    st.header("Economy")

    st.write("Given economy as being one of the main pillars for a nation to develop, analyzing it is essential for precisely understanding Brazil's development through the past years and, in order to do so, a page in this very analysis was dedicated to it. Hence, this page treats of the temporal evolution of Brazil's GDP, GNI and also income share held by the lowest 20% of the population ")

with population:
    st.header("Population")

    st.write("The demography of a country is key for understanding its progress, a country that lacks social equality or a well distributed population will unequivocally face issues with poverty and real state. Keeping that in mind, this analysis brings a page related to the Brazilian population, wherein graphs are plotted to to better visualize the temporal behaviours of indicators as population density and poverty.")
    