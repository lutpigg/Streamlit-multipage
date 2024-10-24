import streamlit as st

def show_bug_reports():
    st.title("Bug Reports")
    
    # Form untuk submit bug baru
    with st.form("bug_report_form"):
        st.subheader("Submit New Bug Report")
        title = st.text_input("Bug Title")
        description = st.text_area("Bug Description")
        severity = st.select_slider("Severity", options=['Low', 'Medium', 'High', 'Critical'])
        submit = st.form_submit_button("Submit Bug Report")
        
        if submit:
            st.success("Bug report submitted successfully!")
    
    # Daftar bug yang ada
    st.subheader("Existing Bug Reports")
    bugs = [
        {"title": "Sample Bug 1", "severity": "High", "status": "Open"},
        {"title": "Sample Bug 2", "severity": "Medium", "status": "In Progress"},
    ]
    
    for bug in bugs:
        with st.expander(f"{bug['title']} ({bug['severity']})"):
            st.write(f"Status: {bug['status']}")