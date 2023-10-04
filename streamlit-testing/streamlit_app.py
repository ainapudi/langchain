import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')
openai_api_key = st.write("Secret Key", st.secrets["openai_secret_key"])

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  st.text_area('My Key:', openai_api_key)
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted:
  # and openai_api_key.startswith('sk-'):
    generate_response(text)