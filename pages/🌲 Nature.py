import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

st.set_page_config(page_title="Nature Handling Over Time", page_icon=":evergreen_tree:", layout="wide")

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

df_original = pd.read_csv('Data_Wrangled.csv')
header = df_original.iloc[0,:]
df = df_original.iloc[3:,:]
df.columns = header
df = df.drop(0, axis=1)

forest = go.Figure()

forest.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'Forest area (sq. km)'], 
                     name='Forest area (sq. km)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

forest.update_layout(
    title='<b>Forest Area</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Forest Area (sq. km)</b>',
    title_font=dict(size=20),
    xaxis=dict(showgrid=True,
        gridwidth=1, 
        gridcolor='LightGray',
        title_font=dict(size=16),
        tickfont=dict(size=12),
        tickvals=df.iloc[:, 0]
        ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
        title_font=dict(size=16),
        tickfont=dict(size=12),
        )
)

emission = go.Figure()

emission.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'CO2 emissions (metric tons per capita)'], 
                     name='CO2 emissions (metric tons per capita)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

emission.update_layout(
    title='<b>CO2 Emissions</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Emission (metric tons per capita)</b>',
    title_font=dict(size=20),
    xaxis=dict(showgrid=True,
        gridwidth=1, 
        gridcolor='LightGray',
        title_font=dict(size=16),
        tickfont=dict(size=12),
        tickvals=df.iloc[:, 0]
        ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
        title_font=dict(size=16),
        tickfont=dict(size=12),
        )
)

st.sidebar.header('Management of Nature')
st.sidebar.write('This page displays the temporal evolution of Brazilian development indicators related to nature.')

st.title('Nature Handling Over Time')

left_column, right_column = st.columns(2)

left_column.plotly_chart(forest, use_container_width=True)

right_column.plotly_chart(emission, use_container_width=True)