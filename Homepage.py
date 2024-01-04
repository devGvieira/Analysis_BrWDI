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

st.title("Development Indicators of Brazil")
st.markdown("##")

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

st.header('Temporal Evolution of Different Metrics')

st.sidebar.success("Select above the aspect you want to know more.")

st.markdown('mumbo jambo')

