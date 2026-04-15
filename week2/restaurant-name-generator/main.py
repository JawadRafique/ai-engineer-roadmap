
import streamlit as st
import langchain_helper
import time


st.title("Restaurant Name Generator with Ollama")

cuisine = st.sidebar.selectbox("Select a cuisine", ["Pakistani","Italian", "Chinese", "Mexican", "Indian", "French"])

print(f"Selected cuisine: {cuisine}")

if cuisine:
  print(f"Generating restaurant name and menu for cuisine: {cuisine}")
  with st.spinner("Generating restaurant name and menu..."):
    start_time = time.time()
    response = langchain_helper.generate_restaurant_name_and_menu(cuisine)
    elapsed = time.time() - start_time
  print(f"Generated response: {response}")
  st.subheader(f"Suggested Restaurant Name: {response['restaurant_name'].strip()}")
  st.subheader("Suggested Menu:")
  for dish in response['menu'].split(","):
    st.write(f"- {dish.strip()}")
  st.info(f"⏱️ Generated in {elapsed:.2f} seconds")