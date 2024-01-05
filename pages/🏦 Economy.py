import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

st.set_page_config(page_title="Economy Over Time", page_icon=":bank:", layout="wide")

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

gdp = go.Figure()

gdp.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'GDP (current US$)'], 
                     name='GDP (Current US$)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

gdp.update_layout(
    title='<b>Gross Domestic Product (GDP)</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b> Dollars</b>',
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

share = go.Figure()

share.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'Income share held by lowest 20%'], 
                     name='Income share held by lowest 20%',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

share.update_layout(
    title='<b>Income Share Held by Lowest 20%</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Share</b>',
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
        dtick=0.25
        )
)

gni = go.Figure()

gni.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'GNI, PPP (current international $)'], 
                     name='GNI, PPP (current international $)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

gni.update_layout(
    title='<b>Gross National Income (GNI) Based on Purchasing Power Parity</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b> Dollars',
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

gni_pc = go.Figure()

gni_pc.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'GNI per capita, PPP (current international $)'], 
                     name='GNI per capita, PPP (current international $)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

gni_pc.update_layout(
    title='<b>Gross National Income (GNI) per Capita Based on Purchasing Power Parity</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b> Dollars',
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

st.sidebar.header('Economical Aspects')
st.sidebar.write('This page displays the temporal evolution of Brazilian development indicators on the economical sphere.')

st.title('Economy Over Time')

left_column_1, right_column_1 = st.columns(2)

left_column_1.plotly_chart(gdp, use_container_width=True)

right_column_1.plotly_chart(gni, use_container_width=True)

left_column_2, right_column_2 = st.columns(2)

left_column_2.plotly_chart(gni_pc, use_container_width=True)

right_column_2.plotly_chart(share, use_container_width=True)