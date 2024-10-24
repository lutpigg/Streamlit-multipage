import streamlit as st

def show_dashboard():
    st.title("Dashboard")
    
    # Contoh konten dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Active Users", value="1,234", delta="12%")
    
    with col2:
        st.metric(label="Total Reports", value="789", delta="-2%")
    
    with col3:
        st.metric(label="System Status", value="98%", delta="3%")
    
    # Tambahkan grafik atau visualisasi lainnya
    st.subheader("System Overview")
    chart_data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'values': [100, 120, 115, 134, 129]
    }
    st.line_chart(chart_data)