import os
from models.student_model import StudentModel


class StudentController:
    def __init__(self):
        self.model= StudentModel()

    def add_student(self, std_name, std_age, course, file):
        file_path = None

        if file is not None:
            os.makedirs("uploads", exist_ok=True)
            file_path = f"uploads/{file.name}"
            with open(file_path,"wb") as f:
                f.write(file.getbuffer())
        
        self.model.add_student(std_name, std_age, course, file_path)

    def fetch_students():
        return self.model.get_students()