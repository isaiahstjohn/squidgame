import streamlit as st
import time
import random
import pandas as pd
import altair as alt

def altair_chart(points):
    players, survivors = (list(axis) for axis in zip(*points))
    data = pd.DataFrame({'Players': players, 'Survivors': survivors})
    chart = alt.Chart(data).mark_point().encode(
        x = 'Players',
        y = 'Survivors',
        tooltip = ['Players', 'Survivors']
    )
    return chart
points = [[2, 0], [3, 1], [4, 4]]
bridge_box = st.empty()
scatter_box = st.empty()
scatter = st.altair_chart(altair_chart(points))
bridge = bridge_box.bar_chart([], width = 20, height = 2)

bridge = [0]*10


for s, step in enumerate(bridge):
    bridge[s] = random.choice([0, 1])
    bridge_box.bar_chart(bridge)
    if bridge[s] == 0:
        break

rerun = st.button("Rerun")
