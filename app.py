import streamlit as st
import time
import random
import pandas as pd
import altair as alt

min_players = st.slider(
    "Minimum players",
    min_value = 1,
    max_value = 20,
    step = 1)

max_players = st.slider(
    "Maximum players",
    min_value = min_players,
    max_value = 20,
    step = 1)

steps = st.slider(
    "Number of glass steps on the bridge",
    min_value = 1,
    max_value = 20,
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
        size = alt.value(300),
        tooltip = ['Players', 'Survivors'],
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
bridge = [0]*20
header_box = st.empty()
sub_box = st.empty()
bridge_box = st.empty()
scatter_box = st.empty()

for players in range(min_players, max_players + 1):
    header_box.header(f"{players} players")
    survivors = 0
    for player in range(players):
        sub_box.subheader(f"Player {player}")
        bridge = []
        for step in range(1, steps + 1):
            alive = random.choice([True, False])
            bridge.append(1 if alive else 0)
            bridge_box.bar_chart(bridge)
            if not alive:
                break
        if alive: 
            survivors = players - player
    points.append([players, survivors]) 
    scatter_box.altair_chart(altair_chart(points))

rerun = st.button("Rerun")
