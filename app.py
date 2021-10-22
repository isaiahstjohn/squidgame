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
    max_value = 100,
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

update_chart = st.checkbox("Update chart during simulation")

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
        color = "#FF0000",
        opacity = 0.1,
        size = 9900,
    )
    return chart
points = []
header_box = st.empty()
sub_box = st.empty()
scatter_box = st.empty()

any_survivors = False
for i in range(iterations):
    for players in range(min_players, max_players + 1):
        header_box.header(f"{players} players")
        survivors = 0
        last_step_reached = 0
        for player in range(players):
            for step in range(last_step_reached, steps):
                alive = random.choice([True, False])
                if not alive:
                    break
            if alive: 
                survivors = players - player
                any_survivors = True
                break
            else:
                last_step_reached = step + 1
        points.append([players, survivors/players]) 
        if any_survivors and update_chart:
            scatter_box.altair_chart(altair_chart(points))
scatter_box.altair_chart(altair_chart(points))

rerun = st.button("Rerun")
