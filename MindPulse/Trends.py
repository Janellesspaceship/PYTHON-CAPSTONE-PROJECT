#-----------------
# IMPORT LIBRARIES
#-----------------
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

from analyzer import analyze_risk


#--------------------
# DATABASE CONNECTION
#--------------------
conn = sqlite3.connect("mindpulse.db", check_same_thread=False)


#------------------------
# MAIN DASHBOARD FUNCTION
#------------------------
def show_trends():

    #------
    # TITLE
    #------
    st.title("MindPulse Behavioral Trends Dashboard")
    st.write(
        "This dashboard analyzes youth mental health patterns based on behavioral survey data."
    )

    
    # ------------------------
    # LOAD ALL DATA (FOR TRENDS)
    # ------------------------
    all_df = pd.read_sql_query("SELECT * FROM survey_responses", conn)

    # Check if database is empty
    if all_df.empty:
        st.warning("No survey data available yet.")
        return

    # ------------------------
    # RUN RISK ANALYSIS FOR ALL USERS
    # ------------------------
    all_df["analysis"] = all_df.apply(analyze_risk, axis=1)

    all_df["risk_level"] = all_df["analysis"].apply(
        lambda x: x["risk_level"]
    )

    all_df["risk_score"] = all_df["analysis"].apply(
        lambda x: x["score"]
    )

    all_df["insights"] = all_df["analysis"].apply(
        lambda x: x["insights"]
    )



    # ------------------------
    # EXTRACT USER DATA ROW
    # ------------------------
    row = all_df.iloc[0]

    # ------------------------
    # OVERALL METRICS (NO PERCENTAGES)
    # ------------------------
    st.subheader("Overall Mental Health Metrics")

    total_users = len(all_df)

    avg_mood = round(all_df["mood_score"].mean(), 2)
    avg_sleep = round(all_df["sleep_hours"].mean(), 2)
    avg_screen = round(all_df["screen_time"].mean(), 2)
    avg_stress = round(all_df["academic_stress"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Users", total_users)
    col2.metric("Avg Mood Score", avg_mood)
    col3.metric("Avg Sleep (hrs)", avg_sleep)
    col4.metric("Avg Screen Time (hrs)", avg_screen)

    st.metric("Avg Academic Stress", avg_stress)

    st.write(
        "These metrics give a quick snapshot of overall mental health trends in the dataset."
    )


    #------------------------
    # RISK DISTRIBUTION GRAPH
    #------------------------
    st.subheader("Risk Level Distribution")

    fig1 = px.histogram(
        all_df,
        x="risk_level",
        color="risk_level",
        title="Distribution of Mental Health Risk Levels",
        color_discrete_map={
            "Low Risk": "green",
            "Moderate Risk": "orange",
            "High Risk": "red"
        }
    )

    st.plotly_chart(fig1)

    st.write(
        "This graph shows how many users fall into Low, Moderate, and High Risk categories. "
        "It helps identify the overall mental health state of the population."
    )


    #--------------
    # SLEEP VS RISK
    #--------------
    st.subheader("Sleep Hours vs Risk Level")

    fig2 = px.box(
        all_df,
        x="risk_level",
        y="sleep_hours",
        color="risk_level",
        title="Relationship Between Sleep and Mental Health Risk",
        color_discrete_map={
            "Low Risk": "green",
            "Moderate Risk": "orange",
            "High Risk": "red"
        }
    )

    st.plotly_chart(fig2)

    st.write(
        "This graph shows how sleep duration varies across risk levels. "
        "Lower sleep is typically associated with higher mental health risk."
    )


    #--------------------
    # SCREEN TIME VS RISK
    #--------------------
    st.subheader("Screen Time vs Risk Level")

    fig3 = px.box(
        all_df,
        x="risk_level",
        y="screen_time",
        color="risk_level",
        title="Impact of Screen Time on Mental Health Risk",
        color_discrete_map={
            "Low Risk": "green",
            "Moderate Risk": "orange",
            "High Risk": "red"
        }
    )

    st.plotly_chart(fig3)

    st.write(
        "This graph analyzes whether high screen exposure is linked to increased mental health risk."
    )


    #---------------
    # STRESS VS RISK
    #---------------
    st.subheader("Academic Stress vs Risk Level")

    fig4 = px.box(
        all_df,
        x="risk_level",
        y="academic_stress",
        color="risk_level",
        title="Academic Stress Across Risk Categories",
        color_discrete_map={
            "Low Risk": "green",
            "Moderate Risk": "orange",
            "High Risk": "red"
        }
    )

    st.plotly_chart(fig4)

    st.write(
        "This graph shows how academic stress levels vary across different mental health risk groups."
    )


    #------------------
    # MOOD DISTRIBUTION
    #------------------
    st.subheader("Mood Score Distribution")

    fig5 = px.histogram(
        all_df,
        x="mood_score",
        nbins=10,
        title="Distribution of Mood Scores",
        color_discrete_sequence=["skyblue"]
    )

    st.plotly_chart(fig5)

    st.write(
        "This graph shows the overall emotional wellbeing of users. "
        "Lower scores indicate negative mood patterns in the population."
    )

    #-------------------------
    # PERSONALIZED INTERPRETATION
    #-------------------------
    st.write(
        "This graph visualizes your personal behavioral patterns across key mental health indicators."
    )

    

    #------------------------
    # PERSONALIZED NEXT STEPS
    #------------------------
    st.subheader("Recommended Next Step")

    if row["risk_level"] == "High Risk":
        st.write(
            "Consider prioritizing sleep improvement, reducing screen exposure, and seeking mental health support from a counselor or trusted professional."
        )

    elif row["risk_level"] == "Moderate Risk":
        st.write(
            "Focus on improving balance through better sleep, stress management, and stronger social support systems."
        )

    else:
        st.write(
            "You currently show healthy behavioral patterns. Maintain your habits and continue monitoring your wellbeing."
        )
    #----------------------
    # SAMPLE INSIGHTS PANEL
    #----------------------
    st.subheader("Sample High-Risk Insights")

    high_risk = all_df[all_df["risk_level"] == "High Risk"].head(3)

    if not high_risk.empty:
        for _, row in high_risk.iterrows():
            st.error(
                f"""
                High Risk User Detected

                - Sleep: {row['sleep_hours']} hrs
                - Screen Time: {row['screen_time']} hrs
                - Mood Score: {row['mood_score']}
                - Risk Score: {row['risk_score']}

                Insights:
                {row['insights']}
                """
            )
    else:
        st.info("No high-risk users detected in current dataset.")
    