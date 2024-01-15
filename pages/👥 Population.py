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

def scatter_plot(plot_title, x_axis, y_axis, name_, title_, y_title):
    plot_title.add_trace(go.Scatter(
        x=x_axis,
        y=y_axis,
        mode='markers',
        name=name_,
        marker=dict(
            color='rgb(72, 202, 228)',
            size=16
        )
    ))

    plot_title.update_layout(
        title=title_,
        xaxis_title='<b>Year</b>',
        yaxis_title=y_title,
        title_font=dict(size=20),
        xaxis=dict(
            showgrid=True,
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

def line_plot(plot_title, x_axis, y_axis, name_, title_, y_title):

    plot_title.add_trace(go.Scatter(
        x=x_axis, 
        y=y_axis, 
        name=name_,
        mode='lines',
        line=dict(
            color='rgb(72, 202, 228)',
            width=5
        )
    ))

    plot_title.update_layout(
        title=title_,
        xaxis_title='<b>Year</b>',
        yaxis_title=y_title,
        title_font=dict(size=20),
        xaxis=dict(
            showgrid=True,
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
        ),
        showlegend=False
    )

def bar_plot(plot_title, x_axis, y_axis, name_, title_, y_title, y_axis_min, y_axis_max):

    plot_title.add_trace(go.Bar(x=x_axis, 
                        y=y_axis, 
                        name=name_,
                        marker_color='rgb(72, 202, 228)'
                        ))

    plot_title.update_layout(
        title=title_,
        xaxis_title='<b>Year</b>',
        yaxis_title=y_title,
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
            range=[y_axis_min, y_axis_max]
            )
    )

population_scatter =  go.Figure()
population_line = go.Figure()
population_bar =  go.Figure()
scatter_plot(population_scatter,
             df.iloc[:,0],
            df.iloc[:,1],
            'Population',
            '<b>Population</b>',
            '<b>Number of People</b>'
            )
line_plot(population_line,
             df.iloc[:,0],
            df.iloc[:,1],
            'Population',
            '<b>Population</b>',
            '<b>Number of People</b>')
bar_plot(population_bar,
             df.iloc[:,0],
            df.iloc[:,1],
            'Population',
            '<b>Population</b>',
            '<b>Number of People</b>',
            df.iloc[:,1].astype(float).min(),
            df.iloc[:,1].astype(float).max())

urban_pop_scatter =  go.Figure()
urban_pop_line =  go.Figure()
urban_pop_bar =  go.Figure()
scatter_plot(urban_pop_scatter,
             df.iloc[:,0],
             df.loc[:,'Urban population growth (annual %)'],
             'Urban population growth (annual %)',
             '<b>Urban Population Growth</b>',
             '<b>Growth (annual %)</b>'
             )
line_plot(urban_pop_line,
             df.iloc[:,0],
             df.loc[:,'Urban population growth (annual %)'],
             'Urban population growth (annual %)',
             '<b>Urban Population Growth</b>',
             '<b>Growth (annual %)</b>')
bar_plot(urban_pop_bar,
             df.iloc[:,0],
             df.loc[:,'Urban population growth (annual %)'],
             'Urban population growth (annual %)',
             '<b>Urban Population Growth</b>',
             '<b>Growth (annual %)</b>',
             df.loc[:,'Urban population growth (annual %)'].astype(float).min(),
             df.loc[:,'Urban population growth (annual %)'].astype(float).max())

density_scatter =  go.Figure()
density_line =  go.Figure()
density_bar =  go.Figure()
scatter_plot(density_scatter,
             df.iloc[:,0],
             df.loc[:,'Population density (people per sq. km of land area)'],
            'Population density (people per sq. km of land area)',
            '<b>Population Density</b>',
            '<b> People per Sq. km of Land Area'
             )
line_plot(density_line,
             df.iloc[:,0],
             df.loc[:,'Population density (people per sq. km of land area)'],
            'Population density (people per sq. km of land area)',
            '<b>Population Density</b>',
            '<b> People per Sq. km of Land Area')

bar_plot(density_bar,
             df.iloc[:,0],
             df.loc[:,'Population density (people per sq. km of land area)'],
            'Population density (people per sq. km of land area)',
            '<b>Population Density</b>',
            '<b> People per Sq. km of Land Area',
            df.loc[:,'Population density (people per sq. km of land area)'].astype(float).min(),
            df.loc[:,'Population density (people per sq. km of land area)'].astype(float).max())

poverty_scatter =  go.Figure()
poverty_line =  go.Figure()
poverty_bar =  go.Figure()
scatter_plot(poverty_scatter,
             df.iloc[:,0],
             df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'],
             'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
             '<b>Poverty - Headcount Ratio at $2.15 a Day (2017 Purchasing Power Parity)</b>',
             '<b> Percentage of Population </b>'
             )
line_plot(poverty_line,
             df.iloc[:,0],
             df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'],
             'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
             '<b>Poverty - Headcount Ratio at $2.15 a Day (2017 Purchasing Power Parity)</b>',
             '<b> Percentage of Population </b>')
bar_plot(poverty_bar,
             df.iloc[:,0],
             df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'],
             'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
             '<b>Poverty - Headcount Ratio at $2.15 a Day (2017 Purchasing Power Parity)</b>',
             '<b> Percentage of Population </b>',
             df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'].astype(float).min(),
             df.loc[:,'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'].astype(float).max())

st.sidebar.header('Demography')
st.sidebar.write("This page displays the temporal evolution of Brazil's demography.")

st.header('Population Over Time')

tab_1, tab_2, tab_3, tab_4 = st.tabs(["Population", "Urban Population", "Population Density", "Poverty"])

with tab_1:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=1
)
    if option == "Scatter":
        st.plotly_chart(population_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(population_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(population_bar, use_container_width=True)

with tab_2:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=2
)
    if option == "Scatter":
        st.plotly_chart(urban_pop_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(urban_pop_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(urban_pop_bar, use_container_width=True)

with tab_3:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=3
)
    if option == "Scatter":
        st.plotly_chart(density_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(density_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(density_bar, use_container_width=True)

with tab_4:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=4
)
    if option == "Scatter":
        st.plotly_chart(poverty_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(poverty_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(poverty_bar, use_container_width=True)