import streamlit as st
import time
import random

bridge = [0]*10


bridge_box = st.empty()
for s, step in range(bridge):
    bridge[s] = random.choice([0, 10])
    bridge_box.bar_chart(bridge)
    if bridge[s] = 0:
        break
