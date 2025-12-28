import streamlit as st
import pandas as pd
from controllers.student_controller import StudentController

def student_ui():
    controller = StudentController()

    st.title = "🎓 Student Management System (MVC)"
    menu = st.selectbox("Menu",["Add Student", "View Student"])

    if menu == "Add Student":
        with st.form("Student Form"):
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=1)
            course = st.text_input("Course")
            file = st.file_uploader("Upload File")
            submit = st.form_submit_button("Submit")
            

            if submit:
                controller.add_student(name,age,course,file)
                st.success("✅ Student Added")

    elif menu == "View Student":
        student = controller.fetch_students()

        if not student:
            st.warning("No Student Found")
            return
        
        # Convert to DataFrame
        df = pd.DataFrame(
            student,
            columns=["Name", "Age", "Course", "File Path", "Created At"]
        )
        st.subheader("Student List")
        st.dataframe(df, use_container_width=True)

        # for s in student:
        #     st.write(f"**{s[1]}** | Age: {s[2]} | Course: {s[3]}")
        

