import streamlit as st

st.set_page_config(
    page_title="Credit Risk Analysis",
    page_icon="📊",
    layout="wide"
)

home = st.Page(
    "pages/Home.py",
    title="Home",
    icon="🏠"
)

univariate = st.Page(
    "pages/Univariate_analysis.py",
    title="Univariate Analysis",
    icon="📊"
)

bivariate = st.Page(
    "pages/Bivariate_analysis.py",
    title="Bivariate Analysis",
    icon="📈"
)

Sql_queries=st.Page(
    "pages/Sql_queries.py",
    title="SQL Queries",
    icon="🛢️"
)
pg = st.navigation({
    "Dashboard": [home],
    "Exploratory Data Analysis": [univariate, bivariate],
    "SQL Queries":[Sql_queries]

})

pg.run()