
# Software Project Documentation | توثيق مشروع البرمجيات

<div class="arabic">
قالب توثيق مشاريع البرمجيات — للمسابقة الأفريقية الآسيوية للتكنولوجيا
</div>

---

## 1. Project Overview | نظرة عامة على المشروع

| Field | Value |
|-------|-------|
| **Project Title** | NEO Challenge |
| **Project Type** | Web App |
| **Description** | A self-improvement platform that provides users with daily challenges in Sports, Language, and General Knowledge, with different difficulty levels, aiming to help users improve themselves and gain new skills and knowledge in an interactive way.

The Sports section includes BMI and Fitness Level calculations, a complete weekly meal plan, fitness challenges, and an interactive human body model where users can hover over or click on muscles to discover suitable exercises for each muscle.

The Language section helps users learn new words and skills through lessons and quizzes, while General Knowledge provides challenges and questions about topics such as science, history, geography, and sports to help users expand their knowledge and continuously develop themselves. |
| **Target Users** | Teens ages 12-20, elderly people who want to track their health |
| **Resolution / Platform** | Responsive (Desktop, Tablet, Mobile) |

### Tech Stack | Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python | Programming language and backend logic |
| **Database** | SQLite | Database for storing user data, challenges, activities, and nutrition plans |
| **Libraries** | Streamlit | Web framework for building the interface |

### Dependencies | المكتبات المستخدمة

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | Latest | Web framework for building the interface |
| sqlite3 | Built-in | Database for storing user data |

<!-- Screenshot: Main screen of your project -->

---

## 2. Problem Statement | بيان المشكلة

<div class="arabic">
هنا تكتب المشكلة التي يحلها مشروعك — لماذا هذا المشروع مهم؟
</div>

### What problem does this project solve? | ما المشكلة التي يحلها هذا المشروع؟

Many people struggle with self-improvement and maintaining healthy habits due to lack of motivation, guidance, and structured challenges. Existing fitness and learning apps are often too complex, expensive, or not engaging enough for long-term use. There's no unified platform that combines physical fitness, language learning, and knowledge expansion in an interactive, gamified way.

### Why does it matter? | لماذا هذا مهم؟

Poor physical and mental health affects millions of people worldwide, leading to decreased productivity, lower quality of life, and long-term health issues. Lack of continuous learning and skill development limits personal and professional growth. A unified, engaging platform can help people build sustainable habits and continuously improve themselves.

### How is it currently solved? | كيف تُحل المشكلة حالياً؟

People use separate apps for fitness (MyFitnessPal, Nike Training Club), language learning (Duolingo, Babbel), and general knowledge (Quiz apps, Wikipedia). These apps are often disconnected, require multiple subscriptions, and lack the gamified challenge aspect that keeps users motivated. NEO Challenge combines all these areas in one free, accessible platform.

---

## 3. Technical Architecture | البنية التقنية

<div class="arabic">
هنا تشرح كيف مشروعك مبني من الداخل — هيكل الملفات والتقنيات المستخدمة
</div>

### Project Structure | هيكل المشروع

```
neo-challange_database/
├── app.py            
├── database/           
│   ├── database.db
│   ├── insert_challenges.sql
│   ├── insert_nutrition_plan.sql
│   ├── insert_users.sql
│   ├── insert.sql
│   └── tables.sql
├── docs/              
│   └── afro_asian_software_template.md
├── pages/            
│   ├── create_catogary.py
│   ├── create_challenges.py
│   ├── create_nutration_plan.py
│   ├── login.py
│   ├── register.py
│   ├── view_activities.py
│   ├── view_challenges.py
│   ├── view_nutration_plan.py
│   └── view_users.py
└── requirements.txt     

```


### Architecture Diagram | مخطط البنية

```
[User] → [Streamlit Browser Interface] → [Python Backend] → [SQLite Database]
                    ↓
              [Multi-page Navigation]
                    ↓
        [Login/Register] [Challenges] [Nutrition] [Profile]
```

### Key Files | الملفات الرئيسية

