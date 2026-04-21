import streamlit as st
import mysql.connector

# Page Configuration
st.set_page_config(page_title="TCF Drawing Library", layout="wide")
st.title("📂 TCF Digital Library Search Portal")

# Database Connection
def get_data(search_query):
    # Har line function ke andar 4 spaces aage honi chahiye
    db = mysql.connector.connect(
        host="mysql-15fcdecc-muhammadanasraza54-5182.g.aivencloud.com", 
        port=11756,
        user="avnadmin",
        password="AVNS_aRLK6thMKERANG1GB5w", 
        database="defaultdb"
    )
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM drawings WHERE campus_name LIKE %s OR file_name LIKE %s LIMIT 100"
    cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
    results = cursor.fetchall()
    db.close()
    return results

# UI - Search Box
search = st.text_input("Campus ka naam ya Drawing ka naam likhein:", "")

if search:
    data = get_data(search)
    if data:
        for row in data:
            with st.expander(f"📍 {row['campus_name']} - {row['file_name']}"):
                st.write(f"**Region:** {row['region']}")
                st.write(f"**Path:** {row['file_path']}")
                if row.get('file_link'):
                    st.link_button("🔗 Open Drawing (OneDrive)", row['file_link'])
                else:
                    st.info("Is drawing ka link maujood nahi hai.")
    else:
        st.warning("Koi drawing nahi mili.")
