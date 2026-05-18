import streamlit as st

# insights.py
# Static explanatory insights for MindPulse graphs
# These descriptions are displayed under each graph to help users understand
# what the visualization means without performing calculations.

graph_insights = {
    "sleep_vs_anxiety": """
💡 Insight:
This graph explores the connection between sleep duration and anxiety levels among young people.

Sleep is a critical part of emotional and psychological well-being. Lower sleep durations are often associated
with higher anxiety because inadequate rest can affect mood regulation, concentration, and stress tolerance.
Teens and young adults who consistently sleep less may experience increased emotional exhaustion and mental strain.

🧠 Key Message:
Healthy sleep habits can play an important role in reducing anxiety and improving overall mental wellness.
""",

    "screen_time_vs_mood": """
💡 Insight:
This graph examines how screen time may influence emotional well-being and mood scores.

Digital devices are central to modern life, but excessive recreational screen time may contribute to mood decline
through social comparison, reduced physical activity, sleep disruption, and digital fatigue.
While technology can provide connection and entertainment, overexposure may increase emotional stress.

🧠 Key Message:
Balanced screen use, digital breaks, and healthy online habits may support better emotional health.
""",

    "cyberbullying_vs_anxiety_region": """
💡 Insight:
This graph highlights how cyberbullying may impact anxiety levels across different regions.

Cyberbullying can significantly affect mental health by increasing stress, fear, social withdrawal,
and emotional distress. Regional differences may reflect variations in online behavior,
digital safety awareness, and access to mental health support systems.

🧠 Key Message:
Addressing online harassment through awareness, education, and support systems is essential
for protecting youth mental health globally.
""",

    "screen_time_by_region": """
💡 Insight:
This graph compares average screen time patterns across different regions.

Screen habits may vary based on internet accessibility, education systems, cultural norms,
social media popularity, and lifestyle differences. Some regions may experience higher screen use due
to increased digital integration in daily life.

🧠 Key Message:
Understanding regional screen behavior can help identify where digital wellness education
and healthier technology habits may be most needed.
""",

    "emotional_trend_over_time": """
💡 Insight:
This graph tracks changes in emotional well-being over time.

Emotional health trends may reflect evolving lifestyle pressures, social media influence,
academic demands, world events, or increased mental health awareness.
Patterns over time can help identify whether emotional wellness is improving, declining,
or remaining stable within youth populations.

🧠 Key Message:
Monitoring emotional trends helps reveal long-term mental health patterns
and supports early intervention strategies for future well-being.
"""
}

# =====================================================
# FUNCTION 1: SHOW SINGLE INSIGHT (UNDER EACH GRAPH)
# =====================================================
def show_insight(graph_name):
    """
    Display a single insight under a specific graph.
    """
    if graph_name in graph_insights:
        st.markdown(graph_insights[graph_name])
    else:
        st.warning("No insight available for this graph yet.")



    