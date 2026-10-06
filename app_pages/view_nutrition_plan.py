import sqlite3
import streamlit as st
from assets.config import DATABASE_PATH

st.title("🥗 Nutrition plans")
st.caption("Meal plans for every BMI category")

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
                if st.button("Choose this plan", key=f"choose_{plan['id']}", width="stretch"):
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
