import requests
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Intelligence Hub",
    page_icon="⚡",
    layout="centered"
)

# 1. New Title & Tagline
st.title("⚡ Text-to-SQL Data Assistant")
st.caption("Ask natural language questions to query live sales and inventory data.")

# 2. Database Overview with Detailed Samples
with st.expander("📊 **Database Context & Schema Details**", expanded=True):
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

st.divider()

# 3. Search Bar with Increased Vertical Size
st.subheader("🔍 Ask a Question")

# Using st.text_area with fixed height gives a larger vertical footprint
user_prompt = st.text_area(
    label="Search query:",
    placeholder="e.g., Which products are low on stock (less than 15 items) and how many sales have they had?",
    height=75,
    label_visibility="collapsed"
)

VERCEL_API_URL = "https://nl-to-sql-engine.vercel.app/analyze"
# Execution Logic
if st.button("Run Query", type="primary") or user_prompt:
    if user_prompt.strip():
        with st.spinner("Analyzing schema, generating SQL, and retrieving results..."):
            try:
                response = requests.get(f"{VERCEL_API_URL}/analyze/{user_prompt}")
                if response.status_code == 200:
                    st.success("Query Result:")
                    st.write(response.json().get("result"))
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")