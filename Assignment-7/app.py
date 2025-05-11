import streamlit as st
from auth import UserManager
from medicine import Medicine
from scheduler import load_medicines, save_medicines
from datetime import datetime, date

st.set_page_config(page_title="MediMind", page_icon="💊", layout="wide")

# CSS Styles for Responsiveness
st.markdown("""
    <style>
        /* General Styles */
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #888;
            text-align: center;
        }
        .med-card {
            background-color: #f9f9f9;
            color: #000;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border-left: 5px solid #4CAF50;
        }
        section[data-testid="stRadio"] label {
            margin-right: 10px;
            font-weight: 600;
            color: #4CAF50;
        }
        input, button {
            border-radius: 8px !important;
        }

        /* Responsive Styles for Mobile and Tablets */
        @media (max-width: 768px) {
            .title {
                font-size: 36px;
            }
            .subtitle {
                font-size: 16px;
            }

            /* Adjust container columns for mobile */
            .stButton, .stTextInput {
                width: 100% !important;
                margin: 10px 0;
            }

            .med-card {
                padding: 12px;
                font-size: 14px;
            }

            .stRadio label {
                font-size: 14px;
            }

            .stColumns .stColumn {
                padding-left: 0;
                padding-right: 0;
            }

            /* Add extra padding for smaller screens */
            .stContainer {
                padding-left: 15px;
                padding-right: 15px;
            }

            /* Adjust input fields for better visibility */
            .stTextInput input {
                font-size: 16px;
                padding: 12px;
            }

            /* Change layout of login screen */
            .stRadio {
                font-size: 14px;
            }

            /* Adjust the columns layout for mobile */
            .stColumns {
                display: block;
            }
        }

        @media (max-width: 1024px) {
            .title {
                font-size: 42px;
            }

            .med-card {
                padding: 14px;
                font-size: 16px;
            }
        }

        /* Large Screens (Desktop) */
        @media (min-width: 1025px) {
            .title {
                font-size: 48px;
            }
        }

        /* Footer Styles */
       .footer {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 10px;
    font-size: 16px;
    color: gray; /* Text color gray */
    background-color: black; /* Background color black */
}

.footer a {
    color: #4CAF50;
    text-decoration: none;
}
    </style>
""", unsafe_allow_html=True)

# Session setup
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'medicines' not in st.session_state:
    st.session_state.medicines = []

# Auth UI
if not st.session_state.logged_in:
    st.markdown("""<div style='text-align: center; padding-top: 2rem;'>
        <h1 style='font-size: 3rem; color: #4CAF50;'>💊 MediMind</h1>
        <p style='color: gray; font-size: 1.2rem;'>Your Smart Medicine Reminder</p>
    </div>
    <hr>
    """, unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            menu = st.radio("Choose Action", ["Login", "Register", "Reset Password"], horizontal=True)
            username = st.text_input("👤 Username", placeholder="Enter your username")

            if menu in ["Login", "Register"]:
                password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")

            if menu == "Login":
                if st.button("🔐 Login", use_container_width=True):
                    if UserManager.login_user(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.medicines = load_medicines(username)
                        st.success("🎉 Logged in successfully!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials.")

            elif menu == "Register":
                if st.button("📝 Register", use_container_width=True):
                    if UserManager.register_user(username, password):
                        st.success("✅ Registration successful. Please login.")
                    else:
                        st.warning("⚠️ Username already exists.")

            elif menu == "Reset Password":
                new_password = st.text_input("🛠️ New Password", type="password", placeholder="Enter new password")
                if st.button("🔁 Reset Password", use_container_width=True):
                    if UserManager.reset_password(username, new_password):
                        st.success("🔑 Password reset successful!")
                    else:
                        st.error("❌ Username not found.")

# Main App
else:
    st.sidebar.header(f"👋 Welcome, {st.session_state.username}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<h1 class='title'>💊 Your Medicine Schedule</h1>", unsafe_allow_html=True)

    colA, colB, colC = st.columns(3)
    colA.metric("📦 Total Medicines", len(st.session_state.medicines))
    colB.metric("📅 Today", datetime.today().strftime("%B %d, %Y"))
    colC.metric("🕒 Current Time", datetime.now().strftime("%I:%M %p"))

    tab1, tab2 = st.tabs(["📋 View Medicines", "➕ Add Medicine"])

    with tab2:
        st.subheader("➕ Add a New Medicine")

        name = st.text_input("Medicine Name")
        dosage = st.text_input("Dosage (e.g. 1 tablet)")
        time = st.time_input("Time")
        selected_date = st.date_input("Date", value=date.today())

        if st.button("💊 Add Medicine"):
            if name and dosage:
                med = Medicine(
                    name=name,
                    time=time.strftime("%I:%M %p"),
                    dosage=dosage,
                    date=selected_date.strftime("%Y-%m-%d")
                )
                st.session_state.medicines.append(med)
                save_medicines(st.session_state.username, st.session_state.medicines)
                st.success(f"✅ Added: {med}")
            else:
                st.warning("⚠️ Please fill all fields.")

    with tab1:
        st.subheader("📋 Your List")
        if st.session_state.medicines:
            for i, med in enumerate(st.session_state.medicines):
                col1, col2 = st.columns([9, 1])
                with col1:
                    st.markdown(
                        f"<div class='med-card'><strong>{med.name}</strong> - {med.dosage} - {med.time}<br/><small>📅 {med.date if med.date else 'No date provided'}</small></div>",
                        unsafe_allow_html=True
                    )
                with col2:
                    if st.button("❌", key=f"del_{i}"):
                        st.session_state.medicines.pop(i)
                        save_medicines(st.session_state.username, st.session_state.medicines)
                        st.rerun()
        else:
            st.info("No medicines scheduled.")

    # Built with section (Footer)
    st.markdown("""
        <div class='footer'>
            <p>Built with ❤️ by Muhammad Annas | &copy; 2025 All Rights Reserved</p>
        </div>
    """, unsafe_allow_html=True)
