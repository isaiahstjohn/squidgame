import streamlit as st
import time
x = st.slider("Value", 0, 10)
while x < 1000:
    x += 1
    st.write("|X| "*x)
