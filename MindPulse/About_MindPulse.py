import streamlit as st

def show_about_mindpulse():

    st.title("About MindPulse")

    st.write("""
    MindPulse is a behavioral mental health analytics system designed to help understand 
    youth wellbeing patterns using data-driven insights.
    """)

    #----------------
    # PROJECT PURPOSE
    #----------------
    st.subheader("Purpose")

    st.write("""
    The goal of MindPulse is to analyze lifestyle behaviors such as sleep, screen time, 
    stress, and social support to identify mental health risk patterns among youth.
    """)

    #-------------
    # HOW IT WORKS
    #-------------
    st.subheader("How It Works")

    st.write("""
    1. Users fill out a behavioral survey  
    2. Responses are stored in a SQLite database  
    3. Data is analyzed using risk scoring logic  
    4. Trends are visualized through graphs  
    5. Personalized recommendations are generated  
    """)

    #--------- 
    # FEATURES
    #---------
    st.subheader("Key Features")

    st.write("""
    - Real-time data collection  
    - Behavioral risk analysis  
    - Interactive dashboards  
    - Mental health trend visualization  
    - Personalized recommendations  
    """)

    #----------- 
    # DISCLAIMER
    #-----------
    st.subheader("Disclaimer")

    st.warning("""
    MindPulse is NOT a medical diagnosis tool.  
    It is an educational and analytical system for understanding behavioral patterns.
    """)

    #-----------
    # TOOLS USED
    #-----------
    st.subheader("Tools Used")

    st.write("""
    - Python  
    - Streamlit  
    - SQLite  
    - Pandas  
    - Plotly  
    """)

    st.markdown("""
    ### Future Vision:
    - Live WHO / UNICEF data integration
    - API-powered trend updates
    - Expanded youth wellness education
    - Regional and continent comparisons
    - Enhanced emotional analytics
    """)

    #------------
    # END MESSAGE
    #------------
    st.success("""
     FINAL MISSION:
    MindPulse exists to help young people understand,
    protect, and improve their mental wellbeing through
    awareness, prevention, and action.
    """)