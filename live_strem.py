import streamlit as st 
import requests 
url = requests.get("https://www.google.com/finance/?hl=en")
print(url.text)
