import streamlit as st

# Import modules with error handling
try:
    import home
except Exception as e:
    st.error(f"Error loading Home module: {e}")
    home = None

try:
    import loan_core_ml
except Exception as e:
    st.error(f"Error loading Prediction module: {e}")
    loan_core_ml = None

try:
    import loan_chatbot
except Exception as e:
    st.error(f"Error loading Chatbot module: {e}")
    loan_chatbot = None

try:
    import about_me
except Exception as e:
    st.error(f"Error loading About Me module: {e}")
    about_me = None

from styles import app_styles
# Set page config with default collapsed sidebar
st.set_page_config(
    page_title="BANK",
    page_icon="🏦",
    layout="wide",

)
app_styles()

# Sidebar Navigation
st.sidebar.title("Navigation 🧭")
app_mode = st.sidebar.radio(
    "Go to:",
    ["Home", "Prediction (Traditional)", "Chatbot (GEN-AI)", "About Me"],
)

# Route to pages based on sidebar selection
if app_mode == "Home":
    if home:
        home.show()
    else:
        st.error("Home module failed to load.")
elif app_mode == "Prediction (Traditional)":
    if loan_core_ml:
        loan_core_ml.show()
    else:
        st.error("Prediction module failed to load. Please check the error messages above.")
elif app_mode == "Chatbot (GEN-AI)":
    if loan_chatbot:
        loan_chatbot.show()
    else:
        st.error("Chatbot module failed to load. Please check the error messages above.")
elif app_mode == "About Me":
    if about_me:
        about_me.show()
    else:
        st.error("About Me module failed to load.")