| File | Purpose | Lines of Code |
|------|---------|:-------------:|
| app.py | Main Streamlit app entry point | ~10 |
| database/tables.sql | Database schema with all tables and data | ~164 |
| pages/login.py | User authentication page | ~20 |
| pages/register.py | User registration page | ~30 |
| pages/view_challenges.py | View all challenges with activities | ~45 |
| pages/view_nutration_plan.py | View nutrition plans based on BMI | ~50 |
| pages/view_users.py | View all registered users | ~45 |
| pages/create_challenges.py | Create new challenges | ~40 |
| pages/create_nutration_plan.py | Create nutrition plans | ~45 |

---

## 4. Features & User Flow | الميزات وتدفق المستخدم

<div class="arabic">
هنا تكتب قائمة الميزات + مخطط تدفق المستخدم عبر الشاشات
</div>

### Feature List | قائمة الميزات

| # | Feature | Description | Status |
|---|---------|-------------|:------:|
| 1 | User Registration & Login | Users can create accounts and authenticate to access personalized features | ✅ |
| 2 | BMI & Fitness Calculator | Calculate BMI and fitness level based on user's height and weight | ✅ |
| 3 | Nutrition Plans | View and create personalized nutrition plans based on BMI categories | ✅ |
| 4 | Sports Challenges | Browse and participate in fitness challenges with different difficulty levels | ✅ |
| 5 | Language Challenges | Learn new languages through interactive challenges and quizzes | ✅ |
| 6 | General Knowledge Challenges | Test knowledge in science, history, geography, and sports | ✅ |
| 7 | Activity Management | View activities associated with each challenge | ✅ |
| 8 | User Profile | View user profile with personal information and enrolled challenges | ✅ |

> Status: ✅ Complete | ⏳ In Progress | ❌ Not Started

### User Flow | تدفق المستخدم

```
                    ┌──────────────┐
                    │   LANDING    │
                    │    PAGE      │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   LOGIN /    │
                    │   REGISTER   │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   MAIN MENU  │
                    │  (navigation) │
                    └──┬───┬───┬───┘
                       │   │   │
              ┌────────┘   │   └────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │CHALLENGES│ │NUTRITION │ │  PROFILE │
        │  (view)  │ │  (plans) │ │  (view)  │
        └──────────┘ └──────────┘ └──────────┘
```

### Screen Reference | دليل الشاشات

| Screen | File / Route | Description | Transitions To |
|--------|-------------|-------------|----------------|
| Login | pages/login.py | User authentication with email/password | Register, Main Menu |
| Register | pages/register.py | New user registration with personal details | Login |
| View Challenges | pages/view_challenges.py | Browse all available challenges with activities | View Activities |
| View Activities | pages/view_activities.py | View activities for specific challenge | View Challenges |
| View Nutrition Plans | pages/view_nutration_plan.py | Browse nutrition plans based on BMI categories | Main Menu |
| View Users | pages/view_users.py | View all registered users | Main Menu |
| Create Challenges | pages/create_challenges.py | Create new fitness/language/knowledge challenges | View Challenges |
| Create Nutrition Plans | pages/create_nutration_plan.py | Create new nutrition plans | View Nutrition Plans |

---

## 5. UI/UX Design | تصميم واجهة المستخدم

<div class="arabic">
هنا تحط لقطات الشاشة + وصف التصميم البصري لمشروعك
</div>

### Screenshots | لقطات الشاشة

<!-- Screenshot: Landing page -->
**Landing Page**: Welcome screen with login and registration options, clean interface with navigation to different challenge categories.

<!-- Screenshot: Main dashboard -->
**Challenges View**: Grid layout showing all available challenges in Sports, Language, and General Knowledge categories with difficulty levels and activity counts.

<!-- Screenshot: Key feature screen -->
**Nutrition Plans**: Display of nutrition plans based on BMI categories with detailed meal plans (breakfast, lunch, dinner) and water intake recommendations.

<!-- Add more screenshots as needed -->

### Design System | نظام التصميم

