import streamlit as st
import pandas as pd
import joblib
from PIL import Image

st.set_page_config(layout="wide")

header = st.container()
dataset = st.container()
recommendation = st.container()

with header:
    header_ = '<p style="font-family:sans-serif; color:DarkGreen; font-size: 60px;">DEEP MOVIE RECOMMENDATION</p>'
    st.markdown(header_, unsafe_allow_html=True)
    text0 = '<p style="font-family:Courier; color:midnightblue; font-size: 24px;">With this application, we would like to make a list of movies that you will love watching!</p>'
    st.markdown(text0, unsafe_allow_html=True)
    #st.text('With this application, we would like to make a list of movies that you will love watching!')

with dataset:
    st.header('WE RECOMMEND MOVIES FROM')
    col1, col2, col3 = dataset.columns(3)
    logo_netflix = Image.open('source/image_streamlit/netflix.jpg')
    logo_amazon_prime = Image.open('source/image_streamlit/primevideo.png')
    logo_apple_tv = Image.open('source/image_streamlit/apple_tv.png')
    logo_hbo = Image.open('source/image_streamlit/hbo.jpg')
    logo_disney = Image.open('source/image_streamlit/disney.png')
    logo_paramount = Image.open('source/image_streamlit/paramount.png')
    with col1:
        st.image(logo_netflix)
        st.image(logo_hbo)
    with col2:
        st.image(logo_amazon_prime)
        st.image(logo_apple_tv)
    with col3:
        st.image(logo_paramount)
        st.image(logo_disney)

with recommendation:
    st.header('LET US MAKE RECOMMENDATION TO YOU')
    text1 = '<p style="font-family:Courier; color:blueviolet; font-size: 20px;">Now you show us one of your favourite movie ...</p>'
    st.markdown(text1, unsafe_allow_html=True)
    text2 = '<p style="font-family:Courier; color:blueviolet; font-size: 20px;">... then let we recommend you movies that you will love</p>'
    st.markdown(text2, unsafe_allow_html=True)
      
    frame = joblib.load('source/model/pickle_frame.joblib')
    movie_chosen = st.selectbox('SELECT or TYPE here below the movie you loved watching:', options=[title for title in frame.columns.sort_values()])
    st.write('Your favourite movie chosen:', movie_chosen)
   
    st.subheader('Here are movies that we recommend you:')
    recommendation_list = list(frame[movie_chosen].sort_values(ascending=False)[1:11].index.values)
    title = ''
    for i in recommendation_list:
        title += "- " + i + "\n"
    st.markdown(title)
   
  