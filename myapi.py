from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        'name': 'manish',
        'age': 22,
        'email': 'manish@example.com'
    },
    2: {
        'name': 'manis',
        'age': 22,
        'email': 'manish@example.com'
    },
    3: {
        'name': 'mani',
        'age': 22,
        'email': 'manish@example.com'
    }
}

class Student(BaseModel):
    name: str
    age: int
    email: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None


@app.get('/')
def index():
    return {'page': 'homepage'}


@app.get('/student-detail/{student_id}')
def student_detail(student_id: int = Path(description='Enter student ID')):
    return students[student_id]


@app.get('/student')
def student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {'Data': 'Not found :<'}


@app.get('/student/{student_id}')
def student(student_id: int, name: Optional[str] = None):
    if name == None:
        return students[student_id]
    else:
        return students[student_id]['name'] == name 


@app.post('/create-student/{student_id}')
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {'Error': 'Student Id already exists'}
    students[student_id] = student
    return students[student_id]


@app.put('/edit-details/{student_id}')
def edit_details(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"Student_id": "Not found in students object"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.email != None:
        students[student_id].email = student.email
    
    return students[student_id]


@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error': 'Student not found'}
    del students[student_id]
    return {'Success': f'student with student id {student_id} deleted successfully'}


@app.get('/all-students')
def get_all_students():
    return students