| Element | Style |
|---------|-------|
| **Primary Color** | Streamlit default blue (#1a73e8) |
| **Secondary Color** | Green for success/completion (#34a853) |
| **Font** | Default Streamlit font (sans-serif) |
| **Button Style** | Rounded buttons with full-width containers |
| **Layout** | Multi-page navigation with sidebar, card-based content display |

### Responsive Design | التصميم المتجاوب

| Breakpoint | Layout | Tested? |
|------------|--------|:-------:|
| Desktop (1024px+) | Full sidebar + 3-column grid layout for challenges | ☐ |
| Tablet (768-1024px) | Collapsible sidebar + 2-column grid layout | ☐ |
| Mobile (< 768px) | Stacked layout, single-column cards | ☐ |

---

## 6. Data Sources | مصادر البيانات

<div class="arabic">
هنا تكتب منين جبت الداتا — قاعدة بيانات، API، ملفات، أو داتا مكتوبة في الكود
</div>

### Data Sources | مصادر البيانات

| Source | Type | Description |
|--------|------|-------------|
| USDA FoodData Central | API | Official US government database for nutritional values and food data |
| Mayo Clinic | Static | Medical nutrition data and dietary recommendations |
| Harvard T.H. Chan School of Public Health | Static | Scientific nutrition research and evidence-based guidelines |
| ACSM (American College of Sports Medicine) | Static | Scientific sports medicine and exercise guidelines |
| CDC | Static | Official physical activity guidelines and recommendations |

### Database Schema | مخطط قاعدة البيانات

| Table | Columns | Description |
|-------|---------|-------------|
| [users] | [id, username, email, password, DOB, height, weight, phone, ssn, created_at] | [users data] |
| [user_challenges] | [user_id, challenge_id] | [user challenges data] |
| [challenges] | [id, name, number_of_levels, number_of_activities, category, duration, description, created_at] | [challenges data] |
| [activities] | [id, name, description, category, difficulty, challenge_id, created_at] | [activities data] |
| [Nutrition_Plans] | [id, bmi, category, goal, calories, breakfast, lunch, dinner, water_intake, created_at] | [nutrition plans data] |
| [user_nutrition_plans] | [user_id, nutrition_plan_id] | [user nutrition plans data] |




---

## 7. Educational Content | المحتوى التعليمي

<div class="arabic">
هنا تكتب المحتوى التعليمي — ماذا يتعلم الطالب من هذا المشروع؟ كيف يتعلق بالمنهج؟
</div>

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. Build a full-stack web application using Python and Streamlit framework
2. Design and implement a SQLite database with multiple related tables and foreign key relationships
3. Create user authentication system with registration and login functionality
4. Implement BMI and fitness level calculations with mathematical formulas
5. Design and manage nutrition plans with meal planning based on BMI categories
6. Create interactive challenges and activities system with different difficulty levels
7. Build responsive user interface with multi-page navigation and data visualization

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| Self-Improvement Culture | The project connects to the growing global culture of self-improvement and lifelong learning, promoting physical health, mental growth, and continuous skill development |
| Health & Fitness | Addresses the importance of physical health and nutrition in modern society, providing accessible tools for people to track and improve their fitness |
| Education & Knowledge | Promotes continuous learning and knowledge expansion, connecting to the tradition of self-education and intellectual growth |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Identifying real-world self-improvement needs and building comprehensive solutions |
| Computational Thinking | Database design with multiple related tables, data modeling, BMI calculations |
| Creativity | UI/UX design for multi-page navigation, card-based layouts, and user experience |
| Collaboration | Working with team members on different features (authentication, challenges, nutrition) |
| Technical Writing | Documenting architecture, features, and creating comprehensive project documentation |

---

## 8. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

<div class="arabic">
نسخة مختصرة — للخطط التسويقية الكاملة، استخدم القالب الرئيسي
</div>

### Target Audience | الجمهور المستهدف

- **Primary**: Teens ages 12-20 interested in self-improvement, fitness, and learning
- **Secondary**: Elderly people who want to track their health and maintain cognitive function
- **Tertiary**: Schools, fitness centers, and educational institutions looking for engagement tools


### Promotion Ideas | أفكار ترويجية

1. Share demo video on YouTube/TikTok showing the challenge features and nutrition plans
2. Present at school science fair or technology exhibition
3. Post screenshots and features on class WhatsApp/Telegram groups
4. Submit to Afro-Asian Tech Forum competition in Educational Tools category
5. Partner with local fitness centers or schools for pilot programs
6. Create social media content highlighting success stories and challenge completions
