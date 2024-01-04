import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

df_original = pd.read_csv('Data_Wrangled.csv')
header = df_original.iloc[0,:]
df = df_original.iloc[3:,:]
df.columns = header
df = df.drop(0, axis=1)

st.set_page_config(page_title="Analysis of Brazil's Development Indicators", page_icon=":flag-br:", layout="wide")

st.title(" :flag-br: Analysis of Brazil's Development Indicators")
st.markdown("##")

population = go.Figure()

population.add_trace(go.Bar(x=df.iloc[:,0], 
                     y=df.iloc[:,1], 
                     name='Population',
                     marker_color='rgb(72, 202, 228)'
                     ))

population.update_layout(
    title='<b>Population</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Total Population</b>',
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
        range=[200_000_000, df.iloc[:, 1].max()],
        title_font=dict(size=16),
        tickfont=dict(size=12)
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
    yaxis_title='<b>GDP (Current US$)</b>',
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

urban_pop = go.Figure()

urban_pop.add_trace(go.Bar(x=df.iloc[:,0], 
                     y=df.loc[:,'Urban population growth (annual %)'], 
                     name='Urban population growth (annual %)',
                     marker_color='rgb(72, 202, 228)'
                     ))

urban_pop.update_yaxes(range=[0.6,1.2])

urban_pop.update_layout(
    title='<b>Urban Population Growth</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Growth (annual %)</b>',
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
        tickfont=dict(size=12)
        )
)

left_column, right_column = st.columns(2)

left_column.plotly_chart(population, use_container_width=True)

right_column.plotly_chart(urban_pop, use_container_width=True)

left_column_2, right_column_2 = st.columns(2)

left_column_2.plotly_chart(gdp, use_container_width=True)

right_column_2.plotly_chart(share, use_container_width=True)

left_column_3, right_column_3 = st.columns(2)

left_column_3.plotly_chart(forest, use_container_width=True)

right_column_3.plotly_chart(emission, use_container_width=True)

