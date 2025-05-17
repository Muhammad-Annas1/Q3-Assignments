import streamlit as st
import json
from utils.auth import Auth
from utils.payment import PaymentProcessor
from models.book import Book

auth = Auth()
payment = PaymentProcessor()

st.set_page_config(page_title="📚 Online Bookstore", layout="centered")
st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>📚 Welcome to the Online Bookstore</h1>", unsafe_allow_html=True)
st.markdown("---")

# Session state init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Sidebar menu
menu_options = ["🔐 Login", "📝 Signup", "📖 Browse Books"]
if st.session_state.logged_in:
    menu_options.append("🚪 Logout")

menu = st.sidebar.selectbox("📋 Menu", menu_options)

# Login
if menu == "🔐 Login":
    st.subheader("🔐 Login to Your Account")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    if st.button("Login ✅"):
        if auth.login(email, password):
            st.success("✅ Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.user_email = email
        else:
            st.error("❌ Invalid email or password.")

# Signup
elif menu == "📝 Signup":
    st.subheader("📝 Create a New Account")
    email = st.text_input("📧 New Email")
    password = st.text_input("🔑 New Password", type="password")
    if st.button("Signup ✅"):
        if auth.signup(email, password):
            st.success("🎉 Account created! You can now log in.")
        else:
            st.error("⚠️ Email already exists. Try logging in.")

# Browse Books
elif menu == "📖 Browse Books":
    if st.session_state.logged_in:
        st.header("📚 Available Books")
        try:
            with open("data/books.json") as f:
                books = json.load(f)

            for b in books:
                book = Book(**b)
                with st.container():
                    st.markdown(f"### 📘 {book.title}")
                    st.markdown(f"👨‍💼 **Author:** {book.author}")
                    st.markdown(f"💵 **Price:** ${book.price}")
                    if st.button(f"🛒 Buy '{book.title}'", key=book.id):
                        session_url = payment.process_payment(
                            st.session_state.user_email, book.price
                        )
                        if session_url:
                            st.success("✅ Payment session created.")
                            st.markdown(
                                f"[💳 Click here to pay for **{book.title}**]({session_url})",
                                unsafe_allow_html=True,
                            )
                        else:
                            st.error("❌ Failed to create payment session.")
                    st.markdown("---")
        except FileNotFoundError:
            st.error("📁 Could not load book data. Make sure `data/books.json` exists.")
    else:
        st.warning("🔑 Please log in to browse and buy books.")

# Logout
elif menu == "🚪 Logout":
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.success("👋 Logged out successfully!")
