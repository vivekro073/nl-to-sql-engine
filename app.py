import requests
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="E-Commerce Natural Language SQL Agent",
    page_icon="🤖",
    layout="centered"
)

# Title & Description
st.title("🤖 E-Commerce Data Assistant")
st.markdown("Ask natural language questions about our store's inventory and transactions.")

# 1. Database Context First
with st.expander("📊 **Database Overview & What You Can Ask**", expanded=True):
    st.write(
        "This assistant queries a **Neon PostgreSQL** database storing simulated e-commerce operations:"
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **📦 `products` Table (20 items)**
        * `product_id`, `name`
        * `category`, `price`
        * `stock_quantity`
        """)
    with col2:
        st.markdown("""
        **💳 `transactions` Table (100 records)**
        * `transaction_id`, `product_id`
        * `quantity_sold`, `total_amount`
        * `sale_date`
        """)

    st.markdown("**💡 Example Questions to Try:**")
    st.caption("• *What are the top 3 best-selling products by total revenue?*")
    st.caption("• *List all products with stock quantity less than 15.*")
    st.caption("• *What was our total sales volume across all categories?*")

st.divider()

# 2. Search Bar Directly Below Database Context
st.subheader("🔍 Ask a Question")
user_prompt = st.text_input(
    label="Ask a question:",
    placeholder="e.g., Which electronics generated the highest revenue?",
    label_visibility="collapsed"
)

# Backend Vercel URL

VERCEL_API_URL = "https://nl-to-sql-engine.vercel.app/analyze"

# Query Execution
if user_prompt:
    with st.spinner("Analyzing schema, drafting SQL, and fetching results..."):
        try:
            response = requests.get(f"{VERCEL_API_URL}/analyze/{user_prompt}")
            if response.status_code == 200:
                st.success("Result:")
                st.write(response.json().get("result"))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Could not connect to backend: {e}")