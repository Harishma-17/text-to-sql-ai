import streamlit as st
from groq import Groq
import sqlite3
import time

st.set_page_config(
    page_title="Text to SQL AI",
    page_icon="🤖",
    layout="wide"
)
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);}
</style>
""", unsafe_allow_html=True)
st.sidebar.title("📊 Database Tables")

st.sidebar.success("students")
st.sidebar.success("employees")
st.sidebar.success("customers")
st.sidebar.success("products")
st.sidebar.success("orders")
st.sidebar.success("books")
st.sidebar.success("hospitals")
st.sidebar.success("movies")
st.sidebar.success("flights")
st.sidebar.success("hotels")
st.sidebar.success("courses") 
if "history" not in st.session_state:
    st.session_state.history = []
st.sidebar.markdown("---")
st.sidebar.subheader("🕒 Recent Queries")

if st.session_state.history:
    for query in reversed(st.session_state.history[-5:]):
        st.sidebar.write(f"• {query}")
    if st.sidebar.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.sidebar.info("No queries yet")

st.title("🤖 AI-Powered Text to SQL Converter")
st.info("🤖 AI Model Connected and Ready")
col1, col2, col3 = st.columns(3)

col1.metric("📊 Tables", "11")
col2.metric("🤖 Model", "Groq Llama3")
col3.metric("💾 Database", "SQLite")

st.markdown("Convert Natural Language into SQL Queries using Llama 3")
st.info("""
Example Queries:

• Show all employees whose salary is greater than 50000

• Display all products costing less than 1000

• Find students whose marks are above 80

• Show customers from Chennai
""")
user_text = st.text_area(
    "Enter your question",
    placeholder="Show all employees whose salary is greater than 50000"
)

if st.button("Generate SQL"):

    prompt = f"""
Convert the following natural language text into a valid SQL query.

Return only the SQL query.
Do not provide explanations.
Do not use markdown.
Text:
{user_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql_query = response.choices[0].message.content
    
    if user_text.strip():
        st.session_state.history.append(user_text)
    
    st.info("🔵 SQL Query Generated Successfully")
    
    st.subheader("Generated SQL Query")

    st.code(sql_query, language="sql")

    try:
        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()
        
        start_time = time.time()
        
        cursor.execute(sql_query)

        rows = cursor.fetchall()
        end_time = time.time()

        execution_time = round(end_time - start_time, 4)
        
        column_names = [desc[0] for desc in cursor.description]
        st.caption(f"⏱ Query Executed in {execution_time} seconds")
        st.subheader("Query Results")
        if rows:
            import pandas as pd
            df = pd.DataFrame(
    rows,
    columns=column_names
)
            
            st.dataframe(df, hide_index=True)
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Results",
                csv,
                "results.csv",
                "text/csv"
            )
        
        
        
        else:
            st.warning("No records found")

        conn.close()

    except Exception as e:
            st.warning(
              "Query generated successfully. However, the requested dataset/table is not available in this demo database."
    )