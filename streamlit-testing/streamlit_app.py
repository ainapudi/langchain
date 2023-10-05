import os
import streamlit as st
from langchain.llms import OpenAI
import requests

st.title('🦜🔗 Quickstart App')
st.write(
    "Has environment variables been set:",
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)

def generate_response(input_text):
  llm = OpenAI(temperature=0.7)

  st.info(llm(input_text))

def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}

payload = {
    "agentId": "HZV7VSADRY",
    "agentAliasId": "TSTALIASID",
    "sessionId": "session",
    "inputText": "How many pets are available for adoption?"
}

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  openai_api_key = os.environ["OPENAI_API_KEY"]
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    r = requests.post(
                'https://invoke-agent-bedrock.us-east-1.amazonaws.com',
                data=payload)

    st.info("testing")
    st.info(r.content.decode())
    generate_response(text)