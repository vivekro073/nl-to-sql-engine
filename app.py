import requests
import streamlit as st

st.set_page_config(page_title="SQL Data Assistant", page_icon="📊")
st.title("📊 Natural Language to SQL Engine")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input(
    "Ask a question (e.g., Show me total revenue per product...)"
):
    # Render user prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Call your FastAPI endpoint
    with st.chat_message("assistant"):
        with st.spinner("Analyzing database..."):
            try:
                # Assuming POST endpoint on FastAPI (or encode params for GET)
                response = requests.get(f"http://127.0.0.1:8000/analyze/{prompt}")
                if response.status_code == 200:
                    answer = response.json().get("result", "No result returned.")
                    st.write(answer)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")