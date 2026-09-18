# import streamlit as st
# from assets.config import PAGE_CONFIG, PRIMARY_GREEN, PRIMARY_BLUE, BACKGROUND_COLOR
# import os



# st.logo("assets/logo.svg")



# # Page configuration
# st.set_page_config(**PAGE_CONFIG)

# # Load custom CSS
# def load_css():
#     css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
#     with open(css_path) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load_css()

# # Custom theme settings
# st.markdown(f"""
# <style>
#     .stApp {{
#         background-color: {BACKGROUND_COLOR};
#     }}
# </style>
# """, unsafe_allow_html=True)

# # Main page
# st.markdown(f"""
# <div style='text-align: center; padding: 2rem 0;'>
#     <h1 style='color: {PRIMARY_BLUE}; margin-bottom: 0.5rem;'>Welcome to Fitness Challenge App</h1>
# </div>
# """, unsafe_allow_html=True)
# st.markdown("---")

# st.markdown("""
# ### 🏋️‍♂️ About This App

# This is a comprehensive fitness challenge management system that helps you:
# - Track and manage fitness challenges
# - Create and monitor activities
# - Plan and follow nutrition plans
# - Manage user profiles and progress

# ### 🚀 Get Started

# Use the navigation menu on the left to explore different sections:
# - **Challenges**: View and create fitness challenges
# - **Activities**: Manage workout activities
# - **Nutrition**: Plan and track nutrition plans
# - **Users**: Manage user accounts

# ### 📊 Quick Links

# - [View All Challenges](pages/view_challenges.py)
# - [Create New Challenge](pages/create_challenges.py)
# - [View Activities](pages/view_activities.py)
# - [View Nutrition Plans](pages/view_nutrition_plan.py)
# """)