import streamlit as st
from scrape import scrape_website


st.title("AI web Scrapper")
url=st.text_input("Enter a website URL:")
if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)