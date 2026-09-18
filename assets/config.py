"""Theme and configuration settings for the Fitness Challenge App"""

# Color scheme - Navy Dark Winter Cold Night Sea theme
PRIMARY_DARKEST = "#1D3E53"  # Darkest navy
PRIMARY_DARK = "#254B62"  # Dark navy
PRIMARY_MEDIUM = "#476D7C"  # Medium navy
PRIMARY_LIGHT = "#77ABB7"  # Light navy
PRIMARY_GRADIENT = "linear-gradient(45deg, #77ABB7, #254B62, #77ABB7)"

# Derived colors
LIGHT_VARIANT = "#E8F4F6"  # Light variant for backgrounds
LIGHTER_VARIANT = "#F0F8FA"  # Lighter variant for backgrounds

# Status colors
SUCCESS_COLOR = "#77ABB7"  # Light navy
INFO_COLOR = "#254B62"  # Dark navy
WARNING_COLOR = "#476D7C"  # Medium navy
ERROR_COLOR = "#1D3E53"  # Darkest navy

# Theme colors
PRIMARY_COLOR = "#77ABB7"  # Primary light navy
SECONDARY_COLOR = "#254B62"  # Secondary dark navy
ACCENT_COLOR = "#476D7C"  # Accent medium navy
BACKGROUND_COLOR = "#f7fafc"  # Light gray background
TEXT_COLOR = "#1a202c"  # Dark text
CARD_BACKGROUND = "#ffffff"  # White card background

# Difficulty level colors
DIFFICULTY_COLORS = {
    "Easy": "#77ABB7",  # Light navy
    "Medium": "#476D7C",  # Medium navy
    "Hard": "#1D3E53",  # Darkest navy
}

# Category colors
CATEGORY_COLORS = {
    "Sports": "#77ABB7",  # Light navy
    "Language": "#254B62",  # Dark navy
    "General Knowledge": "#476D7C",  # Medium navy
}

# Page configuration
PAGE_CONFIG = {
    "page_title": "Fitness Challenge App",
    "page_icon": "💪",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Navigation menu items
NAVIGATION_ITEMS = {
    "Home": "pages/home.py",
    "Challenges": {
        "View Challenges": "pages/view_challenges.py",
        "Create Challenge": "pages/create_challenges.py",
    },
    "Activities": {
        "View Activities": "pages/view_activities.py",
        "Create Activity": "pages/create_activities.py",
    },
    "Nutrition": {
        "View Plans": "pages/view_nutrition_plan.py",
        "Create Plan": "pages/create_nutration_plan.py",
    },
    "Users": {
        "View Users": "pages/view_users.py",
        "Login": "pages/login.py",
        "Register": "pages/register.py",
    }
}

# Card styling
CARD_STYLE = {
    "border_radius": 12,
    "padding": "1.5rem",
    "shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "border": "1px solid #e2e8f0"
}

# Button styling
BUTTON_STYLE = {
    "use_container_width": True,
    "type": "primary"
}

# Database path
DATABASE_PATH = "database/database.db"

# Assets path
ASSETS_PATH = "assets"
