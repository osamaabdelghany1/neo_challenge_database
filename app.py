import streamlit as st
from assets.config import PAGE_CONFIG, PRIMARY_GREEN, PRIMARY_BLUE, BACKGROUND_COLOR
import os

# Page configuration
st.set_page_config(**PAGE_CONFIG)

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Custom theme settings
st.markdown(f"""
<style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("💪 Fitness Challenge")
st.sidebar.markdown("---")

st.sidebar.markdown("### Navigation")
st.sidebar.markdown("- [Home](pages/home.py)")
st.sidebar.markdown("### Challenges")
st.sidebar.markdown("- [View Challenges](pages/view_challenges.py)")
st.sidebar.markdown("- [Create Challenge](pages/create_challenges.py)")
st.sidebar.markdown("### Activities")
st.sidebar.markdown("- [View Activities](pages/view_activities.py)")
st.sidebar.markdown("- [Create Activity](pages/create_activities.py)")
st.sidebar.markdown("- [Take Quiz](pages/gneral_knowledge.py)")
st.sidebar.markdown("- [Execute SQL](pages/execute_sql.py)")
st.sidebar.markdown("### Nutrition")
st.sidebar.markdown("- [View Plans](pages/view_nutrition_plan.py)")
st.sidebar.markdown("- [Create Plan](pages/create_nutration_plan.py)")
st.sidebar.markdown("### Users")
st.sidebar.markdown("- [View Users](pages/view_users.py)")
st.sidebar.markdown("- [Login](pages/login.py)")
st.sidebar.markdown("- [Register](pages/register.py)")

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Stats")

# Display quick stats in sidebar
import sqlite3
conn = sqlite3.connect("database/database.db")
cursor = conn.cursor()

# Get counts
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM challenges")
challenge_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM activities")
activity_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Nutrition_Plans")
nutrition_count = cursor.fetchone()[0]

conn.close()

st.sidebar.metric("Users", user_count)
st.sidebar.metric("Challenges", challenge_count)
st.sidebar.metric("Activities", activity_count)
st.sidebar.metric("Nutrition Plans", nutrition_count)

# Main page
st.markdown(f"""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='color: {PRIMARY_BLUE}; margin-bottom: 0.5rem;'>Welcome to Fitness Challenge App</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
### 🏋️‍♂️ About This App

This is a comprehensive fitness challenge management system that helps you:
- Track and manage fitness challenges
- Create and monitor activities
- Plan and follow nutrition plans
- Manage user profiles and progress

### 🚀 Get Started

Use the navigation menu on the left to explore different sections:
- **Challenges**: View and create fitness challenges
- **Activities**: Manage workout activities
- **Nutrition**: Plan and track nutrition plans
- **Users**: Manage user accounts

### 📊 Quick Links

- [View All Challenges](pages/view_challenges.py)
- [Create New Challenge](pages/create_challenges.py)
- [View Activities](pages/view_activities.py)
- [View Nutrition Plans](pages/view_nutrition_plan.py)
""")