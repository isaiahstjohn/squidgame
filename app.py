import streamlit as st
import time
import random
import pandas as pd
import altair as alt

def altair_chart(points):
    players, survivors = (list(axis) for axis in zip(*points))
    data = pd.DataFrame({
        'Players': players, 
        'Survivors': survivors, 
        'size': [300]*len(players),
    })
    chart = alt.Chart(data).mark_point().encode(
        x = 'Players',
        y = 'Survivors',
        size = 'size',
        tooltip = ['Players', 'Survivors']
    ).properties(
        width = 600,
        height = 400,
    ).configure_mark(
        shape = "square",
        filled = True,
        color = "#FF0000",
        size = 9900,
    )
    return chart
points = []
bridge_box = st.empty()
scatter_box = st.empty()
#bridge_box.bar_chart([], width = 20, height = 2)
#scatter_box.altair_chart(altair_chart(points))

bridge = [0]*10


for s, step in enumerate(bridge):
    ch = random.choice([1, 2])
    bridge[s] = ch
    points.append([s, ch])
    scatter_box.altair_chart(altair_chart(points))
    bridge_box.bar_chart(bridge)
    if bridge[s] == 0:
        break

rerun = st.button("Rerun")
