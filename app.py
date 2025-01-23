import streamlit as st
from NectaPy import st_result

def main():
    # Page config for title and icon
    st.set_page_config(page_title="NectaPro Results Viewer", page_icon="🎓", layout="centered")

    # Main Title
    st.title('📚 NectaPro')

    # Sidebar instructions
    st.sidebar.header('📖 How to Use')
    st.sidebar.info('''
    👉 1. Enter your Student ID  
    👉 2. Select your Exam Level  
    👉 3. Click "🎯 Get Results"  
    ''')

    # Student ID Input
    st.write('🔍 **Enter your Student Details Below:**')
    student_id = st.text_input('📌 Student ID (e.g., s3266/0064/2024)', '')

    # Exam Level Selection
    st.write('✏️ **Choose Your Exam Level:**')
    exam_levels = {
        'CSEE Form 4 📝': 'csee',    # Form 4
        'ACSEE Form 6 🎓': 'acsee',  # Form 6
        'FTNA Form 2 📘': 'ftna',    # Form 2
        'PSLE Standard 7 🌟': 'psle',    # Standard 7
        'SFNA Standard 2 🧮': 'sfna'     # Standard 2
    }
    selected_level = st.selectbox('', list(exam_levels.keys()))

    # Result Retrieval Button
    if st.button('🎯 Get Results'):
        if student_id and selected_level:
            try:
                # Fetch the result using NectaPy
                result = st_result(student_id, exam_levels[selected_level])
                st.success('✅ Results Retrieved Successfully!')
                st.write('🎉 **Your Exam Results:**')
                st.table(result)
                
            except Exception as e:
                st.error(f'⚠️ Error retrieving results: {e}')
        else:
            st.warning('⚠️ Please enter a valid Student ID and select an Exam Level!')

    # Footer
    st.markdown("""
    ---
    Made with 💖 by [Lee](https://henrylee-hd.vercel.app/) | Powered by [NectaPy](https://pypi.org/project/NectaPy/)
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
