import streamlit as st
import pandas as pd
import numpy as np
st.title('Testing')
st.header('Header')
st.subheader('Subheader')
st.markdown('**Bold** & **Italic**')
st.write('Trying out Streamlit')
st.caption('123, Testing')
# st.image (path or link)
name = st.text_input('Name: ')
age = st.number_input(
    'Age', min_value = 0,
    max_value = 120, value = 25
)
val = st.slider(
    'Choose',
    0, 100, 50
)
color = st.selectbox(
    'Favorite Color',
    ['Blue', 'Purple', 'Red']
)
shirt = st.multiselect(
    'Choose a shirt',
    ['White', 'Black']
)
agree = st.checkbox('Agree')
if st.button('Click'):
    st.write('Clicked')
date = st.date_input('Date')
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['A', 'B', 'C']
)
st.line_chart(data)
st.header('Images')
st.image(
 "https://streamlit.io/images/brand/streamlit-logo-secondarycolormark-darktext.png",
 caption="Streamlit logo",
)
