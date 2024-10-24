import streamlit as st

def show_search():
    st.title("Search")
    
    search_query = st.text_input("Search for...", placeholder="Enter keywords")
    search_type = st.radio("Search in:", ["All", "Bug Reports", "Alerts", "History"])
    
    if st.button("Search") and search_query:
        st.info(f"Searching for '{search_query}' in {search_type}")
        
        # Simulasi hasil pencarian
        st.subheader("Search Results")
        with st.expander("Result 1"):
            st.write("Sample search result 1")
        with st.expander("Result 2"):
            st.write("Sample search result 2")