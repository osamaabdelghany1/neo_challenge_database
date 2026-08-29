
# Software Project Documentation | توثيق مشروع البرمجيات

<div class="arabic">
قالب توثيق مشاريع البرمجيات — للمسابقة الأفريقية الآسيوية للتكنولوجيا
</div>

---

## 1. Project Overview | نظرة عامة على المشروع

| Field | Value |
|-------|-------|
| **Project Title** | NEO Challenge Database |
| **Project Type** | Web App |
| **Description** | A web application that helps users find and participate in various challenges including sports, language learning, and general knowledge. It provides personalized nutrition plans based on BMI and fitness goals. |
| **Target Users** | Students, fitness enthusiasts, language learners, general public |
| **Resolution / Platform** | Desktop + Mobile (responsive) |
| **Date** | 2026-08-09 |

### Tech Stack | Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python | Backend logic and web interface |
| **Framework** | Streamlit | Web framework |
| **Database** | SQLite | Store user data, challenges, activities, nutrition plans |

### Dependencies | المكتبات المستخدمة

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | latest | Web framework |
| sqlite3 | built-in | Database |

<!-- Screenshot: Main screen of your project -->

---

## 2. Problem Statement | بيان المشكلة

<div class="arabic">
هنا تكتب المشكلة التي يحلها مشروعك — لماذا هذا المشروع مهم؟
</div>

### What problem does this project solve? | ما المشكلة التي يحلها هذا المشروع؟
الناس يبحثون عن مواقع التدريب والكورسات والدورات التدريبية ويتطلبون وقتاً طويلاً للبحث عنها.

### Why does it matter? | لماذا هذا مهم؟

لانها توفر وقت لاغلب الناس وتساعدهم في التغيير بعض العادات للناس بشكل أفضل.



### How is it currently solved? | كيف تُحل المشكلة حالياً؟

الموقع يحل مشكله الوقت عند معظم الناس ,لأن اغلب الناس يبحثون عن مواقع التدريب والكورسات والدورات التدريبية ويتطلبون وقتاً طويلاً للبحث عنها.


---

## 3. Technical Architecture | البنية التقنية

<div class="arabic">
هنا تشرح كيف مشروعك مبني من الداخل — هيكل الملفات والتقنيات المستخدمة
</div>

### Project Structure | هيكل المشروع

```
neo_challenge_database/
├── app.py               # Main Streamlit app
├── pages/               # Streamlit pages
│   ├── login.py         # User login page
│   ├── register.py      # User registration page
│   ├── view_challenges.py    # View all challenges
│   ├── view_activities.py    # View activities in challenges
│   ├── view_nutration_plan.py # View nutrition plans
│   ├── create_catogary.py    # Create challenge categories
│   ├── create_challenges.py  # Create new challenges
│   ├── create_nutration_plan.py # Create nutrition plans
│   └── view_users.py    # View all users
├── database/            # Database files
│   ├── database.db      # SQLite database
│   ├── tables.sql       # Database schema
│   ├── insert.sql       # Insert statements
│   ├── insert_challenges.sql
│   ├── insert_nutrition_plan.sql
│   └── insert_users.sql
└── docs/                # Documentation
    └── afro_asian_software_template.md
```

### Architecture Diagram | مخطط البنية

```
[User] → [Streamlit Browser] → [Python Backend] → [SQLite Database]
```

### Key Files | الملفات الرئيسية

| File | Purpose | Lines of Code |
|------|---------|:-------------:|
| app.py | Main app entry point | ~1 |
| pages/login.py | User authentication | ~21 |
| pages/register.py | User registration | ~30 |
| pages/view_challenges.py | Display all challenges | ~40 |
| database/tables.sql | Database schema | ~164 |


---

## 4. Features & User Flow | الميزات وتدفق المستخدم

<div class="arabic">
هنا تكتب قائمة الميزات + مخطط تدفق المستخدم عبر الشاشات
</div>

### Feature List | قائمة الميزات

