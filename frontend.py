from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

#Setup UI
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 User Defined Chatbot Agents")
st.markdown("Create and Interact with powerful LLM agents using Groq!")

#System prompt input
system_prompt = st.text_area(
    "🛠️ Define your AI Agent (System Prompt):",
    height=70,
    placeholder="Type your system prompt here (e.g., You are a helpful assistant)..."
)

#Groq model options
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","llama-3.1-8b-instant"]

#Only Groq for now
provider = st.radio("🧠 Select Provider:", ("Groq",), index=0)
selected_model = st.selectbox("📦 Select Groq Model:", MODEL_NAMES_GROQ)

#Web search toggle
allow_web_search = st.checkbox("🔍 Enable Web Search via Tavily")

#User query
user_query = st.text_area("💬 Enter your query:", height=150, placeholder="Ask anything!")

#Backend FastAPI URL
API_URL = "http://127.0.0.1:9999/chat"

#Ask button
if st.button("🚀 Ask Agent"):
    if user_query.strip():
        # Construct payload
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(f"❌ Error: {response_data['error']}")
                else:
                    st.subheader("✅ Agent Response")
                    st.markdown(f"**{response_data.get('response', 'No response returned')}**")
            else:
                st.error(f"❌ Request failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Exception occurred: {e}")
    else:
        st.warning("Please enter a query first.")

