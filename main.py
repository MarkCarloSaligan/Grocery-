import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Grocery App", page_icon="🛒", layout="wide")

# SIDEBAR NAVIGATION
st.sidebar.title("🛒 Grocery Navigation")
page = st.sidebar.radio(
    "Go to:",
    [
        "Home",
        "Grocery Shop",
        "Cart Summary",
        "Deals & Discounts",
        "Nutrition Info",
        "Customer Feedback",
        "About"
    ]
)

# USER SETTINGS
st.sidebar.header("User Settings")
name = st.sidebar.text_input("Enter your name")
budget = st.sidebar.slider("Your grocery budget", 0, 5000, 1000)
newsletter = st.sidebar.checkbox("Subscribe to grocery deals")

# HOME PAGE
if page == "Home":

    st.title("🛒 Smart Grocery Store App")

    st.write("Welcome to the grocery shopping demo app!")

    st.image(
        "https://images.unsplash.com/photo-1542838132-92c53300491e",
        caption="Fresh Grocery Items"
    )

    st.success("Use the sidebar to explore the app.")

    st.info("Tip: Visit the Grocery Shop page to select items!")

    st.progress(40)

    st.metric("Available Categories", "5")

    st.button("Start Shopping")

# GROCERY SHOP
elif page == "Grocery Shop":

    st.title("🛍 Grocery Shop")

    st.subheader("Select your grocery items")

    fruits = st.multiselect(
        "Choose Fruits",
        ["Apple", "Banana", "Orange", "Mango", "Grapes"]
    )

    vegetables = st.multiselect(
        "Choose Vegetables",
        ["Carrot", "Potato", "Tomato", "Cabbage", "Onion"]
    )

    dairy = st.selectbox(
        "Choose Dairy Product",
        ["Milk", "Cheese", "Butter", "Yogurt"]
    )

    quantity = st.number_input("Quantity", 1, 20)

    delivery = st.radio(
        "Delivery Option",
        ["Pickup", "Home Delivery"]
    )

    delivery_date = st.date_input("Delivery Date")

    delivery_time = st.time_input("Delivery Time")

    payment = st.select_slider(
        "Payment Method",
        options=["Cash", "GCash", "Credit Card"]
    )

    note = st.text_area("Special Instructions")

    agree = st.checkbox("Confirm your order")

    if st.button("Submit Order"):

        if agree:
            st.success("Order Submitted Successfully!")
        else:
            st.error("Please confirm your order.")

# CART SUMMARY
elif page == "Cart Summary":

    st.title("🧾 Cart Summary")

    data = {
        "Item": ["Apple", "Milk", "Carrot"],
        "Price": [20, 50, 15],
        "Quantity": [2, 1, 3]
    }

    df = pd.DataFrame(data)

    st.dataframe(df)

    st.table(df)

    total = (df["Price"] * df["Quantity"]).sum()

    st.metric("Total Cost", f"₱{total}")

    rating = st.slider("Rate your shopping experience", 1, 5)

    uploaded = st.file_uploader("Upload grocery list")

# DEALS & DISCOUNTS (NEW PAGE)
elif page == "Deals & Discounts":

    st.title("🔥 Deals & Discounts")

    st.warning("Limited Time Offers!")

    st.checkbox("Show Fruit Discounts")

    st.checkbox("Show Vegetable Discounts")

    st.selectbox(
        "Choose Discount Category",
        ["Fruits", "Vegetables", "Dairy", "Snacks"]
    )

    st.success("Today's Special: Buy 1 Get 1 Apples!")

# NUTRITION INFO (NEW PAGE)
elif page == "Nutrition Info":

    st.title("🥗 Nutrition Information")

    food = st.selectbox(
        "Select Food Item",
        ["Apple", "Banana", "Milk", "Carrot"]
    )

    st.write("Basic nutrition information:")

    nutrition = {
        "Food": ["Apple", "Banana", "Milk", "Carrot"],
        "Calories": [95, 105, 150, 41]
    }

    df = pd.DataFrame(nutrition)

    st.table(df)

# CUSTOMER FEEDBACK (NEW PAGE)
elif page == "Customer Feedback":

    st.title("💬 Customer Feedback")

    name = st.text_input("Your Name")

    email = st.text_input("Email")

    experience = st.slider("Shopping Experience", 1, 10)

    message = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# ABOUT PAGE
elif page == "About":

    st.title("About Us")

    st.write("""
    Welcome to our Grocery App!

    This app was created as a simple project to demonstrate a Streamlit user interface.
    It allows users to explore a sample grocery store, choose items, view deals, and see a cart summary.

    The goal of this app is to show how different Streamlit UI components work together
    to create an interactive and easy-to-use application.
    """)
