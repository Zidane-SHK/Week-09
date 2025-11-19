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
st.markdown('**Bold** & *Italic*')
st.markdown("> This is a blockquote. It will be rendered with a distinct visual style, often with an indentation and a vertical line on the left, to set it apart from the surrounding text.")
st.divider()
name = st.text_input('name')
if st.button('submit'):
    if name:
        st.success(
            (f'Hello {name}')
        )
    else:
        st.warning('Enter name')

col1, col2, col3 = st.columns([1, 2, 1]) # Adjust column ratios for desired spacing

with col1:
    st.button("Left Button")

with col2:
    st.button("Center Button")

with col3:
    st.button("Right Button")
