import streamlit as st
from scripts.supabase_cli import supabase

def main():
    st.button("Press Button", type="primary")
    if st.button("Say hello"):
        #st.write("Why hello there")
        
        # Example usage of Supabase client
        response = supabase.table("football_leagues").select("*").execute()
        #response = SUPABASE_URL
        
        st.write(response.data)
    else:
        st.write("Goodbye my man")

if __name__ == "__main__":
    main()
