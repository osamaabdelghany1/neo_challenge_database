"""Theme and configuration settings for the Fitness Challenge App"""

# Color scheme - Modern gradient theme
PRIMARY_GREEN = "#00F260"  # Bright green
PRIMARY_BLUE = "#00C9FF"  # Cyan blue
PRIMARY_GRADIENT = "linear-gradient(45deg, #00F260, #00C9FF, #00F260)"

# Derived colors
DARK_GREEN = "#00C928"  # Darker green for text
LIGHT_GREEN = "#E6F9EB"  # Light green for backgrounds
DARK_BLUE = "#0099CC"  # Darker blue for text
LIGHT_BLUE = "#E6F7FF"  # Light blue for backgrounds

# Status colors
SUCCESS_COLOR = "#00F260"  # Green
INFO_COLOR = "#00C9FF"  # Blue
WARNING_COLOR = "#FFA500"  # Orange
ERROR_COLOR = "#FF4444"  # Red

# Theme colors
PRIMARY_COLOR = "#00F260"  # Primary green
SECONDARY_COLOR = "#00C9FF"  # Secondary blue
ACCENT_COLOR = "#00F260"  # Accent color
BACKGROUND_COLOR = "#f7fafc"  # Light gray background
TEXT_COLOR = "#1a202c"  # Dark text
CARD_BACKGROUND = "#ffffff"  # White card background

# Difficulty level colors
DIFFICULTY_COLORS = {
    "Easy": "#00F260",  # Bright green
    "Medium": "#FFA500",  # Orange
    "Hard": "#FF4444",  # Red
}

# Category colors
CATEGORY_COLORS = {
    "Sports": "#00F260",  # Green
    "Language": "#00C9FF",  # Blue
    "General Knowledge": "#FFA500",  # Orange
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
