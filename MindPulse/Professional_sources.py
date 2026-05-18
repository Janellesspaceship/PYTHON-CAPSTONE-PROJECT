# Professional Research Sources for MindPulse Insights

import streamlit as st

# Dictionary for graph-specific professional references
professional_references = {
    "sleep_vs_anxiety": """
### Key Trend:
**Lower sleep duration is associated with higher anxiety levels.**

### Why It Matters:
Insufficient sleep may:
- Increase stress hormones (cortisol)
- Reduce emotional regulation
- Increase anxiety and depressive symptoms
- Lower concentration and resilience

### Proven By:
**CDC (Centers for Disease Control and Prevention)**
- Adolescents need 8–10 hours of sleep for healthy development

**WHO (World Health Organization)**
- Sleep is essential for emotional stability and stress management

**APA (American Psychological Association)**
- Sleep deprivation is linked to psychological distress

### Trusted Sources:
CDC Youth Risk Behavior Survey | WHO Adolescent Mental Health | APA Sleep Research
""",

    "screen_time_vs_mood": """
### Key Trend:
**Higher screen time is often associated with lower mood scores.**

### Why It Matters:
Excessive screen exposure may:
- Reduce sleep quality
- Increase social comparison
- Increase loneliness
- Increase depressive symptoms
- Reduce physical activity

### Proven By:
**APA**
- Heavy social media use can negatively affect emotional wellness

**NIH (National Institutes of Health)**
- Excessive screen time may impact adolescent brain and behavior

**UNICEF**
- Digital overexposure may contribute to emotional strain

### Trusted Sources:
APA Digital Wellness Research | NIH Adolescent Brain Study | UNICEF Youth Online Reports
""",

    "cyberbullying_vs_anxiety_region": """
### Key Trend:
**Higher cyberbullying exposure is associated with higher anxiety levels.**

### Why It Matters:
Cyberbullying may:
- Increase emotional distress
- Lower self-esteem
- Trigger depression
- Increase fear and social withdrawal
- Raise long-term psychological harm

### Proven By:
**UNICEF**
- Cyberbullying significantly affects youth mental safety

**CDC**
- Bullying victims face increased emotional and mental health risks

**UNESCO**
- Bullying is linked to educational and emotional harm

### Trusted Sources:
UNICEF Cyberbullying Reports | CDC Bullying Research | UNESCO Youth Safety Reports
""",

    "anxiety_by_region": """
### Key Trend:
Anxiety rates may vary by region due to:
- Economic conditions
- Social pressures
- Conflict exposure
- Education systems
- Mental health support access

### Proven By:
**WHO Mental Health Atlas**
- Global youth mental health patterns differ across regions

**UNICEF**
- Regional social conditions affect youth well-being

**World Bank**
- Social and economic pressures influence emotional health

### Trusted Sources:
WHO Mental Health Atlas | UNICEF Regional Reports | World Bank Social Indicators
""",

    "screen_time_by_region": """
### Key Trend:
Regional screen time differences may reflect:
- Smartphone access
- Internet penetration
- Urbanization
- Education technology
- Cultural digital habits

### Proven By:
**DataReportal**
- Tracks digital behavior trends globally

**Statista**
- Measures regional media consumption

**UNICEF**
- Studies youth digital accessibility

### Trusted Sources:
DataReportal Global Digital Reports | Statista Media Trends | UNICEF Digital Inclusion
""",

    "emotional_trend_over_time": """
### Key Trend:
Declining emotional wellness over time may be influenced by:
- Increased social media dependency
- Academic burnout
- Post-pandemic stress
- Sleep decline
- Economic uncertainty
- Rising cyberbullying

### Proven By:
**WHO**
- Youth mental health challenges have increased globally

**CDC**
- Persistent sadness among adolescents has risen over time

**UNICEF**
- Modern digital and social pressures affect emotional wellness

### Trusted Sources:
WHO Global Mental Health Trends | CDC Youth Behavior Reports | UNICEF State of the World’s Children
"""
}

# Function for displaying professional references under graphs
def show_professional_reference(graph_name):
    if graph_name in professional_references:
        st.info(professional_references[graph_name])
    else:
        st.warning("No professional reference available for this graph yet.")


# Optional Full Professional Sources Page
def show_professional_sources_page():
    st.title("Professional Data Sources & Scientific Validation")

    st.markdown("""
    MindPulse visualizations are supported by internationally recognized organizations
    that study adolescent mental health, digital wellness, and behavioral trends.

    These sources help explain why certain lifestyle patterns may influence emotional well-being.
    """)

    st.divider()

    for title, key in [
        ("Sleep Hours vs Anxiety Levels", "sleep_vs_anxiety"),
        ("Screen Time vs Mood Score", "screen_time_vs_mood"),
        ("Cyberbullying vs Anxiety", "cyberbullying_vs_anxiety_region"),
        ("Anxiety Levels by Region", "anxiety_by_region"),
        ("Average Screen Time by Region", "screen_time_by_region"),
        ("Emotional Trend Over Time", "emotional_trend_over_time")
    ]:
        st.subheader(title)
        st.markdown(professional_references[key])
        st.divider()

    st.subheader("MindPulse Research Foundation")

    st.success("""
    MindPulse is informed by globally recognized behavioral science, mental health,
    and digital wellness research.

    Primary professional organizations include:
    WHO | CDC | APA | UNICEF | UNESCO | NIH | DataReportal | Statista | World Bank
    """)

    st.caption("MindPulse © 2026 | Scientific Insight for Youth Mental Wellness")