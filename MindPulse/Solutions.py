# =========================
# IMPORT LIBRARIES
# =========================
import streamlit as st
import pandas as pd
import sqlite3

from analyzer import analyze_risk


#--------------------
# DATABASE CONNECTION
#--------------------
conn = sqlite3.connect("mindpulse.db", check_same_thread=False)


#---------------
# RECOMMENDATION 
#---------------
def get_recommendations(row):
    """
    Converts risk factors into actionable mental health advice.
    """

    recommendations = []

    #---------------------
    # SLEEP RECOMMENDATION
    #---------------------
    if row["sleep_hours"] < 6:
        recommendations.append("Improve sleep: Aim for 7–8 hours daily. Avoid screens before bed.")
    elif row["sleep_hours"] < 7:
        recommendations.append("Try to slightly increase sleep to reach recommended range (7–8 hrs).")

    #------------
    # SCREEN TIME
    #------------
    if row["screen_time"] > 8:
        recommendations.append("Reduce screen time: Try digital detox periods and limit social media usage.")
    elif row["screen_time"] > 6:
        recommendations.append("Monitor screen time and take regular breaks.")

    #---------
    # EXERCISE
    #---------
    if row["exercise_days"] < 3:
        recommendations.append("Increase physical activity: Aim for at least 3–5 days per week.")

    #-------
    # STRESS
    #-------
    if row["academic_stress"] >= 7:
        recommendations.append("Manage stress: Try planning, breaks, and relaxation techniques.")
    
    #---------------
    # SOCIAL SUPPORT
    #---------------
    if row["social_support"] <= 2:
        recommendations.append("Build support: Talk to friends, family, or trusted adults.")

    #--------------
    # CYBERBULLYING
    #--------------
    if row["cyberbullying"] == 1:
        recommendations.append("Seek support for cyberbullying: Report abuse and talk to a trusted person.")

    #--------------
    # SUBSTANCE USE
    #--------------
    if row["substance_use"] > 0:
        recommendations.append("Consider healthier coping strategies instead of substances.")

    #-----
    # MOOD
    #-----
    if row["mood_score"] < 5:
        recommendations.append("Engage in mood-boosting activities like exercise, hobbies, or social interaction.")

    #-----------------------------
    # SUICIDAL THOUGHTS (CRITICAL)
    #-----------------------------
    if row["suicidal_thoughts"] >= 2:
        recommendations.append("Seek immediate help from a mental health professional or trusted support system.")

    return recommendations


#----------
# MAIN PAGE
#----------
def show_solutions():

    st.title("MindPulse Solutions & Recommendations")
    st.write("Personalized mental health guidance based on behavioral survey responses.")

    #--------------------------------------
    # IDENTIFY CURRENT USER (PRIVATE ACCESS)
    #--------------------------------------
    # First tries automatic session login after survey submission
    user_name = st.session_state.get("current_user", "")

    # If no session exists, allow manual entry
    if not user_name:
        user_name = st.text_input(
            "Enter your name to view your personalized solutions:"
        )

    if not user_name:
        st.info("Please enter your name to access your personalized dashboard.")
        return

    #----------
    # LOAD DATA
    #----------
    all_df = pd.read_sql_query("SELECT * FROM survey_responses", conn)

    user_df = all_df[
        all_df["name"] == user_name
    ].tail(1)

    if user_df.empty:
        st.warning("No data available yet. Please complete the survey first.")
        return

    #----------------------
    # PRIVATE RISK INSIGHTS
    #----------------------
    st.subheader("Your Personalized Mental Health Insights")

    # ------------------------
    # RUN ANALYSIS FOR USER
    # ------------------------
    user_df["analysis"] = user_df.apply(
        analyze_risk, axis=1
    )

    user_df["risk_level"] = user_df["analysis"].apply(
    lambda x: x["risk_level"]
    )

    user_df["risk_score"] = user_df["analysis"].apply(
    lambda x: x["score"]
    )

    user_df["insights"] = user_df["analysis"].apply(
    lambda x: x["insights"]
    )

    # ------------------------
    # NOW EXTRACT USER ROW
    # ------------------------
    row = user_df.iloc[0]

    if row["risk_level"] == "High Risk":
        st.error(
            f"""
            High Risk Detected

            Name: {row['name']}

            - Sleep: {row['sleep_hours']} hrs
            - Screen Time: {row['screen_time']} hrs
            - Exercise Days: {row['exercise_days']}
            - Academic Stress: {row['academic_stress']}
            - Social Support: {row['social_support']}
            - Mood Score: {row['mood_score']}
            - Risk Score: {row['risk_score']}

            Insights:
            {row['insights']}
            """
        )

    elif row["risk_level"] == "Moderate Risk":
        st.warning(
            f"""
            Moderate Risk Detected

            Name: {row['name']}

            - Sleep: {row['sleep_hours']} hrs
            - Screen Time: {row['screen_time']} hrs
            - Exercise Days: {row['exercise_days']}
            - Academic Stress: {row['academic_stress']}
            - Social Support: {row['social_support']}
            - Mood Score: {row['mood_score']}
            - Risk Score: {row['risk_score']}

            Insights:
            {row['insights']}
            """
        )

    else:
        st.success(
            f"""
            Low Risk Profile

            Name: {row['name']}

            - Sleep: {row['sleep_hours']} hrs
            - Screen Time: {row['screen_time']} hrs
            - Exercise Days: {row['exercise_days']}
            - Academic Stress: {row['academic_stress']}
            - Social Support: {row['social_support']}
            - Mood Score: {row['mood_score']}
            - Risk Score: {row['risk_score']}

            Insights:
            {row['insights']}
            """
        )

    #-------------------------------
    # DISPLAY PERSONALIZED SOLUTIONS
    #-------------------------------
    st.subheader("Personalized Recommendations")

    for _, row in user_df.iterrows():

        st.markdown("---")

        st.write(f"**User:** {row['name']}")
        st.write(f"**Risk Level:** {analyze_risk(row)['risk_level']}")

        recommendations = get_recommendations(row)

        if recommendations:
            for rec in recommendations:
                st.info(rec)
        else:
            st.success("No major risk factors detected. Maintain your healthy lifestyle!")