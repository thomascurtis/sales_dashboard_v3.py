import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(layout="wide")

# --- Initialize total_sales in Streamlit's session state ---
if 'total_sales' not in st.session_state:
    st.session_state['total_sales'] = 2998

# --- Data ---
current_year = datetime.now().year
yearly_target = 15000

now = datetime.now()
start_of_year = datetime(current_year, 1, 1)
end_of_year = datetime(current_year + 1, 1, 1)
days_in_year = (end_of_year - start_of_year).days
days_passed = (now - start_of_year).days + 1
days_remaining = days_in_year - days_passed

total_sales = st.session_state['total_sales']
sales_left = yearly_target - total_sales
sales_velocity = total_sales / days_passed if days_passed > 0 else 0
monthly_goal = yearly_target / 12
predicted_completion = sales_velocity * days_in_year
percent_achieved = (total_sales / yearly_target) if yearly_target > 0 else 0
percent_year_passed = (days_passed / days_in_year) * 100

# --- Calculate target sales per day ---
target_sales_per_day = sales_left / days_remaining if days_remaining > 0 else 0

# --- Dashboard Layout ---
st.title(f"📊 {current_year} Sales Dashboard")

with st.form("record_sale_form"):
    new_sale = st.number_input("Enter new sale amount:", value=0, step=1, key="new_sale_input")
    submitted = st.form_submit_button("Record Sale")
    if submitted:
        st.session_state['total_sales'] += new_sale

col1, col2, col3 = st.columns(3)
col1.markdown(f"<span style='color: #00FF00; font-size: 1.5em;'>{total_sales:.0f}</span> Total Sales", unsafe_allow_html=True)
col2.markdown(f"<span style='color: #FFA500; font-size: 1.5em;'>{yearly_target:.0f}</span> Yearly Target", unsafe_allow_html=True)
col3.markdown(f"<span style='color: #FF4500; font-size: 1.5em;'>{sales_left:.0f}</span> Sales Left", unsafe_allow_html=True)

# --- Motivational Message ---
st.subheader("🌟 Motivation")
if percent_achieved < 0.5:
    st.info("Keep pushing forward! Every sale counts towards your goal. 💪")
elif percent_achieved < 0.75:
    st.success("Great progress! You're more than halfway there. Keep the momentum! 🎉")
else:
    st.balloons()
    st.success("Fantastic! You're on track to smash your target! 🏆")

st.subheader("Progress Towards Yearly Target")
st.progress(percent_achieved)
st.write(f"{percent_achieved * 100:.2f}% of target achieved")

st.subheader("Key Performance Indicators")
col_vel, col_target_day = st.columns(2)
col_vel.markdown(f"<span style='color: #1E90FF; font-size: 1.5em;'>{sales_velocity:.2f}</span> Sales Velocity (Daily)", unsafe_allow_html=True)
col_target_day.markdown(f"<span style='color: #DA70D6; font-size: 1.5em;'>{target_sales_per_day:.2f}</span> Target Sales/Day (to Goal)", unsafe_allow_html=True)

st.subheader("ℹ️ Additional Details")
st.write(f"🗓️ Current Date: {now.strftime('%Y-%m-%d')}")
st.write(f"⏳ Days Passed in Year: {days_passed}")
st.write(f"📈 Percentage of Year Passed: {percent_year_passed:.2f}%")
st.write(f"✅ Percentage of Target Achieved: {(total_sales / yearly_target) * 100:.2f}%")