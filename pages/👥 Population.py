import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.graph_objects as go

st.set_page_config(page_title="Population Over Time", page_icon=":busts_in_silhouette:", layout="wide")

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

population = go.Figure()

population.add_trace(go.Bar(x=df.iloc[:,0], 
                     y=df.iloc[:,1], 
                     name='Population',
                     marker_color='rgb(72, 202, 228)'
                     ))

population.update_layout(
    title='<b>Population</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b>Number of People</b>',
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

poverty = go.Figure()

poverty.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'], 
                     name='Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

poverty.update_layout(
    title='<b>Poverty - Headcount Ratio at $2.15 a Day (2017 Purchasing Power Parity)</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b> Percentage of Population </b>',
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

density = go.Figure()

density.add_trace(go.Line(x=df.iloc[:,0], 
                     y=df.loc[:,'Population density (people per sq. km of land area)'], 
                     name='Population density (people per sq. km of land area)',
                     line=dict(
                         color='rgb(72, 202, 228)',
                         width=5
                     )
                     ))

density.update_layout(
    title='<b>Population Density</b>',
    xaxis_title='<b>Year</b>',
    yaxis_title='<b> People per Sq. km of Land Area',
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

st.sidebar.header('Demography')
st.sidebar.write("This page displays the temporal evolution of Brazil's demography.")

st.header('Population Over Time')

option = st.selectbox(
    "Select the graph to be displayed",
    ('Population', 'Urban Population', 'Population Density', 'Poverty'),
    index=None,
    placeholder='Choose an option'

)

if option == 'Population':
    st.plotly_chart(population, use_container_width=True)

elif option == 'Urban Population':
    st.plotly_chart(urban_pop, use_container_width=True)

elif option == 'Population Density':
    st.plotly_chart(density, use_container_width=True)

elif option == 'Poverty':
    st.plotly_chart(poverty, use_container_width=True)