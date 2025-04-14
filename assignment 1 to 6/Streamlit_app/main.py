import streamlit as st
from PIL import Image

st.set_page_config(page_title="Tasty Bites", page_icon="🍔", layout="wide")

# Title
st.title("🍽️ Welcome to Tasty Bites!")
st.markdown("Enjoy delicious food at your doorstep.")

# Sidebar Menu
menu = st.sidebar.radio("Choose Category", ["Home", "Burgers", "Pizza", "Drinks"])

# Home
if menu == "Home":
    st.image("images/pizza.png", use_container_width=True)
    st.header("🔥 Our Specials")
    st.markdown("""
    - 🍕 Pizza loaded with cheese  
    - 🍔 Juicy double patty burgers  
    - 🥤 Chilled soft drinks  
    - 🛵 Fast delivery in 30 mins!
    """)

# Burgers
elif menu == "Burgers":
    st.header("🍔 Burgers")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/burger.png", width=250)
    with col2:
        st.subheader("Classic Burger")
        st.write("Price: $5.99")
        if st.button("Order Classic Burger"):
            st.success("✅ Classic Burger added to cart!")

# Pizza
elif menu == "Pizza":
    st.header("🍕 Pizza")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/pizza 1.png", width=250)
    with col2:
        st.subheader("Pepperoni Pizza")
        st.write("Price: $8.99")
        if st.button("Order Pizza"):
            st.success("✅ Pizza added to cart!")

# Drinks
elif menu == "Drinks":
    st.header("🥤 Drinks")
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/drink.png", width=250)
    with col2:
        st.subheader("Chilled Cola")
        st.write("Price: $1.99")
        if st.button("Order Cola"):
            st.success("✅ Cola added to cart!")

# Footer
st.markdown("---")
st.markdown("© 2025 Tasty Bites | Made with ❤️ using Streamlit")
