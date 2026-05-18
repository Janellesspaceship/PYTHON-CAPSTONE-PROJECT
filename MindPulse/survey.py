import streamlit as st
from Database import insert_response


def show_survey():

    # Main Title
    st.title("MindPulse Youth Mental Health Behavioural Survey")

    #------------------
    # Intro Description
    #------------------

    st.markdown("""
    ### What is this survey?
    """)                

    st.write(
    "This survey evaluates **behavioural patterns** linked to Youth Mental Health based on professional wellbeing benchmarks."                

    "It is NOT a diagnosis — only a wellbeing indicator."
    )

    st.divider()

    #--------------------
    #PERSONAL INFORMATION
    #--------------------

    # Optional User Name
    name = st.text_input("Enter your name or nickname(Optional)")

    # Age selection
    age = st.slider(
    "How old are you?",
    10, 35
)

    # Gender selection
    gender = st.selectbox(
    "Select your gender",
    ["Male", "Female", "Prefer not to say"]
)

    #--------------------- 
    #BEHAVIOURAL QUESTIONS
    #---------------------

    # Sleep question
    sleep_hours = st.selectbox(
    "How many hours do you sleep daily?",
    [3, 4, 5, 6, 7, 8, 9, 10]
) 

    #Professional sleep guide
    st.caption(
    "Sleep Guide: Under 6hrs = High Risk | 7-8hrs = Healthy | 8-10hrs = Recommended"
)

    #Screen time question
    screen_time = st.selectbox(
        "How many hours do you spend on screens daily (outside school/work)?",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    #Screen time guide
    st.caption(
        "Screen Time Guide: 1–3 hrs = Healthy | 4–6 hrs = Moderate | "
        "7+ hrs = Elevated mental health risk"
    )



    #Exercise frequency
    exercise_days = st.selectbox(
        "How many days per week do you exercise for at least 30 mins?",
        [0, 1, 2, 3, 4, 5, 6, 7]
    )

    #Exercise guide
    st.caption(
        "Exercise Guide: 0–1 days = Low Activity | 3–5 days = Healthy | "
        "5+ days = Strong protective factor"
    )



    #Academic stress slider
    academic_stress = st.slider(
        "Rate your academic stress level",
        1, 10
    )

    #Stress scale guide
    st.caption(
        "Stress Scale: 1–3 = Low | 4–6 = Moderate | "
        "7–8 = High | 9–10 = Severe"
    )



    #Social support slider
    social_support = st.slider(
        "How supported do you feel by family/friends?",
        1, 5
    )

    #Social support guide
    st.caption(
        "Support Scale: 1 = Very Unsupported | 3 = Moderate | "
        "5 = Strong Support"
    )



    #Cyberbullying
    cyberbullying = st.radio(
        "Have you experienced cyberbullying in the last year?",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )



    #Substance use
    substance_use = st.selectbox(
        "Do you use substances (alcohol/nicotine/drugs) to cope?",
        [0, 1, 2],
        format_func=lambda x:
            "Never" if x == 0 else
            "Sometimes" if x == 1 else
            "Frequently"
    )

    #Substance guide
    st.caption(
        "Coping Guide: Never = Healthy | Sometimes = Risk Indicator | "
        "Frequently = High Concern"
    )



    # Mood score
    mood_score = st.slider(
        "Rate your mood over the past 2 weeks",
        1, 10
    )

    # Mood scale guide
    st.caption(
        "Mood Scale: 1–2 = Extremely Low | 3–4 = Low | "
        "5–6 = Neutral | 7–8 = Positive | 9–10 = Excellent"
    )



    #Self-harm thoughts
    suicidal_thoughts = st.selectbox(
        "Have you had thoughts of self-harm recently?",
        [0, 1, 2, 3],
        format_func=lambda x:
            "Never" if x == 0 else
            "Rarely" if x == 1 else
            "Sometimes" if x == 2 else
            "Often"
    )

    # Risk guide
    st.caption(
        "Safety Scale: Never = Low Risk | Rarely = Mild Concern | "
        "Sometimes = Moderate Concern | Often = Immediate Attention Recommended"
    )



    #--------------
    #SUBMIT BUTTON
    #--------------

    if st.button("Submit Survey"):

        #Default anonymous name if blank
        if not name:
            name = "Anonymous"

        #Save survey response
        insert_response(
            name,
            age,
            gender,
            sleep_hours,
            screen_time,
            exercise_days,
            academic_stress,
            social_support,
            cyberbullying,
            substance_use,
            mood_score,
            suicidal_thoughts
        )

        #Success message
        st.success(
            f"Thank you, {name}. Your MindPulse behavioral assessment has been "
            "successfully recorded and will contribute to live mental health insights."
        )
    