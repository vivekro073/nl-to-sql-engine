import requests
import streamlit as st

#VERCEL_API_URL = "https://nl-to-sql-engine.vercel.app/analyze"


import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Natural Language SQL Engine",
    page_icon="⚡",
    layout="centered"
)

# Backend Vercel Endpoint URL
VERCEL_API_URL = "https://nl-to-sql-engine.vercel.app/analyze"

# 1. Title
st.title("⚡ Natural Language SQL Engine")
st.caption("Ask questions in plain English—our AI agent translates them into SQL queries against the live database.")

# 2. Database Overview & Schema (Top Section)
with st.expander("📊 **Database Context & Schema Details**", expanded=False):
    tab1, tab2 = st.tabs(["📦 Products Table", "💳 Transactions Table"])

    with tab1:
        st.markdown("**Table:** `products` (20 items total)")
        st.markdown("""
        Contains store catalog details including product categories, pricing, and stock levels.

        *Sample Items:*
        * **Wireless Headphones** (Category: *Electronics*, Price: *$120.00*, Stock: *45*)
        * **Ergonomic Office Chair** (Category: *Furniture*, Price: *$250.00*, Stock: *12*)
        * **Stainless Steel Water Bottle** (Category: *Home & Kitchen*, Price: *$25.00*, Stock: *80*)
        * **Mechanical Gaming Keyboard** (Category: *Electronics*, Price: *$95.00*, Stock: *8*)
        """)

    with tab2:
        st.markdown("**Table:** `transactions` (100 records total)")
        st.markdown("""
        Contains customer purchase logs linked via `product_id`.

        *Sample Transactions:*
        * **ID #101:** Product ID `1` | Qty: `2` | Total: `$240.00` | Date: `2026-06-15`
        * **ID #102:** Product ID `4` | Qty: `1` | Total: `$95.00`  | Date: `2026-06-18`
        * **ID #103:** Product ID `2` | Qty: `3` | Total: `$750.00` | Date: `2026-07-02`
        """)

# 3. Initialize Conversation Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Render Conversation History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 5. Search Box Pinned to the Bottom
if prompt := st.chat_input("Ask a question about sales, products, or revenue..."):

    # Render user prompt immediately in UI
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Fetch answer from backend
    with st.chat_message("assistant"):
        with st.spinner("Translating to SQL & querying database..."):
            try:
                # Strip leading/trailing newlines to ensure clean HTTP parameter parsing
                clean_prompt = prompt.strip()

                response = requests.get(
                    f"{VERCEL_API_URL}/analyze",
                    params={"prompt": clean_prompt}
                )

                if response.status_code == 200:
                    answer = response.json().get("result")
                    st.write(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    error_msg = f"Error {response.status_code}: {response.text}"
                    st.error(error_msg)
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")