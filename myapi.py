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