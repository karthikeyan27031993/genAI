
import streamlit as st
import langChain_helper as lch
sentiment_mapping = ["one", "two", "three", "four", "five"]

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian","Chinese", "Malay","Mexican"))

if cuisine:

    feedback = st.feedback(options="stars", key=None, disabled=False, on_change=None, args=None, kwargs=None)
    menu_items = lch.generate_restaurant_name_and_items(cuisine)
    for item in menu_items:
        st.write("-", item)

    if feedback is not None:
        st.markdown(f"You selected {sentiment_mapping[feedback]} star(s).")

