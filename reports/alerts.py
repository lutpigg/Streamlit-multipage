import streamlit as st

def show_alerts():
    st.title("System Alerts")
    
    # Filter alerts
    st.sidebar.subheader("Filter Alerts")
    alert_type = st.sidebar.multiselect(
        "Alert Type",
        ["Error", "Warning", "Info"],
        default=["Error", "Warning", "Info"]
    )
    
    # Sample alerts
    alerts = [
        {"type": "Error", "message": "Database connection failed", "time": "2024-10-24 13:45"},
        {"type": "Warning", "message": "High CPU usage detected", "time": "2024-10-24 13:30"},
        {"type": "Info", "message": "System backup completed", "time": "2024-10-24 13:15"},
    ]
    
    # Display filtered alerts
    for alert in alerts:
        if alert["type"] in alert_type:
            with st.expander(f"{alert['type']}: {alert['message']}"):
                st.write(f"Time: {alert['time']}")