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
target_sales_per_day = sales_left / days_remaining if days_remaining > 0 else 0

# --- Custom CSS for Metric Cells ---
st.markdown(
    """
    <style>
    .metric-container {
        background-color: #383838; /* A darker gray for dark mode */
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 10px;
        color: white; /* Ensure text inside is visible */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Dashboard Layout ---
st.title(f"📊 {current_year} Sales Dashboard")

#with st.form("record_sale_form"):
#    new_sale = st.number_input("Enter new sale amount:", value=0.0, step=1.0, key="new_sale_input")
#    submitted = st.form_submit_button("Record Sale")
#    if submitted:
#        st.session_state['total_sales'] += new_sale
#        st.experimental_rerun()

st.subheader("Key Metrics")
col1, col2, col3, col_vel_target = st.columns(4)
col1.markdown(f"<div class='metric-container'><span style='color: #00FF00; font-size: 1.5em;'>{total_sales:.0f}</span><br>Total Sales</div>", unsafe_allow_html=True)
col2.markdown(f"<div class='metric-container'><span style='color: #FFA500; font-size: 1.5em;'>{yearly_target:.0f}</span><br>Yearly Target</div>", unsafe_allow_html=True)
col3.markdown(f"<div class='metric-container'><span style='color: #FF4500; font-size: 1.5em;'>{sales_left:.0f}</span><br>Sales Left</div>", unsafe_allow_html=True)
col_vel_target.markdown(f"<div class='metric-container'><span style='color: #1E90FF; font-size: 1.5em;'>{sales_velocity:.2f}</span><br>Sales Velocity (Daily)<br><span style='color: #DA70D6; font-size: 1.0em;'>🎯 Target: {target_sales_per_day:.2f}</span></div>", unsafe_allow_html=True)

st.subheader("Progress")
col_progress, col_target_day = st.columns(2)
with col_progress:
    st.progress(percent_achieved)
    st.write(f"{percent_achieved * 100:.2f}% of target achieved")
# with col_target_day:
#    st.markdown(f"<div class='metric-container'><span style='color: #DA70D6; font-size: 1.5em;'>{target_sales_per_day:.2f}</span><br>Target Sales/Day (to Goal)</div>", unsafe_allow_html=True)

st.subheader("Additional Details")
col_date, col_days, col_year_percent, col_achieved_percent = st.columns(4)
col_date.info(f"🗓️ Current Date: {now.strftime('%Y-%m-%d')}")
col_days.info(f"⏳ Day {days_passed} of {days_in_year}")
col_year_percent.info(f"📈 {percent_year_passed:.2f}% of Year Passed")
col_achieved_percent.info(f"✅ {percent_achieved * 100:.2f}% of Target Achieved")

# --- Motivational Message ---
st.subheader("🌟 Motivation")
if percent_achieved < 0.5:
    st.info("Keep pushing forward! Every sale counts towards your goal. 💪")
elif percent_achieved < 0.75:
    st.success("Great progress! You're more than halfway there. Keep the momentum! 🎉")
else:
    st.balloons()
    st.success("Fantastic! You're on track to smash your target! 🏆")