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
            tickfont=dict(size=12),
            range=[y_axis_min, y_axis_max]
            )
    )

forest_scatter = go.Figure()
forest_line = go.Figure()
forest_bar = go.Figure()
scatter_plot(forest_scatter,
             df.iloc[:,0], df.loc[:,'Forest area (sq. km)'],
            'Forest area (sq. km)',
            '<b>Forest Area</b>',
            '<b>Area (sq. km)</b>')
line_plot(forest_line, df.iloc[:,0],
          df.loc[:,'Forest area (sq. km)'],
          'Forest area (sq. km)',
          '<b>Forest Area</b>',
          '<b>Area (sq. km)</b>')
bar_plot(forest_bar, df.iloc[:,0],
         df.loc[:,'Forest area (sq. km)'],
         'Forest area (sq. km)',
         '<b>Forest Area</b>',
         '<b>Area (sq. km)</b>',
         df.loc[:,'Forest area (sq. km)'].astype(float).min(),
         df.loc[:,'Forest area (sq. km)'].astype(float).max())


emission_scatter = go.Figure()
emission_line = go.Figure()
emission_bar = go.Figure()
scatter_plot(emission_scatter,
             df.iloc[:,0],
             df.loc[:,'CO2 emissions (metric tons per capita)'],
             'CO2 emissions (metric tons per capita)',
             '<b>CO2 Emissions</b>',
             '<b>Emission (metric tons per capita)</b>')
line_plot(emission_line, 
          df.iloc[:,0],
          df.loc[:,'CO2 emissions (metric tons per capita)'],
          'CO2 emissions (metric tons per capita)',
          '<b>CO2 Emissions</b>',
          '<b>Emission (metric tons per capita)</b>')
bar_plot(emission_bar,
         df.iloc[:,0],
         df.loc[:,'CO2 emissions (metric tons per capita)'],
         'CO2 emissions (metric tons per capita)',
         '<b>CO2 Emissions</b>',
         '<b>Emission (metric tons per capita)</b>',
         df.loc[:,'CO2 emissions (metric tons per capita)'].astype(float).min(),
         df.loc[:,'CO2 emissions (metric tons per capita)'].astype(float).max())

energy_scatter = go.Figure()
energy_line = go.Figure()
energy_bar = go.Figure()
scatter_plot(energy_scatter, df.iloc[:,0],
             df.loc[:,'Electric power consumption (kWh per capita)'],
             'Electric power consumption (kWh per capita)',
             '<b>Electric Power Consumption per Capita</b>',
             '<b>kWh per capita</b>')
line_plot(energy_line, df.iloc[:,0],
          df.loc[:,'Electric power consumption (kWh per capita)'],
          'Electric power consumption (kWh per capita)',
          '<b>Electric Power Consumption per Capita</b>',
          '<b>kWh per capita</b>')
bar_plot(energy_bar, df.iloc[:,0],
         df.loc[:,'Electric power consumption (kWh per capita)'],
         'Electric power consumption (kWh per capita)',
         '<b>Electric Power Consumption per Capita</b>',
         '<b>kWh per capita</b>',
          df.loc[:,'Electric power consumption (kWh per capita)'].astype(float).min(),
        df.loc[:,'Electric power consumption (kWh per capita)'].astype(float).max())

protected_scatter = go.Figure()
protected_line = go.Figure()
protected_bar = go.Figure()
scatter_plot(protected_scatter,
             df.iloc[:,0],
             df.loc[:,'Terrestrial and marine protected areas (% of total territorial area)'],
             'Terrestrial and marine protected areas (% of total territorial area)',
             '<b>Terrestrial and Marine Protected Areas</b>',
             '<b>Percentage of Total Territorial Area</b>')
line_plot(protected_line, df.iloc[:,0],
          df.loc[:,'Terrestrial and marine protected areas (% of total territorial area)'],
          'Terrestrial and marine protected areas (% of total territorial area)',
          '<b>Terrestrial and Marine Protected Areas</b>',
          '<b>Percentage of Total Territorial Area</b>' )
bar_plot(protected_bar, df.iloc[:,0],
         df.loc[:,'Terrestrial and marine protected areas (% of total territorial area)'],
         'Terrestrial and marine protected areas (% of total territorial area)',
         '<b>Terrestrial and Marine Protected Areas</b>',
         '<b>Percentage of Total Territorial Area</b>',
         df.loc[:,'Terrestrial and marine protected areas (% of total territorial area)'].astype(float).min(),
         df.loc[:,'Terrestrial and marine protected areas (% of total territorial area)'].astype(float).max())

st.sidebar.header('Management of Nature')
st.sidebar.write('This page displays the temporal evolution of Brazilian development indicators related to nature.')

st.title('Nature Management Over Time')

tab_1, tab_2, tab_3, tab_4 = st.tabs(["Forest", "CO2 Emissions", "Protected Areas", "Electric Power Consumption"])

with tab_1:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=1
)
    if option == "Scatter":
        st.plotly_chart(forest_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(forest_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(forest_bar, use_container_width=True)

with tab_2:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=2
)
    if option == "Scatter":
        st.plotly_chart(emission_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(emission_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(emission_bar, use_container_width=True)

with tab_3:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=3
)
    if option == "Scatter":
        st.plotly_chart(protected_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(protected_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(protected_bar, use_container_width=True)

with tab_4:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=4
)
    if option == "Scatter":
        st.plotly_chart(energy_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(energy_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(energy_bar, use_container_width=True)