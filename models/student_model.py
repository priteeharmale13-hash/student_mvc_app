import mysql.connector
from config import DB_CONFIG

class StudentModel:
    def __init__(self):
        self.db = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.db.cursor()

    def add_student(self, std_name, std_age, course, file_path):
        query = """
               Insert into student(std_name, std_age, course, file_path) 
               Values(%s,%s,%s,%s)
                """
        self.cursor.execute(query,(std_name,std_age,course,file_path))
        self.db.commit()

    def get_students(self):
        self.cursor.execute("Select * from student")
        return self.cursor.fetchall()




