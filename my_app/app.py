import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Layout Demo", layout="wide")
st.title("1. Layout Demo -- Building a Simple Dashboard")

#Side-bar

with st.sidebar:
    st.header('Controls')
    points = st.slider('No. Points', 10, 500, 100)
    table = st.checkbox('Raw data')

#Main
st.header('Main content')
data = pd.DataFrame(
    np.random.randn(points, 3),
    columns = ['Feature 1', 'Feature 2', 'Feature 3']
)
col1, col2 = st.columns(2)

with col1:
    st.header('Line Chart')
    st.line_chart(data)

with col2:
    st.header('Bar Chart')
    st.bar_chart(data)

with st.expander('Raw data'):
    if table:
        st.dataframe(data)
    else:
        st.info('--')
