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

gdp_scatter = go.Figure()
gdp_line = go.Figure()
gdp_bar = go.Figure()
scatter_plot(gdp_scatter,
             df.iloc[:, 0],
             df.loc[:, 'GDP (current US$)'],
             'GDP (Current US$)',
             '<b>Gross Domestic Product (GDP)</b>',
             '<b>Dollars</b>'
             )
line_plot(gdp_line,
             df.iloc[:, 0],
             df.loc[:, 'GDP (current US$)'],
             'GDP (Current US$)',
             '<b>Gross Domestic Product (GDP)</b>',
             '<b>Dollars</b>')
bar_plot(gdp_bar,
             df.iloc[:, 0],
             df.loc[:, 'GDP (current US$)'],
             'GDP (Current US$)',
             '<b>Gross Domestic Product (GDP)</b>',
             '<b>Dollars</b>',
             df.loc[:, 'GDP (current US$)'].astype(float).min(),
             df.loc[:, 'GDP (current US$)'].astype(float).max()
             )

share_scatter = go.Figure()
share_line = go.Figure()
share_bar = go.Figure()
scatter_plot(share_scatter,
             df.iloc[:, 0],
             df.loc[:, 'Income share held by lowest 20%'],
             'Income Share Held by Lowest 20%',
             '<b>Income Share Held by Lowest 20%</b>',
             '<b>Share</b>'
             )
line_plot(share_line,
             df.iloc[:, 0],
             df.loc[:, 'Income share held by lowest 20%'],
             'Income Share Held by Lowest 20%',
             '<b>Income Share Held by Lowest 20%</b>',
             '<b>Share</b>')
bar_plot(share_bar,
             df.iloc[:, 0],
             df.loc[:, 'Income share held by lowest 20%'],
             'Income Share Held by Lowest 20%',
             '<b>Income Share Held by Lowest 20%</b>',
             '<b>Share</b>',
             df.loc[:, 'Income share held by lowest 20%'].astype(float).min(),
             df.loc[:, 'Income share held by lowest 20%'].astype(float).max()
             )

gni_scatter = go.Figure()
gni_line = go.Figure()
gni_bar = go.Figure()
scatter_plot(gni_scatter,
             df.iloc[:, 0],
             df.loc[:, 'GNI, PPP (current international $)'],
             'GNI, PPP (current international $)',
             '<b>Gross National Income (GNI) Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>'
             )
line_plot(gni_line,
             df.iloc[:, 0],
             df.loc[:, 'GNI, PPP (current international $)'],
             'GNI, PPP (current international $)',
             '<b>Gross National Income (GNI) Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>')
bar_plot(gni_bar,
             df.iloc[:, 0],
             df.loc[:, 'GNI, PPP (current international $)'],
             'GNI, PPP (current international $)',
             '<b>Gross National Income (GNI) Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>',
             df.loc[:, 'GNI, PPP (current international $)'].astype(float).min(),
             df.loc[:, 'GNI, PPP (current international $)'].astype(float).max()
             )

gni_pc_scatter = go.Figure()
gni_pc_line = go.Figure()
gni_pc_bar = go.Figure()
scatter_plot(gni_pc_scatter,
             df.iloc[:, 0],
             df.loc[:, 'GNI per capita, PPP (current international $)'],
             'GNI per capita, PPP (current international $)',
             '<b>Gross National Income (GNI) per Capita Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>'
             )
line_plot(gni_pc_line,
             df.iloc[:, 0],
             df.loc[:, 'GNI per capita, PPP (current international $)'],
             'GNI per capita, PPP (current international $)',
             '<b>Gross National Income (GNI) per Capita Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>')
bar_plot(gni_pc_bar,
             df.iloc[:, 0],
             df.loc[:, 'GNI per capita, PPP (current international $)'],
             'GNI per capita, PPP (current international $)',
             '<b>Gross National Income (GNI) per Capita Based on Purchasing Power Parity</b>',
             '<b>Dollars</b>',
             df.loc[:, 'GNI per capita, PPP (current international $)'].astype(float).min(),
             df.loc[:, 'GNI per capita, PPP (current international $)'].astype(float).max()
             )

st.sidebar.header('Economical Aspects')
st.sidebar.write('This page displays the temporal evolution of Brazilian development indicators on the economical sphere.')

st.title('Economy Over Time')

tab_1, tab_2, tab_3, tab_4 = st.tabs(["GDP", "GNI", "GNI per Capita", "Income Share"])

with tab_1:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=1
)
    if option == "Scatter":
        st.plotly_chart(gdp_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(gdp_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(gdp_bar, use_container_width=True)

with tab_2:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=2
)
    if option == "Scatter":
        st.plotly_chart(gni_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(gni_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(gni_bar, use_container_width=True)

with tab_3:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=3
)
    if option == "Scatter":
        st.plotly_chart(gni_pc_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(gni_pc_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(gni_pc_bar, use_container_width=True)

with tab_4:
    option = st.selectbox(
    "Select the type of graph to be displayed",
    ('Scatter', 'Line', 'Bar'),
    index=None,
    placeholder='Choose an option',
    key=4
)
    if option == "Scatter":
        st.plotly_chart(share_scatter, use_container_width=True)
    elif option == "Line":
        st.plotly_chart(share_line, use_container_width=True)
    elif option == "Bar":
        st.plotly_chart(gni_bar, use_container_width=True)