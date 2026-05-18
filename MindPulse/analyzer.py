#------------------------
# MINDPULSE RISK ANALYZER
#------------------------
# This module converts raw survey responses into:
# - Risk score
# - Risk level (Low / Moderate / High)
# - Behavioral insights

#-----------------------
# CORE ANALYSIS FUNCTION
#-----------------------

def analyze_risk(row):
    """
    Takes one survey response (row from DataFrame)
    and returns risk level + score + insights.
    """

    risk_score = 0
    insights = []  # stores explanations for dashboard display


    #------------------
    # 1. SLEEP ANALYSIS
    #------------------
    # Recommended: 7–10 hours (youth benchmark)
    if row["sleep_hours"] < 6:
        risk_score += 2
        insights.append("Severe sleep deprivation detected")
    elif row["sleep_hours"] < 7:
        risk_score += 1
        insights.append("Below recommended sleep range")


    #------------------------
    # 2. SCREEN TIME ANALYSIS
    #------------------------
    if row["screen_time"] > 8:
        risk_score += 2
        insights.append("Excessive screen time (high digital exposure)")
    elif row["screen_time"] > 6:
        risk_score += 1
        insights.append("Moderate-high screen usage")


    #---------------------
    # 3. EXERCISE ANALYSIS
    #---------------------
    # WHO recommends regular activity (3–5+ days/week)
    if row["exercise_days"] < 3:
        risk_score += 1
        insights.append("Low physical activity level")


    #-------------------
    # 4. ACADEMIC STRESS
    #-------------------
    if row["academic_stress"] >= 8:
        risk_score += 2
        insights.append("Severe academic stress")
    elif row["academic_stress"] >= 6:
        risk_score += 1
        insights.append("Moderate academic stress")


    #------------------
    # 5. SOCIAL SUPPORT
    #------------------
    # Scale: 1 (low) → 5 (high)
    if row["social_support"] <= 2:
        risk_score += 2
        insights.append("Low emotional/social support")
    elif row["social_support"] == 3:
        risk_score += 1
        insights.append("Moderate support system")


    #-----------------
    # 6. CYBERBULLYING
    #-----------------
    if row["cyberbullying"] == 1:
        risk_score += 2
        insights.append("History of cyberbullying exposure")


    #-----------------
    # 7. SUBSTANCE USE
    #-----------------
    # 0 = never, 1 = sometimes, 2 = frequent
    if row["substance_use"] == 2:
        risk_score += 2
        insights.append("Frequent substance use for coping")
    elif row["substance_use"] == 1:
        risk_score += 1
        insights.append("Occasional substance use detected")


    #--------------
    # 8. MOOD SCORE
    #--------------
    # 1–10 scale (low = negative mood)
    if row["mood_score"] < 4:
        risk_score += 2
        insights.append("Very low mood levels")
    elif row["mood_score"] < 6:
        risk_score += 1
        insights.append("Below average mood")


    #--------------------------------
    # 9. SUICIDAL THOUGHTS (CRITICAL)
    #--------------------------------
    # 0 = never, 1 = rare, 2 = sometimes, 3 = often
    if row["suicidal_thoughts"] >= 2:
        risk_score += 3
        insights.append("Critical self-harm risk indicator")
    elif row["suicidal_thoughts"] == 1:
        risk_score += 1
        insights.append("Mild self-harm ideation reported")


    #--------------------------
    # FINAL RISK CLASSIFICATION
    #--------------------------

    if risk_score <= 3:
        risk_level = "Low Risk"
    elif risk_score <= 7:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"


    #-------------------------
    # RETURN STRUCTURED OUTPUT
    #-------------------------

    return {
        "risk_level": risk_level,
        "score": risk_score,
        "insights": insights
    }