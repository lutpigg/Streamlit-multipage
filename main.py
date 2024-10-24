import streamlit as st
import hashlib
from datetime import datetime
from reports.login import login_form
from reports.dashboard import show_dashboard
from reports.bugs import show_bug_reports
from reports.alerts import show_alerts
from tools.search import show_search
from tools.history import show_history

# Inisialisasi semua state yang diperlukan
def init_session_state():
    # Login state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "login_attempts" not in st.session_state:
        st.session_state.login_attempts = 0
    if "last_attempt" not in st.session_state:
        st.session_state.last_attempt = None
    if "USERS_DB" not in st.session_state:
        st.session_state.USERS_DB = {
            "admin": hashlib.sha256("admin123".encode()).hexdigest(),
            "lutpi": hashlib.sha256("lutpi123".encode()).hexdigest()
        }
    if "username" not in st.session_state:
        st.session_state.username = None

def main():
    # Inisialisasi state di awal aplikasi
    init_session_state()
    
    if not st.session_state.logged_in:
        login_form()
    else:
        # Sidebar dengan informasi user dan tombol logout
        with st.sidebar:
            st.write(f"Welcome, {st.session_state.username}!")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.rerun()

        # Menu navigasi
        st.sidebar.title("Navigation")
        
        # Section Reports
        st.sidebar.header("Reports")
        page = st.sidebar.radio("", ["Dashboard", "Bug Reports", "System Alerts", "Search", "History"])
        
        if page == "Dashboard":
            show_dashboard()
        elif page == "Bug Reports":
            show_bug_reports()
        elif page == "System Alerts":
            show_alerts()
        elif page == "Search":
            show_search()
        elif page == "History":
            show_history()

if __name__ == "__main__":
    main()