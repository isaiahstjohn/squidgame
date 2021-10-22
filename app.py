import streamlit as st
import time
import random
import pandas as pd
import altair as alt

min_players = st.slider(
    "Minimum players",
    min_value = 1,
    max_value = 100,
    step = 1)

max_players = st.slider(
    "Maximum players",
    min_value = min_players,
    max_value = 100 if min_players < 100 else 101,
    step = 1)

steps = st.slider(
    "Number of glass steps on the bridge",
    min_value = 1,
    max_value = 100,
    step = 1)

iterations = st.slider(
    "Number of trials to run",
    min_value = 1,
    max_value = 1000,
    step = 1)

def altair_chart(points):
    players, survivors = (list(axis) for axis in zip(*points))
    data = pd.DataFrame({
        'Players': players, 
        'Survivors': survivors, 
    })
    chart = alt.Chart(data).mark_point().encode(
        x = 'Players',
        y = 'Survivors',
        size = alt.value(100),
        tooltip = ['Players', 'Survivors'],
    ).properties(
        width = 600,
        height = 400,
    ).configure_mark(
        shape = "square",
        filled = True,
        color = "#990000",
        opacity = 0.05,
        size = 9900,
    )
    return chart
points = []
progress_box = st.empty()
scatter_box = st.empty()

for i in range(iterations):
    if i % 20 == 0:
        progress_box.progress((i+1)/iterations)
    for players in range(min_players, max_players + 1):
        survivors = 0
        last_step_reached = 0
        for player in range(players):
            if last_step_reached == steps:
                survivors = players - player
                break
            for step in range(last_step_reached, steps):
                alive = random.choice([True, False])
                if not alive:
                    break
            if alive:
                survivors = players - player
                break
            else:
                last_step_reached = step + 1
        points.append([players, survivors/players]) 
scatter_box.altair_chart(altair_chart(points))
progress_box.empty()

rerun = st.button("Rerun")
