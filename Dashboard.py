import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

df_original = pd.read_csv('Data_Wrangled.csv')
df = df_original.iloc[3:,:]
df = df.drop('Unnamed: 0', axis=1)

st.write('Exploratory Analysis')

fig = go.Figure()

fig.add_trace(go.Bar(x=df.iloc[:,0], 
                     y=df.iloc[:,1], 
                     name='Population',
                     marker_color='rgb(72, 202, 228)'
                     ))

fig.update_layout(
    title='<b>Population Over the Years</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Total Population</b>',
    title_font=dict(size=50),
    xaxis=dict(showgrid=True,
        gridwidth=1, 
        gridcolor='LightGray',
        title_font=dict(size=25),
        tickfont=dict(size=16),
        tickvals=df.iloc[:, 0]
        ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
        range=[200_000_000, df.iloc[:, 1].max()],
        title_font=dict(size=25),
        tickfont=dict(size=16)
        )
)

fig.show()

st.pyplot(fig)