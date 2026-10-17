import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("🥗 Nutrition plans")
st.caption("Meal plans for every BMI category")




weight = st.number_input("Enter your weight (kg)", min_value=20.0, max_value=200.0, step=0.5)
height = st.number_input("Enter your height (cm)", min_value=100.0, max_value=220.0, step=0.5)

if st.button("Get my weekly plan", type="primary", width="stretch"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.session_state.bmi = bmi

    st.subheader(f"Your BMI is: {bmi:.1f}")

    if bmi < 18.5:
        st.session_state.bmi_result = "Underweight"
        st.warning("Category: Underweight")
        week_plan = {
            "Saturday": ["Oats + milk + nuts", "Rice + chicken + vegetables", "Eggs + bread"],
            "Sunday": ["Peanut butter sandwich + banana", "Pasta + meat", "Yogurt + honey"],
            "Monday": ["Eggs + cheese + bread", "Rice + fish", "Milk + dates"],
            "Tuesday": ["Oats + banana", "Chicken + potatoes", "Boiled eggs"],
            "Wednesday": ["Toast + peanut butter", "Rice + meat", "Yogurt + nuts"],
            "Thursday": ["Egg sandwich", "Pasta + chicken", "Milk + banana"],
            "Friday": ["Oats + honey", "Rice + chicken", "Eggs + cheese"]
        }

    elif 18.5 <= bmi < 25:
        st.session_state.bmi_result = "Normal"
        st.success("Category: Normal Weight")
        week_plan = {
            "Saturday": ["Eggs + toast", "Grilled chicken + rice + salad", "Yogurt + fruit"],
            "Sunday": ["Oats + fruit", "Fish + vegetables", "Boiled eggs"],
            "Monday": ["Cheese sandwich", "Chicken + potatoes", "Yogurt"],
            "Tuesday": ["Eggs + fruit", "Rice + meat + salad", "Milk"],
            "Wednesday": ["Oats + honey", "Fish + rice", "Fruit salad"],
            "Thursday": ["Toast + eggs", "Chicken + vegetables", "Yogurt"],
            "Friday": ["Oats + banana", "Rice + chicken", "Boiled eggs"]
        }

    else:
        st.session_state.bmi_result = "Overweight"
        st.error("Category: Overweight")
        week_plan = {
            "Saturday": ["Oats (low fat milk)", "Grilled chicken + vegetables", "Salad + yogurt"],
            "Sunday": ["Boiled eggs + cucumber", "Fish + salad", "Apple"],
            "Monday": ["Oats + fruit", "Chicken + vegetables", "Yogurt"],
            "Tuesday": ["Eggs + tomato", "Tuna salad", "Orange"],
            "Wednesday": ["Oats (water)", "Grilled meat + salad", "Apple"],
            "Thursday": ["Boiled eggs", "Chicken + steamed vegetables", "Yogurt"],
            "Friday": ["Fruit + yogurt", "Fish + vegetables", "Salad"]
        }

    # Show the 7 days as a table: one row per day with its three meals.
    rows = []
    for day in week_plan:
        meals = week_plan[day]
        rows.append({"Day": day, "Breakfast": meals[0], "Lunch": meals[1], "Dinner": meals[2]})
    st.table(rows)




conn = sqlite3.connect(DATABASE_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
plans = conn.execute("select * from nutrition_plans order by bmi").fetchall()

# If you are logged in, find the plan you chose (if any).
my_plan_id = None
if "user_id" in st.session_state:
    row = conn.execute(
        "select nutrition_plan_id from user_nutrition_plans where user_id = ?",
        (st.session_state.user_id,),
    ).fetchone()
    if row is not None:
        my_plan_id = row["nutrition_plan_id"]
conn.close()

if len(plans) == 0:
    st.info("No nutrition plans yet.")

cols = st.columns(3)
number = 0
for plan in plans:
    with cols[number % 3]:
        with st.container(border=True):
            st.subheader(f"BMI {plan['bmi']}")
            st.caption(f"{plan['category']} · Goal: {plan['goal']}")
            col1, col2 = st.columns(2)
            col1.metric("Calories", f"{plan['calories']} kcal")
            col2.metric("Water", plan["water_intake"])
            with st.expander("Meals"):
                st.write(f"**Breakfast:** {plan['breakfast']}")
                st.write(f"**Lunch:** {plan['lunch']}")
                st.write(f"**Dinner:** {plan['dinner']}")

            if plan["id"] == my_plan_id:
                st.success("This is your plan.")
            elif "user_id" in st.session_state:
                if st.button("Choose this plan", key=f"choose_{plan['id']}", type="primary", width="stretch"):
                    # Every user has one plan, so remove the old one before saving the new one.
                    conn = sqlite3.connect(DATABASE_PATH)
                    conn.execute("PRAGMA foreign_keys = ON")
                    conn.execute("delete from user_nutrition_plans where user_id = ?", (st.session_state.user_id,))
                    conn.execute(
                        "insert into user_nutrition_plans (user_id, nutrition_plan_id) values (?, ?)",
                        (st.session_state.user_id, plan["id"]),
                    )
                    conn.commit()
                    conn.close()
                    st.rerun()
    number = number + 1
