import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

df_original = pd.read_csv('Data_Wrangled.csv')
df = df_original.iloc[3:,:]
df = df.drop('Unnamed: 0', axis=1)

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.title(':bar_chart: Exploratory Analysis')
st.markdown("##")

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Left Column')

with middle_column:
    st.subheader('Middle Column')

with right_column:
    st.subheader('Right Column')

st.markdown("""---""")

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
    title_font=dict(size=40),
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

left_column.plotly_chart(fig, use_container_width=True)