| # | Feature | Description | Status |
|---|---------|-------------|:------:|
| 1 | بيسجل حساب | يسجل البيانات بتاعت المستخدم | ✅ |
| 2 | تسجيل الدخول | يسمح للمستخدمين بالدخول لحساباتهم | ✅ |
| 3 | عرض التحديات | يعرض جميع التحديات المتاحة (رياضة، لغات، معرفة عامة) | ✅ |
| 4 | عرض الأنشطة | يعرض الأنشطة داخل كل تحدي | ✅ |
| 5 | عرض خطط التغذية | يعرض خطط التغذية حسب BMI والهدف | ✅ |

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
                    │   DASHBOARD  │
                    │  (main hub)  │
                    └──┬───┬───┬───┘
                       │   │   │
              ┌────────┘   │   └────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ CHALLENGES│ │ACTIVITIES │ │NUTRITION │
        │ (view)   │ │ (view)   │ │ PLANS    │
        └──────────┘ └──────────┘ └──────────┘
```

[Replace with your actual user flow]

### Screen Reference | دليل الشاشات

| Screen | File / Route | Description | Transitions To |
|--------|-------------|-------------|----------------|
| Landing | app.py | Welcome page with login/register | Register, Login |
| Register | pages/register.py | Create new account with user data | Login |
| Login | pages/login.py | User authentication | Dashboard |
| View Challenges | pages/view_challenges.py | Display all available challenges | View Activities |
| View Activities | pages/view_activities.py | Show activities within a challenge | Dashboard |
| View Nutrition Plans | pages/view_nutration_plan.py | Display nutrition plans based on BMI | Dashboard |
| Create Category | pages/create_catogary.py | Admin page to create challenge categories | Dashboard |
| Create Challenge | pages/create_challenges.py | Admin page to create new challenges | Dashboard |
| Create Nutrition Plan | pages/create_nutration_plan.py | Admin page to create nutrition plans | Dashboard |


---

## 5. UI/UX Design | تصميم واجهة المستخدم

<div class="arabic">
هنا تحط لقطات الشاشة + وصف التصميم البصري لمشروعك
</div>

### Screenshots | لقطات الشاشة

<!-- Screenshot: Landing page -->
**Landing Page**: [describe what the user sees]

<!-- Screenshot: Main dashboard -->
**Dashboard**: [describe what the user sees]

<!-- Screenshot: Key feature screen -->
**Key Feature**: [describe what the user sees]

<!-- Add more screenshots as needed -->

### Design System | نظام التصميم

| Element | Style |
|---------|-------|
| **Primary Color** | [e.g., #1a73e8 (blue)] |
| **Secondary Color** | [e.g., #34a853 (green)] |
| **Font** | [e.g., Inter, Arial, Cairo] |
| **Button Style** | [e.g., rounded, flat, gradient] |
| **Layout** | [e.g., sidebar navigation, top navbar, cards] |

### Responsive Design | التصميم المتجاوب

| Breakpoint | Layout | Tested? |
|------------|--------|:-------:|
| Desktop (1024px+) | [describe layout] | ☐ |
| Tablet (768-1024px) | [describe layout] | ☐ |
| Mobile (< 768px) | [describe layout] | ☐ |


---

## 6. Data Sources | مصادر البيانات

<div class="arabic">
هنا تكتب منين جبت الداتا — قاعدة بيانات، API، ملفات، أو داتا مكتوبة في الكود
</div>

### Data Sources | مصادر البيانات

| Source | Type | Description |
|--------|------|-------------|
| database.db | SQLite Database | Stores user accounts, challenges, activities, nutrition plans |
| User Input | Form Submissions | Registration data, challenge creation, nutrition plan creation |
| Streamlit Session | Session State | Current logged-in user |

### Database Schema | مخطط قاعدة البيانات

| Table | Columns | Description |
|-------|---------|-------------|
| users | id, username, email, password, DOB, height, weight, phone, ssn, created_at | User accounts with personal data |
| challenges | id, name, number_of_levels, number_of_activities, category, duration, description, created_at | Available challenges (sports, language, general knowledge) |
| activities | id, name, description, category, difficulty, challenge_id, created_at | Activities within each challenge |
| user_challenges | user_id, challenge_id | Many-to-many relationship between users and challenges |
| Nutrition_Plans | id, bmi, category, goal, calories, breakfast, lunch, dinner, water_intake, created_at | Nutrition plans based on BMI |
| User_Nutrition_Plans | user_id, nutrition_plan_id | Relationship between users and nutrition plans |

### External APIs (if any) | واجهات برمجة التطبيقات

| API | Purpose | Rate Limit |
|-----|---------|------------|
| None | All data is local | N/A |


---

## 7. Educational Content | المحتوى التعليمي

<div class="arabic">
هنا تكتب المحتوى التعليمي — ماذا يتعلم الطالب من هذا المشروع؟ كيف يتعلق بالمنهج؟
</div>

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. Build a full-stack web application using Python and Streamlit
2. Design and implement a SQLite database with multiple tables and relationships
3. Implement user registration and authentication systems
4. Create and manage challenge-based learning content
5. Develop personalized nutrition planning based on BMI calculations

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| Health & Fitness | The project promotes healthy lifestyles through structured challenges and nutrition planning |
| Language Learning | Supports multilingual education with language learning challenges |
| Personalized Learning | Adapts to individual user needs through BMI-based nutrition plans |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Identifying user needs for challenges and nutrition planning |
| Computational Thinking | Database design, data modeling, user authentication logic |
| Creativity | Designing challenge categories and nutrition plan structures |
| Collaboration | Working with team members on different features |
| Technical Writing | Documenting architecture and writing this template |


---

## 8. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

<div class="arabic">
نسخة مختصرة — للخطط التسويقية الكاملة، استخدم القالب الرئيسي
</div>

### Target Audience | الجمهور المستهدف

- **Primary**: Students ages 12-25 who want to participate in fitness, language, and knowledge challenges
- **Secondary**: Teachers and educators looking for challenge-based learning tools
- **Tertiary**: Fitness enthusiasts and language learners

### Platforms | المنصات

- Web browser (Chrome, Firefox, Edge)
- Mobile phone (responsive design)
- School computers

### Promotion Ideas | أفكار ترويجية

1. Share demo video on YouTube/TikTok showing challenge features
2. Present at school science fair or coding competition
3. Post screenshots on class WhatsApp/Telegram groups
4. Submit to Afro-Asian Tech Forum competition


---

## 9. Student Worksheet | ورقة عمل الطالب

> **Instructions**: Copy this section into your own document and fill it in for YOUR project.

---

### My Project Information | معلومات مشروعي

**Student Name**: ___________________________

**Project Title**: ___________________________

**Date**: ___________________________

---

#### What is your project about? | عن ماذا يتحدث مشروعي؟

_______________________________________________
_______________________________________________

#### What problem does it solve? | ما المشكلة التي يحلها؟

_______________________________________________
_______________________________________________

---

### My Tech Stack | التقنيات المستخدمة

**My project type** (circle one): Web App / Desktop App / Mobile App / Python Script / Other: _______

**Technologies I used**:

| Category | Technology |
|----------|-----------|
| Language | |
| Framework | |
| Database | |
| Libraries | |

---

### My Screens | شاشات مشروعي

Draw or describe all the screens in your project:

| Screen Name | What the user sees/does | How to get here |
|-------------|------------------------|-----------------|
| | | |
| | | |
| | | |

---

### My Features | ميزات مشروعي

| Feature | What it does | Status |
|---------|-------------|:------:|
| | | ✅ / ⏳ / ❌ |
| | | ✅ / ⏳ / ❌ |
| | | ✅ / ⏳ / ❌ |

---

### My Data | بيانات مشروعي

**Where does data come from?**

_______________________________________________

**What data is stored?**

_______________________________________________

---

### What I Learned | ما تعلمته

1. The hardest part of building my project was: _________________________________

2. The most fun part of building my project was: _________________________________

3. If I had more time, I would add: _________________________________

4. One thing I would do differently: _________________________________

---

### Screenshot of My Project | لقطة شاشة من مشروعي

<!-- Paste a screenshot of your project running here -->

---

**Instructor Notes** | ملاحظات المدرس:

_______________________________________________
_______________________________________________

---

<div class="session-footer">
  <p>Techno Kids, Techno Future — Software Documentation Template</p>
  <p>Afro-Asian Tech Forum · Software Category · 2026</p>
</div>
