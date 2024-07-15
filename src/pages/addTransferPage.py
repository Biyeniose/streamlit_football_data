import streamlit as st

st.button("Try Supabase", type="secondary")

# when you press enter it updates
title = st.text_input("Function name", "insert_player.pyS")
st.write("The current movie title is", title)