import streamlit as st
import hashlib
from datetime import datetime

def check_password(username, password):
    """Verifikasi username dan password"""
    if username in st.session_state.USERS_DB:
        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
        return st.session_state.USERS_DB[username] == hashed_pwd
    return False

def login_form():
    st.title("Login System")
    
    # Cek jika sudah terlalu banyak percobaan login
    if st.session_state.login_attempts >= 3:
        if st.session_state.last_attempt:
            time_diff = datetime.now() - st.session_state.last_attempt
            if time_diff.total_seconds() < 300:  # 5 menit cooldown
                st.error(f"Terlalu banyak percobaan login. Silakan coba lagi dalam {5 - int(time_diff.total_seconds()/60)} menit")
                return
            else:
                st.session_state.login_attempts = 0

    # Gunakan form untuk login
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if username and password:  # Pastikan field tidak kosong
                if check_password(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.login_attempts = 0
                    st.success("Login berhasil!")
                    st.rerun()
                else:
                    st.session_state.login_attempts += 1
                    st.session_state.last_attempt = datetime.now()
                    st.error("Username atau password salah!")
            else:
                st.warning("Mohon isi semua field!")