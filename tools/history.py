import streamlit as st
from datetime import datetime, timedelta

def show_history():
    st.title("History")
    
    # Filter tanggal
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=7))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Sample history data
    history_data = [
        {"date": "2024-10-24", "action": "User Login", "user": "admin"},
        {"date": "2024-10-24", "action": "Bug Report Created", "user": "user1"},
        {"date": "2024-10-23", "action": "System Alert Acknowledged", "user": "admin"},
    ]
    
    # Display history
    st.subheader("Activity History")
    for item in history_data:
        st.write(f"{item['date']} - {item['action']} by {item['user']}")