from fastapi import FastAPI, Path
from typing import Optional

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
