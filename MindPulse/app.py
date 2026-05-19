from pathlib import Path
import streamlit as st
import base64

#---------------
# IMPORT MODULES
#---------------

from Database import create_table
from survey import show_survey
from Trends import show_trends
from Solutions import show_solutions
from About_MindPulse import show_about_mindpulse

create_table()

#-----------------
# LOAD CSS (FONTS)
#-----------------
def load_css():
    css_path = Path(__file__).parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


#-----------------------------
# BACKGROUND IMAGE (HOME ONLY)
#-----------------------------
def set_bg(image_file):
    bg_path = Path(__file__).parent / image_file

    if bg_path.exists():
        with open(bg_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Background image not found: {bg_path}")

#-------------------------------
# RESET BACKGROUND (OTHER PAGES)
#-------------------------------
def reset_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: none !important;
            background-color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


#------------
# PAGE CONFIG
#------------
st.set_page_config(
    page_title="MindPulse",
    layout="wide"
)

#----------------
# FOOTER FUNCTION
#----------------
def show_footer():
    st.divider()

    st.markdown("""
    ---
    **MindPulse** | Youth Mental Health Intelligence System  
    Empowering awareness through trends, prevention, and personal insight.  

    Disclaimer: MindPulse is an educational awareness platform and not a substitute
    for professional mental health diagnosis or emergency care.  

    © 2026 MindPulse | Built for youth mental health awareness
    """)


#-------------------
# SIDEBAR NAVIGATION
#-------------------
st.sidebar.title("MindPulse Navigation")

st.sidebar.write(
    "A behavioral mental health analytics system for youth wellbeing insights."
)

page = st.sidebar.selectbox(
    "Choose a section:",
    ["Home", "Survey", "Trends", "Solutions", "About MindPulse"]
)

#----------
# HOME PAGE
#----------
if page == "Home":

    st.title("Welcome to MindPulse")
    st.subheader("Youth Mental Health Intelligence System")

    set_bg("assets/background.jpg")

    st.write(
        """
        MindPulse is a behavioral mental health analytics system that:
        
        - Collects youth lifestyle data  
        - Analyzes mental health risk patterns  
        - Visualizes behavioral trends  
        - Provides personalized recommendations  
        """
    )

    st.subheader("How it works")

    st.write("""
    1. Fill out the survey  
    2. Data is stored in a database  
    3. Trends dashboard shows patterns  
    4. Solutions page gives recommendations  
    """)

    st.info("Use the sidebar to navigate through the system.")


    show_footer()

#------------
# SURVEY PAGE
#------------
elif page == "Survey":
    show_survey()


#-----------------
# TRENDS DASHBOARD
#-----------------
elif page == "Trends":
    show_trends()


#---------------
# SOLUTIONS PAGE
#---------------
elif page == "Solutions":
    show_solutions()
        

    show_footer()

# =========================
# ABOUT PAGE
# =========================
elif page == "About MindPulse":

    show_about_mindpulse()

    show_footer()