import streamlit as st
import time
x = st.slider(1, 10)
while x < 10:
    x += 1
    st.write("*"*x)
