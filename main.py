import streamlit as st
from newsapi import NewsApiClient

api = NewsApiClient(api_key='c565197765884fc588aac5841918a58f')

st.title('News Curator by Abideen')
st.sidebar.write('Welcome to my page')
st.sidebar.button('click me')

topic = st.text_input("Enter the topic you want to get: ")

news = api.get_top_headlines(
    q=topic,
    language='en',
    qintitle=topic
)

for article in news['articles']:
    st.write('Title : ', article['title'])
    st.write('Author : ', article['author'])
    st.write('Description : ', article['description'], '\n\n')
    st.write('Link : ', article['url'])
    st.write('Sources : ', article['source']['name'])
    st.write("*" * 200)
if topic == "Nothing" :
    st.write("Sorry, no result")
elif topic == 'nothing':
    st.write("Sorry, no result")