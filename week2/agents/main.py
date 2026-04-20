
import streamlit as st
import langchain_helper
import time


st.title("Question Answering with Ollama")

chat = st.sidebar.chat_input("Type anything")

print(f"Chat message: {chat}")

if chat:
  st.subheader(f"Your question: {chat}")
  with st.spinner("Generating response"):
      start_time = time.time()
      response = langchain_helper.generateChatResponse(chat)
      elapsed = time.time() - start_time
  print(f"Generated response: {response}")

  st.subheader("Agent's response:")
  st.write(response)
  st.info(f"⏱️ Generated in {elapsed:.2f} seconds")
  