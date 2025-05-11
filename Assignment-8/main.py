import streamlit as st
from models import Restaurant, MenuItem, Order

# Users (Only Annas)
users = {
    "User": "1234"
}

# Session State Setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "cart" not in st.session_state:
    st.session_state.cart = []


st.title("🍽️ Online Restaurant Ordering System")


if not st.session_state.logged_in:
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")
    st.stop()


if st.session_state.logged_in:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.cart = []
        st.rerun()


restaurant = Restaurant()
restaurant.load_orders_from_json()


if not restaurant.menu:
    restaurant.add_menu_item(MenuItem("Zinger Burger", 450))
    restaurant.add_menu_item(MenuItem("Pizza", 1100))
    restaurant.add_menu_item(MenuItem("Fries", 200))
    restaurant.add_menu_item(MenuItem("Cold Drinks", 100))
    restaurant.add_menu_item(MenuItem("Coleslaw", 80))


st.subheader("📋 Menu")
for item in restaurant.menu:
    st.write(f"**{item.name}** - ₨{item.price:.2f}")  

st.subheader("🛒 Place Your Order")

menu_names = [item.name for item in restaurant.menu]
selected_item = st.selectbox("Select item", menu_names)

if st.button("Add to Cart"):
    for item in restaurant.menu:
        if item.name == selected_item:
            st.session_state.cart.append(item)
            st.success(f"{item.name} added to cart!")


if st.session_state.cart:
    st.write("🧺 **Cart Items:**")
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item.name} - ₨{item.price:.2f}")  
        total += item.price
    st.write(f"**Total: ₨{total:.2f}**")  
else:
    st.info("Cart is empty. Please add items.")


address = st.text_input("📍 Address")
mobile = st.text_input("📱 Mobile Number")

if st.button("Place Order"):
    if not st.session_state.cart:
        st.warning("Please add items to your cart.")
    elif not address or not mobile:
        st.warning("Please enter address and mobile number.")
    else:
        order = Order(st.session_state.username, address, mobile)
        for item in st.session_state.cart:
            order.add_item(item)
        restaurant.place_order(order)
        st.success(f"✅ Order placed successfully! Total: ₨{order.total_price():.2f}") 
        st.session_state.cart = [] 


st.subheader("📦 Order History")
for i, order in enumerate(restaurant.orders, 1):
    st.markdown(f"**Order #{i} - {order.customer_name}**")
    st.write(f"📍 Address: {order.address}")
    st.write(f"📱 Mobile: {order.mobile}")
    st.write("Items:")
    for item in order.items:
        st.write(f"- {item.name} - ₨{item.price:.2f}")  
    st.write(f"**Total:** ₨{order.total_price():.2f}")  
    
    
    if st.button(f"Delete Order #{i}"):
        restaurant.orders.pop(i-1)  
        restaurant.save_orders_to_json()  
        st.rerun()  

    st.markdown("---")
